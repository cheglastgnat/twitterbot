twitterbot
==========

Twitter automation using TTYtter


Preparation
-----------
1. Get the command line Twitter client **TTYtter** (http://www.floodgap.com/software/ttytter), the current version is http://www.floodgap.com/software/ttytter/dist2/2.1.00.txt (it's just a text file).
2. Make **TTYtter** executable and tell the twitterbot where to find it (change the global variable `TTYTTER_BIN` in `script.sh`  to the correct path to your **TTYtter** file.
3. Start **TTYtter** and follow its instructions to authenticate the client with your **Twitter** account (you need tot create an account first if you don't already have one).
4. Put some example posts into the text file `posts.txt` (each line is a post).


Usage
-----
Executing `script.sh` will tweet one of the candidate texts together with a random trending hashtag topic.
