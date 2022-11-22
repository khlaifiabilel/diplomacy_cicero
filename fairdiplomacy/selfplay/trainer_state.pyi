#
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
import argparse
import pathlib
import torch.optim
import torch.nn
from typing import Any, Dict, Optional

TRAINER_STATE_VERSION: int

class NetTrainingState:
    model: torch.nn.Module
    optimizer: torch.optim.Optimizer
    scheduler: Optional[torch.optim.lr_scheduler._LRScheduler]
    args: argparse.Namespace
    epoch_id: int = ...
    global_step: int = ...
    def state_dict(self) -> Dict: ...
    @classmethod
    def from_dict(
        cls: Any, state_dict: Dict, default: NetTrainingState, device: str = ...
    ) -> NetTrainingState: ...
    def save(self, filename: pathlib.Path) -> None: ...
    def __init__(
        self,
        model: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        scheduler: Optional[torch.optim.lr_scheduler._LRScheduler],
        args: argparse.Namespace,
        epoch_id: int = ...,
        global_step: int = ...,
    ): ...

class TrainerState:
    net_state: NetTrainingState
    value_net_state: Optional[NetTrainingState]
    version: int = ...
    epoch_id: int = ...
    global_step: int = ...
    @property
    def model(self): ...
    @property
    def optimizer(self): ...
    @property
    def scheduler(self): ...
    @property
    def value_model(self): ...
    def state_dict(self) -> Dict: ...
    def save(self, filename: pathlib.Path) -> None: ...
    @classmethod
    def from_dict(
        cls: Any, state_dict: Dict, default: TrainerState, device: str = ...
    ) -> TrainerState: ...
    @classmethod
    def load(
        cls: Any, filename: pathlib.Path, default: TrainerState, device: str = ...
    ) -> TrainerState: ...
    def __init__(
        self,
        net_state: NetTrainingState,
        value_net_state: Optional[NetTrainingState],
        version: int = ...,
        epoch_id: int = ...,
        global_step: int = ...,
    ): ...