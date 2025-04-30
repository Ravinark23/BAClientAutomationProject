import pytest

from Windows.Scripts.install_package import download_installer

program_name_client = "IBM Storage Protect Client"

def test_extract_package():
    try:
        download_installer()
    except Exception as e:
        pytest.fail(f"Package Installation script raised an exception: {e}")
