{
    "name": "Rental Units",
    "license": "AGPL-3",
    "category": "Rentals",
    "summary": "Displays Units available for Renting",
    "version": "15.0.1.0.0",
    "depends": ["base", "account", "contacts", "partner_id_view"],
    "data": [
        "security/ir.model.access.csv",
        "views/rental_unit_view.xml",
        "views/rental_units_list_template.xml",
        "views/rental_units_menu.xml",
        "views/account_move_form_view.xml",
        "data/monthly_unit_invoice_cron.xml",
    ],
    "installable": True,
    "application": True,
    # "auto_install": False,
}
