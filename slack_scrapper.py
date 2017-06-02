import os
import requests
import sys
from os.path import join, dirname

from dotenv import load_dotenv
from slackclient import SlackClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
# Get the slack token from the .env file
token = os.environ.get("SLACK_TOKEN")

sc = SlackClient(token)

#Get all messages in a channel
def allMessages(channel = 'C5GRK45A9'):
    msg_endpoint = 'https://slack.com/api/channels.history?token=%s&channel=%s&pretty=1' % (token, channel)
    all_messages = requests.get(msg_endpoint)
    text_all_message = all_messages.text
    with open("messages.json", "w") as message_file:
        message_file.write(text_all_message);
        message_file.close()
    return all_messages.json()    

# Get all channels in the Team
channels = sc.api_call("channels.list")['channels']

print("There are {} channels in OPEN-Andela.".format(len(channels)))

# Save the channels information to a .txt file
with open("channels.txt", "w") as textfile:
    textfile.write(
        "There are {} channels in OPEN-Andela.\n".format(len(channels)))
    textfile.write("")
    for channel in channels:
        textfile.write("----------------------------------------------- \n")
        textfile.write("Channel Name: {} \n".format(channel["name"]))
        textfile.write("Channel Name (Normalized): {} \n".format(
            channel["name_normalized"]))
        textfile.write("Number of Members: {} \n".format(
            channel['num_members']))
        textfile.write("Channel ID: {} \n".format(channel["id"]))
        textfile.write("Channel Purpose: {} \n".format(
            channel["purpose"]["value"]))
        textfile.write("---------------------------------------------- \n")

# Get all users
all_users = sc.api_call("users.list")["members"]

print("There are {} members in the OPEN-Andela Team".format(len(all_users)))
with open("users.txt", "w") as textfile:
    for user in all_users:
        textfile.write("------------------------------------------------ \n")
        textfile.write("Username: {} \n".format(user["name"]))
        textfile.write("Bot: {} \n".format(user["is_bot"]))
        textfile.write("Name: {} \n".format(user["profile"]['real_name']))
        # I commented this out because bots don't have email and it will break the code.
        # textfile.write("E-mail: {} \n".format(user["profile"]["email"]))
        textfile.write("ID: {} \n".format(user["id"]))
        textfile.write("------------------------------------------------ \n")

allMessages(sys.args[1])

# Post a message on the api_test channel
message = input(
    "Enter the message you want to post on the api_test channel: \n")
sc.api_call(
    "chat.postMessage",
    channel="#api_test",
    text=message
)
