# import logging
# from odoo.api import Environment, SUPERUSER_ID

# _logger = logging.getLogger(__name__)


# def activate_storage_locations(cr, registry):
#     _logger.info("Activate settings for stock locations")
#     env = Environment(cr, SUPERUSER_ID, {})
#     env["res.config.settings"].sudo().create(
#         {
#             "group_stock_multi_locations": True,
#         }
#     ).execute()


# def activate_uoms(cr, registry):
#     _logger.info("Activate settings for units of measure")
#     env = Environment(cr, SUPERUSER_ID, {})
#     env["res.config.settings"].sudo().create(
#         {
#             "group_uom": True,
#         }
#     ).execute()

# def test_ifc(cr, registry):
#     _logger.info("Activate settings for units of measure")

#     env = Environment(cr, SUPERUSER_ID, {})
#     env["res.config.settings"].sudo().create(
#         {
#             "group_uom": True,
#         }
#     ).execute()



# def invoicing_margin_analysis(cr, registry):
#     _logger.info("Activate settings for margin analysis from invoices")
#     env = Environment(cr, SUPERUSER_ID, {})
#     env["res.config.settings"].sudo().create(
#         {
#             "module_product_margin": True,
#         }
#     ).execute()


# def post_init_hook(cr, registry):
#     # activate_storage_locations(cr, registry)
#     # activate_uoms(cr, registry)
#     test_ifc(cr, registry)
#     # invoicing_margin_analysis(cr, registry)
from . import models
