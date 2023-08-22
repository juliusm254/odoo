{
    "name": "Vision Settings",
    "version": "15.0.1.1.1",
    "category": "Hidden",
    "license": "AGPL-3",
    "summary": "Install custom settings for vision Energy",
    "depends": [
        # OdooSA apps
        "stock",
        "l10n_ke",
        "purchase",
        "stock_account",
        "purchase_stock",
        "account",
        "stock_landed_costs",
        "product_margin",
        # "stock_landed_costs_purchase_auto",
    ],
    "installable": True,
    "auto_install": True,
    "application": False,
    "post_init_hook": "post_init_hook",
}
