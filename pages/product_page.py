from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
  def guest_can_add_product_to_cart(self):
    # self.should_be_button_add_product_to_cart()
    name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
    price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text[0:5]
    self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
    self.solve_quiz_and_get_code()
    name_of_allert = self.browser.find_element(*ProductPageLocators.NAME_OF_ALLERT).text
    price_of_allert = self.browser.find_element(*ProductPageLocators.PRICE_OF_ALLERT).text[0:5]
    
    assert name_of_product == name_of_allert, "Name of the product not the same as allert!"
    assert price_of_product == price_of_allert, "Price of the product not the same as allert!" 

  def should_be_button_add_product_to_cart(self):
    assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add product to cart is not presented!"
  