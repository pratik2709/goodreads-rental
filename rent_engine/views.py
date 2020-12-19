# Create your views here.
from rest_framework import permissions, authentication
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from rent_engine.models import BooksRented, Customer


class BookRentAPI(GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"hello": "world"}, status=HTTP_200_OK)
