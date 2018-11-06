from django.test import TestCase
from . import views

# Create your tests here.


class TestAssignedRequest(TestCase):

    def test_create_item(self):
        test_item = views.item("Pink Hammer", 253, "Pink Metal Hammer", 55, 199)

        self.assertEqual(test_item.name, "Pink Hammer")
        self.assertEqual(test_item.part_num, 253)
        self.assertEqual(test_item.description, "Pink Metal Hammer")
        self.assertEqual(test_item.material, 55)
        self.assertEqual(test_item.price, 199)

    def test_create_address(self):
        test_address = views.address("Chicago", "333 State Street", "60633", "IL", "USA")
        self.assertEqual(test_address.city, "Chicago")
        self.assertEqual(test_address.street, "333 State Street")
        self.assertEqual(test_address.zipcode, "60633")
        self.assertEqual(test_address.state, "IL")
        self.assertEqual(test_address.country, "USA")

    def test_create_vendor(self):
        test_address = views.address("Chicago", "333 State Street", "60633", "IL", "USA")
        test_item1 = views.item("Pink Hammer", 253, "Pink Metal Hammer", 55, 199)
        test_item2 = views.item("Blue Hammer", 364, "Blue Wood Hammer", 23, 400)
        test_vendor = views.vendor(4, "Abc", "723-999-2994", "abc@abc.com", test_address, [test_item1, test_item2],
                                   is_redbook=True)

        self.assertEqual(test_vendor.vendor_id, 4)
        self.assertEqual(test_vendor.name, "Abc")
        self.assertEqual(test_vendor.phone, "723-999-2994")
        self.assertEqual(test_vendor.email, "abc@abc.com")
        self.assertEqual(test_vendor.address, test_address)
        self.assertEqual(test_vendor.inventory, [test_item1, test_item2])
        self.assertEqual(test_vendor.is_redbook, True)

    def test_create_source_request(self):
        test_address = views.address("Chicago", "333 State Street", "60633", "IL", "USA")
        test_item1 = views.item("Pink Hammer", 253, "Pink Metal Hammer", 55, 199)
        test_item2 = views.item("Blue Hammer", 364, "Blue Wood Hammer", 23, 400)
        test_vendor = views.vendor(4, "Abc", "723-999-2994", "abc@abc.com", test_address, [test_item1, test_item2],
                                   is_redbook=True)
        test_request = views.source_request(1, "Open", "Electric", "Z11403992", "AckBee", "Sujay", "7/1/2018",
                                            "7/4/2018", 5, test_vendor, 2)

        self.assertEqual(test_request.request_id, 1)
        self.assertEqual(test_request.status, "Open")
        self.assertEqual(test_request.source_type, "Electric")
        self.assertEqual(test_request.tracking_num, "Z11403992")
        self.assertEqual(test_request.mfg_brand, "AckBee")
        self.assertEqual(test_request.customer_name, "Sujay")
        self.assertEqual(test_request.req_date, "7/1/2018")
        self.assertEqual(test_request.rfq_date, "7/4/2018")
        self.assertEqual(test_request.group_id, 5)
        self.assertEqual(test_request.vendor, test_vendor)
        self.assertEqual(test_request.user_id, 2)

    # TODO: Finish this test
    def test_vendor_data(self):
        pass
