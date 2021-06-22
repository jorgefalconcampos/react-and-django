from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Customer
from . serializers import *



# HTTP statuses
# 2XX status
STATUS_201 = status.HTTP_201_CREATED
STATUS_204 = status.HTTP_204_NO_CONTENT

# 4XX status
STATUS_404 = status.HTTP_404_NOT_FOUND
STATUS_400 = status.HTTP_400_BAD_REQUEST





@api_view(['GET', 'POST'])
def customers_list(request):
    """ List  customers, or create a new customer. """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Customer.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CustomerSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({
            'data': serializer.data, 
            'count': paginator.count, 
            'numpages': paginator.num_pages, 
            # 'nextlink': '/api/customers/?page=' + str(nextPage), 
            'nextlink': f"/api/customers/?page={str(nextPage)}", 
            'prevlink': f"/api/customers/?page={str(previousPage)}"
        })

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=STATUS_201)
        return Response(serializer.errors, status=STATUS_400)



@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    """Retrieve, update or delete a customer by id/pk."""
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=STATUS_404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=STATUS_400)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=STATUS_204)