from rest_framework.views import APIView
from .serializer import ContentSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from ....models import Content

class ContentListApiView(APIView):
    def get(self, request: Request):
        # 1. we need find all content instances
        # 2. serialize them 
        # 3. return the response with proper status code 
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class ContentCreateApiView(APIView):
    def post(self, request:Request):
        # 1. first we need to serialize the data from the request
        # 2. check if the data is serialized and valid 
        # 3. persist the created instance by calling .save()
        # 4. return the proper response 
        serilizer = ContentSerializer(request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.errors(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContentDetailsActionsApiView(APIView):
    def get(self, request:Request, pk:int):
        # 1. try to found the resource with given pk 
        # 2. serialize the found resource 
        # 3. return the response 
        try:
            content = Content.objects.get(pk = pk)
        except Content.DoesNotExist:
            return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
        serialized_data = ContentSerializer(content)
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def put(self, request:Request, pk:int):
        # 1. try to found the resource with given pk 
        # 2. serialize the found resource 
        # 3. update the data by calling save 
        # 4. return the proper response 
        try:
            content = Content.objects.get(pk = pk)
        except Content.DoesNotExist:
            return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContentSerializer(instance=content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        else:
            return Response({"error": "couldn't update the resource"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request:Request, pk:int):
        # 1. try to found the resource with given pk 
        # 2. serialize the found resource 
        # 3. delete the data by calling delete  
        # 4. return the proper response 
        try:
            content = Content.objects.get(pk = pk)
        except Content.DoesNotExist:
            return Response({'error': 'no resource found with given priamry key'}, status=status.HTTP_404_NOT_FOUND)
        content.delete()
        return Response(data = "deleted", status= status.HTTP_204_NO_CONTENT)
    


