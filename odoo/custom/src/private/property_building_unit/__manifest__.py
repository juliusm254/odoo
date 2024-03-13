##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2022- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# {
#     "name": "Property: Building",
#     "version": "14.0.1.0.0",
#     # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
#     "summary": "Adds new variables to property model, useful for buildings.",
#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     "category": "Sales",
#     "description": """
#     Adds new variables to property model, useful for buildings.
#     """,
#     #'sequence': '1',
#     "author": "Vertel AB",
#     "website": "https://vertel.se/apps/odoo-property/property_building",
#     "images": ["static/description/banner.png"],  # 560x280 px.
#     "license": "AGPL-3",
#     "contributor": "",
#     "maintainer": "Vertel AB",
#     "repository": "https://github.com/vertelab/odoo-property",
#     # Any module necessary for this one to work correctly
#     "application": False,
#     "installable": True,
#     "depends": [
#         "contract",
#         "agreement_contract",
#         "property_mgmt",
#         "l10n_se_municipality_class",
#     ],
#     "data": [
#         "views/property_building.xml",
#         "security/ir.model.access.csv",
#     ],
# }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


{
    "name": "Property:Building Units",
    "license": "AGPL-3",
    "category": "property_buildings",
    "summary": "Displays Units available for Property",
    "version": "16.0.1.0.0",
    # "depends": ["base", "account", "contacts", "partner_id_view"],
    "depends": ["base", "account", "contacts", "property_mgmt"],
    "data": [
        "security/ir.model.access.csv",
        "views/property_building_unit_view.xml",
        "views/property_building_units_list_template.xml",
        "views/property_building_units_menu.xml",
        "views/account_move_form_view.xml",
        "views/property_view.xml",
        "data/monthly_unit_invoice_cron.xml",
    ],
    "installable": True,
    "application": True,
    # "auto_install": False,
}
