import sys
from instaloader import Instaloader, Profile

def downloadAllPosts(L, username):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    posts = profile.get_posts()
    total = len(list(profile.get_posts()))
    for post in posts:
        L.download_post(post, PROFILE)
    print("Downloaded " + str(total) + " posts")

def downloadIGTV(L, username):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    total = len(list(profile.get_igtv_posts()))
    L.download_igtv(profile)
    print("Downloaded " + str(total) + " IGTVs")

def downloadProfilePic(L, username):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    L.download_profilepic(profile)
    print("Profile picture downloaded")

def checkFriendship(L, username, username2):     
    try:
        L.load_session_from_file(username)
    except FileNotFoundError:
        print("Session not found")
        L.interactive_login(username)
        L.save_session_to_file()
        
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    followers_list = profile.get_followers()
    following_list = profile.get_followees()
    followers_usernames = []
    following_usernames = []
    for follower in followers_list:
        followers_usernames.append(follower.username)
    for follower in following_list:
        following_usernames.append(follower.username)
    
    if(username2 in following_usernames):
        print( username + " follows " + username2 )
    else:
        print( username + " does not follow " + username2 )
    
    if(username2 in followers_usernames):
        print( username2 + " follows " + username )
    else:
        print( username2 + " does not follow " + username )

def checkNonFollowers(L, username):     
    try:
        L.load_session_from_file(username)
    except FileNotFoundError:
        print("Session not found")
        L.interactive_login(username)
        L.save_session_to_file()

    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    followers_list = profile.get_followers()
    following_list = profile.get_followees()
    followers_usernames = []
    following_usernames = []
    for follower in followers_list:
        followers_usernames.append(follower.username)
    for follower in following_list:
        following_usernames.append(follower.username)
    
def main(argv):
    mode = int(sys.argv[1])
    username = sys.argv[2]
    username2 = ""
    if len(sys.argv) > 3:
        username2 = sys.argv[3]

    L = Instaloader()
    L.save_metadata = False
    L.download_geotags = False
    L.download_comments = False
    if "-m" in sys.argv:
        L.save_metadata = True
    if "-g" in sys.argv:
        L.download_geotags = True
    if "-c" in sys.argv:
        L.download_comments = True

    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)

    if (profile.is_private):
        print("User " + username + " is private")

    if mode > 4:
        print("nothing here")
        exit(0)
    if mode == 1:
        downloadAllPosts(L, username)
    elif mode == 2:
        downloadIGTV(L, username)
    elif mode == 3:
        downloadProfilePic(L, username)
    elif mode == 4:
        checkFriendship(L, username, username2)
    else:
        print("nothing here")

if __name__ == "__main__":
    main(sys.argv[1:])