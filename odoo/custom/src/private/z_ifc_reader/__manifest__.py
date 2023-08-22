{
    "name": "IFC Reader",
    "version": "15.0.1.1.1",
    # "category": "Hidden",
    "license": "AGPL-3",
    "summary": "IFC Reader",
    'data': [
        'security/stock_security.xml',
        "security/ir.model.access.csv",
        "views/ifc_reader_menu_views.xml",
        "views/ifc_reader_views.xml",
        # "views/ifc_checker_template.xml",
    ],
    "depends": ['base', 'web'],
    "installable": True,
    "auto_install": True,
    "application": False,

    'qweb': ['static/src/xml/ifc_checker_template.xml'],
    # "post_init_hook": "post_init_hook",
}
