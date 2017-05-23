from slackclient import SlackClient


token = "xoxp-25081281559-118998934689-184440224640-9325ad860d3a1b304751fbec4c228a78"

sc = SlackClient(token)

# print(sc.api_call("api.test"))

# Get all users
all_users = sc.api_call("users.list")

print(list(all_users.keys()), type(all_users))

# The data returned from all_users is a dictionary with 3 keys: ok, members and cache_ts

# How many users do we get?
print(len(all_users['members']))

# Let us look at the data
