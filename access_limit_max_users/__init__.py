from . import models
from flectra.api import Environment, SUPERUSER_ID
from flectra.tools.safe_eval import safe_eval


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    ref_record = env.ref("access_limit_max_users.max_users_limit")
    ref_record.max_records = env["res.users"].search_count(
        safe_eval(ref_record.domain))
