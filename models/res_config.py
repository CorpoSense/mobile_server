# -*- coding: utf-8 -*-

import os
import odoo
from odoo import models, fields, api
from ast import literal_eval


class MobileServerSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allowed_modules_ids = fields.Many2many('mobile_server.mobile_module', String='Modules', ondelete='cascade')
    meta = fields.Text('Meta Data', help='This is a JSON meta data which will be sent to the mobile')

    @api.multi
    def set_values(self):
        res = super(MobileServerSettings, self).set_values()
        config = self.env['ir.config_parameter'].sudo()
        config.set_param('mobile_server.allowed_modules_ids', self.allowed_modules_ids.ids)
        config.set_param('mobile_server.meta', self.meta)
        return res

    @api.model
    def get_values(self):
        res = super(MobileServerSettings, self).get_values()
        data = self.env['ir.config_parameter'].sudo()
        meta_data = data.get_param('mobile_server.meta')
        if meta_data:
            res.update(
                meta=meta_data
            )
        allowed_modules_data = data.get_param('mobile_server.allowed_modules_ids')
        if allowed_modules_data:
            res.update(
                allowed_modules_ids=[(6, 0, literal_eval(allowed_modules_data))]
            )
        return res


class MobileServerModule(models.Model):
    # _inherit = 'ir.module.module'
    _name = 'mobile_server.mobile_module'
    _rec_name = 'shortdesc'

    technical_name = fields.Char('Name', unique=True)
    # url = fields.Char('url', compute="_compute_url", store=True)
    shortdesc = fields.Char('Module Name')#, readonly=True, translate=True)
    # author = fields.Char("Author", readonly=True)
    # icon_attachment_id = fields.Many2one('ir.attachment', ondelete='restrict')
    # icon = fields.Binary()
    # summary = fields.Char('Summary', readonly=True)

    # @api.multi
    # @api.depends('technical_name')
    # def _compute_url(self):
    #     for record in self:
    #         record.url = "https://www.odoo.com/apps/modules/%s.0/%s/" % (
    #             record.demo_plan_id.server_id.odoo_version, record.technical_name)

    @api.model
    def createModules(self):
        modules = self.env['ir.module.module'].search([('application', '=', True),
                                                       ('state', '=', 'installed')])
        for module in modules:
            self.create({'technical_name': module.name, 'shortdesc': module.shortdesc})

    @api.model_cr
    def _register_hook(self):
        if self.search_count([]) == 0:
            self.createModules()
