"""Evidence fetcher MCP tools."""

from __future__ import annotations

import asyncio
import json
import os
from typing import Any


def register_fetcher_tools(mcp_server: Any, data_loader: Any) -> None:
    """Register evidence fetcher tools with the MCP server."""

    @mcp_server.tool()
    async def grc_list_fetchers() -> str:
        """List all available evidence fetchers grouped by platform.

        Returns fetcher scripts organized by source system (aws, okta, sentinelone, gitlab, k8s, checkov, knowbe4, rippling).
        """
        fetchers = data_loader.list_fetchers()
        summary = {}
        for platform, scripts in fetchers.items():
            summary[platform] = {
                "count": len(scripts),
                "scripts": [s["name"] for s in scripts],
            }
        return json.dumps(summary, indent=2)

    @mcp_server.tool()
    async def grc_run_fetcher(
        platform: str,
        script_name: str,
        output_dir: str = "",
        timeout_seconds: int = 120,
    ) -> str:
        """Execute an evidence fetcher script.

        Args:
            platform: Platform name (e.g., "aws", "okta", "sentinelone")
            script_name: Script filename (e.g., "security_groups.sh", "okta_iam_core.py")
            output_dir: Optional output directory for results
            timeout_seconds: Execution timeout in seconds (default 120)
        """
        fetcher_path = data_loader.get_fetcher_path(platform, script_name)
        if not fetcher_path:
            available = data_loader.list_fetchers()
            platform_scripts = available.get(platform, [])
            return json.dumps({
                "error": f"Fetcher '{script_name}' not found in platform '{platform}'",
                "available_platforms": list(available.keys()),
                "available_scripts": [s["name"] for s in platform_scripts] if platform_scripts else [],
            })

        # Determine the command based on script type
        if fetcher_path.suffix == ".sh":
            cmd = ["bash", str(fetcher_path)]
        elif fetcher_path.suffix == ".py":
            cmd = ["python3", str(fetcher_path)]
        else:
            return json.dumps({"error": f"Unsupported script type: {fetcher_path.suffix}"})

        # Set up environment with the common env loader
        env = os.environ.copy()
        if output_dir:
            env["OUTPUT_DIR"] = output_dir

        try:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=str(fetcher_path.parent),
            )
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(),
                timeout=timeout_seconds,
            )
            return json.dumps({
                "status": "success" if proc.returncode == 0 else "error",
                "return_code": proc.returncode,
                "stdout": stdout.decode("utf-8", errors="replace")[-4000:],
                "stderr": stderr.decode("utf-8", errors="replace")[-2000:],
                "script": script_name,
                "platform": platform,
            }, indent=2)
        except asyncio.TimeoutError:
            return json.dumps({
                "status": "timeout",
                "error": f"Fetcher timed out after {timeout_seconds}s",
                "script": script_name,
                "platform": platform,
            })
        except OSError as e:
            return json.dumps({
                "status": "error",
                "error": str(e),
                "script": script_name,
                "platform": platform,
            })
