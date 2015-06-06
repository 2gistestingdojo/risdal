from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from base_test_case import BaseTestCase
import unittest

class Release5Test(BaseTestCase):
    def test_multi_removing(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        items = products_list.find_elements_by_class_name('ListViewItem')
        item_number_before_removing = len(items)
        item0 = items[0]
        item1 = items[1]

        self.driver.execute_script("input: ctrl_click", item0)
        self.driver.execute_script("input: ctrl_click", item1)

        remove_button = main_window.find_element_by_id('DeleteSelectedMW')
        remove_button.click()

        products_list_after = main_window.find_element_by_id('ProductsMW')
        items_after = products_list_after.find_elements_by_class_name('ListViewItem')
        item_number_after_removing = len(items_after)

        self.assertEqual(item_number_after_removing, item_number_before_removing - 2)
