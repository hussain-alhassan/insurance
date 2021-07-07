from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': 'api/v1/customers',
        'List-Detail': 'api/v1/customers/pk',
        'Create': 'api/v1/create_customer',
        'Update': 'api/v1/update_customer/pk',
        'Delete': 'api/v1/delete_customer/pk',
    }

    return Response(api_urls)


@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response("Customer was delete successfully")
