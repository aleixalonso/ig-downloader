import sys
from instaloader import Instaloader, Profile

def downloadAllPosts(L, username ):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    posts = profile.get_posts()
    total = len(list(profile.get_posts()))
    for post in posts:
        L.download_post(post, PROFILE)
    print("Downloaded " + str(total) + " posts")

def downloadIGTV(L, username ):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    total = len(list(profile.get_igtv_posts()))
    L.download_igtv(profile)
    print("Downloaded " + str(total) + " IGTVs")

def downloadProfilePic(L, username ):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    total = len(list(profile.get_igtv_posts()))
    L.download_profilepic(profile)
    print("Profile picture downloaded")

def checkFriendship(L, username1, username2 ):
    L.interactive_login(username1)
    PROFILE1 = username1
    profile1 = Profile.from_username(L.context, PROFILE1)
    PROFILE2 = username2
    profile2 = Profile.from_username(L.context, PROFILE2)
    followers_list = profile1.get_followers()
    following_list = profile1.get_followees()
    followers_usernames = []
    following_usernames = []
    for follower in followers_list:
        followers_usernames.append(follower.username)
    for follower in following_list:
        following_usernames.append(follower.username)
    
    if(username2 in following_usernames):
        print( username1 + " follows " + username2 )
    else:
        print( username1 + " does not follow " + username2 )
    
    if(username2 in followers_usernames):
        print( username2 + " follows " + username1 )
    else:
        print( username2 + " does not follow " + username1 )

def main(argv):
    mode = int(sys.argv[1])
    username1 = sys.argv[2]
    username2 = ""
    if len(sys.argv) > 3:
        username2 = sys.argv[3]
    L = Instaloader()
    L.save_metadata = False
    L.download_geotags = False
    L.download_comments = False
    PROFILE1 = username1
    PROFILE2 = username2
    profile1 = Profile.from_username(L.context, PROFILE1)
    profile2 = None

    if (profile1.is_private):
        print("user " + username1 + " is private")

    if len(sys.argv) > 3:
        profile2 = Profile.from_username(L.context, PROFILE2)
        if (profile2.is_private):
            print("user " + username2 + " is private")

    if mode > 4:
        print("nothing here")
        exit(0)
    if mode == 1:
        downloadAllPosts(L, username1)
    elif mode == 2:
        downloadIGTV(L, username1)
    elif mode == 3:
        downloadProfilePic(L, username1)
    elif mode == 4:
        checkFriendship(L, username1, username2)
    else:
        print("nothing here")

if __name__ == "__main__":
    main(sys.argv[1:])