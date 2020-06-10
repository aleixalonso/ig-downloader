import sys
from instaloader import Instaloader, Profile

def downloadAllPosts( username ):
    PROFILE = username
    L = Instaloader()
    profile = Profile.from_username(L.context, PROFILE)
    if (profile.is_private):
        print("user is private")
        exit(0)
    posts = profile.get_posts()
    for post in posts:
        L.download_post(post, PROFILE)

def main(argv):
    mode = int(sys.argv[1])
    username = sys.argv[2]
    if mode > 1:
        print("nothing here")
        exit(0)
    #idea: first check if user is private, only if all func share
    if mode == 1:
        downloadAllPosts(username)
    elif mode == 2:
        print("not implemented")
    else:
        print("nothing here")

if __name__ == "__main__":
    main(sys.argv[1:])