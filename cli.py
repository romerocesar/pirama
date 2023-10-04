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

client = mlflow.tracking.MlflowClient()


def create_run(src=None, exid=None):
    logger.debug(f'creating new run in experiment {exid} starting from run {src}')
    # Create a new run in the destination experiment
    dest_run = client.create_run(exid)
    # Log parameters, metrics, and tags
    for key, value in src.data.params.items():
        client.log_param(dest_run.info.run_id, key, value)

    for key, value in src.data.metrics.items():
        client.log_metric(dest_run.info.run_id, key, value)

    for key, value in src.data.tags.items():
        client.set_tag(dest_run.info.run_id, key, value)

    logger.info(f'created new run as {dest_run}')


def read_run(runid: str):
    logger.debug(f'reading run {runid}')
    run = client.get_run(runid)
    logger.info(f'fetched data from run {run}')
    return run



def main():
    args = docopt.docopt(__doc__)
    read_run(args['--run'])

if __name__ == '__main__':
    main()
