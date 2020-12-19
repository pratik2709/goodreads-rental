from engine.MinimumRuleHandler import MinimumRuleHandler
from engine.StartingAndMaximumRuleHandler import StartingAndMaximumRuleHandler
from engine.StartingRuleHandler import StartingRuleHandler


class ChainOfResponsibilityClientHandler:

    @staticmethod
    def client_handler(actual_duration, category, categorywise_charges, rent_rules_info, total):
        minimum = MinimumRuleHandler(rent_rules_info, actual_duration, category)
        starting_and_maximum = StartingAndMaximumRuleHandler(rent_rules_info, actual_duration, category)
        starting = StartingRuleHandler(rent_rules_info, actual_duration, category)
        minimum.set_next(starting_and_maximum).set_next(starting)
        categorywise_charges, total = minimum.handle(total, categorywise_charges)
        return categorywise_charges