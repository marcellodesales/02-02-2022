# 📅 02-02-2022

This is a time capsule for the special day that won't repeat!

There are only 2 characters in today's date. But, I wanted to keep a record of today's time as well in the form of tweets.
This will generate all the tweets for today that matches all combinations of hour:minute:second.

There will be also NFT entries in different blockchains for time capsule purposes!!!

# 🔧 Setup

> **NOTE**: Only proceed after going to https://developer.twitter.com/en/portal/products/elevated
to generate the keys and request your tweeter developer account to be "Elevated".
> First, make sure to get the Elevate account type approved!

The bot now supports writing the tweet to IPFS before sending the tweet as a guarantee of censorship resistence :)

> **IPFS**: At the moment, IFPS Node must be version `0.7.0` as the python client hasn't been updated to support latest 0.12.0.

```
* Will tweet at 21:49:00

=> Writing the tweet 🐦 to the Blockchain ⛓️ (IPFS)
* Saving tweet to local file-system at logs/02202022214900.tweet
* Saved '273' bytes of the tweet message to local file-system at 'logs/02202022214900.tweet'
* Connecting to IPFS to persist the tweet!
* Recorded tweet from 02202022214900 to IPFS as CID: "This is a rare tweet time capsule on 📅 02/20/2022 at ⏰ 21:49:00 only 2 digits on its representation! 🤖 My creator @marcellodesales told me to watch for palindrome times! This will also go to #blockchain ⛓ #IPFS #nft #timecapsule #nft02202022214900 #02202022214900"

* The same tweet was saved in the ⛓️ blockchain IFPS CID=QmeKvLZzcgzov8jMW1Xea9oJoEKgbyQnQuLu2XjBLH2NiQ
* Explore the message after IPFS replication: https://webui.ipfs.io/#/ipfs/QmeKvLZzcgzov8jMW1Xea9oJoEKgbyQnQuLu2XjBLH2NiQ

=> Twitting: 'This is a rare tweet time capsule on 📅 02/20/2022 at ⏰ 21:49:00 represented with only 2 digits 🤖 As asked by my creator @marcellodesales, I've saved it in the blockchain! 🕑 #timecapsule #02202022214900 #IPFS #nft ⛓ #cid_QmeKvLZzcgzov8jMW1Xea9oJoEKgbyQnQuLu2XjBLH2NiQ'

* Tweed saved at https://twitter.com/marcellodesales/status/1495636655595667457
```

## Local Config

The instructions on how to collect the API keys are in https://github.com/piroor/tweet.sh/issues/35#issuecomment-1027686153

* Collect the config as follows
  * Create the file `~/.tweet.client.key` with the following contents

* Go to the developer's page
  * https://developer.twitter.com/en/portal/projects/1488768050035773444/apps/23291738/keys
* Copy the `Consumer Keys` and `Authentication Tokens`
  * Bearer Token is NOT needed for the current version
  * Make sure to re-generate the type after changing the type to `Read-Write` when setting up the production app

Add all the values to the different environment apps by `dev` and `prd`

> **NOTE**: You can use these env vars for the dockerized-version as well!

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

=---> Twitting: 'This is the unique tweet at 02/02/2022 at 20:45:20. #02022022204520'

Success!!!

