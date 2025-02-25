{
    "name": "Bulgarian Accounting Reports",
    "version": "17.0.1.0.0",
    "category": "Accounting/Localizations/Reporting",
    "summary": "Reporting for Bulgarian Localization",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/l10n-bulgaria",
    "depends": [
        "base",
        "sale",
        "account",
        "l10n_bg",
        "l10n_bg_config",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_bg_vat_line_sale_reports.xml",
        "views/account_bg_vat_line_purchase_reports.xml",
        "views/account_bg_vat_line_vies_reports.xml",
        "views/account_account_tag_views.xml",
        "views/res_config_view.xml",
        "views/account_menuitem.xml",
    ],
    "installable": True,
}
