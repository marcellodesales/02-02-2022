# 📅 02-02-2022

This is a time capsule for the special day that won't repeat!

There are only 2 characters in today's date. But, I wanted to keep a record of today's time as well in the form of tweets.
This will generate all the tweets for today that matches all combinations of hour:minute:second.

There will be also NFT entries in different blockchains for time capsule purposes!!!

# 🔧 Setup

> First, make sure to get the Elevate account type approved!

* Collect the config as follows
  * Create the file `~/.tweet.client.key` with the following contents

* Go to the developer's page
  * https://developer.twitter.com/en/portal/projects/1488768050035773444/apps/23291738/keys
* Copy the `Consumer Keys` and `Authentication Tokens`
  * Bearer Token is NOT needed for the current version
  * Make sure to re-generate the type after changing the type to `Read-Write` when setting up the production app

Add all the values to the different environment apps by `dev` and `prd`

```ruby
MY_SCREEN_NAME=marcellodesales
MY_LANGUAGE=en

######## DEVELOPMENT

#CONSUMER_KEY=0u******AfaE
#CONSUMER_SECRET=UZ1***PpO
#ACCESS_TOKEN=280****9CM
#ACCESS_TOKEN_SECRET=5H8***NcQK

#BEARER_TOKEN=AAAA****uat2
#CLIENT_ID=a19***pjaQ
#CLIENT_SECRET=aJbv***2rnXg

########## PRODUCTION

CONSUMER_KEY=Txi****3OH
CONSUMER_SECRET=qwV****JKBqd
ACCESS_TOKEN=280****R2jz
ACCESS_TOKEN_SECRET=XvV****fIDY
BEARER_TOKEN=AAA****if8G7wO
```

# 👽 Main script

* It calls `combinations.py` to generate the list of next hours.
* Then, it waits until one of the hours is a match to tweet.
  * Example: `02/02/2022 at 22:22:00` https://twitter.com/marcellodesales/status/1489121976610267136

## 🔊 Logs

* Running will publish tweets as follows

```console
Current time: 02/02/2022 at 02:02:21  Waiting for 02/02/2022 at 02:02:22
Current time: 02/02/2022 at 02:02:21  Waiting for 02/02/2022 at 02:02:22
Current time: 02/02/2022 at 02:02:21  Waiting for 02/02/2022 at 02:02:22
Current time: 02/02/2022 at 02:02:22  Waiting for 02/02/2022 at 02:02:22

########### Unique !!!!! ----

* Will tweet at 02:02:22

Current time: 02/02/2022 at 02:02:22  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:24  Waiting for 02/02/2022 at 02:20:00
```

# 🐦 Tweet

* We use https://www.tweepy.org/ python dependency to tweet!

## 🔧 Setup Tweet.sh 

> **NOTE**: Only proceed after going to https://developer.twitter.com/en/portal/products/elevated
to generate the keys and request your tweeter developer account to be "Elevated".

1. The instructions on how to collect the API keys are in https://github.com/piroor/tweet.sh/issues/35#issuecomment-1027686153

2. Create file $ cat ~/.tweet.client.key

```python
MY_SCREEN_NAME=marcellodesales
MY_LANGUAGE=en
CONSUMER_KEY=0ud4****kAfaE
CONSUMER_SECRET=UZ18Q****E73kPpO
ACCESS_TOKEN=2806784*****ZJV9CM
ACCESS_TOKEN_SECRET=5H8y****JNcQK
```

## ✅ Test tweet.sh

```console
$ TWEET_TEST_TIME=204520 MODE=test python main.py
Token 2022-02-02 00:00:00  > Current time is 2022-02-03 20:45:13.920616
Token 2022-02-02 00:00:02  > Current time is 2022-02-03 20:45:13.920682

########### Unique ##########

* Will tweet at 20:45:20

=---> Twitting: 'This is the unique tweet at 02/02/2022 at 20:45:20. #02022022204520'

Success!!!
Finished attempting to tweets
```
