#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import Command, api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    is_l10n_bg_record = fields.Boolean(
        string="Bulgaria - Use Bulgaria Accounting",
        compute="_check_is_l10n_bg_record",
        inverse="_inverse_is_l10n_bg_record",
        default=True,
        store=True,
    )
    l10n_bg_uic_type = fields.Selection(
        related="partner_id.l10n_bg_uic_type",
        readonly=True,
    )
    l10n_bg_uic = fields.Char(
        related="partner_id.l10n_bg_uic",
        readonly=True,
    )
    l10n_bg_represent_contact_id = fields.Many2one(
        "res.partner",
        string="Representative",
        compute="_compute_l10n_bg_represent_contact_id",
        inverse="_inverse_l10n_bg_represent_contact_id",
        store=True,
    )
    l10n_bg_departament_code = fields.Integer("Departament code")

    def _compute_l10n_bg_represent_contact_id(self):
        for record in self:
            represent_contact_id = record.partner_id.child_ids.filtered(
                lambda r: r.type == "represent"
            )
            if len(represent_contact_id) > 1:
                represent_contact_id = represent_contact_id[1]
            record.l10n_bg_represent_contact_id = represent_contact_id

    def _inverse_l10n_bg_represent_contact_id(self):
        for record in self:
            if record.l10n_bg_represent_contact_id:
                record.l10n_bg_represent_contact_id.type = "represent"
                record.partner_id.child_ids = [
                    Command.link(record.l10n_bg_represent_contact_id.id)
                ]

    @api.depends("chart_template")
    def _check_is_l10n_bg_record(self):
        for company in self:
            company.is_l10n_bg_record = company.chart_template == "bg"

    def _inverse_is_l10n_bg_record(self):
        for company in self:
            if company.is_l10n_bg_record and company.chart_template == "bg":
                company.is_l10n_bg_record = True
            elif company.chart_template != "bg":
                l10n_bg = self.env["ir.module.module"].search(
                    [("name", "=", "l10n_bg"), ("state", "!=", "installed")]
                )
                if l10n_bg:
                    l10n_bg.button_immediate_install()
            else:
                company.is_l10n_bg_record = False

    def check_is_l10n_bg_record(self, company=False):
        if not company:
            company = self
        else:
            company = self.browse(company)
        return company.is_l10n_bg_record
