# instagram-downloader
Python Instagram downloader based on Instaloader library (https://instaloader.github.io)

## Requirements
Install Instaloader library
```elm
pip3 install instaloader
```

## Running instagram-downloader
```elm
python3 instagram-downloader.py option username
```
* Option 1: download all instagram photos (and videos) of a given user, if you use the flag -c you will also download comments, -m for metadata and -g for geotags
    * Example: ```python3 instagram-downloader.py 1 instagramusername```
    * Example: ```python3 instagram-downloader.py 1 instagramusername -m -c```
* Option 2: download IGTVs of a given user
    * Example: ```python3 instagram-downloader.py 2 instagramusername```
* Option 3: download profile picture of a given user
    * Example: ```python3 instagram-downloader.py 3 instagramusername```
* Option 4: check friendship between your instagram and a given user, you must log in, it will show if you follow that account, and if they follow you 
    * Example: ```python3 instagram-downloader.py 4 yourinstagramusername instagramusername```