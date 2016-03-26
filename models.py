# -*- coding: utf-8 -*-

from openerp import models, fields, api

class product_custom_expert(models.Model):
	_inherit = 'product.template'
	product_length = fields.Char(string='Product Length')
	product_height = fields.Char(string='Product Height')
	product_width = fields.Char(string='Product Width')


class mrp_custom_expert(models.Model):
	_inherit = 'mrp.production'
	job_type_mrp = fields.Selection([
            ('NEW', 'New'),
            ('REPEAT', 'Repeat'),
            ],default='REPEAT', string="Job Type")



class mrp_bom_custom_expert(models.Model):
	_inherit = 'mrp.bom'
	lamination_type = fields.Selection([
            ('mat', 'MAT'),
            ('glass', 'Glass'),
            ('varnish', 'Varnish'),
            ],default='', string="Type of Lamination")

	mrp_mat = fields.Boolean(string='Mat')
	mrp_glass = fields.Boolean(string='Glass')
	mrp_varnish = fields.Boolean(string='Varnish')
	type_of_varnish = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Type of Varnish")
	salofeen_width = fields.Char(string='Salofeen Width')
	salofeen_height = fields.Char(string='Salofeen Height')
	paste_materials = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Paste Material")
	mrp_side_dropdown = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Side")
	mrp_crush = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Crush")
	mrp_pins = fields.Integer(string='Pins')
	mrp_reel = fields.Float(string='Reel')
	mrp_cutting = fields.Float(string='Cutting')
	mrp_cut_width = fields.Float(string='Cut Width')
	mrp_cut_height = fields.Float(string='Cut Height')
	mrp_type = fields.Selection([
            ('a', 'Packets'),
            ('b', 'Rolls'),
            ],default='', string="Type")
	mrp_grams = fields.Float(string='Grams')
	mrp_fac = fields.Integer(string='Fac')
	mrp_nos = fields.Float(string='Nos')
	mrp_filter = fields.Char(string='Filter')
	p_mrp_nos = fields.Float(string='Nos')
	p_mrp_filter = fields.Char(string='Filter')
	p_mrp_ups = fields.Integer(string='UPS')
	p_mrp_brand = fields.Char(string='Brand')

	mrp_machine = fields.Char(string='Machine')
	mrp_grip = fields.Char(string='Grip')
	mrp_color = fields.Char(string='Color')
	mrp_quantity = fields.Float(string='Quantity')
	mrp_remarks = fields.Float(string='Remarks')
	mrp_remarks_description = fields.Text(string='Remarks')
	mrp_die_number = fields.Char(string='Die Number')
	mrp_die_type = fields.Selection([
            ('a', 'Old'),
            ('b', 'New'),
            ],default='', string="Die Type")
	mrp_foiling = fields.Boolean(string='Foiling')
	mrp_rotry_salt = fields.Boolean(string='Rotry & Salt')
	mrp_imbosing = fields.Boolean(string='Imbosing')
	mrp_guilotine = fields.Boolean(string='Guilotine')
	mrp_screen = fields.Boolean(string='Screen')
	mrp_reel_size = fields.Float(string='Reel Size')
	mrp_cutting_size = fields.Float(string='Cutting Size')
	mrp_fact = fields.Float(string='Fact')
	mrp_pcs = fields.Float(string='PCS')
	mrp_ply = fields.Float(string='Ply')
	mrp_act_reel_size = fields.Float(string='Act Reel Size')

	mrp_ups_desc = fields.Char(string='UPS Desc')
	mrp_part_desc = fields.Char(string='Part Desc')
	mrp_sheets_qty = fields.Float(string='Sheets Quantity')
	mrp_job_qty = fields.Float(string='Job Quantity')
	workbook_one_ids = fields.One2many('workbook_one','workbook_one_id')
	workbook_two_ids = fields.One2many('workbook_two','workbook_two_id')

class mrp_bom_custom_expert_workbook_one(models.Model):
	_name = 'workbook_one'
	brand = fields.Char(string='Brand')
	material = fields.Char(string='Material')
	grams = fields.Char(string='Grams')
	w_Sheet = fields.Char(string='W.Sheet')
	line_type = fields.Selection([
            ('a', 'Nali'),
            ('b', 'Paper'),
            ],default='', string="Line Type")
	req_weight = fields.Char(string='Req Weight')
	workbook_one_id = fields.Many2one('mrp.bom','Work Book Id')

class mrp_bom_custom_expert_workbook_two(models.Model):
	_name = 'workbook_two'
	material = fields.Char(string='Material')
	flute = fields.Char(string='Flute')
	reel_size = fields.Float(string='Reel Size')
	required_quantity  = fields.Float(string='Required Quantity')
	workbook_two_id = fields.Many2one('mrp.bom','Work Book Id')