from __future__ import annotations

from dataclasses import dataclass
from typing import List

import firefly as ff

import iam.domain as domain


@dataclass
class Group(ff.Entity):
    id: str = ff.pk()
    name: str = ff.required()

    users: List[domain.User] = ff.list_()
    roles: List[domain.Role] = ff.list_()
