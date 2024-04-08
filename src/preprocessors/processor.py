# Copyright (c) 2023 Amphion.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import re
from preprocessors import custom, vctk


def preprocess_dataset(
        dataset, dataset_path, output_path, cfg, task_type, is_custom_dataset=False
):
  """Call specific function to handle specific dataset
  Args:
      dataset (str): name of a dataset, e.g. opencpop, m4singer
      dataset_path (str): path to dataset
      output_path (str): path to store preprocessing result files
  """
  if is_custom_dataset:
    if task_type == "svc":
      custom.main(output_path, dataset_path, dataset_name=dataset)
    else:
      raise NotImplementedError(
        "Custom dataset for {} task not implemented!".format(cfg.task_type)
      )

  if dataset == "vctk":
    vctk.main(output_path, dataset_path)
  else:
    raise NotImplementedError(f"dataset {dataset} not understood")


def prepare_align(dataset, dataset_path, cfg, output_path):
  """Call specific function to handle specific dataset

  Args:
      dataset (str): name of a dataset, e.g. ljspeech
      dataset_path (str): path to dataset
      output_path (str): path to store preprocessing result files
  """
  if dataset == "LJSpeech":
    ljspeech.prepare_align(dataset, dataset_path, cfg, output_path)
