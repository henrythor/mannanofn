#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import config
from name_generator import NameGenerator
from tweet_generator import TweetGenerator
import tweepy


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    api = get_api(config)

    name_gen = NameGenerator()
    tweet_gen = TweetGenerator()

    name = name_gen.get_name()
    tweet_templ = tweet_gen.get_tweet()

    api.update_status(status=tweet_templ.format(name))


if __name__ == "__main__":
    main()
