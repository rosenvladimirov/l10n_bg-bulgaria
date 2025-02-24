# -*- coding: utf-8 -*-

from odoo import Command, _, models, api
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    # --------------------------------------------------------------------------------
    # Root template functions
    # --------------------------------------------------------------------------------

    @template(model='account.account.tag')
    def _get_account_account_tag(self, template_code):
        return self._parse_csv(template_code, 'account.account.tag')
