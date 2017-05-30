# -*- coding: utf-8 -*-
import random
import datetime

from tweet_db import tweet_list


class TweetGenerator(object):
    tweets = tweet_list

    def _get_tweet(self, tag):
        lentweets = len(self.tweets)
        proposed_tweet = self.tweets[random.randint(0, lentweets - 1)]
        if tag in proposed_tweet['time_tags'] or 'any' in proposed_tweet['time_tags']:
            return proposed_tweet['tweet_templ']
        return self._get_tweet(tag)

    def _get_tag(self):
        now = datetime.datetime.now()
        hour = now.hour

        if hour in range(0, 6):
            return 'night'
        elif hour in range(6, 11):
            return 'morning'
        elif hour in range(11, 14):
            return 'lunch'
        elif hour in range(14, 18):
            return 'afternoon'
        else:
            return 'evening'

    def get_tweet(self):
        return self._get_tweet(self._get_tag())

