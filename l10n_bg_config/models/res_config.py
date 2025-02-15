# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    is_l10n_bg_record = fields.Boolean(compute="_check_is_l10n_bg_record", store=True)

    module_currency_rate_update_bg_bnb = fields.Boolean(
        "Download currency rates from Bulgaria National Bank",
        help="Central currency rates downloaded from National Bank of Bulgaria",
    )
    module_l10n_bg_city = fields.Boolean(
        "Upload Bulgaria city",
        help="Upload cites, municipalities, states, villages and manastiries",
    )
    module_l10n_bg_address_extended = fields.Boolean(
        "Additional data in address", help="Additional data in address like "
    )
    module_l10n_bg_tax_offices = fields.Boolean(
        "NRA Bulgaria, tax offices and departments",
        help="Address and department of NRA Bulgaria added like partners"
        " to use when make a payment ot taxes.",
    )
    # module_l10n_bg_account_financial_report = fields.Boolean(
    #     'Bulgaria - Account Financial Reports',
    #     help='Provide all reports for Bulgarian accounting.'
    # )
    module_l10n_bg_intrastat_product = fields.Boolean(
        "Bulgaria - Intrastat Product Declaration",
        help="Provide Intrastat Product Declaration.",
    )
    module_partner_multilang = fields.Boolean(
        "Partner transliterate names",
        help="Transliterate partner, city, street names ISO9 and other",
    )
    module_l10n_bg_multilang = fields.Boolean(
        "Switch on multilanguage support",
        help="Change to multilingual support for fields without native configurations",
    )
    module_account_financial_forms = fields.Boolean(
        "TAX Audit forms",
        help="Account financial report base on tax administration forms for audit",
    )
    module_l10n_bg_uic_id_number = fields.Boolean(
        "Bulgarian multi register codes",
        help="Bulgarian registration codes base on OCA module partner_identification",
    )
    module_l10n_bg_coa_reports = fields.Boolean(
        "Bulgaria - Accounting tax reports",
        help="Provide all COA reports for Bulgarian.",
    )
    module_l10n_bg_reports_audit = fields.Boolean(
        "Bulgaria - Accounting TAX Audit reports",
        help="Provide all Accounting TAX Audit reports for Bulgarian - NRA.",
    )
    module_l10n_bg_intrastat = fields.Boolean(
        "Bulgaria - Intrastat",
        help="Generate XML files for Bulgaria intrastat",
    )
    module_l10n_bg_assets = fields.Boolean(
        "Bulgaria - Assets",
        help="Add rules for tax desperation base Bulgarian law",
    )

    def _check_is_l10n_bg_record(self):
        return True
