#!/bin/sh
kubectl run pgdemo \
  --generator=run-pod/v1 \
  --restart=OnFailure \
  --rm --attach \
  --env "POSTGRES_HOST=postgres-svc" \
  --image=mzdgnk/pgdemo:stable \
  --image-pull-policy="IfNotPresent" \
  -- $@
