_base_ = [
'../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=8,
)

model = dict(
    # type='FasterRCNN',
    backbone=dict(
        # type='ResNet',
        # depth=50,
        # num_stages=4,
        # out_indices=(0, 1, 2, 3),
        # frozen_stages=1,
        # norm_cfg=dict(type='BN', requires_grad=True),
        # norm_eval=True,
        # style='pytorch',
        with_cp=True,
        frozen_stages=0,
        # dcn=dict( 
        #     #在最后三个block加入可变形卷积 
        #     type='DCNv2',
        #     # type='DCN_AS',
        #     # radius=3,
        #     # type='DCN_AS_DFDC',
        #     # type='DFDC_Conv2D',
        #     # type='ODFDC_Conv2D',
        #     deformable_groups=1, fallback_on_stride=False),
        # stage_with_dcn=(False, True, True, True),
    ),
    # neck=dict(
    #     type='FaPNOri',
    #     deform_groups=8,
    #     use_adaptive_sampling=False,
    #     radius=3,
    # )
)