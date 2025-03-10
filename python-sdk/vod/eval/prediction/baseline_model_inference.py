# VOD dev-kit.
# Code written by Freddy Boulton, 2020.

""" Script for running baseline models on a given vod-split. """

import argparse
import json
import os

from vod import VOD
from vod.eval.prediction.config import load_prediction_config
from vod.eval.prediction.splits import get_prediction_challenge_split
from vod.prediction import PredictHelper
from vod.prediction.models.physics import ConstantVelocityHeading, PhysicsOracle


def main(version: str, data_root: str,
         split_name: str, output_dir: str, config_name: str = 'predict_2020_icra.json') -> None:
    """
    Performs inference for all of the baseline models defined in the physics model module.
    :param version: VOD dataset version.
    :param data_root: Directory where the VOD data is stored.
    :param split_name: VOD data split name, e.g. train, val, mini_train, etc.
    :param output_dir: Directory where predictions should be stored.
    :param config_name: Name of config file.
    """

    nusc = VOD(version=version, dataroot=data_root)
    helper = PredictHelper(nusc)
    dataset = get_prediction_challenge_split(split_name, dataroot=data_root)
    config = load_prediction_config(helper, config_name)
    oracle = PhysicsOracle(config.seconds, helper)
    cv_heading = ConstantVelocityHeading(config.seconds, helper)

    cv_preds = []
    oracle_preds = []
    for token in dataset:
        cv_preds.append(cv_heading(token).serialize())
        oracle_preds.append(oracle(token).serialize())

    json.dump(cv_preds, open(os.path.join(output_dir, "cv_preds.json"), "w"))
    json.dump(oracle_preds, open(os.path.join(output_dir, "oracle_preds.json"), "w"))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Perform Inference with baseline models.')
    parser.add_argument('--version', help='VOD version number.')
    parser.add_argument('--data_root', help='Directory storing VOD data.', default='/data/sets/vod')
    parser.add_argument('--split_name', help='Data split to run inference on.')
    parser.add_argument('--output_dir', help='Directory to store output files.')
    parser.add_argument('--config_name', help='Config file to use.', default='predict_2020_icra.json')

    args = parser.parse_args()
    main(args.version, args.data_root, args.split_name, args.output_dir, args.config_name)
