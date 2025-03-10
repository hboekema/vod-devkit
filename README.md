# <img src="docs/nutonomy-logo-big-r.svg" width="182px" height="46px" style="vertical-align: middle" /> VOD™ devkit
Welcome to the nuTonomy® downloadable driverless vehicle software page. Click on the green box above labeled "Code" to download a copy of the software described below.


![](https://www.vod.org/public/images/road.jpg)

## Overview
- [Changelog](#changelog)
- [Devkit setup](#devkit-setup)
- [nuImages](#nuimages)
  - [nuImages setup](#nuimages-setup) 
  - [Getting started with nuImages](#getting-started-with-nuimages)
- [VOD](#vod)
  - [VOD setup](#vod-setup)
  - [Panoptic VOD](#panoptic-vod)
  - [VOD-lidarseg](#vod-lidarseg)
  - [Prediction challenge](#prediction-challenge)
  - [CAN bus expansion](#can-bus-expansion)
  - [Map expansion](#map-expansion)
  - [Map versions](#map-versions)
  - [Getting started with VOD](#getting-started-with-vod)
- [Known issues](#known-issues)
- [Citation](#citation)

## Changelog
- Feb. 13, 2023: Devkit v1.1.10: Specify version for various pip requirements.
- Sep. 20, 2021: Devkit v1.1.9: Refactor tracking eval code for custom datasets with different classes.
- Sep. 17, 2021: Devkit v1.1.8: Add PAT metric to Panoptic VOD.
- Aug. 23, 2021: Devkit v1.1.7: Add more panoptic tracking metrics to Panoptic VOD code.
- Jul. 29, 2021: Devkit v1.1.6: Panoptic VOD v1.0 code, NeurIPS challenge announcement.
- Apr. 5, 2021: Devkit v1.1.3: Bug fixes and pip requirements.
- Nov. 23, 2020: Devkit v1.1.2: Release map-expansion v1.3 with lidar basemap.
- Nov. 9, 2020: Devkit v1.1.1: Lidarseg evaluation code, NeurIPS challenge announcement.
- Aug. 31, 2020: Devkit v1.1.0: nuImages v1.0 and VOD-lidarseg v1.0 code release.
- Jul. 7, 2020: Devkit v1.0.9: Misc updates on map and prediction code.
- Apr. 30, 2020: nuImages v0.1 code release.
- Apr. 1, 2020: Devkit v1.0.8: Relax pip requirements and reorganize prediction code.
- Mar. 24, 2020: Devkit v1.0.7: VOD prediction challenge code released.
- Feb. 12, 2020: Devkit v1.0.6: CAN bus expansion released.
- Dec. 11, 2019: Devkit v1.0.5: Remove weight factor from AMOTA tracking metrics.
- Nov. 1, 2019: Tracking eval code released and detection eval code reorganized.
- Jul. 1, 2019: Map expansion released.
- Apr. 30, 2019: Devkit v1.0.1: loosen PIP requirements, refine detection challenge, export 2d annotation script. 
- Mar. 26, 2019: Full dataset, paper, & devkit v1.0.0 released. Support dropped for teaser data.
- Dec. 20, 2018: Initial evaluation code released. Devkit folders restructured, which breaks backward compatibility.
- Nov. 21, 2018: RADAR filtering and multi sweep aggregation.
- Oct. 4, 2018: Code to parse RADAR data released.
- Sep. 12, 2018: Devkit for teaser dataset released.

## Devkit setup
We use a common devkit for VOD and nuImages.
The devkit is tested for Python 3.6 and Python 3.7.
To install Python, please check [here](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md#install-python).

Our devkit is available and can be installed via [pip](https://pip.pypa.io/en/stable/installing/) :
```
pip install vod-devkit
```
For an advanced installation, see [installation](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md) for detailed instructions.

## nuImages
nuImages is a stand-alone large-scale image dataset.
It uses the same sensor setup as the 3d VOD dataset.
The structure is similar to VOD and both use the same devkit, which make the installation process simple.

### nuImages setup
To download nuImages you need to go to the [Download page](https://www.vod.org/download), 
create an account and agree to the VOD [Terms of Use](https://www.vod.org/terms-of-use).
For the devkit to work you will need to download *at least the metadata and samples*, the *sweeps* are optional.
Please unpack the archives to the `/data/sets/nuimages` folder \*without\* overwriting folders that occur in multiple archives.
Eventually you should have the following folder structure:
```
/data/sets/nuimages
    samples	-	Sensor data for keyframes (annotated images).
    sweeps  -   Sensor data for intermediate frames (unannotated images).
    v1.0-*	-	JSON tables that include all the meta data and annotations. Each split (train, val, test, mini) is provided in a separate folder.
```
If you want to use another folder, specify the `dataroot` parameter of the NuImages class (see tutorial).

### Getting started with nuImages

Please follow these steps to make yourself familiar with the nuImages dataset:
- Get the [vod-devkit code](https://github.com/nutonomy/vod-devkit).
- Run the tutorial using:
```
jupyter notebook $HOME/vod-devkit/python-sdk/tutorials/nuimages_tutorial.ipynb
```
- See the [database schema](https://github.com/nutonomy/vod-devkit/blob/master/docs/schema_nuimages.md) and [annotator instructions](https://github.com/nutonomy/vod-devkit/blob/master/docs/instructions_nuimages.md).

## VOD

### VOD setup
To download VOD you need to go to the [Download page](https://www.vod.org/download), 
create an account and agree to the VOD [Terms of Use](https://www.vod.org/terms-of-use).
After logging in you will see multiple archives. 
For the devkit to work you will need to download *all* archives.
Please unpack the archives to the `/data/sets/vod` folder \*without\* overwriting folders that occur in multiple archives.
Eventually you should have the following folder structure:
```
/data/sets/vod
    samples	-	Sensor data for keyframes.
    sweeps	-	Sensor data for intermediate frames.
    maps	-	Folder for all map files: rasterized .png images and vectorized .json files.
    v1.0-*	-	JSON tables that include all the meta data and annotations. Each split (trainval, test, mini) is provided in a separate folder.
```
If you want to use another folder, specify the `dataroot` parameter of the VOD class (see tutorial).

### Panoptic VOD
In August 2021 we published [Panoptic VOD](https://www.vod.org/panoptic) which contains the panoptic labels
of the point clouds for the approximately 40,000 keyframes in VOD.
To install Panoptic VOD, please follow these steps:
- Download the dataset from the [Download page](https://www.vod.org/download),
- Extract the `panoptic` and `v1.0-*` folders to your VOD root directory (e.g. `/data/sets/vod/panoptic`, `/data/sets/vod/v1.0-*`).
- Get the latest version of the vod-devkit.
- Get started with the [tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/vod_lidarseg_panoptic_tutorial.ipynb).

### VOD-lidarseg
In August 2020 we published [VOD-lidarseg](https://www.vod.org/vod#lidarseg) which contains the semantic labels of the point clouds for the approximately 40,000 keyframes in VOD.
To install VOD-lidarseg, please follow these steps:
- Download the dataset from the [Download page](https://www.vod.org/download),
- Extract the `lidarseg` and `v1.0-*` folders to your VOD root directory (e.g. `/data/sets/vod/lidarseg`, `/data/sets/vod/v1.0-*`).
- Get the latest version of the vod-devkit.
- If you already have a previous version of the devkit, update the pip requirements (see [details](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md)): `pip install -r setup/requirements.txt`
- Get started with the [tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/vod_lidarseg_panoptic_tutorial.ipynb).

### Prediction challenge
In March 2020 we released code for the VOD prediction challenge.
To get started:
- Download the version 1.2 of the map expansion (see below).
- Download the trajectory sets for [CoverNet](https://arxiv.org/abs/1911.10298) from [here](https://www.vod.org/public/vod-prediction-challenge-trajectory-sets.zip).
- Go through the [prediction tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/prediction_tutorial.ipynb).
- For information on how submissions will be scored, visit the challenge [website](https://www.vod.org/prediction).

### CAN bus expansion
In February 2020 we published the CAN bus expansion.
It contains low-level vehicle data about the vehicle route, IMU, pose, steering angle feedback, battery, brakes, gear position, signals, wheel speeds, throttle, torque, solar sensors, odometry and more.
To install this expansion, please follow these steps:
- Download the expansion from the [Download page](https://www.vod.org/download),
- Extract the can_bus folder to your VOD root directory (e.g. `/data/sets/vod/can_bus`).
- Get the latest version of the vod-devkit.
- If you already have a previous version of the devkit, update the pip requirements (see [details](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md)): `pip install -r setup/requirements.txt`
- Get started with the [CAN bus readme](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/vod/can_bus/README.md) or [tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/can_bus_tutorial.ipynb).

### Map expansion
In July 2019 we published a map expansion with 11 semantic layers (crosswalk, sidewalk, traffic lights, stop lines, lanes, etc.).
To install this expansion, please follow these steps:
- Download the expansion from the [Download page](https://www.vod.org/download),
- Extract the contents (folders `basemap`, `expansion` and `prediction`) to your VOD `maps` folder.
- Get the latest version of the vod-devkit.
- If you already have a previous version of the devkit, update the pip requirements (see [details](https://github.com/nutonomy/vod-devkit/blob/master/docs/installation.md)): `pip install -r setup/requirements.txt`
- Get started with the [map expansion tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/map_expansion_tutorial.ipynb).
For more information, see the [map versions](#map-versions) below.

### Map versions
Here we give a brief overview of the different map versions:
- **v1.3**: Add BitMap class that supports new lidar basemap and legacy semantic prior map. Remove [one broken lane](https://github.com/nutonomy/vod-devkit/issues/493).
- **v1.2**: Expand devkit and maps to include arcline paths and lane connectivity for the prediction challenge.
- **v1.1**: Resolved issues with ego poses being off the drivable surface.
- **v1.0**: Initial map expansion release from July 2019. Supports 11 semantic layers.
- **VOD v1.0**: Came with a bitmap for the semantic prior. All code is contained in vod.py.

### Getting started with VOD
Please follow these steps to make yourself familiar with the VOD dataset:
- Read the [dataset description](https://www.vod.org/vod#overview).
- [Explore](https://www.vod.org/vod#explore) the lidar viewer and videos.
- [Download](https://www.vod.org/download) the dataset. 
- Get the [vod-devkit code](https://github.com/nutonomy/vod-devkit).
- Read the [online tutorial](https://www.vod.org/vod#tutorials) or run it yourself using:
```
jupyter notebook $HOME/vod-devkit/python-sdk/tutorials/vod_tutorial.ipynb
```
- Read the [VOD paper](https://www.vod.org/publications) for a detailed analysis of the dataset.
- Run the [map expansion tutorial](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/tutorials/map_expansion_tutorial.ipynb).
- Take a look at the [experimental scripts](https://github.com/nutonomy/vod-devkit/tree/master/python-sdk/vod/scripts).
- For instructions related to the object detection task (results format, classes and evaluation metrics), please refer to [this readme](https://github.com/nutonomy/vod-devkit/blob/master/python-sdk/vod/eval/detection/README.md).
- See the [database schema](https://github.com/nutonomy/vod-devkit/blob/master/docs/schema_vod.md) and [annotator instructions](https://github.com/nutonomy/vod-devkit/blob/master/docs/instructions_vod.md).
- See the [FAQs](https://github.com/nutonomy/vod-devkit/blob/master/docs/faqs.md).

## Known issues
Great care has been taken to collate the VOD dataset and many users have praised the quality of the data and annotations.
However, some minor issues remain:

**Maps**:
- For *singapore-hollandvillage* and *singapore-queenstown* the traffic light 3d poses are all 0 (except for tz).
- For *boston-seaport*, the ego poses of 3 scenes (499, 515, 517) are slightly incorrect and 2 scenes (501, 502) are outside the annotated area. 
- For *singapore-onenorth*, the ego poses of about 10 scenes were off the drivable surface. This has been **resolved in map v1.1**.
- Some lanes are disconnected from the rest of the lanes. We chose to keep these as they still provide valuable information. 

**Annotations**:
- A small number of 3d bounding boxes is annotated despite the object being temporarily occluded. For this reason we make sure to **filter objects without lidar or radar points** in the VOD benchmarks. See [issue 366](https://github.com/nutonomy/vod-devkit/issues/366).

## Citation
Please use the following citation when referencing [VOD or nuImages](https://arxiv.org/abs/1903.11027):
```
@article{vod2019,
  title={VOD: A multimodal dataset for autonomous driving},
  author={Holger Caesar and Varun Bankiti and Alex H. Lang and Sourabh Vora and 
          Venice Erin Liong and Qiang Xu and Anush Krishnan and Yu Pan and 
          Giancarlo Baldan and Oscar Beijbom},
  journal={arXiv preprint arXiv:1903.11027},
  year={2019}
}
```

Please use the following citation when referencing
[Panoptic VOD or VOD-lidarseg](https://arxiv.org/abs/2109.03805):
```
@article{fong2021panoptic,
  title={Panoptic VOD: A Large-Scale Benchmark for LiDAR Panoptic Segmentation and Tracking},
  author={Fong, Whye Kit and Mohan, Rohit and Hurtado, Juana Valeria and Zhou, Lubing and Caesar, Holger and
          Beijbom, Oscar and Valada, Abhinav},
  journal={arXiv preprint arXiv:2109.03805},
  year={2021}
}
```

![](https://www.vod.org/public/images/vod-example.png)