Current time: 02/02/2022 at 02:02:22  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:23  Waiting for 02/02/2022 at 02:20:00
Current time: 02/02/2022 at 02:02:24  Waiting for 02/02/2022 at 02:20:00
...
...
Finished attempting to tweets
```

# 🐦 Tweet

* We use https://www.tweepy.org/ python dependency to tweet!

# 🛒 List Tweets

* This lists the tweets from this bot

> NOTE: You can from a docker container as well.

```console
$ MODE=list python main.py
🎯 [22:22:22] @ https://twitter.com/marcellodesales/status/1489122070055116800: This is the unique tweet at 02/02/2022 at 22:22:22. #nft #timecapsule #nft02022022222222
🎯 [22:22:20] @ https://twitter.com/marcellodesales/status/1489122060974448640: This is the unique tweet at 02/02/2022 at 22:22:20. #nft #timecapsule #nft02022022222220
❌ [22:22:03] @ https://twitter.com/marcellodesales/status/1489121988002021378: This is the unique tweet at 02/02/2022 at 22:22:02. #nft #timecapsule #nft02022022222202
🎯 [22:22:00] @ https://twitter.com/marcellodesales/status/1489121976610267136: This is the unique tweet at 02/02/2022 at 22:22:00. #nft #timecapsule #nft02022022222200
❌ [22:21:39] @ https://twitter.com/marcellodesales/status/1489121890874511360: This is the unique tweet at 02/02/2022 at 22:20:22. #nft #timecapsule #nft02022022222022
❌ [22:21:36] @ https://twitter.com/marcellodesales/status/1489121877238767616: This is the unique tweet at 02/02/2022 at 22:20:20. #nft #timecapsule #nft02022022222020
❌ [22:21:29] @ https://twitter.com/marcellodesales/status/1489121848818233348: This is the unique tweet at 02/02/2022 at 22:20:02. #nft #timecapsule #nft02022022222002
❌ [22:21:21] @ https://twitter.com/marcellodesales/status/1489121812000612356: This is the unique tweet at 02/02/2022 at 22:20:00. #nft #timecapsule #nft02022022222000
🎯 [22:02:22] @ https://twitter.com/marcellodesales/status/1489117036059893760: This is the unique tweet at 02/02/2022 at 22:02:22. #nft #timecapsule #nft02022022220222
🎯 [22:02:20] @ https://twitter.com/marcellodesales/status/1489117027499319297: This is the unique tweet at 02/02/2022 at 22:02:20. #nft #timecapsule #nft02022022220220
🎯 [22:02:02] @ https://twitter.com/marcellodesales/status/1489116953700491271: This is the unique tweet at 02/02/2022 at 22:02:02. #nft #timecapsule #nft02022022220202
🎯 [22:02:00] @ https://twitter.com/marcellodesales/status/1489116943017648129: This is the unique tweet at 02/02/2022 at 22:02:00. #nft #timecapsule #nft02022022220200
🎯 [22:00:22] @ https://twitter.com/marcellodesales/status/1489116534286913542: This is the unique tweet at 02/02/2022 at 22:00:22. #nft #timecapsule #nft02022022220022
🎯 [22:00:20] @ https://twitter.com/marcellodesales/status/1489116523822153728: This is the unique tweet at 02/02/2022 at 22:00:20. #nft #timecapsule #nft02022022220020
🎯 [22:00:02] @ https://twitter.com/marcellodesales/status/1489116450602160128: This is the unique tweet at 02/02/2022 at 22:00:02. #nft #timecapsule #nft02022022220002
🎯 [22:00:00] @ https://twitter.com/marcellodesales/status/1489116440519057410: This is the unique tweet at 02/02/2022 at 22:00:00. #nft #timecapsule #nft02022022220000
❌ [20:22:23] @ https://twitter.com/marcellodesales/status/1489091874430210049: This is the unique tweet at 02/02/2022 at 20:22:22. #nft #timecapsule #nft02022022202222
🎯 [20:22:20] @ https://twitter.com/marcellodesales/status/1489091861901758464: This is the unique tweet at 02/02/2022 at 20:22:20. #nft #timecapsule #nft02022022202220
❌ [20:22:03] @ https://twitter.com/marcellodesales/status/1489091790426624004: This is the unique tweet at 02/02/2022 at 20:22:02. #nft #timecapsule #nft02022022202202
🎯 [20:22:00] @ https://twitter.com/marcellodesales/status/1489091778774855681: This is the unique tweet at 02/02/2022 at 20:22:00. #nft #timecapsule #nft02022022202200
❌ [20:20:23] @ https://twitter.com/marcellodesales/status/1489091371667386370: This is the unique tweet at 02/02/2022 at 20:20:22. #nft #timecapsule #nft02022022202022
🎯 [20:20:20] @ https://twitter.com/marcellodesales/status/1489091358815965184: This is the unique tweet at 02/02/2022 at 20:20:20. #nft #timecapsule #nft02022022202020
❌ [20:20:04] @ https://twitter.com/marcellodesales/status/1489091292264947712: This is the unique tweet at 02/02/2022 at 20:20:02. #nft #timecapsule #nft02022022202002
❌ [20:20:01] @ https://twitter.com/marcellodesales/status/1489091279023599616: This is the unique tweet at 02/02/2022 at 20:20:00. #nft #timecapsule #nft02022022202000
❌ [20:02:23] @ https://twitter.com/marcellodesales/status/1489086840581681152: This is the unique tweet at 02/02/2022 at 20:02:22. #02022022200222
🎯 [20:02:20] @ https://twitter.com/marcellodesales/status/1489086830280511491: This is the unique tweet at 02/02/2022 at 20:02:20. #02022022200220
❌ [20:02:03] @ https://twitter.com/marcellodesales/status/1489086759103131649: This is the unique tweet at 02/02/2022 at 20:02:02. #02022022200202
🎯 [20:02:00] @ https://twitter.com/marcellodesales/status/1489086745995988994: This is the unique tweet at 02/02/2022 at 20:02:00. #02022022200200
❌ [20:00:29] @ https://twitter.com/marcellodesales/status/1489086364670824448: This is the unique tweet at 02/02/2022 at 20:00:22. #02022022200022
🎯 [20:00:20] @ https://twitter.com/marcellodesales/status/1489086327295336448: This is the unique tweet at 02/02/2022 at 20:00:20. #02022022200020
❌ [20:00:04] @ https://twitter.com/marcellodesales/status/1489086257158254596: This is the unique tweet at 02/02/2022 at 20:00:02. #02022022200002
❌ [20:00:01] @ https://twitter.com/marcellodesales/status/1489086243891662850: This is the unique tweet at 02/02/2022 at 20:00:00. #02022022200000
❌ [02:22:37] @ https://twitter.com/marcellodesales/status/1488820144201551873: This is the unique tweet at 02/02/2022 at 02:22:22. #02022022022222
❌ [02:22:29] @ https://twitter.com/marcellodesales/status/1488820109632163841: This is the unique tweet at 02/02/2022 at 02:22:20. #02022022022220
❌ [02:22:11] @ https://twitter.com/marcellodesales/status/1488820033870389249: This is the unique tweet at 02/02/2022 at 02:22:02. #02022022022202
❌ [02:22:09] @ https://twitter.com/marcellodesales/status/1488820023736954884: This is the unique tweet at 02/02/2022 at 02:22:00. #02022022022200
❌ [02:20:41] @ https://twitter.com/marcellodesales/status/1488819653652533250: This is the unique tweet at 02/02/2022 at 02:20:22
❌ [02:20:31] @ https://twitter.com/marcellodesales/status/1488819612049309697: This is the unique tweet at 02/02/2022 at 02:20:20
❌ [02:20:27] @ https://twitter.com/marcellodesales/status/1488819598459760640: This is the unique tweet at 02/02/2022 at 02:20:02
❌ [02:20:23] @ https://twitter.com/marcellodesales/status/1488819580252217345: This is the unique tweet at 02/02/2022 at 02:20:00
❌ [02:02:24] @ https://twitter.com/marcellodesales/status/1488815054443061250: This is the unique tweet at 02/02/2022 at 02:02:22
🎯 [02:02:20] @ https://twitter.com/marcellodesales/status/1488815038232031233: This is the unique tweet at 02/02/2022 at 02:02:20
❌ [02:02:03] @ https://twitter.com/marcellodesales/status/1488814967281176577: This is the unique tweet at 02/02/2022 at 02:02:02
🎯 [02:02:00] @ https://twitter.com/marcellodesales/status/1488814954719240192: This is the unique tweet at 02/02/2022 at 02:02:00
❌ [02:00:31] @ https://twitter.com/marcellodesales/status/1488814581547823106: This is the unique tweet at 02/02/2022 at 02:00:22
❌ [02:00:21] @ https://twitter.com/marcellodesales/status/1488814537692176386: This is the unique tweet at 02/02/2022 at 02:00:20
❌ [02:00:07] @ https://twitter.com/marcellodesales/status/1488814479156473860: This is the unique tweet at 02/02/2022 at 02:00:02
❌ [02:00:01] @ https://twitter.com/marcellodesales/status/1488814456020733952: This is the unique tweet at 02/02/2022 at 02:00:00
❌ [00:22:25] @ https://twitter.com/marcellodesales/status/1488789893752885254: This is the unique tweet at 02/02/2022 at 00:22:22
❌ [00:22:19] @ https://twitter.com/marcellodesales/status/1488789868167581696: This is the unique tweet at 02/02/2022 at 00:22:20
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
