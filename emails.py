"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

# imports
#import urllib3
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import json



# adding comments for Lab 4:
# creating an empty list named addresses
addresses = []

# prompting the user to affirm if they DO
# or do NOT have an email address to input
more = input("Do you have an email address to enter (y/n)? ")

# starting the while loop. The user had input
# a value into the variable 'more'. Now we're
# checking that value and checking it against
# several conditions
#--------------------------------------------
# sidebar: I would have personally used the
# '.lower()' method so I didn't have to worry about
# them typing a Y or N. To each their own.
#--------------------------------------------
while more == "y":
    # the user input that they DO have an email
    # address to input. Now we are asking for them
    # to enter that email, which will be stored
    # in the variable 'email'
    email = input("Enter the address: ")
    # the '.append' method will add the information
    # stored into variable 'email' on to the end of
    # the list 'addresses'
    addresses.append(email)
    # we are now asking the user if they have another
    # email address to input, and we will start the
    # while loop again to try the new input against
    # our conditions
    more = input("Do you have another address(y/n)? ")
    # this nested while loop is checking conditions for
    # when the user has entered anything BUT 'y'
    while more != "y":
        # if the user input 'n', we will break out of
        # the loop and move on to the next block of code
        if more == "n":
            break
        # if the user gave us any other input (garbage
        # input in our case), we will kindly ask them
        # again to choose either y or n, and the
        # main loop will start over again
        else:
            more = input("Please enter a y or n: ")

# this code will output the information stored in the
# 'addresses' list to the console
# print(addresses)

# this code turns the list into a string so that I can
# pass it into the payload2 of url2
addString = str(addresses).strip('[]')
# debug
print(addString)


#===========================================================
# working with the cisco webex teams api
# here I am creating a spaces instance to use
url = "https://webexapis.com/v1/rooms"

payload = "{\r\n    \"title\": \"Room For Emails\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer **'
}
response = requests.request("POST", url, headers=headers, data = payload)
roomID = str(response.json()['id'])
# debug print statements
#print(response.text.encode('utf8'))
#print()
#print(roomID)

# here I am passing the emails into the room as a message
url2 = "https://webexapis.com/v1/messages"

payload2 = {"roomId": str(roomID), "text": addString}
headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer **'
}
response2 = requests.request("POST", url2, headers=headers2, data = json.dumps(payload2))
# debug print statement
#print(response2.text.encode('utf8'))
