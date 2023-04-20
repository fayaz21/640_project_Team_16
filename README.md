# CS 640 Project_Team_16
## Small Object Detection Challenge for Spotting Birds @MVA2023

# Follow these steps to run our code.
In this README, we provide a step-by-step guide on how to use our repository for training and running the small bird object detection model. Follow these instructions to set up the environment and start training the detector effectively.

Step 1: Choose your environment. You can run the provided Jupyter notebook in the repository or execute the code on your local system. We recommend using the Jupyter notebook for a seamless experience.

Step 2: Clone the GitHub repository. After cloning, replace the configuration files in the original repository with the ones from our repository. This step is crucial, as our configuration files have been fine-tuned and optimized for better performance and integration.

Step 3: Provide the pre-trained weights in one of the code cells within the Jupyter notebook. The pre-trained weights will be normalized, allowing you to use these weights to train the detector. The estimated training time for the detector is approximately six days if you run it on the Drone2021 dataset and around 24 hours for the Train-set1 dataset.

By following these steps, you will successfully set up and run our small bird object detection model. To download the necessary weights, please refer to the provided links in the repository. Additionally, you can find dataset links within the code for easy access. We hope this guide helps you effectively use our repository. Thank you!

# Contents

Models: This directory comprises different models that we experimented with to obtain the best results for the small bird object detection task. You can find three models within this directory: Cascade-RCNN, RetinaNet, and Baseline. To run the respective models, follow the steps outlined in the README guide provided above.

Data: The data used for this project is not included in the repository due to size limitations. However, you can access it from the following Google Drive link: https://drive.google.com/drive/folders/1NWt8lap3spKKK_trOAzkdXAxlEhv2t0m?usp=sharing

## Dataset Directory Structure
**[Download Link](https://drive.google.com/drive/folders/1NWt8lap3spKKK_trOAzkdXAxlEhv2t0m?usp=sharing)**

```
data
 ├ drone2021 (62.4GB)
 │  ├ images
 │  └ annotations
 ├ project_train (9.4GB)
 │  ├ images
 │  └ annotations
 ├ project_test (8.7GB)
    ├ images
    └ annotations(including an empty annotation file)
 ```   

## Repo Structure

```
├── models
│   ├── cascade_rcnn
│   │   ├── notebook.ipynb
│   │   └── config
│   ├── retinanet
│   │   ├── notebook.ipynb
│   │   └── config
│   └── baseline
│       ├── notebook.ipynb
│       └── config
└── data

```

## Pre-Trained Weights

You can download the pre-trained weights using the following link:
**(https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_3x_coco/faster_rcnn_r50_caffe_fpn_mstrain_3x_coco_20210526_095054-1f77628b.pth)**
# CASCADE-RCNN: **(https://download.openmmlab.com/mmdetection/v2.0/cascade_rcnn/cascade_rcnn_r101_fpn_1x_coco/cascade_rcnn_r101_fpn_1x_coco_20200317-0b6a2fbf.pth)**
# RETINA-NET: **(https://download.openmmlab.com/mmdetection/v2.0/retinanet/retinanet_r101_fpn_1x_coco/retinanet_r101_fpn_1x_coco_20200130-7a93545f.pth)**

If you want to access the adjusted weights directly you can find them in the below Drive Link under checkpoint folder: **(https://drive.google.com/drive/folders/1OsyRb97yPafym4_hgx7iAa-sXTRS8Ygf?usp=sharing)**


License

This project is licensed under the MIT License. See the LICENSE file for more information.

