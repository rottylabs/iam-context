from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import firefly as ff
from .iaaa_event import IaaaEvent


@dataclass
class UserRegistered(IaaaEvent):
    user: Dict = ff.dict_()
