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

from typing import Callable

from firefly.ui.web.polyfills import *  # __:skip
from firefly.ui.web.stubs import *  # __:skip
from firefly.ui.web.bus import bus

import firefly.domain as ffd

from datetime import datetime, date
from iam.domain.entity.user import User
from iam_web.state import state


def __pragma__(*args):
    pass

# __pragma__('kwargs')


class Form:
    def __init__(self, entity: ffd.Entity, config: dict = None):
        self._entity = entity
        self._config = {
            'placeholders': True,
            'labels': True,
            'id': 'form'
        }
        self._config.update(config or {})
        self._fields = {}

        for field_ in dir(self._entity):
            if field_.startswith('__'):
                continue
            config = {
                'required': False,
                'type': str
            }
            val = getattr(entity.__class__, field_)
            if callable(val):
                continue

            if isinstance(val, (datetime, date)):
                config['required'] = False
            elif isinstance(val, str) and val == 'missing':
                config['required'] = False
            elif isinstance(val, ffd.Empty):
                config['required'] = True

            self._fields[field_] = config

    @staticmethod
    def _wrap(component: str, vnode):
        return vnode

    def _form(self, config=None, children=None):
        return self._wrap(
            'form',
            m(
                'div.form-container.flex.flex-col.mx-5',
                m(
                    f'form#{self._config["id"]}',
                    config,
                    children
                )
            )
        )

    def _field_row(self, field_: str):
        children = []
        if self._config['labels']:
            children.append(self._label(field_))
        children.append(self._field(field_))

        return self._wrap('field_row', m('div.form-row.my-3', children))

    def _label(self, field_: str, config=None, children=None):
        return self._wrap(f'label', m(f'label[for="{field_}"].block', config, field_))

    def _field(self, field_: str, config=None, children=None):
        if self._config['placeholders']:
            config = config or {}
            config['placeholder'] = field_
        return self._wrap(
            'field',
            m(
                f'input[type="text"][id="{field_}"].form-text-input.border.border-gray-500.px-2.py-1.rounded-sm',
                config,
                children
            )
        )

    def _handle_submit(self, event):
        event.preventDefault()
        console.log(document.getElementById(self._config['id']))
        form_data = __new__(FormData(document.getElementById(self._config['id'])))
        data = {}

        def assign(v, k):
            data[k] = v
        form_data.forEach(assign)
        if 'onsubmit' in self._config:
            self._config['onsubmit'](data)

    def view(self):
        config = {'onsubmit': self._handle_submit}
        form_fields = list(map(self._field_row, self._fields.keys()))
        form_fields.append(m('input[type="submit"][value="Submit"]'))
        return self._form(config, form_fields)


# __pragma__('opov')
class MyComp:
    @staticmethod
    def view():
        new_user = User()

        return [
            m('button', {'onclick': lambda: bus.invoke('CreateUser', {'given_name': 'Meep'})}, 'Click Me'),
            m('h1', 'User Form'),
            m(Form(new_user, {'onsubmit': lambda data: bus.invoke('CreateUser', data)})),
            m('h1', 'Users'),
            m('ul', map(lambda u: m('li', u.given_name), state.users()))
        ]
# __pragma__('noopov')


m.mount(document.body, {
    'view': lambda: m(MyComp())
})

__pragma__('js', '{}', '''
if (module.hot) {
  module.hot.accept();
}
''')
