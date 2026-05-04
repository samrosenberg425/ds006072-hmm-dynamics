#!/usr/bin/env python3
"""Adapter: convert parcellated CIFTI (.ptseries/.dtseries) to glhmm .npz files

Saves: np.savez(output_file, X=np.empty((0,)), Y=Y, indices=indices)
"""
from pathlib import Path
import argparse
import nibabel as nb
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def find_files(input_dir, pattern='*.ptseries.nii'):
    p = Path(input_dir)
    return sorted([str(x) for x in p.rglob(pattern)])


def load_ptseries(path):
    img = nb.load(str(path))
    data = np.array(img.get_fdata())
    # Ensure time x parcels
    if data.ndim == 2:
        t, p = data.shape
        if t < p and p >= 10:
            data = data.T
    elif data.ndim == 1:
        data = data[:, None]
    return data


def convert_file(path, out_dir, suffix=None):
    Y = load_ptseries(path)
    indices = np.array([[0, Y.shape[0]]], dtype=int)
    stem = Path(path).stem
    if suffix:
        out_name = f"{stem}_{suffix}.npz"
    else:
        out_name = f"{stem}.npz"
    out_path = Path(out_dir) / out_name
    np.savez(out_path, X=np.empty((0,)), Y=Y, indices=indices)
    logging.info('Wrote %s (T=%d, p=%d)', out_path, Y.shape[0], Y.shape[1])
    return str(out_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', '-i', required=True, help='Input directory or file')
    ap.add_argument('--output', '-o', required=True, help='Output directory')
    ap.add_argument('--pattern', default='*.ptseries.nii', help='Glob pattern to find parcellated files')
    ap.add_argument('--suffix', default=None, help='Optional suffix for output files')
    args = ap.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    if in_path.is_file():
        files = [str(in_path)]
    else:
        files = find_files(in_path, args.pattern)

    if not files:
        logging.error('No files found in %s matching %s', in_path, args.pattern)
        raise SystemExit(1)

    written = []
    for f in files:
        try:
            written.append(convert_file(f, out_dir, suffix=args.suffix))
        except Exception as e:
            logging.exception('Failed to convert %s: %s', f, e)

    logging.info('Converted %d files', len(written))


if __name__ == '__main__':
    main()
