_base_ = './deeplabv3_r50-d8_4xb4-160k_ade20k-512x512.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
#_base_ = './deeplabv3_r50-d8_512x512_160k_ade20k.py'
#model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
