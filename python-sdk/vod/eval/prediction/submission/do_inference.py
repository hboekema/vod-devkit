# VOD dev-kit.
# Code written by Freddy Boulton, 2020.
""" Script for generating a submission to the VOD prediction challenge. """
import argparse
import json
import os
from typing import List, Any

from vod import VOD
from vod.eval.prediction.config import PredictionConfig
from vod.eval.prediction.config import load_prediction_config
from vod.eval.prediction.data_classes import Prediction
from vod.eval.prediction.splits import get_prediction_challenge_split
from vod.prediction import PredictHelper
from vod.prediction.models.physics import ConstantVelocityHeading


def load_model(helper: PredictHelper, config: PredictionConfig, path_to_model_weights: str) -> Any:
    """ Loads model with desired weights. """
    return ConstantVelocityHeading(config.seconds, helper)


def do_inference_for_submission(helper: PredictHelper,
                                config: PredictionConfig,
                                dataset_tokens: List[str]) -> List[Prediction]:
    """
    Currently, this will make a submission with a constant velocity and heading model.
    Fill in all the code needed to run your model on the test set here. You do not need to worry
    about providing any of the parameters to this function since they are provided by the main function below.
    You can test if your script works by evaluating on the val set.
    :param helper: Instance of PredictHelper that wraps the VOD test set.
    :param config: Instance of PredictionConfig.
    :param dataset_tokens: Tokens of instance_sample pairs in the test set.
    :return: List of predictions.
    """

    # User: Fill in the path to the model weights here.
    path_to_model_weights = ""

    cv_heading = load_model(helper, config, path_to_model_weights)

    cv_preds = []
    for token in dataset_tokens:
        cv_preds.append(cv_heading(token))

    return cv_preds


def main(version: str, data_root: str, split_name: str, output_dir: str, submission_name: str, config_name: str) \
        -> None:
    """
    Makes predictions for a submission to the VOD prediction challenge.
    :param version: VOD version.
    :param data_root: Directory storing VOD data.
    :param split_name: Data split to run inference on.
    :param output_dir: Directory to store the output file.
    :param submission_name: Name of the submission to use for the results file.
    :param config_name: Name of config file to use.
    """
    nusc = VOD(version=version, dataroot=data_root)
    helper = PredictHelper(nusc)
    dataset = get_prediction_challenge_split(split_name)
    config = load_prediction_config(helper, config_name)

    predictions = do_inference_for_submission(helper, config, dataset)
    predictions = [prediction.serialize() for prediction in predictions]
    json.dump(predictions, open(os.path.join(output_dir, f"{submission_name}_inference.json"), "w"))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Perform Inference with baseline models.')
    parser.add_argument('--version', help='VOD version number.')
    parser.add_argument('--data_root', help='Root directory for VOD json files.')
    parser.add_argument('--split_name', help='Data split to run inference on.')
    parser.add_argument('--output_dir', help='Directory to store output file.')
    parser.add_argument('--submission_name', help='Name of the submission to use for the results file.')
    parser.add_argument('--config_name', help='Name of the config file to use', default='predict_2020_icra.json')

    args = parser.parse_args()
    main(args.version, args.data_root, args.split_name, args.output_dir, args.submission_name, args.config_name)
