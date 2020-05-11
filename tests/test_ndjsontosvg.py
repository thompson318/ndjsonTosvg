# coding=utf-8

"""ndjsonTosvg tests"""
import pytest
from ndjsontosvg.ndjsontosvg import ndjsontosvg

# Pytest style

def test_default():
    filein = 'tests/data/mushroom_10.ndjson'
    fileout = 'tests/.output'
    samples = 1
    ndjsontosvg(filein, samples, outdir = fileout)





