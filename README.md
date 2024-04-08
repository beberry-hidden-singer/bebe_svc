# bebe-svc
based on [TransformerSVC](https://github.com/open-mmlab/Amphion/tree/main/egs/svc/TransformerSVC) from Amphion

## Setup
* Python 3.10
* CUDA 12.1
  * NOTE: Amphion requires CUDA 11.8

### [SVC Corpora]((https://github.com/open-mmlab/Amphion/blob/main/egs/datasets/README.md))
1. [VCTK](https://github.com/open-mmlab/Amphion/blob/main/egs/datasets/README.md#vctk)

### [Pretrained Checkpoints](https://github.com/open-mmlab/Amphion/blob/main/pretrained/README.md)
1. [ContentVec](https://github.com/open-mmlab/Amphion/blob/main/pretrained/README.md#contentvec)
2. [WeNet](https://github.com/open-mmlab/Amphion/blob/main/pretrained/README.md#wenet)
3. [Whisper](https://github.com/open-mmlab/Amphion/blob/main/pretrained/README.md#whisper)

## Preprocessing
* see TODOs in [config](config/vanilla_svc.json) of choice
```shell
$ PYTHONPATH=src python scripts/preprocess.py \
  --config ./config/vanilla_svc.json \
  --num_workers 4
```
