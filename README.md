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
* Option 1: download all instagram photos (and videos) for a given user
    * Example: ```python3 instagram-downloader.py 1 yourinstagramusername```
* Option 2: download IGTVs for a given user
    * Example: ```python3 instagram-downloader.py 2 yourinstagramusername```