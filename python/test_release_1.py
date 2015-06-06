from base_test_case import BaseTestCase
import unittest

class Release1Test(BaseTestCase):
    def test_search_by_name_with_button_click(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        search_string = main_window.find_element_by_id('QueryMW')
        search_string.send_keys(' ', '1')

        search_button = main_window.find_element_by_id('SearchMW')
        search_button.click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')

        self.assertEqual(len(product_items), 0)

    def test_search_by_name_with_button_click(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        search_string = main_window.find_element_by_id('QueryMW')
        search_string.send_keys('s', 'O', 'N', 'Y')

        search_button = main_window.find_element_by_id('SearchMW')
        search_button.click()

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')

        self.assertEqual(len(product_items), 1)
