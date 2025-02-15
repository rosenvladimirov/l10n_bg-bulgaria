#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _

L10N_BG_INTRASTAT = [
    ("standard", _("Standard base on levelling up")),
    ("statistical", _("Statistical base on levelling up")),
]


class BgAuditMixin(models.AbstractModel):
    _inherit = "l10n_bg.audit.mixin"

    l10n_bg_intra_stat_type = fields.Selection(L10N_BG_INTRASTAT, string="Leval of registration")
    l10n_bg_intra_stat_incomes = fields.Boolean("An obligation to submit intra-Community supplies")
    l10n_bg_intra_stat_outcomes = fields.Boolean("An obligation to submit intra-Community incomes")

    # def init(self):
    #     super().init()
    #     if not sql.column_exists(self.env.cr, self._table, "l10n_bg_intra_stat_incomes;"):
    #         self.env.cr.execute("ALTER TABLE res_users ADD COLUMN l10n_bg_intra_stat_incomes boolean")
    #     if not sql.column_exists(self.env.cr, self._table, "l10n_bg_intra_stat_outcomes;"):
    #         self.env.cr.execute("ALTER TABLE res_users ADD COLUMN l10n_bg_intra_stat_outcomes boolean")
    #     if not sql.column_exists(self.env.cr, self._table, "l10n_bg_departament_code;"):
    #         self.env.cr.execute("ALTER TABLE res_users ADD COLUMN l10n_bg_departament_code integer;")
