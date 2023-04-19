_base_ = './retinanet_r50_caffe_fpn_1x_coco.py'

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://detectron2/resnet101_caffe'
        )
    ),
    bbox_head=dict(
        num_classes=1,  # Only one class (bird)
    )
)
