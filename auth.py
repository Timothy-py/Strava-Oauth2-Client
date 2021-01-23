from strava_credentials import user_credentials

# request access from the auth page
AUTHENTICATION_URL = "http://www.strava.com/oauth/authorize?client_id={}&response_type=code&redirect_uri={}&approval_prompt=auto&scope=read_all".format(
    user_credentials['client_id'],
    user_credentials['auth_callback_domain']
)

print("Go to this url in your browser to get the code: {}".format(AUTHENTICATION_URL))
