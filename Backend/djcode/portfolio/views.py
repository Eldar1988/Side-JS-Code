from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioListView(APIView):
    def get(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)


class PortfolioDetailView(APIView):
    def get(self, request, slug):
        portfolio = Portfolio.objects.get(slug=slug)
        serializer = PortfolioSerializer(portfolio, many=False)
        return Response(serializer.data)
