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

def main(argv):
    mode = int(sys.argv[1])
    username = sys.argv[2]
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    if (profile.is_private):
        print("user is private")
        exit(0)

    if mode > 2:
        print("nothing here")
        exit(0)
    if mode == 1:
        downloadAllPosts(username)
    elif mode == 2:
        downloadIGTV(username)
    else:
        print("nothing here")

if __name__ == "__main__":
    main(sys.argv[1:])