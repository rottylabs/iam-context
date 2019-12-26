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

from firefly.ui.web.polyfills import *  # __:skip

from typing import Any, Callable

from firefly import Query, MessageFactory
from firefly.ui.web import bus

# __pragma__('opov')
# __pragma__('kwargs')

import iam

mf = MessageFactory()


class FireflyStream:
    _bus = bus

    def __init__(self, query: Query = None, default: Any = None, fetch: str = 'lazy'):
        self._initialized = False
        self._query = query
        self._stream = m.stream(default or [])
        self._stream.map(lambda: m.redraw())
        self._aggregate = inflection.singularize(query.__class__.__name__)

        if fetch == 'eager':
            self._execute_query()

    def __call__(self, value: Callable = None):
        if value is None:
            return self._stream()
        return self._stream(value)

    def __getattr__(self, item):
        console.log(item)
        return getattr(self._stream, item)

    def matches_aggregate(self, aggregate: str):
        return self._aggregate == aggregate

    def _execute_query(self):
        self._bus.request(self._query).then(lambda result: self._stream(lambda: result))
        self._initialized = True


class State:
    def __init__(self):
        self.users = FireflyStream(
            query=mf.query('Users'),
            default=[
                iam.User(given_name='Doofus'),
                iam.User(given_name='Dumbass')
            ]
        )

        self.foo = self.users.map(lambda us: filter(lambda u: u.given_name != 'Doofus', us))


state = State()
