import unittest

from engine.StartingRuleHandler import StartingRuleHandler


class TestStartingRuleHandler(unittest.TestCase):

    def setUp(self):
        rent_rules_info = {
                "starting": {
                    "rule": {">" : [ { "var" : "duration" }, 2 ]},
                    "amount": 2,
                    "unit": "day"
                }
        }
        actual_duration = 10
        self.category = "MockCategory"
        self.starting_rule_handler = StartingRuleHandler(rent_rules_info, actual_duration, self.category)

    def test_get_rent_amount(self):
        self.assertEqual(2, self.starting_rule_handler.get_rent_amount())

    def test_compute_total(self):
        self.assertEqual(21, self.starting_rule_handler.compute_total(1))

    def test_update_category_charges(self):
        category_charges = {}
        self.starting_rule_handler.update_category_charges(category_charges, 1)
        self.assertTrue(self.category in category_charges)
        self.assertEqual(1,category_charges.get(self.category))

    def test_check_if_starting_rule_applicable_when_valid(self):
        self.assertTrue(self.starting_rule_handler.check_if_starting_rule_applicable())

    def test_check_if_starting_rule_applicable_when_invalid(self):
        self.starting_rule_handler.starting_rule = {
            "rule": {">" : [ { "var" : "duration" }, 2 ]},
            "amount": 3,
            "unit": "day"
        }
        self.assertTrue(self.starting_rule_handler.check_if_starting_rule_applicable())
