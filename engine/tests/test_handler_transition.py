import unittest
from unittest.mock import Mock

from engine.MinimumRuleHandler import MinimumRuleHandler
from engine.StartingRuleHandler import StartingRuleHandler


class TestHandlerTransition(unittest.TestCase):

    def setUp(self):
        rent_rules_info = {
            "minimum": {
                "rule": {"<" : [ { "var" : "duration" }, 4 ]},
                "amount": 4.5,
                "unit": "overall"
            }
        }
        actual_duration = 5
        self.category = "MockCategory"
        self.minimum_rule_handler = MinimumRuleHandler(rent_rules_info, actual_duration,self.category)
        starting = Mock(spec=StartingRuleHandler)
        self.minimum_rule_handler.set_next(starting)
        self.minimum_rule_handler._next_handler.handle = Mock()

    def test_transition(self):
        self.minimum_rule_handler.handle(0, {})
        self.minimum_rule_handler._next_handler.handle.assert_called_once()
