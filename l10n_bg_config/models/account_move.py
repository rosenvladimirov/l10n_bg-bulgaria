#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models
from odoo.addons.l10n_bg_reports_audit.models.l10n_bg_file_helper import get_type_vat, get_doc_type, get_delivery_type


class AccountMove(models.Model):
    _inherit = ["account.move", "l10n.bg.config.mixin"]
    _name = "account.move"

    l10n_bg_name = fields.Char(
        "Number of locale document", index="trigram", tracking=True, copy=False
    )
    l10n_bg_date = fields.Date(
        "Date of locale document", tracking=True, copy=False
    )
