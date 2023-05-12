from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        user_odoo = self.env.ref("base.user_admin")
        #         self.env = self.env(user=user_odoo)
        # Find the user with the login "odoo"
        # user_odoo = self.env['res.users'].search([("login", "=", "odoo")])
        # Raise an exception if no users are found or multiple users are found
        if not user_odoo:
            raise Exception("User with login 'odoo' not found")
        if len(user_odoo) > 1:
            raise Exception("Multiple users with login 'odoo' found")
        # Set the user context for self.env to the user with login "odoo"
        self.env = self.env(user=user_odoo)
        # Access the library.book model as the user with login "odoo"
        self.Book = self.env["library.book"]
        # Create a new book as the user with login "odoo"
        self.book1 = self.Book.create(
            {"name": "Odoo Development Essentials", "isbn": "0-571-05686-5"}
        )
        # Add check to ensure book1 was created successfully
        if not self.book1:
            raise Exception("Failed to create book1")

    def test_book_create(self):
        "New Books are active by default"
        # Add check to ensure book1 exists
        if not hasattr(self, "book1"):
            raise Exception("book1 attribute not set")
        self.assertEqual(self.book1.active, True)

    # class TestBook(TransactionCase):

    #     def setUp(self, *args, **kwargs):
    #         super().setUp(*args, **kwargs)
    #         user_odoo = self.env.ref("base.user_admin")
    #         self.env = self.env(user=user_odoo)
    #         self.Book = self.env["library.book"]
    #         self.book1 = self.Book.create({
    #             "name": "Odoo Development Essentials",
    #             "isbn": "879-1-78439-279-6"
    #         })
    #         # Add check to ensure book1 was created successfully
    #         if not self.book1:
    #             raise Exception("Failed to create book1")

    # def test_book_create(self):
    #     "New Books are active by default"
    #     # Add check to ensure book1 exists
    #     if not hasattr(self, "book1"):
    #         raise Exception("book1 attribute not set")
    #     self.assertEqual(self.book1.active, True)

    # def setUp(self, *args, **kwargs):
    #     super().setUp(*args, **kwargs)
    #     user_admin = self.env.ref("base.user_admin")
    #     self.env = self.env(user=user_admin)
    #     self.Book = self.env["library.book"]
    #     self.book1 = self.Book.create({
    #         "name": "Odoo Development Essentials",
    #         "isbn": "879-1-78439-279-6"
    #     })

    # def test_book_create(self):
    #     "New Books are active by default"
    #     self.assertEqual(
    #         self.book1.active, True
    #     )

    def test_check_isbn(self):
        "Check valid ISBN"
        self.assertTrue(self.book1._check_isbn)

    # def setUp(self, *args, **kwargs):
    #     super() .setUp(*args, **kwargs)
    #     user_admin = self.env.ref("base.user_admin")
    #     self.env = self.env(user=user_admin)
    #     self.Book = self.env["library.book"]
    #     self.book_ode = self.Book.create({
    #         "name": "Odoo Development Essentials",
    #         "isbn": "879-1-78439-279-6"
    #     })
