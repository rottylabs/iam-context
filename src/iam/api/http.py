import firefly as ff

import iam.domain as domain


@ff.http(cors=True)
class HttpApi:

    @ff.crud.http(domain.User)
    def user_crud(self):
        pass
