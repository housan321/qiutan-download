# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiutanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SaichengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    league = scrapy.Field()
    season = scrapy.Field()
    lunci = scrapy.Field()
    bs_num_id = scrapy.Field()
    FTR = scrapy.Field()
    FTRR = scrapy.Field()
    bs_time = scrapy.Field()
    hometeam = scrapy.Field()
    h_team_id = scrapy.Field()
    res_score = scrapy.Field()
    awayteam = scrapy.Field()
    a_team_id = scrapy.Field()
    all_rang = scrapy.Field()
    half_rang = scrapy.Field()
    sizes_balls_a = scrapy.Field()
    sizes_balls_h = scrapy.Field()
    half_score = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_bs_data values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['league'], self['season'], self['lunci'], self['bs_num_id'], self['FTR'], self['FTRR'], self['bs_time'], self['hometeam'],
        self['h_team_id'], self['res_score'], self['awayteam'], self['a_team_id'], self['all_rang'],
        self['half_rang'], self['sizes_balls_a'], self['sizes_balls_h'], self['half_score'])
        return insert_sql, data


# all_bs_data 建表语句
# CREATE TABLE all_bs_data(id INT PRIMARY KEY AUTO_INCREMENT,
# league VARCHAR(20),
# season VARCHAR(20),
# lunci TINYINT,
# bs_num_id INT,
# FTR VARCHAR(10),
# FTRR VARCHAR(10),
# bs_time VARCHAR(20),
# hometeam VARCHAR(20),
# h_team_id VARCHAR(6),
# res_score VARCHAR(10),
# awayteam VARCHAR(20),
# a_team_id VARCHAR(6),
# all_rang VARCHAR(6),
# half_rang VARCHAR(6),
# sizes_balls_a VARCHAR(6),
# sizes_balls_h VARCHAR(6),
# half_score VARCHAR(6)
# )DEFAULT CHARSET=utf8mb4;
# alter table all_bs_data add bs_num_id int after lunci;


class Team_DataItem(scrapy.Item):
    # define the fields for your item here like:
    team_id = scrapy.Field()
    team_name = scrapy.Field()
    Eng_name = scrapy.Field()
    team_city = scrapy.Field()
    team_home = scrapy.Field()
    build_team_time = scrapy.Field()
    var_coach = scrapy.Field()
    team_youshi = scrapy.Field()
    team_style = scrapy.Field()
    team_ruodian = scrapy.Field()
    team_stats = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_team_data(team_id,team_name,Eng_name,team_city,team_home,build_team_time,var_coach,team_youshi,team_style,team_ruodian,team_stats)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['team_id'], self['team_name'], self['Eng_name'], self['team_city'], self['team_home'],
                self['build_team_time'],
                self['var_coach'], self['team_youshi'], self['team_style'], self['team_ruodian'], self['team_stats'])

        return insert_sql, data


# CREATE TABLE all_team_data(id INT PRIMARY KEY AUTO_INCREMENT,
# team_id INT,
# team_name VARCHAR(20),
# Eng_name VARCHAR(30),
# team_city VARCHAR(30),
# team_home VARCHAR(30),
# build_team_time VARCHAR(20),
# var_coach VARCHAR(20),
# team_youshi VARCHAR(200),
# team_style VARCHAR(200),
# team_ruodian VARCHAR(200),
# team_stats VARCHAR(300)
# )DEFAULT CHARSET=utf8mb4;


