# Library of functions for analyses of CABLE-WRF output
import xarray as xr
from pathlib import Path

def toPath(flist):
    '''convert a list of strings to a list of Path objects'''
    return [Path(x) for x in flist]