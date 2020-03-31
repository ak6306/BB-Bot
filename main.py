from time import sleep

from selenium import webdriver


class BigBasketBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bigbasket.com/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li[3]/ul/li['
                                          '2]/a[3]').click()
        sleep(2)
        window_before = self.driver.window_handles[0]
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[1]/login/div/div[1]/a[1]') \
            .click()
        sleep(2)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input') \
            .send_keys('your user name here')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input') \
            .send_keys('your password here')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]').click()
        sleep(2)
        self.driver.switch_to.window(window_before)
        sleep(10)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li[2]').click()
        element = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li[2]/div/a')

        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)
        sleep(5)
        status = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li['
                                                   '2]/div/div/div[2]/ul/li[1]/a/div/div/div').text
        print(status)

        while "All Slots Full." in status:
            self.driver.refresh()
            element = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li[2]/div/a')

            self.driver.execute_script("arguments[0].scrollIntoView()", element)
            self.driver.execute_script("arguments[0].click()", element)
            sleep(5)
            status = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/header/div/div/div/div/ul/li['
                                                       '2]/div/div/div[2]/ul/li[1]/a/div/div/div').text
            print("Looping!!")
            sleep(60)

        self.driver.get("https://outlook.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"loginfmt\"]").send_keys("your email here")
        self.driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[3]/div/div/div/div[3]/div['
                                          '2]/div/div/div/input').click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@type=\"password\"]").send_keys("your password here")
        self.driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button') \
            .click()
        sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div['
                                          '1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div['
                                          '1]/div/div/input').send_keys("your email here")
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div['
                                          '1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/input') \
            .send_keys("Slot Available!")
        self.driver.find_element_by_xpath("//button[@aria-label=\"Send\"]").click()
        sleep(15)


BigBasketBot()
