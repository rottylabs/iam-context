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

import firefly as ff
import inflection

from iam import User, Role, Group


@ff.on(['iam.RoleDeleted', 'iam.GroupDeleted'])
class RemoveDeletedRoleGroupFromUsers(ff.ApplicationService):
    _message_factory: ff.MessageFactory = None
    _registry: ff.Registry = None

    def __call__(self, name: str, **kwargs):
        type_ = Group if kwargs['_message'].__class__.__name__ == 'GroupDeleted' else Role
        if type_ == Group:
            search_criteria = User.c.groups.contains(name)
        else:
            search_criteria = User.c.roles.contains(name)

        entity = self._registry(type_).find(name)
        for user in self.query(self._message_factory.query('iam.Users', search_criteria)):
            getattr(user, f'remove_{inflection.underscore(type_.__name__)}')(entity)
            self.invoke(self._message_factory.command('iam.UpdateUser', user.to_dict()))
        self.dispatch(f'iam.{type_.__name__}RemovedFromUsers', {name: name})
