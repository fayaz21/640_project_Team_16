_base_ = './retinanet_r101_fpn_1x_coco.py'
data_root = 'data/'

data = dict(
    test=dict(
        samples_per_gpu=4,
        ann_file=data_root + 'project_train/annotations/split_train_coco.json',
        img_prefix=data_root + 'project_train/images/',
    ) 
)

