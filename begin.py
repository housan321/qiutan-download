# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:43:56 2019

@author: ASUS
"""

import os,time
from multiprocessing import Process
from scrapy import cmdline
from qiutan.db_sql import MySql
import pymysql
import csv
import codecs

def spider():
    print('爬虫进程开始运行...')
    cmdline.execute('scrapy crawl Ec'.split())



if __name__=='__main__':#在win系统下必须要满足这个if条件
    db = MySql('localhost', 'root', '123456', 'qiutan', 3306)

    #1 先清除旧数据
    # del_sql1 = 'truncate table all_match_score;'
    # del_sql2 = 'truncate table all_match_oz_odds;'
    # del_sql3 = 'truncate table all_match_az_odds;'
    # del_sql4 = 'truncate table league_match_data;'
    # db.del_item(del_sql1)
    # db.del_item(del_sql2)
    # db.del_item(del_sql3)
    # db.del_item(del_sql4)

    #2 开启爬虫进程
    print('%主进程号',os.getpid())#主进程号
    spi = Process(target=spider)#创建子进程对象，并传参args=(X,),注意只传一个参数的时候必须在参数后加逗号
    spi.start()
    spi.join()
    print('爬虫进程结束...')
    print('%主进程的父进程', os.getppid())#主进程的父进程

    #3 合并数据，保存到文件
    print('合并数据...')
    union_sql = 'insert into league_match_data (league,season,bs_num_id,lunci,hometeam, awayteam,bs_time,FTR,FTRR,h_win,h_draw,h_lost,a_win,a_draw,a_lost,HTGS,ATGS,HTGC,ATGC,HTGD,ATGD,HTP,ATP,HomeLP,AwayLP,VTFormPtsStr,HTFormPtsStr,ATFormPtsStr,' \
                ' oz_home0_mean, oz_draw0_mean, oz_away0_mean, oz_home9_mean, oz_draw9_mean, oz_away9_mean, oz_home0_std, oz_draw0_std, oz_away0_std, oz_home9_std, oz_draw9_std, oz_away9_std, ' \
                'az_home0_mean, az_size0_mean, az_away0_mean, az_home9_mean, az_size9_mean, az_away9_mean, az_home0_std, az_size0_std, az_away0_std, az_home9_std, az_size9_std, az_away9_std, az_value0, az_value9)' \
                ' SELECT score.league, score.season, score.bs_num_id, score.lunci, score.hometeam, score.awayteam, score.bs_time, score.FTR, score.FTRR, score.h_win, score.h_draw, score.h_lost, score.a_win, score.a_draw, score.a_lost, ' \
                'score.HTGS, score.ATGS, score.HTGC, score.ATGC, score.HTGD, score.ATGD, score.HTP, score.ATP, score.HomeLP, score.AwayLP, score.VTFormPtsStr, score.HTFormPtsStr, score.ATFormPtsStr, ' \
                'oz.oz_home0_mean, oz.oz_draw0_mean, oz.oz_away0_mean, oz.oz_home9_mean, oz.oz_draw9_mean, oz.oz_away9_mean, oz.oz_home0_std, oz.oz_draw0_std, oz.oz_away0_std, oz.oz_home9_std, oz.oz_draw9_std, oz.oz_away9_std,' \
                ' az.az_home0_mean, az.az_size0_mean, az.az_away0_mean, az.az_home9_mean, az.az_size9_mean, az.az_away9_mean, az.az_home0_std, az.az_size0_std, az.az_away0_std, az.az_home9_std, az.az_size9_std, az.az_away9_std, az.az_value0, az.az_value9 ' \
                'FROM all_match_score score JOIN  all_match_oz_odds oz  ON score.bs_num_id=oz.bs_num_id JOIN all_match_az_odds az ON score.bs_num_id=az.bs_num_id ;'
    db.union_item(union_sql)

    #4 保存表到文件
    print('保存表到文件...')
    save_sql = "select * into outfile \'D:/qiutan_predict/prediction/datasets/league/league_match_data(31).csv\'character set gbk fields terminated by ',' lines terminated by '\n' " \
               "from(select 'league', 'season', 'bs_num_id', 'lunci', 'hometeam', 'awayteam', 'bs_time', 'FTR','FTRR', 'h_win', 'h_draw', 'h_lost', 'a_win', 'a_draw', 'a_lost'," \
               " 'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTGD', 'ATGD', 'HTP', 'ATP', 'HomeLP', 'AwayLP', 'VTFormPtsStr', 'HTFormPtsStr', 'ATFormPtsStr', " \
               " 'oz_home0_mean', 'oz_draw0_mean', 'oz_away0_mean', 'oz_home9_mean', 'oz_draw9_mean', 'oz_away9_mean', 'oz_home0_std', 'oz_draw0_std', 'oz_away0_std', 'oz_home9_std', 'oz_draw9_std', 'oz_away9_std'," \
               " 'az_home0_mean', 'az_size0_mean', 'az_away0_mean', 'az_home9_mean', 'az_size9_mean', 'az_away9_mean', 'az_home0_std', 'az_size0_std', 'az_away0_std', 'az_home9_std', 'az_size9_std', 'az_away9_std', 'az_value0', 'az_value9'" \
               " UNION SELECT league, season, bs_num_id, lunci, hometeam, awayteam, bs_time, FTR, FTRR, h_win, h_draw, h_lost, a_win, a_draw, a_lost, HTGS, ATGS, HTGC, ATGC, HTGD, ATGD, HTP, ATP, HomeLP, AwayLP, VTFormPtsStr, HTFormPtsStr, ATFormPtsStr," \
               " oz_home0_mean, oz_draw0_mean, oz_away0_mean, oz_home9_mean, oz_draw9_mean, oz_away9_mean, oz_home0_std, oz_draw0_std, oz_away0_std, oz_home9_std, oz_draw9_std, oz_away9_std," \
               " az_home0_mean, az_size0_mean, az_away0_mean, az_home9_mean, az_size9_mean, az_away9_mean, az_home0_std, az_size0_std, az_away0_std, az_home9_std, az_size9_std, az_away9_std, az_value0, az_value9 from league_match_data) a ;"
    db.save_to_csv(save_sql)










    # 创建合并的新表语句
    # union_sql = 'CREATE TABLE league_match_data SELECT score.league, score.season, score.bs_num_id, score.lunci, score.hometeam, score.awayteam, score.bs_time, score.FTR, score.FTRR, score.h_win, score.h_draw, score.h_lost, score.a_win, score.a_draw, score.a_lost, ' \
    #             'score.HTGS, score.ATGS, score.HTGC, score.ATGC, score.HTGD, score.ATGD, score.HTP, score.ATP, score.HomeLP, score.AwayLP, score.VTFormPtsStr, score.HTFormPtsStr, score.ATFormPtsStr,' \
    #             'oz.oz_home0_mean, oz.oz_draw0_mean, oz.oz_away0_mean, oz.oz_home9_mean, oz.oz_draw9_mean, oz.oz_away9_mean, oz.oz_home0_std, oz.oz_draw0_std, oz.oz_away0_std, oz.oz_home9_std, oz.oz_draw9_std, oz.oz_away9_std, ' \
    #             'az.az_home0_mean, az.az_size0_mean, az.az_away0_mean, az.az_home9_mean, az.az_size9_mean, az.az_away9_mean, az.az_home0_std, az.az_size0_std, az.az_away0_std, az.az_home9_std, az.az_size9_std, az.az_away9_std, az.az_value0, az.az_value9 ' \
    #             'FROM all_match_score score JOIN  all_match_oz_odds oz  on score.bs_num_id=oz.bs_num_id JOIN all_match_az_odds az ON score.bs_num_id=az.bs_num_id ;'
    #


