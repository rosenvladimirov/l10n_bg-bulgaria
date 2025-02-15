#  Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models, Command

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = ["res.partner", "l10n_bg.registrations.mixin"]
    _name = "res.partner"

    l10n_bg_represent_contact_id = fields.Many2one(
        "res.partner",
        string="Representative",
        compute="_compute_l10n_bg_represent_contact_id",
        inverse="_inverse_l10n_bg_represent_contact_id",
        store=True,
    )
    # Technical field tor check is a company master
    is_company_master = fields.Boolean(compute='_compute_is_company_master')

    def _compute_l10n_bg_represent_contact_id(self):
        for record in self:
            record.l10n_bg_represent_contact_id = record.child_ids.filtered(lambda r: r.type == "represent")

    def _inverse_l10n_bg_represent_contact_id(self):
        for record in self:
            if record.l10n_bg_represent_contact_id:
                record.l10n_bg_represent_contact_id.type = "represent"
                record.child_ids = [Command.link(record.l10n_bg_represent_contact_id.id)]
            else:
                record.l10n_bg_represent_contact_id = False

    def _compute_is_company_master(self):
        for record in self:
            company_id = self.env['res.company'].search([('partner_id', '=', record.id)], limit=1)
            if company_id \
                and (company_id.l10n_bg_tax_contact_id.id == record.id or company_id.partner_id.id == record.id):
                record.is_company_master = True
            else:
                record.is_company_master = False

    @api.onchange("vies_valid")
    def _onchange_vies_valid(self):
        self._validate_l10n_bg_uic()

    @api.onchange("type")
    @api.depends("child_ids")
    def _onchange_type(self):
        if self.type == "represent":
            l10n_bg_represent_contact_id = self.child_ids.filtered(lambda r: r.type == "represent")
            if len(l10n_bg_represent_contact_id) > 1:
                l10n_bg_represent_contact_id = l10n_bg_represent_contact_id[1]
            company_id = self.env['res.company'].search([('partner_id', '=', self.id)], limit=1)
            if company_id:
                company_id.l10n_bg_represent_contact_id = self.id
            elif not company_id and l10n_bg_represent_contact_id:
                self.l10n_bg_represent_contact_id = l10n_bg_represent_contact_id
