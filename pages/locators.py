from selenium.webdriver.common.by import By


class MainPageLocators(object):
  LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
  LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
  REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
  ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
  NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
  PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main>.price_color")
  NAME_OF_ALLERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong")
  PRICE_OF_ALLERT = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p>strong")

  
  
