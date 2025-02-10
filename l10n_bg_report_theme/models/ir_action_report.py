# Copyright 2023 Rosen Vladimirov
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import models, tools, _
from odoo.tools.misc import format_date, format_time, format_datetime

_logger = logging.getLogger(__name__)


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _get_rendering_context(self, report, docids, data):
        values = super()._get_rendering_context(report, docids, data)
        values.update({
            'format_date': lambda date, date_format=False, lang_code=False: format_date(self.env, date, date_format,
                                                                                        lang_code),
            'format_datetime': lambda dt, tz=False, dt_format=False, lang_code=False: format_datetime(self.env, dt, tz,
                                                                                                      dt_format,
                                                                                                      lang_code),
            'format_time': lambda time, tz=False, time_format=False, lang_code=False: format_time(self.env, time, tz,
                                                                                                  time_format,
                                                                                                  lang_code),
            'format_amount': lambda amount, currency, lang_code=False: tools.format_amount(self.env, amount, currency,
                                                                                           lang_code),
            'format_duration': lambda value: tools.format_duration(value),
        })
        # _logger.info(f"REPORT {values}")
        return values
