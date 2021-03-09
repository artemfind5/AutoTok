# AutoTok - Automatic unsubscribe after mass following

main.py - main file

user.py - fixed file from tiktokpy lib (replace it)

Authorization by token (settings.toml)

When you start the program for the first time: (Authorization is needed once!)
```python
await bot.login_session()
```
And comment out this

# Example unsubscribing
```python
nameid = getIdByUsername("kinoepisodes") # Once and comment out too! Write the data to the variable manually.
print("ID = " + str(nameid))

followers = list()
await getFollowingList(nameid, followers)
print("Followers " + str(nameid) + ": ")
print(followers)
for user in followers:
    await bot.unfollow(user)
```

# Additional features: 
- massliking
- get trending videos + (un)like
- get users feed
- functional tiktokpy, TikTokApi and tiktokpyNorthenFox libs
