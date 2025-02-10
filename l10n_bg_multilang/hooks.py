#  Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.api import SUPERUSER_ID, Environment


def pre_init_hook(cr):
    env = Environment(cr, SUPERUSER_ID, {})
    if not env["res.lang"].search([("code", "=", "bg_BG")]):
        env["res.lang"].action_activate_langs()


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    for partner_id in env["res.partner"].search([]):
        partner_id.with_context(lang="bg_BG").write(
            {
                "name": partner_id.name,
                "city": partner_id.city,
                "street": partner_id.street,
            }
        )

    for partnr_id in env["res.partner"].search([]):
        partnr_id.with_context(lang="bg_BG").write(
            {
                "city": partnr_id.city,
                "street": partnr_id.street,
            }
        )