class Match_Score_New_Item(scrapy.Item):
    # define the fields for your item here like:
    league = scrapy.Field()
    season = scrapy.Field()
    bs_num_id = scrapy.Field()
    lunci = scrapy.Field()
    hometeam = scrapy.Field()
    awayteam = scrapy.Field()
    bs_time = scrapy.Field()
    FTR = scrapy.Field()
    FTRR = scrapy.Field()
    h_nb_wins = scrapy.Field()
    h_nb_draws = scrapy.Field()
    h_nb_losts = scrapy.Field()
    HTGS = scrapy.Field()
    HTGC = scrapy.Field()
    HTGD = scrapy.Field()
    HTP = scrapy.Field()
    HLP = scrapy.Field()
    hh_nb_games = scrapy.Field()
    hh_nb_wins = scrapy.Field()
    hh_nb_draws = scrapy.Field()
    hh_nb_losts = scrapy.Field()
    HHTGS = scrapy.Field()
    HHTGC = scrapy.Field()
    HHTGD = scrapy.Field()
    HHTP = scrapy.Field()
    HHLP = scrapy.Field()

    a_nb_wins = scrapy.Field()
    a_nb_draws = scrapy.Field()
    a_nb_losts = scrapy.Field()
    ATGS = scrapy.Field()
    ATGC = scrapy.Field()
    ATGD = scrapy.Field()
    ATP = scrapy.Field()
    ALP = scrapy.Field()
    aa_nb_games = scrapy.Field()
    aa_nb_wins = scrapy.Field()
    aa_nb_draws = scrapy.Field()
    aa_nb_losts = scrapy.Field()
    AATGS = scrapy.Field()
    AATGC = scrapy.Field()
    AATGD = scrapy.Field()
    AATP = scrapy.Field()
    AALP = scrapy.Field()

    VTFormPtsStr = scrapy.Field()
    HTFormPtsStr = scrapy.Field()
    ATFormPtsStr = scrapy.Field()


    def get_insert_data(self):
        insert_sql = 'INSERT  IGNORE  INTO all_match_score values (' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
                     '%s,%s,%s)'
        data = (
        self['league'], self['season'], self['bs_num_id'], self['lunci'], self['hometeam'], self['awayteam'], self['bs_time'], self['FTR'], self['FTRR'],
        self['h_nb_wins'], self['h_nb_draws'], self['h_nb_losts'], self['HTGS'],  self['HTGC'], self['HTGD'], self['HTP'], self['HLP'],
        self['hh_nb_games'], self['hh_nb_wins'], self['hh_nb_draws'], self['hh_nb_losts'], self['HHTGS'], self['HHTGC'], self['HHTGD'], self['HHTP'], self['HHLP'],
        self['a_nb_wins'], self['a_nb_draws'], self['a_nb_losts'], self['ATGS'], self['ATGC'],self['ATGD'], self['ATP'], self['ALP'],
        self['aa_nb_games'], self['aa_nb_wins'], self['aa_nb_draws'], self['aa_nb_losts'], self['AATGS'], self['AATGC'], self['AATGD'], self['AATP'], self['AALP'],
        self['VTFormPtsStr'], self['HTFormPtsStr'], self['ATFormPtsStr'])

        return insert_sql, data

# CREATE TABLE all_match_score(
# league VARCHAR(20),
# season VARCHAR(20),
# bs_num_id INT,
# lunci TINYINT,
# hometeam VARCHAR(20),
# awayteam VARCHAR(20),
# bs_time VARCHAR(30),
# FTR VARCHAR(10),
# FTRR VARCHAR(10),
# h_nb_wins INT,
# h_nb_draws INT,
# h_nb_losts INT,
# HTGS INT,
# HTGC INT,
# HTGD INT,
# HTP INT,
# HLP INT,
# hh_nb_games INT,
# hh_nb_wins INT,
# hh_nb_draws INT,
# hh_nb_losts INT,
# HHTGS INT,
# HHTGC INT,
# HHTGD INT,
# HHTP INT,
# HHLP INT,
# a_nb_wins INT,
# a_nb_draws INT,
# a_nb_losts INT,
# ATGS INT,
# ATGC INT,
# ATGD INT,
# ATP INT,
# ALP INT,
# aa_nb_games INT,
# aa_nb_wins INT,
# aa_nb_draws INT,
# aa_nb_losts INT,
# AATGS INT,
# AATGC INT,
# AATGD INT,
# AATP INT,
# AALP INT,
# VTFormPtsStr VARCHAR(20),
# HTFormPtsStr VARCHAR(20),
# ATFormPtsStr VARCHAR(20),
# PRIMARY KEY(bs_num_id)
# )DEFAULT CHARSET=utf8mb4;


class Match_OZ_Odds_New_Item(scrapy.Item):
    # define the fields for your item here like:
    league = scrapy.Field()
    season = scrapy.Field()
    bs_num_id = scrapy.Field()
    oz_home0_mean = scrapy.Field()
    oz_draw0_mean = scrapy.Field()
    oz_away0_mean = scrapy.Field()
    oz_home9_mean = scrapy.Field()
    oz_draw9_mean = scrapy.Field()
    oz_away9_mean = scrapy.Field()
    oz_home0_std = scrapy.Field()
    oz_draw0_std = scrapy.Field()
    oz_away0_std = scrapy.Field()
    oz_home9_std = scrapy.Field()
    oz_draw9_std = scrapy.Field()
    oz_away9_std = scrapy.Field()


    def get_insert_data(self):
        insert_sql = 'INSERT IGNORE INTO all_match_oz_odds values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['league'], self['season'], self['bs_num_id'],
        self['oz_home0_mean'], self['oz_draw0_mean'], self['oz_away0_mean'], self['oz_home9_mean'], self['oz_draw9_mean'], self['oz_away9_mean'],
        self['oz_home0_std'], self['oz_draw0_std'], self['oz_away0_std'], self['oz_home9_std'], self['oz_draw9_std'], self['oz_away9_std'])

        return insert_sql, data

