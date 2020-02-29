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
from firefly.ui.web.components.form import Form
from firefly.ui.web.components.layouts.default import MenuItem, AppContainer, Crud
from firefly.ui.web.js_libs.mithril import m
from firefly.ui.web.plugins import add_menu_item, add_route
from firefly.ui.web.polyfills import *  # __:skip

from iam.domain.entity.user import User
from iam.domain.entity.client import Client

add_menu_item(m('div.ff-title', 'IAM'))
add_menu_item(m(MenuItem('Users', icon='solid/users', route='/iam/users')))
add_menu_item(m(MenuItem('Clients', icon='solid/mobile-alt', route='/iam/clients')))

add_route('/iam/users', Crud('iam.User', User, '/iam/users'))
add_route('/iam/clients', Crud('iam.Client', Client, '/iam/clients'))
