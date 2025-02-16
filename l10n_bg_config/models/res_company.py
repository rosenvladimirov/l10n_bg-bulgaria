#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, Command
from odoo.tools import sql


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_bg_uic_type = fields.Selection(
        related='partner_id.l10n_bg_uic_type',
    )
    l10n_bg_uic = fields.Char(
        related="partner_id.l10n_bg_uic"
    )
    l10n_bg_represent_contact_id = fields.Many2one(
        "res.partner",
        string="TAX Report creator",
        compute="_compute_l10n_bg_represent_contact_id",
        inverse="_inverse_l10n_bg_represent_contact_id",
        store=True,
    )
    l10n_bg_departament_code = fields.Integer("Departament code")

    def _compute_l10n_bg_represent_contact_id(self):
        for record in self:
            represent_contact_id = record.partner_id.child_ids.filtered(lambda r: r.type == "represent")
            if len(represent_contact_id) > 1:
                represent_contact_id = represent_contact_id[1]
            record.l10n_bg_represent_contact_id = represent_contact_id

    def _inverse_l10n_bg_represent_contact_id(self):
        for record in self:
            if record.l10n_bg_represent_contact_id:
                record.l10n_bg_represent_contact_id.type = "represent"
                record.partner_id.child_ids = [Command.link(record.l10n_bg_represent_contact_id.id)]
