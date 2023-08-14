from django.shortcuts import redirect

# Create your views here.
# class kakakoView(View):
#     def get(self, request):
#         kakao_api = "http://kauth.kakao.com/oauth/authorize?response_type=code"
#         redirect_url = "http://127.0.0.1:8000/users/kakako/callback"
#         client_id = "994119c41ed20b049df4490a11488e5d"

#         return redirect(f"{kakao_api}&client_id={client_id}&redirect_url={redirect_url}")
    

# class kakaoCallBackView(View):
#     def get(self,request):
#         data={
#             "grant_type" : "authorization_code",
#             "cliend_id" : "994119c41ed20b049df4490a11488e5d",
#             "redirect_url" : "http://127.0.0.1:8000/users/kakako/callback",
#             "code" : request.GET["code"]
#         }
#     kakao_token_api = "https://kauth.kakao.com/oauth/token"
#     access_tocken = requests.post(kakao_token_api, data=data).json()["access_tocken"]
