# Create your views here.
from rest_framework import permissions, authentication
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rent_engine.models import BooksRented, Customer
from rent_engine.serializers import BookRentSerializer


class BookRentAPI(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = self.get_queryset()
        serialiser = BookRentSerializer(queryset)
        data = serialiser.data
        return Response(data, status=HTTP_200_OK)

    def get_queryset(self):
        user_object = self.request.user
        customer = Customer.objects.get(user=user_object)
        all_books_rented = BooksRented.objects.filter(customer=customer, active=False, book__category__version=1)
        return all_books_rented
