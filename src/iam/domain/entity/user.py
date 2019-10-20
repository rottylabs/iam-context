#  Copyright (c) 2019 JD Williams
#
#  This file is part of Firefly, a Python SOA framework built by JD Williams. Firefly is free software; you can
#  redistribute it and/or modify it under the terms of the GNU General Public License as published by the
#  Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#
#  Firefly is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
#  implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
#  Public License for more details. You should have received a copy of the GNU Lesser General Public
#  License along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  You should have received a copy of the GNU General Public License along with Firefly. If not, see
#  <http://www.gnu.org/licenses/>.

from __future__ import annotations

from datetime import datetime
from typing import List

import firefly as ff

import iam.domain as domain


class User(ff.Entity):
    # OpenID standard fields
    sub: str = ff.id_()
    name: str = ff.optional()
    given_name: str = ff.optional()
    family_name: str = ff.optional()
    middle_name: str = ff.optional()
    nickname: str = ff.optional()
    preferred_username: str = ff.optional()
    profile: str = ff.optional()
    picture: str = ff.optional()
    website: str = ff.optional()
    email: str = ff.optional()
    email_verified: bool = False
    gender: str = ff.optional()
    birthdate: datetime = ff.optional()
    zoneinfo: str = ff.optional()
    locale: str = ff.optional()
    phone_number: str = ff.optional()
    phone_number_verified: bool = False
    address: domain.Address = ff.optional()
    updated_at: datetime = ff.now()

    # Custom fields
    created_at: datetime = ff.now()
    deleted_at: datetime = None
    password_hash: str = ff.optional(length=32)

    groups: List[domain.Group] = ff.list_()
    roles: List[domain.Role] = ff.list_()
