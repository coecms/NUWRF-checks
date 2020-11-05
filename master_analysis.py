#%%
import xarray as xr
from pathlib import Path
import pandas as pd
import argparse as ap
from lib import checkoutput_lib as co
import yaml
#%%
def read_yaml(filename):
    '''Read the inputs from the yaml file. Transform them
    to useful formats and output as dictionary.
    filename: str name of the YAML file to read'''

    with open(filename,"r") as in_data:
        dd = yaml.load(in_data)

    pdata={}
    # get LIS output directories
    pdata["dir_lis"]=dd["dir_lis"]

    # Create an date array of months between start and end
    pdata["dates"]=pd.date_range(start=dd["start_date"],end=dd["end_date"],freq="MS")
    
    return pdata
# %%
#dir_lisout=[Path("/g/data/w35/ccc561/LIS-WRF/LISWRF_configs/hires_up/LIS_output")]
#list(dir_lisout[0].glob("*.nc"))
# %%
# Dates:
#start=pd.to_datetime("1999-05")
#end=pd.to_datetime("1999-05")
# %%
if __name__ == "__main__":

    # Read inputs from yaml file
    in_data = read_yaml("input.yaml")

    # Open file to save plots

    for time in in_data["dates"]:
        # Choose the analysis to perform
        #co.comp_AWAP()
        co.comp_LIS(time,in_data["dir_lis"])

        print(time)
    pass

# %%
