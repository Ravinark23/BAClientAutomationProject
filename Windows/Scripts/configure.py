import time
from pywinauto import Application, Desktop
import subprocess


programpath = r"C:\Program Files\Tivoli\TSM\baclient\dsm.exe"

# Next --> radio - create a new options file --> Node Name Type and then Next  --> Server Name and Port No Type and then Next --> Next ---> Next----Next --> Apply --> Finish

def configure_ba_client():
    try:
        app = Application(backend="win32").start(programpath)
        time.sleep(10)
        print("Opening Configuration window")
        dlg = Desktop(backend="win32").window(title="IBM Storage Protect Client Configuration Wizard")
        dlg.child_window(title="&OK", class_name="Button").click()
    except Exception as e:
        print(f"Configuration failed due to an unexpected error: {e}")


if __name__ == "__main__":
    configure_ba_client()










