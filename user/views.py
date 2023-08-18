from django.shortcuts import redirect

import requests
import jwt
import time

from django.conf import settings
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

import os

KAKAO_CONFIG = {
    "KAKAO_REST_API_KEY": "994119c41ed20b049df4490a11488e5d",
    "KAKAO_REDIRECT_URI": "http://127.0.0.1:8000/oauth/kakao/login/callback",
    "KAKAO_CLIENT_SECRET_KEY": "1jcwul3m8oiRWdaqhwuZDmVO83mXicbi",
}

kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
#kakao_api = "http://kauth.kakao.com/oauth/authorize?response_type=code"
kakao_token_uri = "https://kauth.kakao.com/oauth/token"


class KakaoLoginView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        client_id = KAKAO_CONFIG['KAKAO_REST_API_KEY']
        redirect_uri = KAKAO_CONFIG['KAKAO_REDIRECT_URI']
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        
        res = redirect(uri)
        return res


# # class kakaoCallBackView(View):
# #     def get(self,request):
# #         data={
# #             "grant_type" : "authorization_code",
# #             "cliend_id" : "994119c41ed20b049df4490a11488e5d",
# #             "redirect_url" : "http://127.0.0.1:8000/users/kakako/callback",
# #             "code" : request.GET["code"]
#             # }
#         kakao_token_api = "https://kauth.kakao.com/oauth/token"
#         access_tocken = requests.post(kakao_token_api, data=data).json()["access_tocken"]
#         print(access_tocken)
#         return redirect('/')

# class KakaoCallbackView(APIView):
#     permission_classes = (AllowAny,)
#     def get(self, request):
#         data = request.query_params.copy()

#         # access_token 발급 요청
#         code = data.get('code')
#         if not code:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         request_data = {
#             'grant_type': 'authorization_code',
#             'client_id': KAKAO_CONFIG['KAKAO_REST_API_KEY'],
#             'redirect_uri': KAKAO_CONFIG['KAKAO_REDIRECT_URI'],
#             'client_secret': KAKAO_CONFIG['KAKAO_CLIENT_SECRET_KEY'],
#             'code': code,
#         }
#         token_headers = {
#             'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
#         }
#         token_res = requests.post(kakao_token_uri, data=request_data, headers=token_headers)

#         token_json = token_res.json()
#         access_token = token_json.get('access_token')

#         if not access_token:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         access_token = f"Bearer {access_token}"  # 'Bearer ' 마지막 띄어쓰기 필수

#         # kakao 회원정보 요청
#         auth_headers = {
#             "Authorization": access_token,
#             "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
#         }
#         user_info_res = requests.get(headers=auth_headers)
#         user_info_json = user_info_res.json()

#         social_type = 'kakao'
#         social_id = f"{social_type}_{user_info_json.get('id')}"

#         kakao_account = user_info_json.get('kakao_account')
#         if not kakao_account:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         user_email = kakao_account.get('email')

#         '''
#         # 회원가입 및 로그인 처리 알고리즘 추가필요
#         '''

#         # 테스트 값 확인용
#         res = {
#             'social_type': social_type,
#             'social_id': social_id,
#             'user_email': user_email,
#         }
#         response = Response(status=status.HTTP_200_OK)
#         response.data = res
#         return res
