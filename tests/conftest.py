import pytest
from base.WebdriverFactory import webdriverFactory


@pytest.yield_fixture()
def setup():
    print("Executing setup function before every test case")
    yield
    print("Executing setup function after every test case")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, suite_level_setup):
    print("Executing one time setup function before every module")
    wdf = webdriverFactory(suite_level_setup)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()
    print("Executing one time setup function after every module")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.yield_fixture(scope="session")
def suite_level_setup(request):
    print("Executing one time setup function before suite")
    return request.config.getoption("--browser")
    #print("Executing one time setup function before suite")
   # yield
    #print("Executing one time setup function after suite")

