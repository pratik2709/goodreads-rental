import unittest

from engine.StartingAndMaximumRuleHandler import StartingAndMaximumRuleHandler


class TestStartingAndMaximumRuleHandler(unittest.TestCase):

    def setUp(self):
        rent_rules_info = {
                "starting": {
                    "rule": {"<=" : [ { "var" : "duration" }, 3 ]},
                    "amount": 1,
                    "unit": "day"
                },
                "maximum": {
                    "rule": {">" : [ { "var" : "duration" }, 3 ]},
                    "amount": 1.5,
                    "unit": "day"
                },
        }
        actual_duration = 10
        self.category = "MockCategory"
        self.starting_and_maximum_rule_handler = StartingAndMaximumRuleHandler(rent_rules_info, actual_duration, self.category)

    def test_get_rent_amount_for_maximum(self):
        self.assertEqual(1.5, self.starting_and_maximum_rule_handler.get_rent_amount_for_maximum())

    def test_get_rent_amount_for_starting(self):
        self.assertEqual(1, self.starting_and_maximum_rule_handler.get_rent_amount_for_starting())

    def test_apply_maximum_and_starting_rules(self):
        self.starting_and_maximum_rule_handler.actual_duration = 10
        t = (3 + (7*1.5)) + 1
        self.assertEqual(t, self.starting_and_maximum_rule_handler.apply_maximum_and_starting_rules(1))

    def test_update_category_charges(self):
        category_charges = {}
        self.starting_and_maximum_rule_handler.update_category_charges(category_charges, 1)
        self.assertTrue(self.category in category_charges)
        self.assertEqual(1,category_charges.get(self.category))

    def test_check_if_maximum_rule_applicable_when_valid(self):
        self.assertTrue(self.starting_and_maximum_rule_handler.check_if_maximum_rule_applicable())

    def test_check_if_maximum_rule_applicable_when_invalid(self):
        self.starting_and_maximum_rule_handler.actual_duration = 1
        self.assertFalse(self.starting_and_maximum_rule_handler.check_if_maximum_rule_applicable())
