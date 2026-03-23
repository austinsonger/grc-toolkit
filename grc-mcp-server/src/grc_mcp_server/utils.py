"""Utility functions for ID normalization, text search, and path resolution."""

from __future__ import annotations

import re
from pathlib import Path


def normalize_control_id(control_id: str) -> str:
    """Normalize a control ID to lowercase with dots for enhancements.

    Examples:
        AC-2     -> ac-2
        AC-2(1)  -> ac-2.1
        ac-2(1)  -> ac-2.1
        GOV-01   -> gov-01
    """
    cid = control_id.strip().lower()
    cid = re.sub(r"\((\d+)\)", r".\1", cid)
    return cid


def extract_family_from_control_id(control_id: str) -> str | None:
    """Extract the 2-letter family code from a NIST-style control ID.

    Examples:
        AC-2     -> ac
        ac-2.1   -> ac
        IA-5(1)  -> ia
    """
    match = re.match(r"^([a-z]{2})-", control_id.strip().lower())
    if match:
        return match.group(1)
    return None


def tokenize(text: str) -> list[str]:
    """Simple tokenization for full-text search."""
    return re.findall(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*", text.lower())


def text_matches(query: str, text: str) -> bool:
    """Check if all query tokens appear in the text."""
    query_tokens = tokenize(query)
    text_lower = text.lower()
    return all(token in text_lower for token in query_tokens)


def resolve_repo_root() -> Path:
    """Resolve the repository root (parent of grc-mcp-server/)."""
    # Walk up from this file to find the repo root
    current = Path(__file__).resolve().parent
    for _ in range(5):
        if (current / "data").is_dir() and (current / "grc-pro").is_dir():
            return current
        current = current.parent
    # Fallback: assume standard layout
    return Path(__file__).resolve().parent.parent.parent.parent
