# from odoo import api, fields, models


# class ResPartner(models.Model):
#     _inherit = "res.partner"
#     rental_unit_id = fields.Many2one("rental.unit", string="Rental Unit")
#     # rental_unit_id = fields.One2many("rental.unit", "partner_id", string="Rental Units")
#     # rental_unit_id = fields.One2many('rental.unit'
#     # , string='Rental Units', compute="_compute_rental_unit_id",)
#     rental_unit_names = fields.Char(
#         string="Rental Unit Names", compute="_compute_rental_unit_names", store=True
#     )

#     @api.depends("rental_unit_id")
#     def _compute_rental_unit_names(self):
#         for partner in self:
#             rental_unit_names = ", ".join(partner.rental_unit_id.mapped("name"))
#             partner.rental_unit_names = rental_unit_names

#     # @api.depends("rental_unit_id")
#     # def _compute_rental_unit_id(self):
#     #     for partner in self:
#     #         partner.rental_unit_id = partner.rental_unit_id
