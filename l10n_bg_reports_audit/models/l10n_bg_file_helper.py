#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _


def l10n_bg_lang(env, lang_modules='partner'):
    if lang_modules == 'partner':
        return """#>>'{bg_BG}'""" if env['ir.module.module'].search([
            ('name', '=', 'partner_multilang'),
            ('state', '=', 'installed')
        ]) else """"""
    else:
        return """#>>'{bg_BG}'""" if env['ir.module.module'].search([
            ('name', 'in', ('l10n_bg_multilang', 'partner_multilang')),
            ('state', '=', 'installed')
        ]) else """"""


def l10n_bg_odoo_compatible(env, mode):
    l10n_bg_odoo_compatible = env.user.company_id.l10n_bg_odoo_compatible
    if l10n_bg_odoo_compatible and mode == 'tag_20':
        return """(
                CASE
                    WHEN (
                            SUM(accs.account_tag_22)
                        ) <= 0 THEN
                            ABS(SUM(accs.account_tag_22)) + SUM(accs.account_tag_23 + accs.account_tag_24 + accs.account_tag_21)
                    ELSE
                        SUM(-accs.account_tag_22) + SUM(accs.account_tag_23 + accs.account_tag_24 + accs.account_tag_21)
                END
            ) AS account_tag_20"""
    elif not l10n_bg_odoo_compatible and mode == 'tag_20':
        return """SUM(accs.account_tag_21 + accs.account_tag_22 + accs.account_tag_23 + accs.account_tag_24) AS account_tag_20"""
    elif l10n_bg_odoo_compatible and mode == 'tag_22':
        return """(
            CASE
                WHEN (
                        SUM(accs.account_tag_22)
                    ) < 0 THEN
                        ABS(SUM(accs.account_tag_22))
                ELSE
                    SUM(-accs.account_tag_22)
            END
        ) AS account_tag_22"""
    elif not l10n_bg_odoo_compatible and mode == 'tag_22':
        return """SUM(accs.account_tag_22) AS account_tag_22"""
    elif l10n_bg_odoo_compatible and mode == 'tag_50':
        return """(
            (CASE
                WHEN (
                    SUM(accs.account_tag_22)
                ) >= 0 THEN
                    CASE
                        WHEN (
                            SUM(accs.account_tag_21 + accs.account_tag_22 + accs.account_tag_23 + accs.account_tag_24)
                                - SUM(accp.account_tag_41 + accp.account_tag_42 + accp.account_tag_43)
                        ) >= 0 THEN
                            ABS(SUM(accs.account_tag_21 + accs.account_tag_22 + accs.account_tag_23 + accs.account_tag_24)
                                - SUM(accp.account_tag_41 + accp.account_tag_42 + accp.account_tag_43))
                        ELSE 0.00
                    END
                ELSE
                    CASE
                        WHEN (
                            SUM(accs.account_tag_22)
                        ) < 0 THEN
                            ABS(SUM(accs.account_tag_22)) + SUM(accs.account_tag_23 + accs.account_tag_24 + accs.account_tag_21)
                                - SUM(accp.account_tag_41 + accp.account_tag_42 + accp.account_tag_43)
                        ELSE 0.00
                END
            END)
        ) AS account_tag_50"""
    elif not l10n_bg_odoo_compatible and mode == 'tag_50':
        return """SUM(accr.account_tag_50) AS account_tag_50"""
    elif l10n_bg_odoo_compatible and mode == 'tag_60':
        return """(
            CASE
                WHEN (
                    SUM(accs.account_tag_21 + accs.account_tag_22 + accs.account_tag_23 + accs.account_tag_24) -
                        SUM(accp.account_tag_41 + accp.account_tag_42 + accp.account_tag_43)
                ) > 0 THEN
                    0.00
                ELSE
                    ABS(
                        SUM(accs.account_tag_21 + accs.account_tag_22 + accs.account_tag_23 + accs.account_tag_24) -
                            SUM(accp.account_tag_41 + accp.account_tag_42 + accp.account_tag_43)
                    )
            END
        ) AS account_tag_60"""
    elif not l10n_bg_odoo_compatible and mode == 'tag_60':
        return """SUM(accr.account_tag_60) AS account_tag_60"""


def l10n_bg_where(env, report_options):
    date_from = report_options['date']['date_from']
    date_to = report_options['date']['date_to']
    date_from_date = fields.Date.from_string(date_from)
    tax_period = date_from_date.strftime('%Y%m')
    company_id = env.company.id
    unposted_in_period = report_options['unposted_in_period']
    all_entries = report_options['all_entries']
    state = ['posted', 'cancel']

    if unposted_in_period or all_entries:
        state.append('draft')
    return date_from, date_to, tax_period, company_id, state


def parce_str_2(value):
    value = value or ""
    return f'{value.ljust(2, " ")}'[:2]


def parce_str_5(value):
    value = value or ""
    return f'{value.ljust(5, " ")}'[:5]


