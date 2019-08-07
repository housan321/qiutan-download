import pymysql


class MySql:

    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host=host, user=user, password=password, database=database,
                                  port=port, cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def update(self, sql, data):
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
        except:
            self.db.rollback()
            print('数据修改失败,请检查sql语句~')
            print(sql, data)

    def query(self, sql, data):
        try:
            result = self.cursor.execute(sql, data)
            return result
        except:
            print('数据查询失败,请查看sql语句~')

    def save_to_csv(self, sql):
        self.cursor.execute(sql)

    def union_item(self, sql):
        # union_sql = 'insert into today_matchs (league,season,bs_num_id,lunci,hometeam, awayteam,FTR,h_win,h_draw,h_lost,a_win,a_draw,a_lost,HTGS,ATGS,HTGC,ATGC,HTGD,ATGD,HTP,ATP,HomeLP,AwayLP,VTFormPtsStr,HTFormPtsStr,ATFormPtsStr,WHH0,WHD0,WHA0,WHH9, WHD9,WHA9) ' \
        #             'select score.league,score.season,score.bs_num_id,score.lunci,score.hometeam,score.awayteam,score.FTR,score.h_win,score.h_draw,score.h_lost,score.a_win,score.a_draw,score.a_lost,score.HTGS,score.ATGS,score.HTGC,score.ATGC,score.HTGD,score.ATGD,score.HTP,score.ATP,' \
        #             'score.HomeLP,score.AwayLP,score.VTFormPtsStr,score.HTFormPtsStr,score.ATFormPtsStr,odds.WHH0,odds.WHD0,odds.WHA0,odds.WHH9,odds.WHD9,odds.WHA9 from all_match_odds odds join all_match_score score on odds.bs_num_id = score.bs_num_id ;'
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print('数据合并失败,请检查sql语句~')

    def del_item(self, sql):
        try:
            self.cursor.execute(sql)
        except:
            print('数据删除失败,请查看sql语句~')

if __name__ == '__main__':
    db = MySql('localhost', 'root', '123456', 'qiutan', 3306)



    #创建合并的新表语句
    # union_sql = 'CREATE TABLE league_match_data SELECT score.league, score.season, score.bs_num_id, score.lunci, score.hometeam, score.awayteam, score.FTR, score.h_win, score.h_draw, score.h_lost, score.a_win, score.a_draw, score.a_lost, score.HTGS, score.ATGS, score.HTGC, score.ATGC, score.HTGD, score.ATGD, score.HTP, score.ATP, score.HomeLP, score.AwayLP, score.VTFormPtsStr, score.HTFormPtsStr, score.ATFormPtsStr,oz.oz_home0_mean, oz.oz_draw0_mean, oz.oz_away0_mean, oz.oz_home9_mean, oz.oz_draw9_mean, oz.oz_away9_mean, oz.oz_home0_std, oz.oz_draw0_std, oz.oz_away0_std, oz.oz_home9_std, oz.oz_draw9_std, oz.oz_away9_std, az.az_home0_mean, az.az_size0_mean, az.az_away0_mean, az.az_home9_mean, az.az_size9_mean, az.az_away9_mean, az.az_home0_std, az.az_size0_std, az.az_away0_std, az.az_home9_std, az.az_size9_std, az.az_away9_std, az.az_value0, az.az_value9 FROM all_match_score score JOIN  all_match_oz_odds oz  on score.bs_num_id=oz.bs_num_id JOIN all_match_az_odds az ON score.bs_num_id=az.bs_num_id ;'
