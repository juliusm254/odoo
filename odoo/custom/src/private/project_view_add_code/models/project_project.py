# Copyright 2017-19 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Luxim d.o.o.
# Copyright 2017 Matmoz d.o.o.
# Copyright 2017 Deneroteam.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class Project(models.Model):
    _inherit = "project.project"
    _description = "ZWBS element"
    # _order = "complete_wbs_code"
    parent_id = fields.Many2one(
        "account.analytic.account", string="Parent", index=True, ondelete="cascade"
    )
    z_code = fields.Char(compute="_compute_parent_prefix", store=True)

    @api.depends("parent_id.parent_path")
    def _compute_parent_prefix(self):
        for record in self:
            parent_path = record.parent_id.parent_path
            record.parent_id.name
            header_value = (
                record["__context"]["group_by"][0]
                if "__context" in record and "group_by" in record["__context"]
                else None
            )
            print(header_value)
            if parent_path and "/" in parent_path:
                record.z_code = parent_path.partition("/")[0]
            else:
                record.z_code = record.project_analytic_id.id
