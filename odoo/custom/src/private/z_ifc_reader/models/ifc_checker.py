from odoo import models, fields, api

class IfcChecker(models.Model):
    _name = 'ifc.checker'
    _description = 'IFC Checker'
    _readonly = True

    # is_ifcopenshell_installed = fields.Boolean(string='Is ifcopenshell Installed?', compute='_compute_is_ifcopenshell_installed', store=False)

    # @api.depends('is_ifcopenshell_installed')
    # def _compute_is_ifcopenshell_installed(self):
    #     for record in self:
    #         record.is_ifcopenshell_installed = self.check_ifcopenshell_installed()

    def check_ifcopenshell_installed(self):
        try:
            import ifcopenshell
            return True
        except ImportError:
            return False

    def action_check_ifcopenshell_installed(self):
        result = self.check_ifcopenshell_installed()
        if result:
            message = "IFCOpenShell is installed."
        else:
            message = "IFCOpenShell is not installed."
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'IFCOpenShell Installation Check',
                'message': message,
                'sticky': False,
            }
        }
