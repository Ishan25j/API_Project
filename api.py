# API Project

from random import choice # for randomizing the output
import pyfiglet # for getting a figlet heading
import termcolor # chaning color of the string
import requests # for getting GET request and requesting POST request
text = termcolor.colored("API Project", color="yellow")
print(text)
print("")


header = pyfiglet.figlet_format("DAD JOKES 3000")
header = termcolor.colored(header, color="yellow")
print(header)

user_input = str(input("enter the joke u want to search: ")) # taking input from a user
url = "https://icanhazdadjoke.com/search" # url supporting api
response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": user_input, "limit": 1}
)
data = response.json() # data in the form of json format to dictionary
nums = data["total_jokes"]
result = data["results"]
if nums > 1:
    print(f"There are many jokes! i.e {nums}")
    print(choice(result)["joke"])
elif nums == 1:
    print("There is exactly one joke")
    print(result[0]["joke"])
else:
    print(f"There are no jokes!!! that u want i.e {user_input}")
