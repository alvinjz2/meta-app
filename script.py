import requests
url = f'https://api.instagram.com/oauth/authorize
  ?client_id=298397099661769
  &redirect_uri=https://alvinjz.me/
  &scope=user_profile,user_media
  &response_type=code'
x = requests.post(url)