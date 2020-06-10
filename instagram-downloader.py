import sys
from instaloader import Instaloader, Profile

def downloadAllPosts( username ):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    posts = profile.get_posts()
    total = len(list(profile.get_posts()))
    for post in posts:
        L.download_post(post, PROFILE)
    print("Downloaded " + str(total) + " posts")

def downloadIGTV( username ):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    total = len(list(profile.get_igtv_posts()))
    L.download_igtv(profile)
    print("Downloaded " + str(total) + " IGTVs")

def downloadProfilePic( username ):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    total = len(list(profile.get_igtv_posts()))
    L.download_profilepic(profile)
    print("Profile picture downloaded")

'''
#you have to be logged
def checkFriendship( username1, username2 ):
    L = Instaloader()
    PROFILE1 = username1
    profile1 = Profile.from_username(L.context, PROFILE1)
    PROFILE2 = username2
    profile2 = Profile.from_username(L.context, PROFILE2)
    followers_list = profile1.get_followers()
    print(len(list(followers_list)))
'''

def main(argv):
    mode = int(sys.argv[1])
    username1 = sys.argv[2]
    username2 = ""
    if len(sys.argv) > 3:
        username2 = sys.argv[3]
    L = Instaloader()
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

    if mode > 3:
        print("nothing here")
        exit(0)
    if mode == 1:
        downloadAllPosts(username1)
    elif mode == 2:
        downloadIGTV(username1)
    elif mode == 3:
        downloadProfilePic(username1)
    elif mode == 4:
        #checkFriendship(username1, username2)
        print("coming")
    else:
        print("nothing here")

if __name__ == "__main__":
    main(sys.argv[1:])