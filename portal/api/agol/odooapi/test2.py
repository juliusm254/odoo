import xmlrpc
from xmlrpc import client

srv = "http://172.19.0.1:8069"
common = xmlrpc.client.ServerProxy("%s/xmlrpc/2/common" % srv)
db, user, password = "Agol-db", "admin@admin.com", "Admin"
uid = common.authenticate(db, user, password, {})

api = xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % srv)

x = api.execute_kw(db, uid, password, "res.partner", "create", 
[{'name': 'Shey Pub'}])

print(x)
print(api.execute_kw(db, uid, password, "res.partner", "read", 
			[[x], ["name"]]))

print(api.execute_kw(db, uid, password, "res.partner", "write", 
			[[x], {'name': 'Packt  Shey Publishing'}]))

print('before unlink')
print(x)
print(api.execute_kw(db, uid, password, "res.partner", "read", 
			[[x], ["name"]]))

print(api.execute_kw(db, uid, password, "res.partner", "unlink", [[x]]))
print('after unlink')
print(x)

print(api.execute_kw(db, uid, password, "res.partner", "read", 
			[[x], ["name"]]))