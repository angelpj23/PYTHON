# -*- coding: utf-8 -*-
from odoo import http

class Asignar(http.Controller):
    @http.route('/asignar/asignar/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/asignar/asignar/objects/', auth='public')
    def clients(self, **kw):
        return http.request.render('asignar.listing', {
            'root': '/asignar/asignar',
            'objects': http.request.env['asignar.asignar'].search([]),
        })

    @http.route('/asignar/asignar/objects/<model("asignar.asignar"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('asignar.object', {
            'object': obj
        })