import unittest
from selenium import webdriver


def setUpModule():
    print("Executed before executing any class or any method present in the test class")

def tearDownModule():
    print("Executed after completing everything present in the module")


class LearnMethodsTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        print("Execute before every method")
        self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")

    @classmethod
    def tearDown(self) -> None:
        print("Execute After end of every method")
        self.driver.close()

    @classmethod
    def setUpClass(cls) -> None:
        print("Execute only once when the class is started: launching application")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Execute only once after the class is completed: close application")

    def test_title(self):
        # self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")
        print(f"The title of the page is {self.driver.title}")
        # self.driver.close()

    def test_pageUrl(self):
        # self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")
        print(f"The url of the page is {self.driver.current_url}")
        # self.driver.close()


if __name__ == '__main__':
    unittest.main()
