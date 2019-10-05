import pytest
from pages.LoginPO import LoginPO
from pages.HomePO import HomePO
from pages.CreatenewuserPO import CreateuserPO

@pytest.mark.usefixtures("setup","one_time_setup","suite_level_setup")
class Test_case3:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("Before Class level setup")
        self.lp = LoginPO(self.driver)
        self.hp = HomePO(self.driver)
        self.cnup=CreateuserPO(self.driver)
        yield
        print("After class level setup")

    def test_createnewuser(self):
        try:
            self.lp.login("admin","manager")
            self.hp.clickusertab()
            self.hp.clicknewuserbtn()
            self.cnup.createnewuser("qspider","python","naveen","test@gmail.com","test","nav@123","nav@123","Production")

            self.hp.clicklogoutlnk()
        except:
            self.driver.get_screenshot_as_file("screenshots\\"+"test_createnewuser.png")
            raise
