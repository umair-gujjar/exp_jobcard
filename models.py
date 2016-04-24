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
	mo_lamination_type = fields.Selection([
            ('mat', 'MAT'),
            ('glass', 'Glass'),
            ('varnish', 'Varnish'),
            ],default='', string="Type of Lamination")

	mo_mrp_mat = fields.Boolean(string='Mat')
	mo_mrp_glass = fields.Boolean(string='Glass')
	mo_mrp_varnish = fields.Boolean(string='Varnish')
	mo_type_of_varnish = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Type of Varnish")
	mo_salofeen_width = fields.Char(string='Salofeen Width')
	mo_salofeen_height = fields.Char(string='Salofeen Height')
	mo_paste_materials = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Paste Material")
	mo_mrp_side_dropdown = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Side")
	mo_mrp_crush = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ],default='', string="Crush")
	mo_mrp_pins = fields.Char(string='Pins')
	mo_mrp_reel = fields.Float(string='Reel')
	mo_mrp_cutting = fields.Float(string='Cutting')
	mo_mrp_cut_width = fields.Float(string='Cut Width')
	mo_mrp_cut_height = fields.Float(string='Cut Height')
	mo_mrp_type = fields.Selection([
            ('a', 'Packets'),
            ('b', 'Rolls'),
            ],default='', string="Type")
	mo_mrp_grams = fields.Float(string='Grams')
	mo_mrp_fac = fields.Integer(string='Fac')
	mo_mrp_nos = fields.Float(string='Nos')
	mo_mrp_filter = fields.Char(string='Filter')
	mo_p_mrp_nos = fields.Float(string='Nos')
	mo_p_mrp_filter = fields.Char(string='Filter')
	mo_p_mrp_ups = fields.Char(string='UPS')
	mo_p_mrp_brand = fields.Char(string='Brand')

	mo_mrp_machine = fields.Char(string='Machine')
	mo_mrp_grip = fields.Char(string='Grip')
	mo_mrp_color = fields.Char(string='Color')
	mo_mrp_quantity = fields.Float(string='Quantity')
	mo_mrp_remarks = fields.Text(string='Remarks')
	mo_mrp_remarks_description = fields.Text(string='Remarks')
	mo_mrp_die_number = fields.Char(string='Die Number')
	mo_mrp_die_type = fields.Selection([
            ('a', 'Old'),
            ('b', 'New'),
            ],default='', string="Die Type")
	mo_mrp_die_loc = fields.Char(string="Die Location")
	mo_mrp_foiling = fields.Boolean(string='Foiling')
	mo_mrp_rotry_salt = fields.Boolean(string='Rotry & Salt')
	mo_mrp_imbosing = fields.Boolean(string='Imbosing')
	mo_mrp_guilotine = fields.Boolean(string='Guilotine')
	mo_mrp_screen = fields.Boolean(string='Screen')
	mo_mrp_reel_size = fields.Float(string='Reel Size')
	mo_mrp_cutting_size = fields.Float(string='Cutting Size')
	mo_mrp_fact = fields.Float(string='Fact')
	mo_mrp_pcs = fields.Float(string='PCS')
	mo_mrp_ply = fields.Float(string='Ply')
	mo_mrp_act_reel_size = fields.Float(string='Act Reel Size')

	mo_mrp_ups_desc = fields.Char(string='UPS Desc')
	mo_mrp_part_desc = fields.Char(string='Part Desc')
	mo_mrp_sheets_qty = fields.Float(string='Sheets Quantity')
	mo_mrp_job_qty = fields.Float(string='Job Quantity')
	mo_workbook_one_ids = fields.One2many('mo_workbook_one','mo_workbook_one_id')
	mo_workbook_two_ids = fields.One2many('mo_workbook_two','mo_workbook_two_id')
	bom_id_for_change = fields.Many2one('mrp.bom','onchange Bom')

	@api.onchange('bom_id')
	def bom_id_change(self, cr, uid, ids, bom_id, context=None):
		values = super(mrp_custom_expert, self).bom_id_change(cr, uid, ids, bom_id, context=context)
		all_mrp_prd_recs = self.pool.get('mrp.bom').browse(cr, uid, bom_id, context=context)

		return {
                    'value': {
                    			'mo_lamination_type' : all_mrp_prd_recs.lamination_type,
								'mo_salofeen_width' : all_mrp_prd_recs.salofeen_width,
								'mo_salofeen_height' : all_mrp_prd_recs.salofeen_height,
								'mo_paste_materials' : all_mrp_prd_recs.paste_materials,
								'mo_mrp_side_dropdown' : all_mrp_prd_recs.mrp_side_dropdown,
								'mo_mrp_crush' : all_mrp_prd_recs.mrp_crush,
								'mo_mrp_pins' : all_mrp_prd_recs.mrp_pins,
								'mo_mrp_reel' : all_mrp_prd_recs.mrp_reel,
								'mo_mrp_cutting' : all_mrp_prd_recs.mrp_cutting,
								'mo_mrp_cut_width' : all_mrp_prd_recs.mrp_cut_width,
								'mo_mrp_cut_height' : all_mrp_prd_recs.mrp_cut_height,
								'mo_mrp_type' : all_mrp_prd_recs.mrp_type,
								'mo_mrp_grams' : all_mrp_prd_recs.mrp_grams,
								'mo_mrp_fac' : all_mrp_prd_recs.mrp_fac,
								'mo_mrp_nos' : all_mrp_prd_recs.mrp_nos,
								'mo_mrp_filter' : all_mrp_prd_recs.mrp_filter,
								'mo_p_mrp_nos' : all_mrp_prd_recs.p_mrp_nos,
								'mo_p_mrp_filter' : all_mrp_prd_recs.p_mrp_filter,
								'mo_p_mrp_ups' : all_mrp_prd_recs.p_mrp_ups,
								'mo_p_mrp_brand' : all_mrp_prd_recs.p_mrp_brand,
								'mo_mrp_machine' : all_mrp_prd_recs.mrp_machine,
								'mo_mrp_grip' : all_mrp_prd_recs.mrp_grip,
								'mo_mrp_color' : all_mrp_prd_recs.mrp_color,
								'mo_mrp_quantity' : all_mrp_prd_recs.mrp_quantity,
								'mo_mrp_remarks' : all_mrp_prd_recs.mrp_remarks,
								'mo_mrp_remarks_description' : all_mrp_prd_recs.mrp_remarks_description,
								'mo_mrp_die_number' : all_mrp_prd_recs.mrp_die_number,
								'mo_mrp_die_type' : all_mrp_prd_recs.mrp_die_type,
								'mo_mrp_die_loc' : all_mrp_prd_recs.mrp_die_loc,
								'mo_mrp_foiling' : all_mrp_prd_recs.mrp_foiling,
								'mo_mrp_rotry_salt' : all_mrp_prd_recs.mrp_rotry_salt,
								'mo_mrp_imbosing' : all_mrp_prd_recs.mrp_imbosing,
								'mo_mrp_guilotine' : all_mrp_prd_recs.mrp_guilotine,
								'mo_mrp_screen' : all_mrp_prd_recs.mrp_screen,
								'mo_mrp_reel_size' : all_mrp_prd_recs.mrp_reel_size,
								'mo_mrp_cutting_size' : all_mrp_prd_recs.mrp_cutting_size,
								'mo_mrp_fact' : all_mrp_prd_recs.mrp_fact,
								'mo_mrp_pcs' : all_mrp_prd_recs.mrp_pcs,
								'mo_mrp_ply' : all_mrp_prd_recs.mrp_ply,
								'mo_mrp_act_reel_size' : all_mrp_prd_recs.mrp_act_reel_size,
								'mo_mrp_ups_desc' : all_mrp_prd_recs.mrp_ups_desc,
								'mo_mrp_part_desc' : all_mrp_prd_recs.mrp_part_desc,
								'mo_mrp_sheets_qty' : all_mrp_prd_recs.mrp_sheets_qty,
								'mo_mrp_job_qty' : all_mrp_prd_recs.mrp_job_qty,
								'bom_id_for_change' : bom_id,
								#'mo_workbook_two_ids[0].material' : all_mrp_prd_recs.workbook_two_ids.material,
                }
                }
	@api.onchange('bom_id_for_change')
	def onchange_mo_mrp_reel_size(self):
		if self.mo_mrp_reel_size or self.bom_id:
			self.mo_workbook_one_ids.unlink()
			self.mo_workbook_one_ids = self._prepare_mo_workbook_one_ids()
	@api.onchange('bom_id_for_change')
	def onchange_mo_mrp_pcs(self):
		if self.mo_mrp_pcs or self.bom_id:
			self.mo_workbook_two_ids.unlink()
			self.mo_workbook_two_ids = self._prepare_mo_workbook_two_ids()

	@api.multi
	def _prepare_mo_workbook_one_ids(self):
		new_data = []
		for line in self.bom_id.workbook_one_ids:
			data = self._prepare_workbook_one_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_one_line(self, data):
		if self.bom_id.workbook_one_ids:
			data = {
			'material': data.material,
			'brand': data.brand,
			'grams': data.grams,
			'w_Sheet': data.w_Sheet,
			'line_type': data.line_type,
			'req_weight': data.req_weight,
			}
		return data
	@api.multi
	def _prepare_mo_workbook_two_ids(self):
		new_data = []
		for line in self.bom_id.workbook_two_ids:
			data = self._prepare_workbook_two_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_two_line(self, data):
		if self.bom_id.workbook_two_ids:
			data = {
			'material': data.material,
			'flute': data.flute,
			'reel_size': data.reel_size,
			'required_quantity': data.required_quantity,
			}
		return data

