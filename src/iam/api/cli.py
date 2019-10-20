from __future__ import annotations

import firefly as ff
import iam.domain as domain


@ff.cli(device_id='firefly')
class FireflyCli:

    @ff.cli(description='Identification, Authentication, Authorization and Accounting')
    class Iaaa:

        @ff.crud.cli(target=domain.User)
        def user_crud(self):
            pass

        @ff.crud.cli(target=domain.Group)
        def group_crud(self):
            pass

        @ff.crud.cli(target=domain.Role)
        def role_crud(self):
            pass
