# -*- coding: utf-8 -*-
from pgdemo.utils import PostgresTools
import fire
from tabulate import tabulate


class MainCmd(object):
    def __init__(self, host='localhost', port='5432', db='postgres', user='postgres', password='postgres'):
        self.host = host
        self.port = port
        self.dbname = db
        self.user = user
        self.password = password
        self.tool = PostgresTools(self.pg_info)

    @property
    def pg_info(self):
        return {
            'host': self.host,
            'port': self.port,
            'dbname': self.dbname,
            'user': self.user,
            'password': self.password
        }

    def create(self):
        self.tool.create_table()

    def insert(self, *args):
        for name in args:
            self.tool.insert(name)

    def list(self):
        print(tabulate(
            self.tool.list(),
            headers='keys',
            tablefmt='psql'
        ))

    def delete(self, name):
        if name == 'all':
            self.tool.delete_all()
        else:
            self.tool.delete(name=name)

def main():
    fire.Fire(MainCmd)


if __name__=='__main__':
    main()
