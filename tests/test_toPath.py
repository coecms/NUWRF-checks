from ..utils import nwuchecks as nwu
import pathlib
import pytest

def test_empty():
    assert len(nwu.toPath([]))==0

def test_nostring():
    with pytest.raises(TypeError):
        nwu.Path([1])

def test_Path():
    assert all([isinstance(x,pathlib.PosixPath) for x in nwu.toPath([pathlib.Path("/g/data/w35/ccc561")])])

def test_strings():
    assert all([isinstance(x,pathlib.PosixPath) for x in nwu.toPath(["/g/data/w35/ccc561","/g/data"])])

# %%
# %%
