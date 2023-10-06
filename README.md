# pirama
this repo contains a CLI to facilitate the steps to maintain a
collection of benchmarks or leaderboards using mlflow

## authentication
set the credentials as environment variables before using the CLI

``` shell
export MLFLOW_TRACKING_USERNAME=
export MLFLOW_TRACKING_PASSWORD=
```

## usage
following POSIX standards you can get a message on how to use the command:

``` shell
$ python cli.py -h
copy runs across mlflow experiments

usage:
  pirama [options]

options:
 -m --metric=<name>    name of the performance metric used to identify the best run in an experiment. ignored if a run id is provided.
 -r --run=<id>         run from which to read data.
 -s --source=<id>      id of the experiment from which to copy data. cannot be used together with -r. if used, -m is required as well.
 -t --target=<id>      target experiment id in which a new run will be created and data logged.
 -h --help             show this message.
```
