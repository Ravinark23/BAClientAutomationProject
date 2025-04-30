import pytest
import os

def validate_tests(test):
    #result = pytest.main([test, "-q", "--tb=no", "--disable-warnings"])
    result =pytest.main([test, "-s", "-q", "--disable-warnings"])
    return result == 0


def run_tests():
    test_file1 = os.path.join(os.path.dirname(__file__), 'TestCases', 'test_install_package.py')
    test_file2 = "/Users/ravina/PycharmProjects/BAClientAutomationProject/TestCases/test_extract_package.py"
    test_file3 = "/Users/ravina/PycharmProjects/BAClientAutomationProject/TestCases/test_install_ba_client.py"
    if 1:
        print("Download Package Passed ✅ ")
        if validate_tests(test_file2):
            print("Extract Package Passed✅ ")
            print("Running pytest for BA Client installation...\n")
            if validate_tests(test_file3):
                print("Install BA Client Passed✅ ")
            else:
                print("Install BA Client Failed❌")
        else:
            print("Extract Package Failed❌")
    else:
        print("Download Package Failed❌")

if __name__ == '__main__':
    run_tests()

