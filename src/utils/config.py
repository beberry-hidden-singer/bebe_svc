# Copyright (c) 2023 Amphion.
# Copyright (c) 2024 karljeon44.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
import logging
import os

import json5

logger = logging.getLogger(__name__)


def override_config(base_config, new_config):
  """Update new configurations in the original dict with the new dict

  Args:
      base_config (dict): original dict to be overridden
      new_config (dict): dict with new configurations

  Returns:
      dict: updated configuration dict
  """
  for k, v in new_config.items():
    if type(v) == dict:
      if k not in base_config.keys():
        base_config[k] = {}
      base_config[k] = override_config(base_config[k], v)
    else:
      base_config[k] = v
  return base_config


def get_lowercase_keys_config(cfg):
  """Change all keys in cfg to lower case

  Args:
      cfg (dict): dictionary that stores configurations

  Returns:
      dict: dictionary that stores configurations
  """
  updated_cfg = dict()
  for k, v in cfg.items():
    if type(v) == dict:
      v = get_lowercase_keys_config(v)
    updated_cfg[k.lower()] = v
  return updated_cfg

def _load_config(config_fn, lowercase=False):
  """Load configurations into a dictionary

  Args:
      config_fn (str): path to configuration file
      lowercase (bool, optional): whether changing keys to lower case. Defaults to False.

  Returns:
      dict: dictionary that stores configurations
  """
  with open(config_fn, "r") as f:
    data = f.read()
  config_ = json5.loads(data)
  if "base_config" in config_:
    # load configurations from new path
    # p_config_path = os.path.join(os.getenv("WORK_DIR"), config_["base_config"])
    p_config_path = config_["base_config"]
    p_config_ = _load_config(p_config_path)
    config_ = override_config(p_config_, config_)
  if lowercase:
    # change keys in config_ to lower case
    config_ = get_lowercase_keys_config(config_)
  return config_


def load_config(config_fn, lowercase=False):
  """Load configurations into a dictionary

  Args:
      config_fn (str): path to configuration file
      lowercase (bool, optional): _description_. Defaults to False.

  Returns:
      JsonHParams: an object that stores configurations
  """
  config_ = _load_config(config_fn, lowercase=lowercase)
  # create an JsonHParams object with configuration dict
  cfg = JsonHParams(**config_)
  return cfg


def save_config(save_path, cfg):
  """Save configurations into a json file

  Args:
      save_path (str): path to save configurations
      cfg (dict): dictionary that stores configurations
  """
  with open(save_path, "w") as f:
    json5.dump(
      cfg, f, ensure_ascii=False, indent=4, quote_keys=True, sort_keys=True
    )

class JsonHParams:
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      if type(v) == dict:
        v = JsonHParams(**v)
      self[k] = v

  def keys(self):
    return self.__dict__.keys()

  def items(self):
    return self.__dict__.items()

  def values(self):
    return self.__dict__.values()

  def __len__(self):
    return len(self.__dict__)

  def __getitem__(self, key):
    return getattr(self, key)

  def __setitem__(self, key, value):
    return setattr(self, key, value)

  def __contains__(self, key):
    return key in self.__dict__

  def __repr__(self):
    return self.__dict__.__repr__()
