# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from ast import literal_eval

class MobileServer(http.Controller):

    @http.route('/mobile_server/modules', auth='none', type='json', csrf=False)
    def get_modules(self):
        modules_ids = request.env["ir.config_parameter"].sudo().get_param("mobile_server.allowed_modules_ids")
        modules = []
        for module in request.env['mobile_server.mobile_module'].sudo().browse(literal_eval(modules_ids)):
            modules.append(module.technical_name)
        return modules

    @http.route('/mobile_server/meta', auth="none", type='json', csrf=False)
    def get_meta(self):
        meta = request.env["ir.config_parameter"].sudo().get_param("mobile_server.meta")
        try:
            return json.loads(meta)
        except:
            return {}

#     @http.route('/mobile_server/mobile_server/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mobile_server.listing', {
#             'root': '/mobile_server/mobile_server',
#             'objects': http.request.env['mobile_server.mobile_server'].search([]),
#         })

#     @http.route('/mobile_server/mobile_server/objects/<model("mobile_server.mobile_server"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mobile_server.object', {
#             'object': obj
#         })
