import pytest
import os
import subprocess

from Scripts.install_ba_client import is_program_installed, install_ba_client

program_name_client = "IBM Storage Protect Client"

def test_install_ba_client():
    try:
        install_ba_client()
    except Exception as e:
        pytest.fail(f"Installation script raised an exception: {e}")

    # Step 3: Verify installation succeeded
    assert is_program_installed(program_name_client), f"{program_name_client} should be installed but was not found."

    print("Test completed: BA Client installation verified.")
