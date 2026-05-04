# GLHMM Adapter for ds006072 (parcellated CIFTI)

This small adapter converts parcellated CIFTI timeseries (.ptseries.nii / .dtseries.nii) into
glhmm-compatible `.npz` files containing `Y` (time x parcels) and `indices` (session boundaries).

Quick start

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Run adapter (example):

```bash
./run_adapter.sh \
  --input /path/to/parcellated_cifti_timeseries/Schaefer400_17Networks_TianS2 \
  --output /path/to/output_npz
```

Files produced: `subject_<...>_Schaefer400_17Networks_TianS2.npz` with keys `Y` and `indices`.

Next steps: point the main `glhmm` pipeline at the generated `.npz` files.

License: MIT
