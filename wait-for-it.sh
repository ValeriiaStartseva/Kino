#!/usr/bin/env bash
# wait-for-it.sh

host="$1"
shift
port="$1"
shift
cmd="$@"

while ! nc -z "$host" "$port"; do
  sleep 1
done

exec $cmd
