class BookRentAPIUtils:

    @staticmethod
    def extract_data(book_rented):
        rent_rules_info = book_rented.book.category.rules
        actual_duration = book_rented.days_rented
        category = book_rented.book.category.name
        return actual_duration, category, rent_rules_info