from django.shortcuts import render
from .models import User, Address, Category, Product
from .serializers import UserSerializer, AddressSerializer, CategorySerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from rest_framework import status
from django.http import Http404, JsonResponse
from rest_framework.pagination import PageNumberPagination
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.core.mail import send_mail, BadHeaderError, EmailMessage
import pyotp


class register_user(APIView):

    def post(self, request):

        if request.data['password'] == request.data['password2']:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data={'message': 'User created sucessfully'}, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(data={'message': "Passwords didn't match"}, status=status.HTTP_400_BAD_REQUEST)


class user_list(APIView):

    def get(self, request):

        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class user_detail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)

        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(
            instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()

        return JsonResponse(data={'message': 'User is deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class forgot_password(APIView):

    email = ""
    otp = ""

    def post(self, request):
        try:
            email = request.data['email']
            forgot_password.email = request.data['email']
            try:
                user = User.objects.get(
                    email=email)
                user.otp_counter += 1
                user.save()
                secret_key = pyotp.random_base32()
                otp = pyotp.HOTP(secret_key)
                forgot_password.otp = otp.at(user.otp_counter)
                print(forgot_password.otp)

                #send_mail('OTP for reset password',f'your otp is {otp.at(user.otp_counter)}', settings.EMAIL_HOST_USER, [email], fail_silently=False)

                return Response(message={'message': 'otp has been sent to your email'}, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return JsonResponse(data={"message": "This email is not found in our data"}, status=status.HTTP_404_NOT_FOUND)

        except:
            return JsonResponse(data={"message": "Either request data or request method is not correct"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        try:

            if forgot_password.otp == request.data['otp']:

                password = request.data['password']
                password2 = request.data['password2']

                if password == password2:

                    user = User.objects.get(email=forgot_password.email)

                    user.set_password(password)
                    user.save()

                    return JsonResponse(data={"message": "password Changed Succesfully"}, status=status.HTTP_200_OK)
                else:

                    return JsonResponse(data={"message": "Passwords didn't match. Try again!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(data={"message": "Otp is not correct"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return JsonResponse(data={"message": "Either data or method is not correct"}, status=status.HTTP_400_BAD_REQUEST)


class register_product(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data={'message': 'Product has been added successfully'}, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


class product_list(APIView):

    def get(self, request, category):
        products = Product.objects.filter(
            product_category__category_name__iexact=category)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class product_detail(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse(data={'message': 'Product does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return JsonResponse(data={'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return JsonResponse(status=status.HTTP_204_NO_CONTENT)

        except ObjectDoesNotExist:
            return JsonResponse(data={'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)


class category_list(APIView):

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        print(serializer.data[0])

        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
