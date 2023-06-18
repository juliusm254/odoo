import logging
from odoo.api import Environment, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def activate_storage_locations(cr, registry):
    _logger.info("Activate settings for stock locations")
    env = Environment(cr, SUPERUSER_ID, {})
    env["res.config.settings"].sudo().create(
        {
            "group_stock_multi_locations": True,
        }
    ).execute()


def post_init_hook(cr, registry):
    activate_storage_locations(cr, registry)
