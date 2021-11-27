from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Reader, Address
from .serializers import ReaderSerializer, AddressSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # TEST: Address 모델 인스턴스 수정에 따라 Reader의 연관 필드값이 동적으로 변함
    # def update(self, request, *args, **kwargs):

    # TEST: Address 모델 인스턴스 생성에 따라 Reader의 연관 필드값이 동적으로 변함
    def create(self, request, *args, **kwargs):
        request_body = request.data
        model_relationship = isinstance(request_body, list)
        reader_id = request_body.get('reader')
        reader = Reader.objects.get(id=reader_id)
        total_city = getattr(reader, 'total_city')
        print(f'request_body: {request_body}')

        serializer = AddressSerializer(data=request_body, many=model_relationship)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
