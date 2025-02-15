{
    "name": "Bulgarian Accounting Reports",
    "version": "17.0.1.0.0",
    "category": "Accounting/Localizations/Reporting",
    "summary": "Reporting for Bulgarian Localization",
    "license": "AGPL-3",
    "website": "https://github.com/rosenvladimirov/l10n-bulgaria-ee",
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
    ],
    "auto_install": [
        "l10n_bg",
    ],
    "installable": True,
}
