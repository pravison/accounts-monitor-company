from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from . models import User
import jwt , datetime
# from django.http import JsonResponse
# Create your views here.
class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)

    
class Login(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username = username).first()

        if user is None:
            raise AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        
        paylod = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(weeks=1),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(paylod, 'secret', algorithm='HS256').format('utf-8')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "jwt":token
        }
        return response

# class Login(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = User.objects.filter(username=username).first()

#         if user is None:
#             raise AuthenticationFailed('User not found')
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password')

#         payload = {
#             "id": user.id,
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(weeks=1),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').format('utf-8')  # Decode the bytes to a string
#         response = JsonResponse({'jwt': token})

#         # Set the JWT token as an HTTP-only cookie
#         response.set_cookie(key='jwt', value=token, httponly=True)

#         return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('unathenticated')
        try:
            paylod = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unathenticated')
        
        user = User.objects.filter(id=paylod['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Thanks for spending sometime with us welcome again"
        }
        return response