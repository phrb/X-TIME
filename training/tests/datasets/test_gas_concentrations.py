###
# Copyright (2023) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###

import pytest

from xtime.datasets import DatasetSplit, DatasetTestCase
from xtime.datasets._gas_concentrations import GasConcentrationsBuilder
from xtime.ml import TaskType

pytestmark = pytest.mark.datasets


class TestGasConcentrations(DatasetTestCase):
    _PARAMS = {
        "splits": [DatasetSplit.TRAIN, DatasetSplit.TEST, DatasetSplit.VALID],
        "task": TaskType.MULTI_CLASS_CLASSIFICATION,
        "num_features": 129,
        "num_classes": 6,
    }

    NAME = "gas_concentrations"
    CLASS = GasConcentrationsBuilder
    DATASETS = [DatasetTestCase.standard("default", _PARAMS), DatasetTestCase.standard("numerical", _PARAMS)]

    def test_all(self) -> None:
        self._test_datasets()