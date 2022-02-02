# 02022022

This is a time capsule for the special day that won't repeat!

There are only 2 characters in today's date. But, I wanted to keep a record of today's time as well in the form of tweets.
This will generate all the tweets for today that matches all combinations of hour:minute:second.

There will be also NFT entries in different blockchains for time capsule purposes!

# Main script

* It calls `combinations.py` to generate the list of next hours.
* Then, it waits until one of the hours is a match to tweet.
  * Example: `02/02/2022 at 02:22:22` https://twitter.com/marcellodesales/status/1488820144201551873

## Logs

```console
Current time: 02/02/2022 at 02:02:18  Waiting for 02/02/2022 at 02:02:20
Current time: 02/02/2022 at 02:02:18  Waiting for 02/02/2022 at 02:02:20
Current time: 02/02/2022 at 02:02:19  Waiting for 02/02/2022 at 02:02:20
Current time: 02/02/2022 at 02:02:19  Waiting for 02/02/2022 at 02:02:20
Current time: 02/02/2022 at 02:02:19  Waiting for 02/02/2022 at 02:02:20
Current time: 02/02/2022 at 02:02:20  Waiting for 02/02/2022 at 02:02:20

########### Unique !!!!! ----

* Will tweet at 02:02:20

Current time: 02/02/2022 at 02:02:20  Waiting for 02/02/2022 at 02:02:22
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

# Tweet.sh

This script was copied from https://github.com/piroor/tweet.sh

## Setup Tweet.sh 

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

## Test tweet.sh

1. Call `./tweet.sh post "Message"`
