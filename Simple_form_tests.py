import pytest
from selenium import webdriver
import urllib.parse as urlparse
from urllib.parse import parse_qs
import re


class TestSimpleForm:

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome("C:/Users/Dom/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.7/Scripts/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test complited")


    def test_correct_default_login(self, test_setup):
        driver.get("C:/Users/Dom/Desktop/PYTHON/Formularz/index2.html")
        first_name = driver.find_element_by_id("firstname-input").get_attribute("value")
        last_name = driver.find_element_by_id("lastname-input").get_attribute("value")
        assert first_name == "Mickey"
        assert last_name == "Mouse"
        submit = driver.find_element_by_id("submit-button").click()
        actual_title = driver.title
        expected_title = "Test Form"
        assert actual_title == expected_title


    def clear_fields(self):
        driver.get("C:/Users/Dom/Desktop/PYTHON/Formularz/index2.html")
        driver.find_element_by_id("firstname-input").clear()
        driver.find_element_by_id("lastname-input").clear()
        print("Text Field Cleared")

    def parse_url(self):
        current_url = driver.current_url
        parsed = urlparse.urlparse(current_url)
        url_first_name = parse_qs(parsed.query).get("firstname")[0]
        url_last_name = parse_qs(parsed.query).get("lastname")[0]
        return url_first_name, url_last_name


    def test_correct_entered_login(self, test_setup):
        self.clear_fields()
        first_name = driver.find_element_by_id("firstname-input")
        first_name.send_keys("Jan")
        last_name = driver.find_element_by_id("lastname-input")
        last_name.send_keys("Kowalski")
        submit = driver.find_element_by_id("submit-button").click()
        current_url = driver.current_url
        expected_url = "file:///C:/Users/Dom/Desktop/PYTHON/Formularz/index2.html?firstname=Jan&lastname=Kowalski"
        assert current_url == expected_url

        parsed = urlparse.urlparse(current_url)
        url_first_name = parse_qs(parsed.query)["firstname"][0]
        url_last_name = parse_qs(parsed.query)["lastname"][0]
        print(url_first_name, url_last_name)
        assert url_first_name == 'Jan' and url_last_name == 'Kowalski'


    def test_correct_login_with_special_characters(self, test_setup):
        self.clear_fields()
        first_name = driver.find_element_by_id("firstname-input")
        first_name.send_keys("Mądak")
        last_name = driver.find_element_by_id("lastname-input")
        last_name.send_keys("Hector Sausage-Hausen")
        submit = driver.find_element_by_id("submit-button").click()
        url_first_name, url_last_name = self.parse_url()
        print(bool(re.findall("([A-Za-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð\. -]+)", url_first_name)))
        print(bool(re.findall("([A-Za-zàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð\. -]+)", url_last_name)))


    def test_no_data_input(self, test_setup):
        self.clear_fields()
        first_name = driver.find_element_by_id("firstname-input")
        first_name.send_keys("Jan")
        submit = driver.find_element_by_id("submit-button").click()
        current_url = driver.current_url
        parsed = urlparse.urlparse(current_url)
        url_first_name = parse_qs(parsed.query).get("firstname")
        url_last_name = parse_qs(parsed.query).get("lastname")
        print(url_first_name, url_last_name)

        if url_first_name == None or url_last_name == None:
            print("Brak wartości w polu, nie można zatwierdzić formularza")
        else:
            print("Formularz zatwierdzony")


    def test_long_input(self, test_setup):
        self.clear_fields()
        first_name = driver.find_element_by_id("firstname-input")
        first_name.send_keys("ZbytDługiTesktDoPolaImienia")
        last_name = driver.find_element_by_id("lastname-input")
        last_name.send_keys("Hector Sausage-Hausen")
        submit = driver.find_element_by_id("submit-button").click()
        url_first_name, url_last_name = self.parse_url()
        print(url_first_name, url_last_name)

        if len(url_first_name) > 10  or len(url_last_name) > 20:
            print("Zbyt długa wartość w polu, nie można zatwierdzić formularza")
        else:
            print("Formularz zatwierdzony")


