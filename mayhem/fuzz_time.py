#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import random


with atheris.instrument_imports(include=['arrow']):
    import arrow


def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        arrow.get(fdp.ConsumeRemainingString())
    except (ValueError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
