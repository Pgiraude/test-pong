from django.http import JsonResponse
from .models import Ball
from .serializers import BallSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny


@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def coordManager(request):
    if request.method == "GET":
        ball = Ball.objects.all()
        serializer = BallSerializer(ball, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        ball = Ball.objects.filter(name=request.data.get('name')).first()
        if ball:
            serializer = BallSerializer(ball, data=request.data, partial=True)
        else:  # if the ball doesn't exist, create it
            serializer = BallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if ball:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


