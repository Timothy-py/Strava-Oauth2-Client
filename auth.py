from strava_credentials import user_credentials

# request access from the auth page
AUTHENTICATION_URL = f"""http://www.strava.com/oauth/authorize?client_id={user_credentials['client_id']}&response_type=code&redirect_uri={user_credentials['auth_callback_domain']}&approval_prompt=auto&scope=read_all"""

print(f"Go to this url in your browser to get the code: {AUTHENTICATION_URL}")
