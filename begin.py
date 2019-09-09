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
    del_sql1 = 'truncate table all_match_score;'
    del_sql2 = 'truncate table all_match_oz_odds;'
    del_sql3 = 'truncate table all_match_az_odds;'
    del_sql4 = 'truncate table league_match_data;'
    db.del_item(del_sql1)
    db.del_item(del_sql2)
    db.del_item(del_sql3)
    db.del_item(del_sql4)

    #2 开启爬虫进程
    print('%主进程号',os.getpid())#主进程号
    spi = Process(target=spider)#创建子进程对象，并传参args=(X,),注意只传一个参数的时候必须在参数后加逗号
    spi.start()
    spi.join()
    print('爬虫进程结束...')
    print('%主进程的父进程', os.getppid())#主进程的父进程

    #3 合并数据，保存到文件
    print('合并数据...')
    union_sql = 'insert into league_match_data (league,season,bs_num_id,lunci,hometeam, awayteam,bs_time,FTR,FTRR,' \
                'h_nb_wins,h_nb_draws,h_nb_losts,HTGS,HTGC,HTGD,HTP,HLP,hh_nb_games,hh_nb_wins,hh_nb_draws,hh_nb_losts,HHTGS,HHTGC,HHTGD,HHTP,HHLP,' \
                'a_nb_wins,a_nb_draws,a_nb_losts,ATGS,ATGC,ATGD,ATP,ALP,aa_nb_games,aa_nb_wins,aa_nb_draws,aa_nb_losts,AATGS,AATGC,AATGD,AATP,AALP,VTFormPtsStr,HTFormPtsStr,ATFormPtsStr,' \
                'oz_home0_mean, oz_draw0_mean, oz_away0_mean, oz_home9_mean, oz_draw9_mean, oz_away9_mean, oz_home0_std, oz_draw0_std, oz_away0_std, oz_home9_std, oz_draw9_std, oz_away9_std, ' \
                'az_home0_mean, az_size0_mean, az_away0_mean, az_home9_mean, az_size9_mean, az_away9_mean, az_home0_std, az_size0_std, az_away0_std, az_home9_std, az_size9_std, az_away9_std, az_value0, az_value9)' \
                ' SELECT sc.league, sc.season, sc.bs_num_id, sc.lunci, sc.hometeam, sc.awayteam, sc.bs_time, sc.FTR, sc.FTRR, ' \
                'sc.h_nb_wins, sc.h_nb_draws, sc.h_nb_losts, sc.HTGS, sc.HTGC, sc.HTGD, sc.HTP, sc.HLP, sc.hh_nb_games, sc.hh_nb_wins, sc.hh_nb_draws, sc.hh_nb_losts, sc.HHTGS, sc.HHTGC, sc.HHTGD, sc.HHTP, sc.HHLP,' \
                'sc.a_nb_wins, sc.a_nb_draws, sc.a_nb_losts, sc.ATGS, sc.ATGC, sc.ATGD, sc.ATP, sc.ALP, sc.aa_nb_games, sc.aa_nb_wins, sc.aa_nb_draws, sc.aa_nb_losts, sc.AATGS, sc.AATGC, sc.AATGD, sc.AATP, sc.AALP, sc.VTFormPtsStr, sc.HTFormPtsStr, sc.ATFormPtsStr,' \
                'oz.oz_home0_mean, oz.oz_draw0_mean, oz.oz_away0_mean, oz.oz_home9_mean, oz.oz_draw9_mean, oz.oz_away9_mean, oz.oz_home0_std, oz.oz_draw0_std, oz.oz_away0_std, oz.oz_home9_std, oz.oz_draw9_std, oz.oz_away9_std, ' \
                'az.az_home0_mean, az.az_size0_mean, az.az_away0_mean, az.az_home9_mean, az.az_size9_mean, az.az_away9_mean, az.az_home0_std, az.az_size0_std, az.az_away0_std, az.az_home9_std, az.az_size9_std, az.az_away9_std, az.az_value0, az.az_value9 ' \
                'FROM all_match_score sc JOIN all_match_oz_odds oz ON sc.bs_num_id = oz.bs_num_id JOIN all_match_az_odds az ON sc.bs_num_id = az.bs_num_id ;'
    db.union_item(union_sql)

    # #4 保存表到文件
    # print('保存表到文件...')
    # save_sql = "select * into outfile \'D:/qiutan_predict/prediction/datasets/league/league_match_data(4).csv\'character set gbk fields terminated by ',' lines terminated by '\n' " \
    #            "from(select 'league','season','bs_num_id','lunci','hometeam','awayteam','bs_time','FTR','FTRR'," \
    #            " 'h_nb_wins','h_nb_draws','h_nb_losts','HTGS','HTGC','HTGD','HTP','HLP','hh_nb_games','hh_nb_wins','hh_nb_draws','hh_nb_losts','HHTGS','HHTGC','HHTGD','HHTP','HHLP'," \
    #            " 'a_nb_wins','a_nb_draws','a_nb_losts','ATGS','ATGC','ATGD','ATP','ALP','aa_nb_games','aa_nb_wins','aa_nb_draws','aa_nb_losts','AATGS','AATGC','AATGD','AATP','AALP','VTFormPtsStr','HTFormPtsStr','ATFormPtsStr'," \
    #            " 'oz_home0_mean', 'oz_draw0_mean', 'oz_away0_mean', 'oz_home9_mean', 'oz_draw9_mean', 'oz_away9_mean', 'oz_home0_std', 'oz_draw0_std', 'oz_away0_std', 'oz_home9_std', 'oz_draw9_std', 'oz_away9_std'," \
    #            " 'az_home0_mean', 'az_size0_mean', 'az_away0_mean', 'az_home9_mean', 'az_size9_mean', 'az_away9_mean', 'az_home0_std', 'az_size0_std', 'az_away0_std', 'az_home9_std', 'az_size9_std', 'az_away9_std', 'az_value0', 'az_value9' " \
    #            "UNION SELECT league,season,bs_num_id,lunci,hometeam,awayteam,bs_time,FTR,FTRR," \
    #            "h_nb_wins,h_nb_draws,h_nb_losts,HTGS,HTGC,HTGD,HTP,HLP,hh_nb_games,hh_nb_wins,hh_nb_draws,hh_nb_losts,HHTGS,HHTGC,HHTGD,HHTP,HHLP," \
    #            "a_nb_wins,a_nb_draws,a_nb_losts,ATGS,ATGC,ATGD,ATP,ALP,aa_nb_games,aa_nb_wins,aa_nb_draws,aa_nb_losts,AATGS,AATGC,AATGD,AATP,AALP,VTFormPtsStr,HTFormPtsStr,ATFormPtsStr," \
    #            "oz_home0_mean, oz_draw0_mean, oz_away0_mean, oz_home9_mean, oz_draw9_mean, oz_away9_mean, oz_home0_std, oz_draw0_std, oz_away0_std, oz_home9_std, oz_draw9_std, oz_away9_std, " \
    #            "az_home0_mean, az_size0_mean, az_away0_mean, az_home9_mean, az_size9_mean, az_away9_mean, az_home0_std, az_size0_std, az_away0_std, az_home9_std, az_size9_std, az_away9_std, az_value0, az_value9 from league_match_data) a ;"
    # db.save_to_csv(save_sql)




    # 创建合并的新表语句
    # creat_sql = 'CREATE TABLE league_match_data SELECT sc.league, sc.season, sc.bs_num_id, sc.lunci, sc.hometeam, sc.awayteam, sc.bs_time, sc.FTR, sc.FTRR,' \
    #             ' sc.h_nb_wins, sc.h_nb_draws, sc.h_nb_losts, sc.HTGS, sc.HTGC, sc.HTGD, sc.HTP, sc.HLP, sc.hh_nb_games, sc.hh_nb_wins, sc.hh_nb_draws, sc.hh_nb_losts, sc.HHTGS, sc.HHTGC, sc.HHTGD, sc.HHTP, sc.HHLP,' \
    #             ' sc.a_nb_wins, sc.a_nb_draws, sc.a_nb_losts, sc.ATGS, sc.ATGC, sc.ATGD, sc.ATP, sc.ALP, sc.aa_nb_games, sc.aa_nb_wins, sc.aa_nb_draws, sc.aa_nb_losts, sc.AATGS, sc.AATGC, sc.AATGD, sc.AATP, sc.AALP, sc.VTFormPtsStr, sc.HTFormPtsStr, sc.ATFormPtsStr, ' \
    #             'oz.oz_home0_mean, oz.oz_draw0_mean, oz.oz_away0_mean, oz.oz_home9_mean, oz.oz_draw9_mean, oz.oz_away9_mean, oz.oz_home0_std, oz.oz_draw0_std, oz.oz_away0_std, oz.oz_home9_std, oz.oz_draw9_std, oz.oz_away9_std, ' \
    #             'az.az_home0_mean, az.az_size0_mean, az.az_away0_mean, az.az_home9_mean, az.az_size9_mean, az.az_away9_mean, az.az_home0_std, az.az_size0_std, az.az_away0_std, az.az_home9_std, az.az_size9_std, az.az_away9_std, az.az_value0, az.az_value9 ' \
    #             'FROM all_match_score sc JOIN  all_match_oz_odds oz  on sc.bs_num_id=oz.bs_num_id JOIN all_match_az_odds az ON sc.bs_num_id=az.bs_num_id ;'



