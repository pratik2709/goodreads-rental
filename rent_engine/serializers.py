from rest_framework import serializers

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
            starting = StartingRuleHandler(rent_rules_info, actual_duration, category)
            categorywise_charges, total = starting.handle(total, categorywise_charges)
        return categorywise_charges
