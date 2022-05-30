from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CartItem
from .serializers import CartItemSerializer


# Create your views here.
def get(request, *args, **kwargs):
    """
    List all the cart item for given requested user
    """
    cartitems = CartItem.objects.filter(user=request.user.id)
    serializer = CartItemSerializer(CartItem, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CartItemViews(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        List all the cart items for given requested user
        """
        cartitems = CartItem.objects.filter(user=request.user.id)
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        Create the Todo with given todo data
        """
        data = {
            'product_name': request.data.get('product_name'),
            'product_price': request.data.get('product_price'),
            'product_quantity': request.data.get('product_quantity'),
            'user': request.user.id
        }
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingCartDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, cart_id, user_id):
        """
        Helper method to get the object with given cart_id, and user_id
        """
        try:
            return CartItem.objects.get(id=cart_id, user=user_id)
        except CartItem.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, cart_id, *args, **kwargs):
        """
        Retrieves the cart with given cart_id
        """
        cart_instance = self.get_object(cart_id, request.user.id)
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CartItemSerializer(cart_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, cart_id, *args, **kwargs):
        """
        Updates the todo item with given todo_id if exists
        """
        cart_instance = self.get_object(cart_id, request.user.id)
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'product_name': request.data.get('product_name'),
            'product_price': request.data.get('product_price'),
            'product_quantity': request.data.get('product_quantity'),
            'user': request.user.id
        }
        serializer = CartItemSerializer(instance=cart_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, cart_id, *args, **kwargs):
        """
        Deletes the cart item with given cart_id if exists
        """
        cart_instance = self.get_object(cart_id, request.user.id)
        if not cart_instance:
            return Response(
                {"res": "Object with cart id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        cart_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