def parce_str_5_vies(value):
    value = value or ""
    return f'{value.rjust(5, " ").rjust(5)}'[:5]


def parce_str_6(value):
    value = value or ""
    return f'{value.ljust(6, " ")}'[:6]


def parce_str_15(value):
    value = value or ""
    return f'{value.ljust(15, " ")}'[:15]


def parce_str_20(value):
    value = value or ""
    return f'{value.ljust(20, " ")}'[:20]


def parce_str_30(value):
    value = value or ""
    return f'{value.ljust(30, " ")}'[:30]


def parce_str_50(value):
    value = value or ""
    return f'{value.ljust(50, " ")}'[:50]


def parce_str_150(value):
    value = value or ""
    return f'{value.ljust(150, " ")}'[:150]


def parce_str_200(value):
    value = value or ""
    return f'{value.ljust(200, " ")}'[:200]


def parce_date_6(value):
    if value is None or value == '':
        return "".ljust(6, " ")
    value = fields.Date.from_string(value)
    return f"{value.strftime('%Y%m')}"[:6]


def parce_date_10(value):
    if value is None or value == '':
        return "".ljust(10, " ")
    value = fields.Date.from_string(value)
    return f"{value.strftime('%d/%m/%Y')}"[:10]


def convert_date_vies(value):
    # Extract year and month
    year = value[:4]
    month = value[4:]
    return f"{month}/{year}"[:7]


def parce_fload_4(value):
    value = value or 0.00
    return "{:.2f}".format(value).rjust(4)[:4]


def parce_fload_15_2(value):
    value = value or 0.00
    return f"{value:.2f}".ljust(15, " ")[:15]


def parce_integer_4(value):
    value = value or 0
    return f"{int(float(value))}".ljust(4, " ")[:4]


def parce_integer_15(value):
    value = value or 0
    return f"{int(float(value))}".ljust(15, " ")[:15]


L10N_BG_DECLARATION_FIELDS = {
    "info_tag_1": lambda value: parce_str_15(value),
    "info_tag_2": lambda value: parce_str_50(value),
    "info_tag_3": lambda value: parce_str_6(value),
    "info_tag_4": lambda value: parce_str_50(value),
    "info_tag_5": lambda value: parce_integer_15(value),
    "info_tag_6": lambda value: parce_integer_15(value),
    "account_tag_10": lambda value: parce_fload_15_2(value),
    "account_tag_20": lambda value: parce_fload_15_2(value),
    "account_tag_11": lambda value: parce_fload_15_2(value),
    "account_tag_21": lambda value: parce_fload_15_2(value),
    "account_tag_12": lambda value: parce_fload_15_2(value),
    "account_tag_22": lambda value: parce_fload_15_2(value),
    "account_tag_23": lambda value: parce_fload_15_2(value),
    "account_tag_13": lambda value: parce_fload_15_2(value),
    "account_tag_24": lambda value: parce_fload_15_2(value),
    "account_tag_14": lambda value: parce_fload_15_2(value),
    "account_tag_15": lambda value: parce_fload_15_2(value),
    "account_tag_16": lambda value: parce_fload_15_2(value),
    "account_tag_17": lambda value: parce_fload_15_2(value),
    "account_tag_18": lambda value: parce_fload_15_2(value),
    "account_tag_19": lambda value: parce_fload_15_2(value),
    "account_tag_30": lambda value: parce_fload_15_2(value),
    "account_tag_31": lambda value: parce_fload_15_2(value),
    "account_tag_41": lambda value: parce_fload_15_2(value),
    "account_tag_32": lambda value: parce_fload_15_2(value),
    "account_tag_42": lambda value: parce_fload_15_2(value),
    "account_tag_43": lambda value: parce_fload_15_2(value),
    "account_tag_33": lambda value: parce_fload_4(value),
    "account_tag_40": lambda value: parce_fload_15_2(value),
    "account_tag_50": lambda value: parce_fload_15_2(value),
    "account_tag_60": lambda value: parce_fload_15_2(value),
    "account_tag_70": lambda value: parce_fload_15_2(value),
    "account_tag_71": lambda value: parce_fload_15_2(value),
    "account_tag_80": lambda value: parce_fload_15_2(value),
    "account_tag_81": lambda value: parce_fload_15_2(value),
    "account_tag_82": lambda value: parce_fload_15_2(value),
}

