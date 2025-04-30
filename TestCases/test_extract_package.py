import pytest
import os
import subprocess

from Scripts.extract_package import extract_installer

program_name_client = "IBM Storage Protect Client"

def test_extract_package():
    try:
        extract_installer()
    except Exception as e:
        pytest.fail(f"Package Extraction script raised an exception: {e}")
