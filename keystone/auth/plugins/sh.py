from keystone import auth
from keystone.common import wsgi
from keystone import exception
from keystone.openstack.common import log
from keystone.openstack.common import timeutils
from keystone.token import provider


LOG = log.getLogger(__name__)


class SH(auth.AuthMethodHandler):

    method = 'sh'

    def __init__(self):
        self.provider = provider.Manager()

    def authenticate(self, context, auth_payload, user_context):
        for k, v in auth_payload.iteritems():
            if k in ('expires_at',):
                user_context[k] = v
            else:
                user_context['extras'][k] = v
