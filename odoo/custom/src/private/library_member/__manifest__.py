{
    "name": "Library Member",
    "license": "AGPL-3",
    "descriptom": "Manage member borrowing books.",
    "author": "The Social Experiment",
    "depends": ["library_app", "mail"],
    "application": False,
    "data": [
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
    ],
}
