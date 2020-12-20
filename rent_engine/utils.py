class BookRentAPIUtils:

    @staticmethod
    def extract_data(book_rented):
        rent_rules_info = book_rented.book.category.rules
        actual_duration = book_rented.days_rented
        category = book_rented.book.category.name
        return actual_duration, category, rent_rules_info

    @staticmethod
    def create_meta_data_dict(book_rented, category, categorywise_charges, meta_data):
        if category in meta_data:
            meta_data[category]['charges'] = categorywise_charges[category]
            dat = {"book_name": book_rented.book.name,
                   "date_rented": book_rented.date_rented,
                   "date_deposited": book_rented.date_deposited}
            if 'books' in meta_data[category]:
                meta_data[category]['books'].append(dat)
            else:
                meta_data[category]['books'] = [dat]
        else:
            meta_data[category] = {}
            meta_data[category]['charges'] = categorywise_charges[category]
            dat = {"book_name": book_rented.book.name,
                   "date_rented": book_rented.date_rented,
                   "date_deposited": book_rented.date_deposited}
            meta_data[category]['books'] = [dat]