L10N_BG_PURCHASES_FIELDS = {
    "info_tag_2": lambda value: parce_str_15(value),
    "info_tag_1": lambda value: parce_str_6(value),
    "info_tag_3": lambda value: parce_integer_4(value),
    "info_tag_4": lambda value: parce_integer_15(value),
    "info_tag_5": lambda value: parce_str_2(value),
    "info_tag_6": lambda value: parce_str_20(value),
    "info_tag_7": lambda value: parce_date_10(value),
    "info_tag_8": lambda value: parce_str_15(value),
    "info_tag_9": lambda value: parce_str_50(value),
    "info_tag_10": lambda value: parce_str_30(value),
    "account_tag_30": lambda value: parce_fload_15_2(value),
    "account_tag_31": lambda value: parce_fload_15_2(value),
    "account_tag_41": lambda value: parce_fload_15_2(value),
    "account_tag_32": lambda value: parce_fload_15_2(value),
    "account_tag_42": lambda value: parce_fload_15_2(value),
    "account_tag_43": lambda value: parce_fload_15_2(value),
    "account_tag_44": lambda value: parce_fload_15_2(value),
    "info_tag_45": lambda value: parce_str_2(value),
}

L10N_BG_SALES_FIELDS = {
    "info_tag_0": lambda value: parce_str_15(value),
    "info_tag_1": lambda value: parce_str_6(value),
    "info_tag_2": lambda value: parce_integer_4(value),
    "info_tag_3": lambda value: parce_integer_15(value),
    "info_tag_4": lambda value: parce_str_2(value),
    "info_tag_5": lambda value: parce_str_20(value),
    "info_tag_6": lambda value: parce_date_10(value),
    "info_tag_7": lambda value: parce_str_15(value),
    "info_tag_8": lambda value: parce_str_50(value),
    "info_tag_9": lambda value: parce_str_30(value),
    "account_tag_10": lambda value: parce_fload_15_2(value),
    "account_tag_20": lambda value: parce_fload_15_2(value),
    "account_tag_11": lambda value: parce_fload_15_2(value),
    "account_tag_21": lambda value: parce_fload_15_2(value),
    "account_tag_12": lambda value: parce_fload_15_2(value),
    "account_tag_26": lambda value: parce_fload_15_2(value),
    "account_tag_22": lambda value: parce_fload_15_2(value),
    "account_tag_23": lambda value: parce_fload_15_2(value),
    "account_tag_13": lambda value: parce_fload_15_2(value),
    "account_tag_24": lambda value: parce_fload_15_2(value),
    "account_tag_14": lambda value: parce_fload_15_2(value),
    "account_tag_15": lambda value: parce_fload_15_2(value),
    "account_tag_16": lambda value: parce_fload_15_2(value),
    "account_tag_17": lambda value: parce_fload_15_2(value),
    "account_tag_18": lambda value: parce_fload_15_2(value),
    "account_tag_19": lambda value: parce_fload_15_2(value),
    "account_tag_25": lambda value: parce_fload_15_2(value),
    "info_tag_27": lambda value: parce_str_2(value),
}

L10N_BG_VIES_FIELDS = {
    "info_tag_vhr_1": lambda value: value if value is not None else '',
    "info_tag_vhr_2": lambda value: convert_date_vies(value) if value is not None else '',
    "info_tag_vhr_3": lambda value: "{:d}".format(value).rjust(5) + "\r\n" if value is not None else '' + "\r\n",
    "info_tag_vdr_1": lambda value: value if value is not None else '',
    "info_tag_vdr_2": lambda value: parce_str_15(value) if value is not None else '',
    "info_tag_vdr_3": lambda value: parce_str_150(value) if value is not None else '',
    "info_tag_vdr_4": lambda value: parce_str_50(value) if value is not None else '',
    "info_tag_vdr_5": lambda value: value if value is not None else '',
    "info_tag_vdr_6": lambda value: parce_str_150(value) if value is not None else '',
    "info_tag_vdr_7": lambda value: parce_str_5_vies(value) + "\r\n" if value is not None else '' + "\r\n",
    "info_tag_vtr_1": lambda value: value if value is not None else '',
    "info_tag_vtr_2": lambda value: parce_str_15(value) if value is not None else '',
    "info_tag_vtr_3": lambda value: parce_str_150(value) if value is not None else '',
    "info_tag_vtr_4": lambda value: parce_str_200(value) + "\r\n" if value is not None else '' + "\r\n",
    "info_tag_ttr_1": lambda value: value,
    "account_tag_ttr_2": lambda value: "{:.2f}".format(value).rjust(12),
    "account_tag_ttr_3": lambda value: "{:.2f}".format(value).rjust(12),
}

L10N_BG_VIES_LINES_FIELDS = {
    "info_tag_vir_1": lambda value: value,
    "info_tag_vir_2": lambda value: "{:d}".format(value).rjust(5),
    "info_tag_vir_3": lambda value: parce_str_15(value),
    "account_tag_vir_4": lambda value: "{:.2f}".format(value).rjust(12),
    "account_tag_vir_5": lambda value: "{:.2f}".format(value).rjust(12),
    "account_tag_vir_6": lambda value: "{:.2f}".format(value).rjust(12) + "       "
}

def get_l10n_bg_applicability():
    return [
        ("declaration", _("Declaration")),
        ("purchase", _("Purchase report")),
        ("sale", _("Sale report")),
        ("vies", _("VIES Report")),
    ]
