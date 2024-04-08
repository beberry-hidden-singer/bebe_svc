# Copyright (c) 2023 Amphion.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import numpy as np


def remove_outlier(values):
  values = np.array(values)
  p25 = np.percentile(values, 25)
  p75 = np.percentile(values, 75)
  lower = p25 - 1.5 * (p75 - p25)
  upper = p75 + 1.5 * (p75 - p25)
  normal_indices = np.logical_and(values > lower, values < upper)
  return values[normal_indices]
