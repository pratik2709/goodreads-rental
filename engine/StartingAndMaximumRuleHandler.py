from json_logic import jsonLogic

from engine.AbstractHandler import AbstractHandler


class StartingAndMaximumRuleHandler(AbstractHandler):

    def __init__(self, rent_rules_info, actual_duration, category):
        self.maximum_rule = rent_rules_info.get('maximum')
        self.starting_rule = rent_rules_info.get('starting')
        self.actual_duration = actual_duration
        self.category = category

    def handle(self, total, category_charges=None):
        if self.check_if_maximum_rule_applicable():
            total = self.apply_maximum_and_starting_rules(total)
            category_charges = self.update_category_charges(category_charges, total)
            return category_charges, total
        else:
            return super().handle(total, category_charges)

    def apply_maximum_and_starting_rules(self, total):
        while self.actual_duration > 0:
            if self.check_if_starting_rule_applicable():
                total += self.get_rent_amount_for_starting()
            elif self.check_if_maximum_rule_applicable():
                total += self.get_rent_amount_for_maximum()
            self.actual_duration -= 1
        return total

    def get_rent_amount_for_maximum(self):
        rent_amount = self.maximum_rule.get('amount')
        return rent_amount

    def get_rent_amount_for_starting(self):
        rent_amount = self.starting_rule.get('amount')
        return rent_amount

    def check_if_maximum_rule_applicable(self):
        if self.maximum_rule and bool(self.maximum_rule):
            maximum_rule_decision = jsonLogic(self.maximum_rule['rule'], {"duration": self.actual_duration})
            return maximum_rule_decision

    def check_if_starting_rule_applicable(self):
        if self.starting_rule and bool(self.starting_rule):
            return jsonLogic(self.starting_rule['rule'], {"duration": self.actual_duration})

    def update_category_charges(self, category_charges, total):
        if self.category not in category_charges:
            category_charges[self.category] = 0
        category_charges[self.category] += total
        return category_charges

