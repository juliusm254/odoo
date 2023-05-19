from odoo import models

# class RentalUnit(models.Model):
#     _name = 'rental.unit'
#     _description = 'Rental Unit'

#     name = fields.Char(string='Name', required=True)
#     partner_id = fields.Many2one('res.partner', string='Tenant')
#     price = fields.Float(string='Rental Price')
#     is_vacant = fields.Boolean(string='Vacant', compute='_compute_is_vacant', store=True)
#     # tenant_id = fields.Many2one('res.partner', string='Tenant')

#     # @api.model
#     # def assign_tenant(self, unit_id, tenant_id):
#     #     """
#     #     Assigns a tenant to a rental unit by updating the
#           tenant_id field of the rental.unit record.
#     #     :param unit_id: the ID of the rental.unit record to update
#     #     :param tenant_id: the ID of the tenant to assign to the rental unit
#     #     """
#     #     rental_unit = self.browse(unit_id)
#     #     if rental_unit:
#     #         rental_unit.write({'tenant_id': tenant_id})

#     @api.depends('partner_id')
#     def _compute_is_vacant(self):
#         for rental_unit in self:
#             if rental_unit.partner_id:
#                 rental_unit.is_vacant = False
#             else:
#                 rental_unit.is_vacant = True


class ResPartner(models.Model):
    _inherit = "res.partner"

    # rental_unit_id = fields.Many2one('rental.unit', string='Rental Unit'
    #                                 #  , domain="[('is_company','=',True)]"
    #                                  )

    # rental_unit_status = fields.Selection([
    #     ('vacant', 'Vacant'),
    #     ('occupied', 'Occupied')
    # ], string='Status', default='vacant')

    # @api.onchange('rental_unit_id')
    # def _onchange_rental_unit_id(self):
    #     if self.rental_unit_id:
    #         self.rental_unit_status = 'occupied'
    #     else:
    #         self.rental_unit_status = 'vacant'
