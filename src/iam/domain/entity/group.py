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

from typing import List

import firefly as ff


class Group(ff.AggregateRoot):
    id: str = ff.id_()
    name: str = ff.required()

    users: List[str] = ff.list_()

    def assign_user_to_group(self, user_id: str):
        if user_id not in self.users:
            self.users.append(user_id)
        return 'iam.GroupAssigned', {'user_id': user_id, 'group_id': self.id}

    def remove_user_from_group(self, user_id: str):
        if user_id in self.users:
            self.users.remove(user_id)
        return 'iam.GroupRemoved', {'user_id': user_id, 'group_id': self.id}
