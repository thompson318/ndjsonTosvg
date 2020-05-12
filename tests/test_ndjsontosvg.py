# coding=utf-8

"""ndjsonTosvg tests"""
import pytest
import os
import warnings
from ndjsontosvg.ndjsontosvg import ndjsontosvg

# Pytest style

def test_default():
    filein = 'tests/data/mushroom_10.ndjson'
    fileout = 'tests/output'
    samples = 1
    with pytest.raises(IOError):
        ndjsontosvg(filein, samples, outdir = fileout)

    os.mkdir(fileout)

    ndjsontosvg(filein, samples, outdir = fileout)
    
    assert os.path.isfile(os.path.join(fileout, 'mushroom_10_0000.svg'))

def test_settings():
    filein = 'tests/data/mushroom_10.ndjson'
    fileout = 'tests/output'
    samples = 9
    outsize = 600
    linecolour = 'white'
    backgroundcolour = 'black'
    checkifidentified = False
    randomsort = False
    inputsize = 256
    
    if not os.path.isdir(fileout):
        os.mkdir(fileout)

    ndjsontosvg(filein, samples, outsize, linecolour, backgroundcolour,
                fileout, checkifidentified, randomsort, inputsize)

    assert os.path.isfile(os.path.join(fileout, 'mushroom_10_0008.svg'))
    
    samples = 10

    ndjsontosvg(filein, samples, outsize, linecolour, backgroundcolour,
                fileout, checkifidentified, randomsort, inputsize)

    assert os.path.isfile(os.path.join(fileout, 'mushroom_10_0009.svg'))

    checkifidentified = True
    
    with pytest.warns(UserWarning):
        ndjsontosvg(filein, samples, outsize, linecolour, backgroundcolour,
                    fileout, checkifidentified, randomsort, inputsize)
    
    samples = 10001
    with pytest.raises(ValueError):
        ndjsontosvg(filein, samples, outsize, linecolour, backgroundcolour,
                    fileout, checkifidentified, randomsort, inputsize)
