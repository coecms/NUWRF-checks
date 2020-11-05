from ..analysis import comp_LIS as lis
import pytest
import pandas as pd

time=pd.date_range("1999-05","1999-05",freq="MS")
def test_toLISdstring():
    
    assert lis.dates_to_LISdstring(time)[0] == "199905"

