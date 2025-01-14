#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="gaming_bucko",
    password="holyangles98",
    like_per_day=1000,
    comments_per_day=0,
    tag_list=['arquiteturaeinteriores', 'homedecor', 'instadecor', 'decoracao', 'adornos', 'decoracaobh', 'decoracaobetim', 'betim', 'noivado', 'listadecasamento', 'noivadoano', 'banheirodecorado', 'cozinhadecorada', 'design', 'designdeinteriores', 'interiores', 'home', 'saladecorada'],
    tag_blacklist=['hot', 'porn'],
    location_list=['213255513/belo-horizonte-brazil', '224209461/bh-shopping', '376912722/belo-horizonte-lourdes', '216164356/espaco-meet-porcao', '213396416/minas-brasilia-tenis-clube', '1550619/feira-hippie-de-bh', '3296752/betim', '235138272/partage-shopping-betim', '1015146082/betim-minas-gerais', '9481680/metropolitan-shopping-betim', 'condominio-ouro-verde-betim', '216459798/teuto-esporte-clube', '261803734/condominio-montserrat', '5516128/hudson-restaurante-e-pizzaria', '447149396/espaco-wedding-vestidos-dia-da-noiva', '359560619/condominio-saraiva', '1031366930/jardim-da-cidade'],
    user_blacklist={'aaa':''},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[[]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags', 'loja', 'escritorio', 'online', 'daimlerneves', 'alyssoncastro', 'daimler', 'alysson',
        'casa', 'cortina', 'decoracao', 'decor', 'moveis', 'mobilia', 'joias', 'digital', 'multimarcas', 'dress', 'fotografia', 'moda', 'modas'
    ],
    unfollow_whitelist=[])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")
    #print("####### MODE 6 = ORIGINAL MODE 0 MODIFICADO POR RENAN VILELA PARA PEGAR POR LOCATIONS. ")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 6

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    elif mode == 6:
        bot.new_auto_mod_location()

    else:
        print("Wrong mode!")
