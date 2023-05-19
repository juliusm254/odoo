import xmlrpc.client

# srv = "http://127.0.0.1:15069"
# common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % srv)
# db, user, password = "devel", "admin", "admin"
# uid = common.authenticate(db, user, password, {})

# api = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % srv)


class LibraryAPI:
    def __init__(self, host, port, db, user, pwd):
        common = xmlrpc.client.ServerProxy(
            "http://%s:%d/xmlrpc/2/common" % (host, int(port))
        )
        self.api = xmlrpc.client.ServerProxy(
            "http://%s:%d/xmlrpc/2/object" % (host, int(port))
        )
        self.uid = common.authenticate(db, user, pwd, {})
        self.pwd = pwd
        self.db = db
        # self.model = "library.book"
        self.model = "sale.order"

    def _execute(self, method, model, args):
        # Create a new sales order
        if method == "create_sales_order":
            # Extract the arguments for the create method
            partner_id = args[0].get("partner_id")
            warehouse_id = 1
            partner_invoice_id = partner_id
            partner_shipping_id = partner_id
            pricelist_id = 1
            company_id = 1
            name = args[0].get("so_name")
            picking_policy = "direct"
            product_id = 2
            product_qty = ""
            product_price = ""
            # name = ''
            customer_lead = ""
            order_id = ""
            # Create the order line
            order_line = [
                (
                    0,
                    0,
                    {
                        "product_id": product_id,
                        "product_uom_qty": product_qty,
                        "price_unit": product_price,
                        "name": name,
                        "customer_lead": customer_lead,
                        "order_id": order_id,
                    },
                )
            ]

            # Create the sales order with the given partner and order line
            order_vals = {
                "partner_id": partner_id,
                "warehouse_id": warehouse_id,
                "partner_invoice_id": partner_invoice_id,
                "partner_shipping_id": partner_shipping_id,
                "pricelist_id": pricelist_id,
                "name": name,
                "company_id": company_id,
                "picking_policy": picking_policy,
                "order_line": order_line,
            }
            order_id = self.api.execute_kw(
                self.db, self.uid, self.pwd, model, "create", [order_vals]
            )

            return order_id

        # Handle unknown methods
        raise ValueError(f"Unknown method: {method}")

    # def _execute(self, method, arg_list, kwarg_dict=None):
    #     return self.api.execute_kw(
    #         self.db, self.uid, self.pwd, self.model,
    #         method, arg_list, kwarg_dict or {})

    # def search_read(self, title=None):
    #     domain = [("name", "ilike", title)] if title else []
    #     fields = ["id", "name"]
    #     return self._execute("search_read", [domain,
    #         fields])

    # def create(self, title):
    #     vals = {"name": title}
    #     return self._execute("create", [vals])

    # def write(self, id, title):
    #     vals = {"name": title}
    #     return self._execute("write", [[id], vals])

    # def unlink(self, id):
    #     return self._execute("unlink", [[id]])

    def create_sales_order(self, order_lines, partner_id):
        # Build the sales order data
        sales_order_data = {
            "partner_id": partner_id,
            "order_line": order_lines,
        }

        # Create the sales order
        sales_order_id = self._execute("create", ["sale.order", sales_order_data])

        return sales_order_id


if __name__ == "__main__":
    # Sample test configurations
    host, port, db = "localhost", 15069, "devel"
    user, pwd = "admin", "admin"
    api = LibraryAPI(host, port, db, user, pwd)
    # from pprint import pprint

    # pprint(api.search_read())
