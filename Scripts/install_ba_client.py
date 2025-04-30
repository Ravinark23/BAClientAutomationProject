import time
from pywinauto import Application, Desktop
import subprocess

# Define program names
program_name_client = "IBM Storage Protect Client"
program_name_jvm = "IBM Storage Protect JVM"  # Adjust this name as needed

programpath = r"C:\Users\onecloud-user\Downloads\TSMClient\spinstall.exe"


def check_program_using_powershell(program_name):
    """
    Use PowerShell to check if a program is installed.
    """
    try:
        # Run PowerShell command to get installed programs
        result = subprocess.run(
            ["powershell", "-Command",
             f"Get-WmiObject -Class Win32_Product | Where-Object {{ $_.Name -like '*{program_name}*' }}"],
            capture_output=True, text=True
        )

        # Check if output contains the program name
        if result.stdout.strip():
            return True
        return False
    except Exception as e:
        print(f"Error checking program via PowerShell: {e}")
        return False


def is_program_installed(program_name):
    """
    Check if a program is installed by using PowerShell.
    """
    if check_program_using_powershell(program_name):
        print(f"{program_name} is installed.")
        return True
    return False


def install_ba_client():
    try:
        # Check if IBM Storage Protect Client is already installed
        if is_program_installed(program_name_client):
            print(f"{program_name_client} is already installed. Skipping installation.")
            return  # Exit if client is already installed

        app = Application(backend="win32").start(programpath)
        time.sleep(3)
        dlg = Desktop(backend="win32").window(title="IBM Storage Protect Client - InstallShield Wizard")

        # Select the language
        combo = dlg.child_window(title="English (United States)", class_name="ComboBox")
        combo.select("English (United States)")  # Select the option in ComboBox
        dlg.child_window(title="&OK", class_name="Button").click()

        # If JVM is already installed, skip the first Install button
        if is_program_installed(program_name_jvm):
            print(f"{program_name_jvm} is already installed. Skipping first Install button.")
        else:
            # Click Install button if JVM is not installed
            install_btn = dlg.child_window(title="Install", class_name="Button")
            install_btn.wait("exists enabled visible ready", timeout=60)
            install_btn.click_input()

        # Click Next button twice
        next_btn = dlg.child_window(title="&Next >", class_name="Button")
        next_btn.wait("exists enabled visible ready", timeout=30)
        next_btn.click_input()

        next_btn = dlg.child_window(title="&Next >", class_name="Button")
        next_btn.wait("exists enabled visible ready", timeout=30)
        next_btn.click_input()

        # Select Typical installation
        typical_radio_button = dlg.child_window(title="&Typical", class_name="Button")
        typical_radio_button.click_input()  # Select the "Typical" option

        # Click Next
        next_btn = dlg.child_window(title="&Next >", class_name="Button")
        next_btn.wait("exists enabled visible ready", timeout=30)
        next_btn.click_input()

        # Click Install again
        install_btn = dlg.child_window(title="&Install", class_name="Button")
        install_btn.wait("exists enabled visible ready", timeout=30)
        install_btn.click_input()

        # Wait for Finish button and click it
        finish_btn = dlg.child_window(title="&Finish", class_name="Button")
        finish_btn.wait("exists enabled visible ready", timeout=1800)
        finish_btn.click_input()

        print("Installation completed successfully!")

    except Exception as e:
        print(f"Installation failed due to an unexpected error: {e}")


if __name__ == "__main__":
    install_ba_client()
