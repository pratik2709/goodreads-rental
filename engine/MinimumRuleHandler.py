from json_logic import jsonLogic

from engine.AbstractHandler import AbstractHandler


class MinimumRuleHandler(AbstractHandler):

    def __init__(self, rent_rules_info, actual_duration, category):
        self.minimum_rule = rent_rules_info.get('minimum')
        self.actual_duration = actual_duration
        self.category = category

    def handle(self, total, category_charges=None):
        if self.check_if_minimum_rule_applicable():
            total = self.compute_total(total)
            category_charges = self.update_category_charges(category_charges, total)
            return category_charges, total
        else:
            return super().handle(total, category_charges)

    def update_category_charges(self, category_charges, total):
        if self.category not in category_charges:
            category_charges[self.category] = 0
        category_charges[self.category] += total
        return category_charges

    def compute_total(self, total):
        total += self.actual_duration * self.get_rent_amount()
        return total

    def get_rent_amount(self):
        rent_amount = self.minimum_rule.get('amount')
        return rent_amount

    def check_if_minimum_rule_applicable(self):
        if self.minimum_rule and bool(self.minimum_rule):
            minimum_rule_decision = jsonLogic(self.minimum_rule['rule'], {"duration": self.actual_duration})
            return minimum_rule_decision