from base_test_case import BaseTestCase
import unittest

class Release2Test(BaseTestCase):
    def test_cancel_adding_without_name(self):

        main_window = self.driver.find_element_by_id('MainWindow')

        products_list_before = main_window.find_element_by_id('ProductsMW')
        product_items_before = products_list_before.find_elements_by_class_name('ListViewItem')
        items_number_before = len(product_items_before)

        search_button = main_window.find_element_by_id('AddNewProductMW')
        search_button.click()

        add_new_product_window = self.driver.find_element_by_id('AddNewProductWindow')
        search_button = add_new_product_window.find_element_by_id('CancelAW')
        search_button.click()

        products_list_after = main_window.find_element_by_id('ProductsMW')
        product_items_after = products_list_after.find_elements_by_class_name('ListViewItem')

        items_number_after = len(product_items_after)

        self.assertEqual(items_number_after, items_number_before)

