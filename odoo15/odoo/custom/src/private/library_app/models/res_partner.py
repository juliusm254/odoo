from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    published_books = fields.One2many(
        "library.book", "publisher_id", string="Published Books"
    )
