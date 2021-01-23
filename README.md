# Strava-Oauth2-Client
A Python application that Authorizes a user to connect to Strava App
 and then save some of the User Data in a json file which
  is then send to Google Drive.
  
## Setting up this module
i. Clone the project files into your local machine  
ii. cd into the project folder, create a virtualenv and activate it.  
iii. pip install the app dependencies - `pip install requirements.txt`  

## Configuring Strava
i. Go to your Strava App - https://www.strava.com/settings/api  
ii. Copy the following values into strava_credentials.py 
file in this module folder - Client_id, Client_secret, 
'Authorization Callback Domain'

## Configuring Google Drive
i. Login into your Gmail account in your browser  
ii. Go to https://developers.google.com/drive/api/v3/quickstart/python
iii. Click on the blue button that reads 'Enable the Drive API' and setup  
iv. You will be prompted to **DOWNLOAD CLIENT CONFIGURATION**, click on it to 
download the file named **credentials.json**
v. copy/cut the file and paste it into this module directory.  

## Using this module for Strava Authorization and Saving to Google Drive
i. Run _auth.py_ file and click on the output link  
**OR**  
Just go to http://www.strava.com/oauth/authorize?client_id={XXXXXX}&response_type=code&redirect_uri={XXXXXX}&approval_prompt=auto&scope=read_all  
replacing {XXXXX} with your client_id and 'Authorization Callback Domain' respectively.  
ii. Input your details and Login, and/or click on **Authorize**  
iii. On the page redirected to, copy the 40 characters long code that is in front of 
**code=** in the url  
iv. paste the code in _strava_credentials.py_ file  
v. Run _main.py_ file and observe the output.
 