#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${OUTPUT_DIR:-evidence/artifacts/aws}"
PROFILE="${AWS_PROFILE:-default}"
REGION="${AWS_REGION:-us-east-1}"

usage() {
  cat <<USAGE
Usage: $0 [--output-dir <path>] [--profile <aws-profile>] [--region <aws-region>]
Collects AWS evidence artifacts for controls CTRL-AC-001 and CTRL-AU-001.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
    --profile) PROFILE="$2"; shift 2 ;;
    --region) REGION="$2"; shift 2 ;;
    --help|-h) usage; exit 0 ;;
    *) echo "Unknown argument: $1"; usage; exit 1 ;;
  esac
done

mkdir -p "$OUTPUT_DIR"

aws --profile "$PROFILE" --region "$REGION" cloudtrail describe-trails > "$OUTPUT_DIR/cloudtrail-trails.json"
aws --profile "$PROFILE" --region "$REGION" logs describe-log-groups > "$OUTPUT_DIR/cloudwatch-log-groups.json"
aws --profile "$PROFILE" --region "$REGION" iam generate-credential-report > "$OUTPUT_DIR/iam-credential-report-status.json"

TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
cat > "$OUTPUT_DIR/collection-metadata.json" <<META
{
  "collected_at_utc": "${TIMESTAMP}",
  "aws_profile": "${PROFILE}",
  "aws_region": "${REGION}",
  "controls": ["CTRL-AC-001", "CTRL-AU-001"]
}
META

echo "Evidence collection complete: $OUTPUT_DIR"
