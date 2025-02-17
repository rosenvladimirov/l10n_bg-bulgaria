# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from .res_company import L10N_BG_INTRASTAT


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_bg_odoo_compatible = fields.Boolean(related="company_id.l10n_bg_odoo_compatible")
    l10n_bg_intra_stat_incomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_incomes")
    l10n_bg_intra_stat_outcomes = fields.Boolean(related="company_id.l10n_bg_intra_stat_outcomes")
    l10n_bg_intra_stat_type = fields.Selection(L10N_BG_INTRASTAT, string="Leval of registration")

    module_account_usability = fields.Boolean(
        "Account - Missing Menus",
        help="Adds missing menu entries for Account module and adds the option to enable Saxon Accounting",
    )
    module_account_financial_report = fields.Boolean(
        "Account Financial Reports (OCA)",
        help="OCA Financial Reports",
    )
    module_account_reports = fields.Boolean(
        "Accounting Reports",
        help="View and create reports",
    )