# CREATE TABLE all_match_oz_odds(
# league VARCHAR(20),
# season VARCHAR(20),
# bs_num_id INT,
# oz_home0_mean FLOAT,
# oz_draw0_mean FLOAT,
# oz_away0_mean FLOAT,
# oz_home9_mean FLOAT,
# oz_draw9_mean FLOAT,
# oz_away9_mean FLOAT,
# oz_home0_std FLOAT,
# oz_draw0_std FLOAT,
# oz_away0_std FLOAT,
# oz_home9_std FLOAT,
# oz_draw9_std FLOAT,
# oz_away9_std FLOAT,
# PRIMARY KEY(bs_num_id)
# )DEFAULT CHARSET=utf8mb4;


class Match_AZ_Odds_New_Item(scrapy.Item):
    # define the fields for your item here like:
    league = scrapy.Field()
    season = scrapy.Field()
    bs_num_id = scrapy.Field()
    az_home0_mean = scrapy.Field()
    az_size0_mean = scrapy.Field()
    az_away0_mean = scrapy.Field()
    az_home9_mean = scrapy.Field()
    az_size9_mean = scrapy.Field()
    az_away9_mean = scrapy.Field()
    az_home0_std = scrapy.Field()
    az_size0_std = scrapy.Field()
    az_away0_std = scrapy.Field()
    az_home9_std = scrapy.Field()
    az_size9_std = scrapy.Field()
    az_away9_std = scrapy.Field()
    az_value0 = scrapy.Field()
    az_value9 = scrapy.Field()


    def get_insert_data(self):
        insert_sql = 'INSERT IGNORE  INTO all_match_az_odds values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['league'], self['season'], self['bs_num_id'],
        self['az_home0_mean'], self['az_size0_mean'], self['az_away0_mean'], self['az_home9_mean'], self['az_size9_mean'], self['az_away9_mean'],
        self['az_home0_std'], self['az_size0_std'], self['az_away0_std'], self['az_home9_std'], self['az_size9_std'], self['az_away9_std'],
        self['az_value0'], self['az_value9'])

        return insert_sql, data

# CREATE TABLE all_match_az_odds(
# league VARCHAR(20),
# season VARCHAR(20),
# bs_num_id INT,
# az_home0_mean FLOAT,
# az_size0_mean FLOAT,
# az_away0_mean FLOAT,
# az_home9_mean FLOAT,
# az_size9_mean FLOAT,
# az_away9_mean FLOAT,
# az_home0_std FLOAT,
# az_size0_std FLOAT,
# az_away0_std FLOAT,
# az_home9_std FLOAT,
# az_size9_std FLOAT,
# az_away9_std FLOAT,
# az_value0 FLOAT,
# az_value9 FLOAT,
# PRIMARY KEY(bs_num_id)
# )DEFAULT CHARSET=utf8mb4;











class Member_Data_New_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bs_num_id = scrapy.Field()
    team_id = scrapy.Field()
    member_id = scrapy.Field()
    member_name = scrapy.Field()
    position = scrapy.Field()
    shoot_d = scrapy.Field()
    shoot_z = scrapy.Field()
    key_ball = scrapy.Field()
    guoren = scrapy.Field()
    chuanq_count = scrapy.Field()
    chuanq_succ = scrapy.Field()
    passing = scrapy.Field()
    hengchuanc = scrapy.Field()
    success_zd = scrapy.Field()
    body_jc = scrapy.Field()
    score = scrapy.Field()
    key_event = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_member_data values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (
        self['bs_num_id'], self['team_id'], self['member_id'], self['member_name'], self['position'], self['shoot_d'],
        self['shoot_z'], self['key_ball'], self['guoren'], self['chuanq_count'], self['chuanq_succ'], self['passing']
        , self['hengchuanc'], self['success_zd'], self['body_jc'], self['score'], self['key_event'])

        return insert_sql, data


# CREATE TABLE all_member_data(id INT PRIMARY KEY AUTO_INCREMENT,
# bs_num_id INT,
# team_id INT,
# member_id INT,
# member_name VARCHAR(30),
# position VARCHAR(10),
# shoot_d INT,
# shoot_z INT,
# key_ball INT,
# guoren INT,
# chuanq_count INT,
# chuanq_succ INT,
# passing VARCHAR(200),
# hengchuanc INT,
# success_zd INT,
# body_jc INT,
# score FLOAT,
# key_event VARCHAR(20)
# )DEFAULT CHARSET=utf8mb4;

class Member_Data_Old_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bs_num_id = scrapy.Field()
    team_id = scrapy.Field()
    member_id = scrapy.Field()
    member_name = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO all_member_data(bs_num_id,team_id,member_id,member_name) values (%s,%s,%s,%s)'
        data = (self['bs_num_id'], self['team_id'], self['member_id'], self['member_name'])

        return insert_sql, data
