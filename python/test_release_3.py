from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from base_test_case import BaseTestCase
import unittest

class Release3Test(BaseTestCase):
    def test_save_edition(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        items = products_list.find_elements_by_class_name('ListViewItem')
        item0 = items[0]
        id_item = item0.find_elements_by_class_name('TextBlock')
        id_before_change = id_item[0].get_attribute('Name')


        actions = ActionChains(self.driver)
        actions.double_click(item0)
        actions.perform()

        change_product_window = self.driver.find_element_by_id('ChangeProductWindow')
        save_button = change_product_window.find_element_by_id('SaveCW')
        save_button.click()

        items_after = products_list.find_elements_by_class_name('ListViewItem')
        item0_after = items_after[0]
        id_item_after = item0_after.find_elements_by_class_name('TextBlock')
        id_after_change = id_item_after[0].get_attribute('Name')

        self.assertEqual(id_after_change, id_before_change)

    def test_save_edition_2(self):
        main_window = self.driver.find_element_by_id('MainWindow')

        products_list = main_window.find_element_by_id('ProductsMW')
        product_items = products_list.find_elements_by_class_name('ListViewItem')
        items = products_list.find_elements_by_class_name('ListViewItem')
        item0 = items[0]
        id_item = item0.find_elements_by_class_name('TextBlock')
        id_before_change = id_item[0].get_attribute('Name')


        actions = ActionChains(self.driver)
        actions.double_click(item0)
        actions.perform()

        change_product_window = self.driver.find_element_by_id('ChangeProductWindow')
        search_string = change_product_window.find_element_by_id('NameCW')
        search_string.send_keys('1')

        save_button = change_product_window.find_element_by_id('SaveCW')
        save_button.click()

        items_after = products_list.find_elements_by_class_name('ListViewItem')
        item0_after = items_after[0]
        id_item_after = item0_after.find_elements_by_class_name('TextBlock')
        id_after_change = id_item_after[0].get_attribute('Name')

        self.assertEqual(id_after_change, id_before_change)