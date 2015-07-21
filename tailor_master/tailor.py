# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Serpent Consulting Services Pvt. Ltd.
#    Copyright (C) 2014-2015 Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import models, fields, api

class tmaster(models.Model):
    _name = 'tmaster.model'
    
    
    order = fields.Integer(string='Order No.')
    dealer = fields.Char(string='Dealer')
    choose = fields.Selection([('dfa','DFA'),('cmt','CMT')],'Choose', default="dfa")
    name = fields.Many2one('res.partner', "Customer")
    active = fields.Boolean(string='Active', default=True)
    odate = fields.Date(string='Order Date')
    pdate = fields.Date(string='Promise Date')
    shirt = fields.Integer(string='Custom Shirts (Pcs)')
    kurta = fields.Integer(string='Shalwar Kameez (Pcs)')
    trouser = fields.Integer(string='Trouser/Pants (Pcs)')
    monogram = fields.Integer(string='Monogram (Rs.)')
    oversize = fields.Integer(string='Over Size (Rs.)')
    fitting = fields.Selection([('slim','Slim Fit'),('regular','Regular Fit'),('loose','Loose Fit')],'Fitting', default="regular")
    
    neck = fields.Float(string='Neck')
    tail = fields.Float(string='Tail')
    chest = fields.Float(string='Chest')
    yoke = fields.Float(string='Yoke')
    waist = fields.Float(string='Waist')
    lsleeve = fields.Float(string='Sleeve (Left)')
    rsleeve = fields.Float(string='Sleeve (Right)')
    hip = fields.Float(string='Hips/Seat')
    lwrist = fields.Float(string='Wrist (Left)')
    rwrist = fields.Float(string='Wrist (Right)')
    dneck = fields.Selection([('ns','Narrow Straight'),('cs','Classic Straight'),('nws','Narrow Wide Straight'),('tsp','Traditional Spread'),('csp','Classic Spread'),('wsp','Wide Spread'),('cspc','Counter Side Spread-Cut away'),('tbd','Traditional Button Down'),('hbd','Hidden Button Down'),('cpc','Curve Point Classic'),('ctc','Classic Tab Collar'),('tb','Traditional Band')],'Neck Design', default="ns")
    dsleeve = fields.Selection([('obr','One Button Round'),('oba','One Button Angled'),('cc','Convertible Cuff'),('tbs','Two Button Square'),('tbr','Two Button Round'),('tba','Two Button Angled'),('caf','Cut-away French'),('scf','Square Corner French'),('acf','Angled Corner French'),('rcf','Round Corner French')],'Sleeve Design', default="obr")
    dpocket = fields.Selection([('rp','Regular Pocket'),('rc','Round Cornered')],'Pocket Design', default="rp")
    dfront = fields.Selection([('pf','Pleat Front'),('sf','Sport Front'),('ff','Fly Front')],'Front Design', default="pf")
    dback = fields.Selection([('tsp','Two Side Pleats'),('sb','Smooth Back'),('cbp','Center Box Pleat')],'Back Design', default="tsp")

