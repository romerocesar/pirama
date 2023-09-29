'''
copy runs across mlflow experiments

usage:
  pirama [options]

options:
 -m --metric=<name>    name of the performance metric used to identify the best run in an experiment. ignored if a run id is provided.
 -r --run=<id>         run from which to read data.
 -s --source=<id>      id of the experiment from which to copy data. cannot be used together with -r. if used, -m is required as well.
 -t --target=<id>      target experiment id in which a new run will be created and data logged.
 -h --help             show this message.
'''
import logging
import sys

import docopt
import mlflow

logger = logging.getLogger('pirama')
logging.basicConfig(level=logging.DEBUG)


def main():
    pass

if __name__ == '__main__':
    main()
