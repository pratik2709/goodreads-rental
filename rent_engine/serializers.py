from rest_framework import serializers

from engine.ChainOfResponsibilityClientHandler import ChainOfResponsibilityClientHandler
from rent_engine.utils import BookRentAPIUtils


class BookRentSerializer(serializers.Serializer):
    Fiction = serializers.IntegerField()
    Regular = serializers.IntegerField()
    Novel = serializers.IntegerField()

    def to_representation(self, all_books_rented):
        meta_data = dict()
        meta_data['user'] = all_books_rented[0].customer.user.username
        categorywise_charges = {}
        for book_rented in all_books_rented:
            actual_duration, category, rent_rules_info = BookRentAPIUtils.extract_data(book_rented)
            categorywise_charges = ChainOfResponsibilityClientHandler.client_handler(actual_duration,
                                                                                     category,
                                                                                     categorywise_charges,
                                                                                     rent_rules_info,
                                                                                     total=0)
        print(meta_data)
        return categorywise_charges


