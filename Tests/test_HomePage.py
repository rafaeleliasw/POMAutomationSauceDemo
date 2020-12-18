from Tests.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_addtocart(self):
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        assert self.header.get_cart_items() == "3"

    def test_removefromhomepage(self):
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        assert self.header.get_cart_items() == "2"
        self.homePage.remove_backpack_fromcart()
        assert self.header.get_cart_items() == "1"