class mrp_bom_custom_expert_workbook_one(models.Model):
	_name = 'mo_workbook_one'
	brand = fields.Char(string='Brand')
	material = fields.Char(string='Material')
	grams = fields.Char(string='Grams')
	w_Sheet = fields.Char(string='W.Sheet')
	line_type = fields.Selection([
            ('a', 'Nali'),
            ('b', 'Paper'),
            ],default='', string="Line Type")
	req_weight = fields.Char(string='Req Weight')
	mo_workbook_one_id = fields.Many2one('mrp.bom','Work Book Id')

class mrp_bom_custom_expert_workbook_two(models.Model):
	_name = 'mo_workbook_two'
	material = fields.Char(string='Material')
	flute = fields.Char(string='Flute')
	reel_size = fields.Float(string='Reel Size')
	required_quantity  = fields.Float(string='Required Quantity')
	mo_workbook_two_id = fields.Many2one('mrp.bom','Work Book Id')



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
	mrp_pins = fields.Char(string='Pins')
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
	p_mrp_ups = fields.Char(string='UPS')
	p_mrp_brand = fields.Char(string='Brand')

	mrp_machine = fields.Char(string='Machine')
	mrp_grip = fields.Char(string='Grip')
	mrp_color = fields.Char(string='Color')
	mrp_quantity = fields.Float(string='Quantity')
	mrp_remarks = fields.Text(string='Remarks')
	mrp_remarks_description = fields.Text(string='Remarks')
	mrp_die_number = fields.Char(string='Die Number')
	mrp_die_type = fields.Selection([
            ('a', 'Old'),
            ('b', 'New'),
            ],default='', string="Die Type")
	mrp_die_loc = fields.Char(string="Die Location")
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