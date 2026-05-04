
# GLHMM Adapter for ds006072 (parcellated CIFTI)

This adapter converts parcellated CIFTI timeseries (.ptseries.nii / .dtseries.nii) into
glhmm-compatible `.npz` files containing `Y` (time x parcels) and `indices` (session boundaries).

Repository contents
- `adapter.py` — main converter script (CLI).
- `run_adapter.sh` — small wrapper to run the adapter.
- `requirements.txt` — Python dependencies.
- `example_config.yaml` — example settings.

Quick start

1. Clone the repo and create a virtualenv:

```bash
git clone https://github.com/samrosenberg425/ds006072-hmm-dynamics.git glhmm_ds006072
cd glhmm_ds006072
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the adapter on a directory of parcellated CIFTI files:

```bash
python3 adapter.py --input /full/path/to/parcellated_cifti_timeseries/Schaefer400_17Networks_TianS2 --output /full/path/to/output_npz
```

3. The output folder will contain `.npz` files compatible with the `glhmm` pipeline (keys: `Y`, `indices`).

Notes
- If you only want a single file converted, pass the full file path to `--input`.
- For large batches use the provided `run_adapter.sh` or schedule via SLURM (example in this repo issues).

Contributing

Contributions welcome — see `CONTRIBUTING.md` for guidelines.

License

This project is released under the MIT License (see `LICENSE`).

