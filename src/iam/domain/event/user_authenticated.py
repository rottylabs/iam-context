from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import firefly as ff
from .iaaa_event import IaaaEvent


@dataclass
class UserAuthenticated(IaaaEvent):
    user_id: str = ff.required()
