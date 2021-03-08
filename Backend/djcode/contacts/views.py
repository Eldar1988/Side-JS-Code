from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CallBack
from .serializers import CallBackSerializer
from .bot import tg_send_call_back


class CallBackCreateView(APIView):

    def post(self, request):
        serializer = CallBackSerializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.save()
            tg_send_call_back(obj)
            return Response(status=201)

        return Response(status=400)
