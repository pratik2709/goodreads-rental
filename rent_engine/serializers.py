from rest_framework import serializers

from engine.MinimumRuleHandler import MinimumRuleHandler
from engine.StartingAndMaximumRuleHandler import StartingAndMaximumRuleHandler
from engine.StartingRuleHandler import StartingRuleHandler
from rent_engine.utils import BookRentAPIUtils


class BookRentSerializer(serializers.Serializer):
    Fiction = serializers.IntegerField()
    Regular = serializers.IntegerField()
    Novel = serializers.IntegerField()

    def to_representation(self, all_books_rented):
        categorywise_charges = {}
        for book_rented in all_books_rented:
            total = 0
            actual_duration, category, rent_rules_info = BookRentAPIUtils.extract_data(book_rented)
            minimum = MinimumRuleHandler(rent_rules_info, actual_duration, category)
            starting_and_maximum = StartingAndMaximumRuleHandler(rent_rules_info, actual_duration, category)
            starting = StartingRuleHandler(rent_rules_info, actual_duration, category)
            minimum.set_next(starting_and_maximum).set_next(starting)
            categorywise_charges, total = minimum.handle(total, categorywise_charges)
        return categorywise_charges
