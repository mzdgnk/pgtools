# -*- coding: utf-8 -*-
from pgdemo.utils import PostgresTools
import fire
from tabulate import tabulate
import os


class MainCmd(object):
    def __init__(self, host=None, port=None, db=None, user=None, password=None):
        self.host = host if host else os.environ.get('POSTGRES_HOST', 'localhost')
        self.port = port if port else os.environ.get('POSTGRES_PORT', '5432')
        self.dbname = db if db else os.environ.get('POSTGRES_DB', 'postgres')
        self.user = user if user else os.environ.get('POSTGRES_USER', 'postgres')
        self.password = password if password else os.environ.get('POSTGRES_PASSWORD', 'postgres')
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
        self.list()

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
        self.list()

def main():
    fire.Fire(MainCmd)


if __name__=='__main__':
    main()
