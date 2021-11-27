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

    # TODO: Address 모델 인스턴스 수정에 따라 Reader의 연관 필드값이 동적으로 변함
    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        request_body = request.data
        reader_id = request_body.get('reader')
        reader = Reader.objects.get(id=reader_id)
        latest_city = getattr(reader, 'latest_city')
        new_city = request_body.get('city')

        # 새로 생성되는 address가 최신 city일 경우(가장 값이 높은 city일 경우)
        # Reader 내 latest_city 값 수정
        if new_city > latest_city:
            reader.latest_city = new_city
            reader.save(update_fields=['latest_city'])
            request_body.update({"city": new_city})

        if kwargs.pop("pk", None):
            serializer = self.get_serializer(
                instance=self.get_object(), data=request_body, **kwargs
            )
        else:
            kwargs["many"] = isinstance(request_body, list)
            serializer = self.get_serializer(
                self.get_queryset(), data=request_body, **kwargs
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Address 모델 인스턴스 생성에 따라 Reader의 연관 필드값이 동적으로 변함
    def create(self, request, *args, **kwargs):
        request_body = request.data

        is_bulk = isinstance(request_body, list)

        if is_bulk:
            object_list_in_request = request_body
            print(f'request_body: {request_body}')
            for object_in_request in object_list_in_request:
                reader_id = object_in_request.get('reader')
                reader = Reader.objects.get(id=reader_id)
                latest_city = getattr(reader, 'latest_city')
                new_city = object_in_request.get('city')
                print(f'latest_city: {latest_city}, new_city: {new_city}')

                # 새로 생성되는 address가 최신 city일 경우(가장 값이 높은 city일 경우)
                # Reader 내 latest_city 값 수정
                if new_city > latest_city:
                    reader.latest_city = new_city
                    reader.save()

        else:
            object_in_request = request_body
            reader_id = object_in_request.get('reader')
            reader = Reader.objects.get(id=reader_id)
            latest_city = getattr(reader, 'latest_city')
            new_city = object_in_request.get('city')
            print(f'latest_city: {latest_city}, new_city: {new_city}')

            # 새로 생성되는 address가 최신 city일 경우(가장 값이 높은 city일 경우)
            # Reader 내 latest_city 값 수정
            if new_city > latest_city:
                reader.latest_city = new_city
                reader.save()

        kwargs["many"] = is_bulk
        serializer = self.get_serializer(data=request_body, **kwargs)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
