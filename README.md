# BoxDownloader
Shared folders in [Box](https://www.box.com/home) have a 150 GB batch limit. Thus, downloading large datasets manually can be tedious.
This script programatically downloads all the files in a shared Box folder one at the time.

E.g. to download all the files in https://app.box.com/s/rf6p81j3o507e8c5saywtlc1p91f8po9, add a config.json file in the CWD and then run
```
python3 download.py https://app.box.com/s/rf6p81j3o507e8c5saywtlc1p91f8po9
```

Don't know how to create the config.json file? → Watch [this video](todo).

Credit for most of the script goes to [Rui Barbosa](https://forum.box.com/u/rbarbosa/summary).

# Requirements
* Python 3
* boxsdk==3.9.2
