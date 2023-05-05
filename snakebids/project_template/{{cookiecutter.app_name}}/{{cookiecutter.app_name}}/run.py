#!/usr/bin/env python3
from pathlib import Path

from snakebids.app import SnakeBidsApp
from snakebids.plugins.validate import BidsValidator


def get_parser():
    """Exposes parser for sphinx doc generation, cwd is the docs dir"""
    app = SnakeBidsApp("../")
    return app.parser


def main():
    app = SnakeBidsApp(
        Path(__file__).resolve().parent.parent,  # to get repository root
        plugins=[BidsValidator],
    )
    app.run_snakemake()


if __name__ == "__main__":
    main()
