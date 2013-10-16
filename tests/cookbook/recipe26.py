# -*- coding: utf-8 -*-
import unittest


class ShoppingCart(object):
    
    def __init__(self):
        self.items = []

    def add(self, item, price):
        for cart_item in self.items:
            # Since we found the item, we increment
            # instead of append
            if cart_item.item == item:
                cart_item.q += 1
                return self
        self.items.append(Item(item, price))
        return self

    def item(self, index):
        return self.items[index-1].item

    def price(self, index):
        return self.items[index-1].price * self.item[index-1].q

    def total(self, sales_tax):
        sum_price = sum([item.price * item.q for item in self.items])
        return sum_price * (1.0 + sales_tax / 100.0)

    def __len__(self):
        return sum([item.q for item in self.items])


class Item(object):
    
    def __init__(self, item, price, q=1):
        self.item = item
        self.price = price
        self.q = q


class CartWithOneItem(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart().add("tuna sandwich", 15.00)

    def test_when_checking_the_size_should_be_one_based(self):
        self.assertEquals(1, len(self.cart))

    def test_when_looking_into_cart_should_be_one_based(self):
        self.assertEquals("tuna sandwich", self.cart.item(1))
        self.assertEquals(15.00, self.cart.price(1))
    
    def test_total_should_have_in_sales_tax(self):
        self.assertAlmostEquals(15.0 * 1.0925, self.cart.total(9.25), 2)


class CartWithTwoItems(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart().add("tuna sandwich", 15.00) \
                                  .add("rootbeer", 3.75)

    def test_when_checking_size_should_be_two(self):
        self.assertEquals(2, len(self.cart))

    def test_items_should_be_in_same_order_as_entered(self):
        self.assertEquals("tuna sandwich", self.cart.item(1))
        self.assertAlmostEquals(15.00, self.cart.price(1), 2)
        self.assertEquals("rootbeer", self.cart.item(2))
        self.assertAlmostEquals(3.75, self.cart.price(2), 2)

    def test_total_price_should_have_in_sales_tax(self):
        self.assertAlmostEquals((15.0 + 3.75) * 1.0925, \
                                self.cart.total(9.25), 2)


class CartWithNoItems(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()

    def test_when_checking_size_should_be_empty(self):
        self.assertEquals(0, len(self.cart))

    def test_finding_item_out_of_range_should_raise_error(self):
        self.assertRaises(IndexError, self.cart.item, 2)

    def test_find_price_out_of_range_should_raise_error(self):
        self.assertRaise(IndexError, self.cart.price, 2)

    def test_when_looking_at_total_price_should_be_zero(self):
        self.assertAlmostEquals(0.0, self.cart.total(9.25), 2)

    def test_adding_items_returns_back_same_cart(self):
        empty_cart = self.cart
        cart_with_one_item = self.cart.add("tuna sandwich", 15.00)
        self.assertEquals(empty_cart, cart_with_one_item)
        cart_with_one_items = self.cart.add("rootbeer", 3.75)
        self.assertEquals(empty_cart, cart_with_one_item)
        self.assertEquals(cart_with_one_item, cart_with_two_items)
