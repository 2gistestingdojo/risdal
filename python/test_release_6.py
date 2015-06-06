from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from base_test_case import BaseTestCase
import unittest

class Release6Test(BaseTestCase):
    def test_change_category(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        items = products_list.find_elements_by_class_name('ListViewItem')
        item0 = items[0]
        texts = item0.find_elements_by_class_name('TextBlock')
        category_name_before = texts[2].get_attribute('Name')

        actions = ActionChains(self.driver)
        actions.double_click(item0)
        actions.perform()

        change_product_window = self.driver.find_element_by_id('ChangeProductWindow')
        category_select = change_product_window.find_element_by_id('CategoryCW')
        category_select.click()

        category_items = category_select.find_elements_by_class_name('ListBoxItem')
        category_items[0].click()

        # CategoryCW
        save_button = change_product_window.find_element_by_id('SaveCW')
        save_button.click()

        items_after = products_list.find_elements_by_class_name('ListViewItem')
        item0_after = items_after[0]
        texts_after = item0_after.find_elements_by_class_name('TextBlock')
        category_name_after = texts_after[2].get_attribute('Name')

        self.assertNotEqual(category_name_after, category_name_before)
