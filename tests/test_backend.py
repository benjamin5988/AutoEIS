import pytest

from autoeis import julia_helpers


def test_init_julia():
    Main = julia_helpers.init_julia()
    assert Main.eval("1+1") == 2


def test_import_julia_modules():
    Main = julia_helpers.init_julia()

    # Ensure installed modules can be imported
    ec = julia_helpers.import_package("EquivalentCircuits", Main=Main)
    # Test Main is not required
    ec = julia_helpers.import_package("EquivalentCircuits")

    # Throw error for non-existent module
    with pytest.raises(Exception):
        julia_helpers.import_package("NonExistentModule", Main)