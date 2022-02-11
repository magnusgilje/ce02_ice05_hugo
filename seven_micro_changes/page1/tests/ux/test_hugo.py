"""hugo pytest suite"""
# pylint: disable=unused-import, import-error, no-member

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class TestHugo:
    """Test Hugo site with Selenium"""

    def get_default_url(self,url):
        """get default url for site"""
        # pylint: disable=no-self-use, no-else-return

        if url[-1] != "/":
            return url + "/"
        else:
            return url

    def get_default_title(self):
        """get default title for site"""
        # pylint: disable=no-self-use
        return "Seven Years War"

    def get_button_by_link_name(self, linktext):
        """find a button based on in its link text"""
        return self.driver.find_element(By.LINK_TEXT, linktext)

    def wait_for_page_to_load(self,url,title):
        """wait 15 seconds to allow a page to fully load"""
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            lambda driver: title in self.driver.title
        )

    def load_index_page(self,url):
        """get the site main page"""
        self.wait_for_page_to_load(url,self.get_default_title())


    def test_index_page(self,url):
        """test the index page for a hugo site"""
        page_url = self.get_default_url(url)
        title = self.get_default_title()

        self.load_index_page(url)
        assert title == self.driver.title
        assert page_url == self.driver.current_url
        self.driver.save_screenshot("test_index_page_00.png")

    def test_first_year_post(self,url):
        """test the first-year post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/first-year/"
        page_title = "The Year 1756 | "+self.get_default_title()

        second_post = self.get_button_by_link_name("The Year 1756")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        # social media links

        # facebook_placeholder = self.driver.find_element(By.CSS_SELECTOR, '.facebook')
        # assert facebook_placeholder is not None

        # twitter_placeholder = self.driver.find_element(By.CSS_SELECTOR,".twitter")
        # assert twitter_placeholder is not None

        # linedin_placeholder = self.driver.find_element(By.CSS_SELECTOR,".linkedin")
        # assert linedin_placeholder is not None


        self.driver.save_screenshot("test_first_year.png")

    def test_first_year_post(self,url):
        """test the first-year post"""
        self.load_index_page(url)

        page_url = self.get_default_url(url)+"posts/first-year/"
        page_title = "The Year 1756 | "+self.get_default_title()

        second_post = self.get_button_by_link_name("The Year 1756")
        second_post.click()

        self.wait_for_page_to_load(page_url,page_title)

        assert page_title == self.driver.title
        assert page_url == self.driver.current_url

        self.driver.save_screenshot("test_first_year.png")

 