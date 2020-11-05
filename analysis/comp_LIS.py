# Functions necessary to prepare LIS outputs for plotting
from ..utils import nwuchecks as nwu

def dates_to_LISdstring(time):
    '''Transform datetime "time" into a string for LIS output filenames: YYYYMM'''

    return time.strftime("%Y%m")

def read_LIS_data(sim,time):
    '''Read LIS output data. The filename is assumed to follow the convention:
    LIS.<LSM>.<startdate>.<domain>.nc
    sim: pathlib.PosixPath object directory with LIS outputs
    time: datetime object month to read data for'''

    # Convert time to a date string

    # Find all files to read
#    filelist=list(sim.glob('LIS.*{date}*.nc'))
#    return xr.open_dataset(filelist)

def comp_LIS(time,file_list,simmax=4):
    '''Function to compare the output of several LIS simulations.
    We can't use more than simmax simulations stipulated as argument.
    The first simulation is considered the "dataset". The plots are
    organised:
    1st line: monthly mean of the "dataset"
    2nd line: monthly mean of all other simulations
    3rd line: monthly mean of absolute difference of each simulation with the dataset
    4th line: relative difference of the monthly mean of each simulation with the dataset
    
    time: Datetime object month to compare
    file_list: list of string Directories containing the LIS output for all simulations
    simmax: integer Maximum number of simulations to compare'''

    # Check the number of simulations is < simmmax
    if (len(file_list)>simmax):
        raise f"Too many simulations. We can only analyse {simmax} simulations together"

    # Convert file_list elements to Path objects.   
    file_list=nwu.toPath(file_list)

    # Get all the data in a dataset.
    # Read in each data and ensure we have the same grid for all the datasets
    ds=[]
    for sim in file_list:
        da = read_LIS_data(sim,time)
        ds.append(da)