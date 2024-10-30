# payments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from sslcommerz_lib import SSLCOMMERZ
from .models import Order
from courses.models import Course
from django.conf import settings
import random
import string
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderListView(APIView):
    # permission_classes = [IsAuthenticated]  

    def get(self, request):
        # Fetch the orders for the authenticated user
        orders = Order.objects.filter(ordered=True)
        # orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)



def generate_transaction_id(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class InitiatePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        print("Request Headers:", request.headers)
        # Fetch the course based on the provided course ID
        course = get_object_or_404(Course, id=course_id)

        # Create Order
        order = Order.objects.create(
            user=request.user,
            course=course,
            tran_id=generate_transaction_id(),
            amount=course.price
        )

        # SSLCommerz settings
        ssl_settings = {
            'store_id': 'abins671fc56b7ee72',  # Replace with your actual store ID
            'store_pass': 'abins671fc56b7ee72@ssl',  # Replace with your actual store password
            'issandbox': True  # Set to False when you are ready for live transactions
        }

        sslcommerz = SSLCOMMERZ(ssl_settings)

        # Prepare the payment request body
        post_body = {
            'total_amount': str(course.price),  # Amount must be a string
            'currency': "BDT",
            'tran_id': order.tran_id,
            'success_url': f'{settings.SITE_URL}/api/complete/',  
            'fail_url': f'{settings.SITE_URL}/api/fail/',  
            'cancel_url': f'{settings.SITE_URL}/api/cancel/',  
            'emi_option': 0,  # No EMI option
            'cus_name': request.user.username,  # User's name
            'cus_email': request.user.email,  # User's email
            'cus_phone': '01700000000',  # Ideally should be user-provided
            'cus_add1': 'Customer Address',  # Update this to the user's address
            'cus_city': 'Dhaka',
            'cus_country': 'Bangladesh',
            'shipping_method': 'NO',
            'multi_card_name': "",  # If multiple cards are used, specify here
            'num_of_item': 1,  # Number of items in the order
            'product_name': course.title,  # Product name from the course
            'product_category': 'Education',  # Define the category of your product
            'product_profile': 'general'  # General product profile
        }

        try:
            # Create the payment session
            response = sslcommerz.createSession(post_body)

            # Check if the response contains a URL for redirection
            if 'GatewayPageURL' in response:
                return Response({'payment_url': response['GatewayPageURL']}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Failed to initiate payment', 'details': response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': 'An error occurred while initiating payment', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




from django.shortcuts import get_object_or_404, render
class CompletePaymentView(APIView):
    def post(self, request):
        payment_data = request.data
        tran_id = payment_data.get('tran_id')
        payment_status = payment_data.get('status')

        order = get_object_or_404(Order, tran_id=tran_id, ordered=False)

        if payment_status == 'VALID':
            order.ordered = True
            order.status = 'completed' 
            order.save()
            # return Response({'message': 'Payment successful', 'status': order.status}, status=status.HTTP_200_OK)
            return render(request, 'complete.html')
        else:
            # return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
            return render(request, 'fail.html')


class PaymentFailView(APIView):
    def post(self, request):
        payment_data = request.data
        tran_id = payment_data.get('tran_id')

        order = get_object_or_404(Order, tran_id=tran_id, ordered=False)
        order.ordered = False
        order.status = 'failed'  
        order.save()

        # return Response({'message': 'Payment failed', 'status': order.status}, status=status.HTTP_400_BAD_REQUEST)
        return render(request, 'fail.html')


class PaymentCancelView(APIView):
    def post(self, request):
        payment_data = request.data
        tran_id = payment_data.get('tran_id')

        order = get_object_or_404(Order, tran_id=tran_id, ordered=False)
        order.ordered = False
        order.status = 'canceled'  # Optionally set status to canceled
        order.save()

        # return Response({'message': 'Payment canceled', 'status': order.status}, status=status.HTTP_400_BAD_REQUEST)
        return render(request, 'fail.html')





