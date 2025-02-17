# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from .res_company import L10N_BG_INTRASTAT


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_bg_odoo_compatible = fields.Boolean(related="company_id.l10n_bg_odoo_compatible")
    l10n_bg_intra_stat_incomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_incomes")
    l10n_bg_intra_stat_outcomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_outcomes")
    l10n_bg_intra_stat_type = fields.Selection(L10N_BG_INTRASTAT, string="Leval of registration")
