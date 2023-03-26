from xmlrpc import client
import xmlrpc

print('Test Api')

# srv = "http://172.19.0.1:8069"
srv = "http://127.0.0.1:15069"
common = client.ServerProxy("%s/xmlrpc/2/common" % srv)
print(common.version())


db, user, password = "devel", "admin", "admin"
uid = common.authenticate(db, user, password, {})
print(uid)

api = client.ServerProxy('%s/xmlrpc/2/object' % srv)
print(api.execute_kw(db, uid, password, "res.users", "search_count", [[]]))

api = xmlrpc.client.ServerProxy("%s/xmlrpc/2/object" % srv)
print(api.execute_kw(db, uid, password, "res.users", "read", [2, ["login", "name", "company_id"]]))

domain = [("login", "=", "admin@admin.com")]
print(api.execute_kw(db, uid, password, "res.users", "search", [domain]))

domain = [("name", "=", "Administrator")]
print(api.execute_kw(db, uid, password, "res.users", "search", [domain]))

print(api.execute_kw(db, uid, password, "res.users", "search_read", [domain, ["login", "name"]]))

print(api.execute_kw(db, uid, password, "res.users", "search_read", [domain, ["login", "name"]]))