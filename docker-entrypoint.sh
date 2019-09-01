#!/bin/sh

pgdemo \
  --host $POSTGRES_HOST \
  --port $POSTGRES_PORT \
  --db $POSTGRES_DB \
  --user $POSTGRES_USER \
  --password $POSTGRES_PASSWORD \
  $@
