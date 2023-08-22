from odoo import http
from odoo.http import request

class IfcChecker(http.Controller):

    @http.route('/ifc_checker', type='http', auth='user')
    def ifc_checker(self, **kw):
        is_installed = self.check_ifcopenshell_installed()
        view_id = request.env.ref('z_ifc_reader.view_ifc_checker_form')
        return request.render('z_ifc_reader.ifc_checker_template', {
            'is_ifcopenshell_installed': is_installed,
            'view_id': view_id,
        })

    def check_ifcopenshell_installed(self):
        try:
            import ifcopenshell
            return True
        except ImportError:
            return False
