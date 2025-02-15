#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = ["res.company", "l10n_bg.audit.mixin"]
    _name = "res.company"

    l10n_bg_tax_contact_id = fields.Many2one(
        "res.partner",
        string="TAX Report creator",
        compute="_compute_l10n_bg_tax_contact_id",
    )

    def _compute_l10n_bg_tax_contact_id(self):
        for record in self:
            tax_contact_id = record.partner_id.child_ids.filtered(lambda r: r.type == "tax")
            if len(tax_contact_id) > 1:
                tax_contact_id = tax_contact_id[1]
            record.l10n_bg_tax_contact_id = tax_contact_id
