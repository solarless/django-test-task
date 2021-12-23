from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Footballer
from .serializers import FootballerSerializer


class FootballerListCreateView(ListCreateAPIView):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer


class FootballerDeleteView(APIView):
    def delete(self, request, pk):
        footballer = get_object_or_404(Footballer, pk=pk)
        
        if footballer.number == 10:
            raise PermissionDenied(
                'You cannot delete the footballer with number 10.'
            )
        footballer.delete()

        return Response(status=204)
