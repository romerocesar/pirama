'''
copy runs across mlflow experiments

usage:
  pirama [options]

options:
 -m --metric=<name>    name of the performance metric used to identify the best run in an experiment. ignored if a run id is provided.
 -r --run=<id>         run from which to read data.
 -s --source=<name>    name of the experiment from which to copy data. cannot be used together with -r. if used, -m is required as well.
 -t --target=<name>    name of the target experiment in which a new run will be created and data logged.
 -h --help             show this message.
'''
import logging
import sys

import docopt
import mlflow

logger = logging.getLogger('pirama')
logging.basicConfig(level=logging.INFO)

client = mlflow.tracking.MlflowClient(tracking_uri='https://mlflow.ouva.dev')


def create_run(src=None, exname:str = None):
    if not exname:
        raise ValueError('cannot create run without an experiment name')
    logger.debug(f'creating new run in experiment {exname} starting from run {src}')
    # Create a new run in the destination experiment
    experiment = client.get_experiment_by_name(name=exname)
    dest_run = client.create_run(experiment.experiment_id)
    # Log parameters, metrics, and tags
    for key, value in src.data.params.items():
        client.log_param(dest_run.info.run_id, key, value)

    for key, value in src.data.metrics.items():
        client.log_metric(dest_run.info.run_id, key, value)

    for key, value in src.data.tags.items():
        client.set_tag(dest_run.info.run_id, key, value)

    logger.info(f'created new run as {dest_run}')


def read_run(runid: str):
    if not runid:
        logger.error('run id (-r) is required to copy data from one run into another experiment. see -h for more help.')
        sys.exit(1)
    logger.debug(f'reading run {runid}')
    run = client.get_run(runid)
    logger.info(f'fetched data from run {run.info}')
    return run


def main():
    args = docopt.docopt(__doc__)
    runid = args['--run']
    run = read_run(runid)
    exname = args['--target']
    create_run(src=run, exname=exname)

if __name__ == '__main__':
    main()
