import pytest
from pages.LoginPO import LoginPO
from pages.HomePO import HomePO
from ddt import ddt,unpack,data
from utilities.readdata import getcsvdata

@pytest.mark.usefixtures("setup","one_time_setup","suite_level_setup")
@ddt
class Test_case4:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("Before Class level setup")
        self.lp  = LoginPO(self.driver)
        self.hp = HomePO(self.driver)
        yield
        print("After class level setup")

    @data(*getcsvdata("C:\\Users\\shekar\\PycharmProjects\\AutomatiomFWsep\\testdata.csv"))
    @unpack
    def test_invalidlogin(self,admin,pwd):
        try:
            self.lp.login(admin,pwd)
            assert self.lp.errormsgvalidation() == "Username or Password is invalid. Please try "

        except:
            self.driver.get_screenshot_as_file("screenshots\\"+"test_invalidlogin.png")
            raise
