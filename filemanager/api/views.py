from .models import File
from django.http import JsonResponse
from .serializers import FileSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action

'''def get_file(request, pk):
    if request.method == 'GET':
        file = get_object_or_404(File, id=pk)
        serializer = FileSerializer(file)
        return JsonResponse(serializer.data)'''

'''@csrf_exempt
def upload(request):
    if request.method == 'POST':
        print('lol')
        print(request)
        serializer = FileSerializer(file=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class ApiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class DownloadViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

