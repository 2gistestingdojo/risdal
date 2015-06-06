from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from base_test_case import BaseTestCase
import unittest

class Release4Test(BaseTestCase):
    def test_change_sort(self):
        main_window = self.driver.find_element_by_id('MainWindow')
        products_list_before = main_window.find_element_by_id('ProductsMW')
        product_items_before = products_list_before.find_elements_by_class_name('ListViewItem')
        items_before = products_list_before.find_elements_by_class_name('ListViewItem')

        sort_group_box = main_window.find_element_by_id('SortGroupBoxMW')
        sort_down_check = sort_group_box.find_element_by_id('SortDownMW')
        sort_down_check.click()

        products_list_after = main_window.find_element_by_id('ProductsMW')
        product_items_after = products_list_after.find_elements_by_class_name('ListViewItem')
        items_after = products_list_after.find_elements_by_class_name('ListViewItem')

        self.assertNotEqual(items_before, items_after)

