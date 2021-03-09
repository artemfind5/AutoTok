import asyncio
from tiktokpy import TikTokPy
from TikTokApi import TikTokApi
from tiktokpyNorthenFox import tiktokpy
import os
import requests
import json
import urllib3
urllib3.disable_warnings()

def getIdByUsername(username):
    api = TikTokApi.get_instance()
    return api.getUserObject(username)

#example:
#await getIdByUsername("kinoepisodes")

async def getFollowingList(uid, followers):
    data = tiktokpy.api.get_following_list(uid,200)
    for car in json.loads(data)['followings']:
       followers.append(car['unique_id'])

nameid = 6833799979456381958
#nameid = getIdByUsername("kinoepisodes") # Execute once and the program crashes. After receiving the information, comment out.
#print("ID = " + str(nameid))

async def main():
    async with TikTokPy() as bot:
        followers = list()
        await getFollowingList(6833799979456381958, followers)
        #6835712389884134405 - @tiktokriddle
        #6833799979456381958 - @kinoepisodes
        print("Followers " + str(nameid) + ": ")
        print(followers)

        #await bot.login_session() - Authorization is needed once!

        for user in followers:
            await bot.unfollow(user)
        #or example:
        #await bot.follow("kinoepisodes")


        # get trending videos and work with
        #trending_items = await bot.trending(amount=5)
        #for item in trending_items:
                # like videos
            # await bot.like(item)
                # unlike them
            # await bot.unlike(item)
                # follow users
            #await bot.follow(item.author.username)
                #  unfollow
            #await bot.unfollow(item.author.username)

        # 😏 getting user's feed
        #user_feed_items = await bot.user_feed(username="kinoepisodes", amount=5)
        #print(await bot.user_feed(username="tiktokriddle", amount=5))

        #for item in user_feed_items:
           # bot.like(item)
            # 🎧 get music title, cover, link, author name..
           # print("Music title: ", item.music.title)
            # #️⃣ print all tag's title of video
            #print([tag.title for tag in item.challenges])
            # 📈 check all video stats
            #print("Comments: ", item.stats.comments)
            #print("Plays: ", item.stats.plays)
            #print("Shares: ", item.stats.shares)
            #print("Likes: ", item.stats.likes)

#while 1<2 :
asyncio.run(main())