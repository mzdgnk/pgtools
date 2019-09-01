# -*- coding: utf-8 -*-
import psycopg2
import pandas as pd


class PostgresTools():
    def __init__(self, pg_info):
        self.table = 'users'
        self.pg_info=pg_info

    def create_table(self):
        columns = {
            'id': 'serial',
            'name': 'text',
            'primary': 'key(id)'
        }
        with psycopg2.connect(**self.pg_info) as conn:
            util = PostgresUtils(conn)
            util.create_table(
                name=self.table,
                columns=columns
            )

    def insert(self, name):
        with psycopg2.connect(**self.pg_info) as conn:
            util = PostgresUtils(conn)
            util.insert(
                table=self.table,
                data={'name': name}
            )

    def list(self):
        with psycopg2.connect(**self.pg_info) as conn:
            util = PostgresUtils(conn)
            return util.select(
                    table=self.table,
                    index_col='id'
                )

    def delete_all(self):
        with psycopg2.connect(**self.pg_info) as conn:
            util = PostgresUtils(conn)
            util.delete_all_rows(self.table)

    def delete(self, name):
        with psycopg2.connect(**self.pg_info) as conn:
            util = PostgresUtils(conn)
            util.delete(self.table, name=name)


class PostgresUtils():
    def __init__(self, conn):
        self.conn = conn

    def create_table(self, name, columns):
        sql = 'create table {name} ({columns})'.format(
            name=name,
            columns=','.join(['{0} {1}'.format(k, v) for (k, v) in columns.items()])
        )
        with self.conn.cursor() as cur:
            cur.execute(sql)
        self.conn.commit()

    def insert(self, table, data):
        sql = 'insert into {table} ({keys}) values ({values})'.format(
            table=table,
            keys=','.join(data.keys()),
            values=','.join(["'{}'".format(v) for v in data.values()])
        )
        with self.conn.cursor() as cur:
            cur.execute(sql)
        self.conn.commit()

    def select(self, table, index_col):
        return pd.read_sql(
            sql='select * from {table}'.format(table=table),
            con=self.conn,
            index_col=index_col
        )

    def delete(self, table, **kwargs):
        sql = "delete from {table} where {where}".format(
            table=table,
            where=' AND '.join(["{0}='{1}'".format(k, v) for (k, v) in kwargs.items()])
        )
        with self.conn.cursor() as cur:
            cur.execute(sql)
        self.conn.commit()

    def delete_all_rows(self, table):
        sql = 'delete from {}'.format(table)
        with self.conn.cursor() as cur:
            cur.execute(sql)
        self.conn.commit()

