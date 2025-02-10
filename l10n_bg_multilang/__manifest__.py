# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Multi Language Partner, Company, Employee",
    "version": "17.0.0.1.0",
    "author": "Rosen Vladimirov",
    "category": "Localization",
    "license": "AGPL-3",
    "description": """
    Multi language support for Partner, Company, Employee.
    """,
    "depends": [
        "base",
        "hr",
        "stock",
        "partner_multilang",
    ],
    "data": [],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
