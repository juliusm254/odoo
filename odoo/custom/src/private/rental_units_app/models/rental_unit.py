from odoo import api, fields, models


class RentalUnit(models.Model):
    _name = "rental.unit"
    _description = "Rental Unit"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one("res.partner", string="Tenant")
    price = fields.Monetary("Price", "currency_id")
    # price helper
    currency_id = fields.Many2one("res.currency")
    is_occupied = fields.Boolean(
        string="Occupied", compute="_compute_is_occupied", store=True
    )

    # @api.model
    # def assign_tenant(self, unit_id, tenant_id):
    #     """
    #     Assigns a tenant to a rental unit by updating the
    #       tenant_id field of the rental.unit record.
    #     :param unit_id: the ID of the rental.unit record to update
    #     :param tenant_id: the ID of the tenant to assign to the rental unit
    #     """
    #     rental_unit = self.browse(unit_id)
    #     if rental_unit:
    #         rental_unit.write({'tenant_id': tenant_id})

    @api.depends("partner_id")
    def _compute_is_occupied(self):
        for rental_unit in self:
            if rental_unit.partner_id:
                rental_unit.is_occupied = True
            else:
                rental_unit.is_occupied = False

    @api.model
    def create_sales_orders(self):
        rental_units = self.search([("partner_id", "!=", False)])
        for rental_unit in rental_units:
            delivey_invoice = self.env["account.move"].create(
                [
                    {
                        "move_type": "out_invoice",
                        "invoice_date": fields.Date.context_today(self),
                        "partner_id": rental_unit.partner_id.id,
                        "currency_id": 92,
                        # 'amount_total': 10,
                        "invoice_line_ids": [
                            (
                                0,
                                0,
                                {
                                    "product_id": 1,
                                    "name": "Rent",
                                    "quantity": 1,
                                    "price_unit": rental_unit.price,
                                    "tax_ids": [(6, 0, [1])],
                                    # 'price_subtotal': 10,
                                },
                            ),
                        ],
                    },
                ]
            )
            delivey_invoice.action_post()
