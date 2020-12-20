from rest_framework import serializers

from engine.ChainOfResponsibilityClientHandler import ChainOfResponsibilityClientHandler
from rent_engine.utils import BookRentAPIUtils


class BookRentSerializer(serializers.Serializer):

    def to_representation(self, all_books_rented):
        meta_data = dict()
        categorywise_charges = {}
        for book_rented in all_books_rented:
            actual_duration, category, rent_rules_info = BookRentAPIUtils.extract_data(book_rented)
            categorywise_charges = ChainOfResponsibilityClientHandler.client_handler(actual_duration,
                                                                                     category,
                                                                                     categorywise_charges,
                                                                                     rent_rules_info,
                                                                                     total=0)
            BookRentAPIUtils.create_meta_data_dict(book_rented, category, categorywise_charges, meta_data)

        return meta_data




