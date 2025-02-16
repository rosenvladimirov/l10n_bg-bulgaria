# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_bg_odoo_compatible = fields.Boolean(related="company_id.l10n_bg_odoo_compatible")
    l10n_bg_intra_stat_incomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_incomes")
    l10n_bg_intra_stat_outcomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_outcomes")
