import jwt
from .serializers import Account, AccountSerializer, AccountPorfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



"""@api_view(['POST'])
def register_client_user(request):
    serializer = ClientUserProfileSerializer(request.data)
    if serializer.is_valid():
        new_user = serializer.save()
        return Response(ClientUserProfileSerializer(new_user))
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class SignUp(APIView):
    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"token":token, "msg":"You are registered successfully", "user":AccountSerializer(user).data},  status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            serializer = AccountPorfileSerializer(request.user, context={'request': request})
            return Response({'profile': serializer.data, 'msg': 'Login successful'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'errors': 'password or email is not valid'}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = authenticate(email=email, password=password, id=request.user.pk)
        token = get_tokens_for_user(user)
        if user is not None:
            return Response({'token':token, 'msg':'Login successful','user':AccountPorfileSerializer(request.user, context={'request': request}).data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'errors':'password or email is not valid'}, status=status.HTTP_404_NOT_FOUND)


"""@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = authenticate(email=email, password=password)
    if user is not None:
        encoded_jwt = jwt.encode(
            {'pk':user.pk}, 'b$c4*L#u#E&CFyHU4!&HcnkxjRn', algorithm="HS256"
        )
        return Response(data={'msg':'You are logged in successfully','token':encoded_jwt})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)"""

"""@api_view(['POST'])
def register(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        new_user = serializer.save()
        return Response(data=AccountSerializer(new_user).data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

"""class CreateUser(CreateAPIView):
    queryset = Account.objects.only('username',
                                    'first_name',
                                    'last_name',
                                    'email',
                                    'date_joined',
                                    'last_login',
                                    'is_client',
                                    'is_tour_guide')

    serializer_class = AccountSerializer"""



class AccountView(RetrieveUpdateAPIView):
    queryset = Account.objects.only('id',
                                    'username',
                                    'first_name',
                                    'last_name',
                                    'email',
                                    'password',
                                    'phone_number',
                                    'profile_image',
                                    'language')
    serializer_class = AccountPorfileSerializer
    permission_classes = [IsAuthenticated]



"""class AccountView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        return Response(AccountPorfileSerializer(request.user).data)

    def put(self, request, format=None):
        serializer = AccountPorfileSerializer(request.user, context={'request':request}, partial=True).data
        if serializer.is_valid():
            data = serializer.save()
            return Response({'data':data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)"""





"""class TourGuideView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            request.user.is_tour_guide = True
            return Response(AccountSerializer(request.user).data)

    def put(self, request):
        if request.user.is_authenticated():
            request.user.is_tour_guide = True
            serializer = AccountSerializer(request.user, context={'request':request}, partial=True).data
            if serializer.is_valid():
                data = serializer.save()
                return Response({'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)"""

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = AccountPorfileSerializer(request.user, context={'request':request})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
































































