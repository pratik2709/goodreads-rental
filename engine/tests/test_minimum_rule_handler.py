import unittest

from engine.MinimumRuleHandler import MinimumRuleHandler


class TestMinimumRuleHandler(unittest.TestCase):

    def setUp(self):
        rent_rules_info = {
            "minimum": {
                "rule": {"<" : [ { "var" : "duration" }, 4 ]},
                "amount": 4.5,
                "unit": "overall"
            }
        }
        actual_duration = 3
        self.category = "minimum"
        self.minimum_rule_handler = MinimumRuleHandler(rent_rules_info, actual_duration, self.category)

    def test_get_rent_amount(self):
        self.assertEqual(4.5, self.minimum_rule_handler.get_rent_amount())

    def test_compute_total(self):
        self.assertEqual(14.5, self.minimum_rule_handler.compute_total(1))

    def test_update_category_charges(self):
        category_charges = {}
        self.minimum_rule_handler.update_category_charges(category_charges, 1)
        self.assertTrue(self.category in category_charges)
        self.assertEqual(1,category_charges.get(self.category))

    def test_check_if_starting_rule_applicable_when_valid(self):
        self.assertTrue(self.minimum_rule_handler.check_if_minimum_rule_applicable())

    def test_check_if_starting_rule_applicable_when_invalid(self):
        self.minimum_rule_handler.starting_rule = {
            "rule": {"<" : [ { "var" : "duration" }, 4 ]},
            "amount": 4.5,
            "unit": "overall"

        }
        self.minimum_rule_handler.actual_duration = 10
        self.assertFalse(self.minimum_rule_handler.check_if_minimum_rule_applicable())
