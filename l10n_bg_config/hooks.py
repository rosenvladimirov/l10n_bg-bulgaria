#  Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo.tools.translate import load_language

_logger = logging.getLogger(__name__)


def pre_init_hook(env):
    modules = env["ir.module.module"].search([("state", "=", "installed")])
    for lang in ["base.lang_bg", "base.lang_en"]:
        res_id = env.ref(lang, raise_if_not_found=False)
        language = env["res.lang"].search(
            [("id", "=", res_id.id), ("active", "=", False)]
        )
        if language:
            load_language(env.cr, language.code)
            modules._update_translations(language.code)
