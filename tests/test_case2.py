import pytest
from pages.LoginPO import LoginPO
from pages.HomePO import HomePO


@pytest.mark.usefixtures("setup","one_time_setup","suite_level_setup")
class Test_case1:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("Before Class level setup")
        self.lp  = LoginPO(self.driver)
        self.hp = HomePO(self.driver)
        yield
        print("After class level setup")

    def test_validlogin(self):
        print("Executing test method A")
        try:
            self.lp.login("admin","manager")

            self.hp.clicklogoutlnk()
        except:
            self.driver.get_screenshot_as_file("screenshots\\"+"test_validlogin.png")

