{
    "name": "Rental Units",
    "license": "AGPL-3",
    "category": "Rentals",
    "summary": "Displays Units available for Renting",
    "version": "15.0.1.0.0",
    "depends": ["base", "account", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/rental_units_view.xml",
        "views/res_partner_view.xml",
        "views/rental_units_menu.xml",
        "data/so_cron.xml",
    ],
    "installable": True,
    "application": True,
    # "auto_install": False,
}
