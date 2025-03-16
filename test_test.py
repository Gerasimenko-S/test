from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="C:\\Windows\\SysWOW64\\geckodriver.exe")
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(15)

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element(By.LINK_TEXT, "groups").click()

    def group_create(self, wd, name, header, footer):
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def return_to_group_page(self, webdriver):
        # return to groups page
        webdriver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self, wd):
        # logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.group_create(wd, "jfjfj", "lalalalk", "lldlldldk")
        self.return_to_group_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

