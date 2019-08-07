# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from qiutan.db_sql import MySql


class QiutanPipeline(object):

    def process_item(self, item, spider):
        return item


class MySql_data_Pipeline(object):
    def __init__(self):
        self.db = MySql('localhost', 'root', '123456', 'qiutan', 3306)

    def process_item(self, item, spider):
        if hasattr(item, 'get_insert_data'):
            insert_sql, data = item.get_insert_data()
            self.db.update(insert_sql, data)

        return item

