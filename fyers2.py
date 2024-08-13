#generate access token

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel
from credentials import client_id, secret_key, redirect_uri

# Define your Fyers API credentials
response_type = "code" 
grant_type = "authorization_code"  

# The authorization code received from Fyers after the user grants access
auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MDE5Mjc2NDQsImV4cCI6MTcwMTk1NzY0NCwibmJmIjoxNzAxOTI3MDQ0LCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYRjAwMDMxIiwib21zIjoiSzEiLCJoc21fa2V5IjoiNmIzMjYzY2Q5OThkNGExNWRiN2Y2ZjBiYTI3NGU3MTEyYjI5YWE5NzBlZWJlMzI0ZGIxOGFjYzAiLCJub25jZSI6IiIsImFwcF9pZCI6IkRYSjQwUlFLREIiLCJ1dWlkIjoiNGUwMjdlZjkzZDA3NGQ4NGJmZTRjNjRmZjdlNGJkZGUiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.bmPWXefx19t_4iL931BiwRA2vm1OKcReDpRIRXu4_9M"

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response['access_token'])

