/*
 * Copyright (c) 2019 JD Williams
 *
 * This file is part of Firefly, a Python SOA framework built by JD Williams. Firefly is free software; you can
 * redistribute it and/or modify it under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 3 of the License, or (at your option) any later version.
 *
 * Firefly is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
 * implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
 * Public License for more details. You should have received a copy of the GNU Lesser General Public
 * License along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * You should have received a copy of the GNU General Public License along with Firefly. If not, see
 * <http://www.gnu.org/licenses/>.
 */

import m from "mithril";
import state from "./state";
import {bus, startWorker} from "firefly-framework";

startWorker();

function wait(el, cond) {
    console.log(cond);
    let waiting = !cond;
    if (typeof cond === 'function') {
        waiting = !cond();
    }
    return waiting ?
        m('div', el) :
        el;
}

function MyComp() {
    return {
        view() {
            return [
                m('h1', 'IAM Context'),
                m(
                    'button',
                    { onclick: () => bus.invoke('iam.CreateUser', {given_name: 'Doofus'}) },
                    'Click Me'
                ),
                wait(m('ul', state.users().map(u => m('li', u.sub))), state.isNotLoading('users')),
            ];
        }
    };
}

m.mount(document.body, {
    view: () => m(MyComp())
});