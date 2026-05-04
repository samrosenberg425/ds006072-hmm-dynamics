#!/usr/bin/env bash
set -euo pipefail
# Example runner for the adapter
INPUT=${1:-/path/to/parcellated_cifti_timeseries/Schaefer400_17Networks_TianS2}
OUTPUT=${2:-./output_npz}
PATTERN=${3:-"*.ptseries.nii"}

python3 adapter.py --input "$INPUT" --output "$OUTPUT" --pattern "$PATTERN"
