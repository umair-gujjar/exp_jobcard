# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _
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
            ('heatsealable', 'Heat Sealable'),
            ('metalize', 'Metalize'),
            ],default='', string="Type of Lamination")

	mo_mrp_mat = fields.Boolean(string='Mat')
	mo_mrp_glass = fields.Boolean(string='Glass')
	mo_mrp_varnish = fields.Boolean(string='Varnish')
	mo_type_of_varnish = fields.Selection([
            ('op varnish', 'Op Varnish'),
            ('waterbase varnish', 'Waterbase Varnish'),
            ('uv varnish', 'UV Varnish'),
            ('spot varnish', 'Spot Varnish'),
            ],default='', string="Type of Varnish")
	mo_salofeen_width = fields.Char(string='Salofeen Width')
	mo_salofeen_height = fields.Char(string='Salofeen Height')
	mo_lamination_width = fields.Char(string='Lamination Width')
	mo_lamination_height = fields.Char(string='Lamination Height')
	mo_qty_lamination_reel = fields.Char(string='Qty of Lamination Reel')
	mo_paste_materials = fields.Selection([
            ('glue', 'Glue'),
			('sodium silicate', 'Sodium Silicate'),
			('samadbondwhite', 'SamadBond White'),
			('samadbondyellow', 'SamadBond Yellow'),
            ],default='', string="Paste Material")
	mo_mrp_side_dropdown = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Side")
	mo_mrp_crush = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Crush")
	mo_mrp_pins = fields.Char(string='Pins')
	mo_mrp_machine = fields.Char(string='Machine')
	mo_mrp_grip = fields.Char(string='Grip')
	mo_mrp_remarks_description = fields.Text(string='Remarks')
	#mo_mrp_die_number = fields.Char(string='Die Number')
	#mo_mrp_die_type = fields.Selection([
    #        ('a', 'Old'),
    #        ('b', 'New'),
    #        ],default='', string="Die Type")
	#mo_mrp_die_loc = fields.Char(string="Die Location")
	mo_mrp_foiling = fields.Boolean(string='Foiling')
	mo_mrp_rotry_salt = fields.Boolean(string='Rotry & Salt')
	mo_mrp_imbosing = fields.Boolean(string='Imbosing')
	mo_mrp_guilotine = fields.Boolean(string='Guilotine')
	mo_mrp_screen = fields.Boolean(string='Screen')
	mo_mrp_cc_qty = fields.Char(string='C.C Qty')
	wrbk_corrugation_two = fields.One2many('workbook_corrugation_two','wrkbk_corrugation_id')
	mo_workbook_one_ids = fields.One2many('mo_workbook_one','mo_workbook_one_id')
	mo_workbook_two_ids = fields.One2many('mo_workbook_two','mo_workbook_two_id')
	wrkbk_three_ids = fields.One2many('workbook_three_paper_board','wrkbk_three_id')
	wrkbk_five_ids = fields.One2many('workbook_five_die','wrkbk_five_id')
	wrkbk_color_ids = fields.One2many('workbook_color_production','wrkbk_production_id')
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
								'mo_mrp_machine' : all_mrp_prd_recs.mrp_machine,
								'mo_mrp_grip' : all_mrp_prd_recs.mrp_grip,
								'mo_mrp_remarks_description' : all_mrp_prd_recs.mrp_remarks_description,
								#'mo_mrp_die_number' : all_mrp_prd_recs.mrp_die_number,
								#'mo_mrp_die_type' : all_mrp_prd_recs.mrp_die_type,
								#'mo_mrp_die_loc' : all_mrp_prd_recs.mrp_die_loc,
								'mo_mrp_foiling' : all_mrp_prd_recs.mrp_foiling,
								'mo_mrp_rotry_salt' : all_mrp_prd_recs.mrp_rotry_salt,
								'mo_mrp_imbosing' : all_mrp_prd_recs.mrp_imbosing,
								'mo_mrp_guilotine' : all_mrp_prd_recs.mrp_guilotine,
								'mo_mrp_screen' : all_mrp_prd_recs.mrp_screen,
								'mrp_cc_qty' : all_mrp_prd_recs.mrp_cc_qty,
								#'mo_mrp_reel_size' : all_mrp_prd_recs.mrp_reel_size,
								#'mo_mrp_cutting_size' : all_mrp_prd_recs.mrp_cutting_size,
								#'mo_mrp_fact' : all_mrp_prd_recs.mrp_fact,
								#'mo_mrp_pcs' : all_mrp_prd_recs.mrp_pcs,
								#'mo_mrp_ply' : all_mrp_prd_recs.mrp_ply,
								#'mo_mrp_act_reel_size' : all_mrp_prd_recs.mrp_act_reel_size,
								#'mo_mrp_ups_desc' : all_mrp_prd_recs.mrp_ups_desc,
								#'mo_mrp_part_desc' : all_mrp_prd_recs.mrp_part_desc,
								#'mo_mrp_sheets_qty' : all_mrp_prd_recs.mrp_sheets_qty,
								#'mo_mrp_job_qty' : all_mrp_prd_recs.mrp_job_qty,
								'bom_id_for_change' : bom_id,
								#'mo_workbook_two_ids[0].material' : all_mrp_prd_recs.workbook_two_ids.material,
                }
                }

	@api.onchange('bom_id_for_change')
	def onchange_mo_mrp_reel_size(self):
		self.mo_workbook_one_ids.unlink()
		self.mo_workbook_one_ids = self._prepare_mo_workbook_one_ids()
		self.wrbk_corrugation_two.unlink()
		self.wrbk_corrugation_two = self._prepare_mo_workbook_corrugation_ids()
	@api.onchange('bom_id_for_change')
	def onchange_mo_mrp_pcs(self):
		self.mo_workbook_two_ids.unlink()
		self.mo_workbook_two_ids = self._prepare_mo_workbook_two_ids()
		self.wrkbk_three_ids.unlink()
		self.wrkbk_three_ids = self._prepare_mo_workbook_three_ids()
		self.wrkbk_color_ids.unlink()
		self.wrkbk_color_ids = self._prepare_mo_workbook_color_ids()
		self.wrkbk_five_ids.unlink()
		self.wrkbk_five_ids = self._prepare_mo_workbook_five_ids()
# for corrugation
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
			'part_desc': data.part_desc,
			'w_Sheet': data.w_Sheet,
			'line_type': data.line_type,
			'req_weight': data.req_weight,
			}
		return data
# for rolls required
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
			'part_desc':data.part_desc,
			}
		return data
# for paperboard
	@api.multi
	def _prepare_mo_workbook_three_ids(self):
		new_data = []
		for line in self.bom_id.wrkbk_four_ids:
			data = self._prepare_workbook_three_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_three_line(self, data):
		if self.bom_id.wrkbk_four_ids:
			data = {
			'mrp_reel' : data.mrp_reel,
			'mrp_cutting' : data.mrp_cutting,
			'mrp_cut_width' : data.mrp_cut_width,
			'mrp_cut_height' : data.mrp_cut_height,
			#'mrp_cut_height_printed' : data.mrp_cut_height_printed,
			'mrp_type' : data.mrp_type,
			'mrp_grams' : data.mrp_grams,
			'mrp_fac' : data.mrp_fac,
			'mrp_nos' : data.mrp_nos,
			'mrp_filter' : data.mrp_filter,
			'p_mrp_nos' : data.p_mrp_nos,
			'p_mrp_filter' : data.p_mrp_filter,
			'p_mrp_ups' : data.p_mrp_ups,
			'p_mrp_brand' : data.p_mrp_brand,
			}
		return data
#for color
# for paperboard
	@api.multi
	def _prepare_mo_workbook_color_ids(self):
		new_data = []
		for line in self.bom_id.wrkbk_color_bom_ids:
			data = self._prepare_workbook_color_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_color_line(self, data):
		if self.bom_id.wrkbk_color_bom_ids:
			data = {
			'mrp_color' : data.mrp_color,
			'mrp_quantity' : data.mrp_quantity,
			'mrp_remarks' : data.mrp_remarks,
			'side' : data.side,
			}
		return data

	@api.multi
	def _prepare_mo_workbook_five_ids(self):
		new_data = []
		for line in self.bom_id.wrkbk_six_ids:
			data = self._prepare_workbook_five_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_five_line(self, data):
		if self.bom_id.wrkbk_six_ids:
			data = {
			'mo_mrp_die_number' : data.mrp_die_number,
			'mo_mrp_die_type' : data.mrp_die_type,
			'mo_mrp_die_loc' : data.mrp_die_loc,
			'mo_mrp_die_remarks' : data.mrp_die_remarks,
			'mo_mrp_die_as_per' : data.mrp_die_as_per,
			}
		return data	

	@api.multi
	def _prepare_mo_workbook_corrugation_ids(self):
		new_data = []
		for line in self.bom_id.workbook_corrugation_ids:
			data = self._prepare_workbook_corrugation_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_corrugation_line(self, data):
		if self.bom_id.workbook_corrugation_ids:
			data = {
			'mo_mrp_reel_size' : data.mrp_reel_size,
			'mo_mrp_cutting_size' : data.mrp_cutting_size,
			'mo_mrp_fact' : data.mrp_fact,
			'mo_mrp_pcs' : data.mrp_pcs,
			'mo_mrp_ply' : data.mrp_ply,
			'mo_mrp_act_reel_size' : data.mrp_act_reel_size,
			'mo_mrp_ups_desc' : data.mrp_ups_desc,
			'mo_mrp_part_desc' : data.mrp_part_desc,
			'mo_mrp_sheets_qty' : data.mrp_sheets_qty,
			'mo_mrp_job_qty' : data.mrp_job_qty,
			'mo_mrp_prod_length' : data.mrp_prod_length,
			'mo_mrp_prod_height' : data.mrp_prod_height,
			'mo_mrp_prod_width' : data.mrp_prod_width,
			}
		return data		

	@api.multi
	def write(self,values):
		result =  super(mrp_custom_expert, self).write(values)
		self.mo_workbook_one_ids.unlink()
		self.mo_workbook_one_ids = self._prepare_mo_workbook_one_ids()
		self.mo_workbook_two_ids.unlink()
		self.mo_workbook_two_ids = self._prepare_mo_workbook_two_ids()
		self.wrkbk_three_ids.unlink()
		self.wrkbk_three_ids = self._prepare_mo_workbook_three_ids()
		self.wrkbk_color_ids.unlink()
		self.wrkbk_color_ids = self._prepare_mo_workbook_color_ids()
		return result

# Corrugation workbook for manifacture order
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
	part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")
	mo_workbook_one_id = fields.Many2one('mrp.production','Work Book Id')

# Rolls required workbook for manifacture order
class mrp_bom_custom_expert_workbook_two(models.Model):
	_name = 'mo_workbook_two'
	material = fields.Char(string='Material')
	flute = fields.Selection([
            ('b', 'B Flute 2.5'),
            ('e', 'E Flute 1.5'),
            ('c', 'C Flute 3.5'),
            ],default='', string="Flute")
	reel_size = fields.Float(string='Reel Size')
	required_quantity  = fields.Float(string='Required Quantity')
	part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")
	mo_workbook_two_id = fields.Many2one('mrp.production','Work Book Id')


# Paper board workbook for manifacture order
class workbook_three_paper_board(models.Model):
	_name = 'workbook_three_paper_board'
	mrp_reel = fields.Float(string='Reel')
	mrp_cutting = fields.Float(string='Cutting')
	mrp_cut_width = fields.Float(string='Cut Width')
	mrp_cut_height = fields.Float(string='Cut Height')
	#mrp_cut_height_printed = fields.Float(string='Cut Height')
	mrp_type = fields.Selection([
            ('a', 'Packets'),
            ('b', 'Sheet'),
            ],default='', string="Type")
	mrp_grams = fields.Float(string='Grams')
	mrp_fac = fields.Integer(string='Fac')
	mrp_nos = fields.Float(string='Nos')
	mrp_filter = fields.Char(string='Filter')
	p_mrp_nos = fields.Float(string='Printed Sheet Nos ')
	p_mrp_filter = fields.Char(string='Filter')
	p_mrp_ups = fields.Char(string='UPS')
	p_mrp_brand = fields.Char(string='Brand')
	wrkbk_three_id = fields.Many2one('mrp.production','Work Book Id')


# Paper board workbook for manifacture order
class workbook_five_die(models.Model):
	_name = 'workbook_five_die'
	mo_mrp_die_number = fields.Char(string='Die Number')
	mo_mrp_die_type = fields.Selection([
            ('a', 'Old'),
            ('b', 'New'),
            ],default='', string="Die Type")
	mo_mrp_die_loc = fields.Char(string="Die Location")
	mo_mrp_die_remarks = fields.Text(string="Remarks")
	mo_mrp_die_as_per = fields.Char(string="Die as Per")
	wrkbk_five_id = fields.Many2one('mrp.production','Work Book Id')

class workbook_corrugation_two(models.Model):
	name = 'workbook_corrugation_two'
	mo_mrp_reel_size = fields.Float(string='Reel Size')
	mo_mrp_cutting_size = fields.Float(string='Cutting Size')
	mo_mrp_fact = fields.Float(string='Fact')
	mo_mrp_pcs = fields.Float(string='PCS')
	mo_mrp_ply = fields.Float(string='Ply')
	mo_mrp_prod_length = fields.Float(string='Product Length')
	mo_mrp_prod_height = fields.Float(string='Product Height')
	mo_mrp_prod_width = fields.Float(string='Product Width')
	mo_mrp_act_reel_size = fields.Float(string='Act Reel Size')

	mo_mrp_ups_desc = fields.Char(string='UPS Desc')
	mo_mrp_part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")
	mo_mrp_sheets_qty = fields.Float(string='Sheets Quantity')
	mo_mrp_job_qty = fields.Float(string='Job Quantity')
	wrkbk_corrugation_id = fields.Many2one('mrp.production','Work Book Id')



# Color workbook for manifacture order
class workbook_color_production(models.Model):
	_name = 'workbook_color_production'
	mrp_color = fields.Char(string='Color')
	mrp_quantity = fields.Float(string='Quantity')
	mrp_remarks = fields.Text(string='Remarks')
	side = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Side")
	wrkbk_production_id = fields.Many2one('mrp.production','Work production Id')

class mrp_bom_custom_expert(models.Model):
	_inherit = 'mrp.bom'
	lamination_type = fields.Selection([
            ('mat', 'MAT'),
            ('glass', 'Glass'),
            ('heatsealable', 'Heat Sealable'),
            ('metalize', 'Metalize'),
            ],default='', string="Type of Lamination")

	mrp_mat = fields.Boolean(string='Mat')
	mrp_glass = fields.Boolean(string='Glass')
	mrp_varnish = fields.Boolean(string='Varnish')
	type_of_varnish = fields.Selection([
            ('op varnish', 'Op Varnish'),
            ('waterbase varnish', 'Waterbase Varnish'),
            ('uv varnish', 'UV Varnish'),
            ('spot varnish', 'Spot Varnish'),
            ],default='', string="Type of Varnish")
	salofeen_width = fields.Char(string='Salofeen Width')
	salofeen_height = fields.Char(string='Salofeen Height')
	lamination_width = fields.Char(string='Lamination Width')
	lamination_height = fields.Char(string='Lamination Height')
	qty_lamination_reel = fields.Char(string='Qty of Lamination Reel')
	paste_materials = fields.Selection([
            ('glue', 'Glue'),
			('sodium silicate', 'Sodium Silicate'),
			('samadbondwhite', 'SamadBond White'),
			('samadbondyellow', 'SamadBond Yellow'),
            ],default='', string="Paste Material")
	mrp_side_dropdown = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Side")
	mrp_crush = fields.Selection([
            ('a', 'By Hand'),
            ('b', 'By Machine'),
            ],default='', string="Crush")
	mrp_pins = fields.Char(string='Pins')
	mrp_machine = fields.Char(string='Machine')
	mrp_grip = fields.Char(string='Grip')
	mrp_remarks_description = fields.Text(string='Remarks')
	#mrp_die_number = fields.Char(string='Die Number')
	#mrp_die_type = fields.Selection([
    #        ('a', 'Old'),
    #        ('b', 'New'),
    #        ],default='', string="Die Type")
	#mrp_die_loc = fields.Char(string="Die Location")
	mrp_foiling = fields.Boolean(string='Foiling')
	mrp_rotry_salt = fields.Boolean(string='Rotry & Salt')
	mrp_imbosing = fields.Boolean(string='Imbosing')
	mrp_guilotine = fields.Boolean(string='Guilotine')
	mrp_screen = fields.Boolean(string='Screen')
	mrp_cc_qty = fields.Char(string='C.C Qty')
	workbook_corrugation_ids = fields.One2many('workbook_corrugation_one','wrkbk_corrugation_id')
	workbook_one_ids = fields.One2many('workbook_one','workbook_one_id')
	workbook_two_ids = fields.One2many('workbook_two','workbook_two_id')
	wrkbk_four_ids = fields.One2many('workbook_four_paper_board','wrkbk_four_id')
	wrkbk_six_ids = fields.One2many('workbook_six_die','wrkbk_six_id')
	wrkbk_color_bom_ids = fields.One2many('workbook_color_bom','wrkbk_color_id')
# Corrugation workbook for bill of materials
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
	part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")
	workbook_one_id = fields.Many2one('mrp.bom','Work Book Id')
# Rolls required workbook for bill of materials
class mrp_bom_custom_expert_workbook_two(models.Model):
	_name = 'workbook_two'
	material = fields.Char(string='Material')
	flute = fields.Selection([
            ('b', 'B Flute 2.5'),
            ('e', 'E Flute 1.5'),
            ('c', 'C Flute 3.5'),
            ],default='', string="Flute")
	reel_size = fields.Float(string='Reel Size')
	required_quantity  = fields.Float(string='Required Quantity')
	part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")

	workbook_two_id = fields.Many2one('mrp.bom','Work Book Id')


# paper/board workbook for bill of materials
class workbook_four_paper_board(models.Model):
	_name = 'workbook_four_paper_board'
	mrp_reel = fields.Float(string='Reel')
	mrp_cutting = fields.Float(string='Cutting')
	mrp_cut_width = fields.Float(string='Cut Width')
	mrp_cut_height = fields.Float(string='Cut Height')
	#mrp_cut_height_printed = fields.Float(string='Cut Height')
	mrp_type = fields.Selection([
            ('a', 'Packets'),
            ('b', 'Sheet'),
            ],default='', string="Type")
	mrp_grams = fields.Float(string='Grams')
	mrp_fac = fields.Integer(string='Fac')
	mrp_nos = fields.Float(string='Nos')
	mrp_filter = fields.Char(string='Filter')
	p_mrp_nos = fields.Float(string='Printed Sheet Nos')
	p_mrp_filter = fields.Char(string='Filter')
	p_mrp_ups = fields.Char(string='UPS')
	p_mrp_brand = fields.Char(string='Brand')
	wrkbk_four_id = fields.Many2one('mrp.bom','Work Book Id')

class workbook_six_die(models.Model):
	_name = 'workbook_six_die'
	mrp_die_number = fields.Char(string='Die Number')
	mrp_die_type = fields.Selection([
            ('a', 'Old'),
            ('b', 'New'),
            ],default='', string="Die Type")
	mrp_die_loc = fields.Char(string="Die Location")
	mrp_die_remarks = fields.Text(string="Remarks")
	mrp_die_as_per = fields.Char(string="Die as Per")
	wrkbk_six_id = fields.Many2one('mrp.bom','Work Book Id')	

class workbook_corrugation_one(models.Model):
	_name = 'workbook_corrugation_one'
	mrp_reel_size = fields.Float(string='Reel Size')
	mrp_cutting_size = fields.Float(string='Cutting Size')
	mrp_fact = fields.Float(string='Fact')
	mrp_pcs = fields.Float(string='PCS')
	mrp_ply = fields.Float(string='Ply')
	mrp_act_reel_size = fields.Float(string='Act Reel Size')
	mrp_prod_length = fields.Float(string='Product Length')
	mrp_prod_height = fields.Float(string='Product Height')
	mrp_prod_width = fields.Float(string='Product Width')
	mrp_ups_desc = fields.Char(string='UPS Desc')
	mrp_part_desc = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Part Desc")
	mrp_sheets_qty = fields.Float(string='Sheets Quantity')
	mrp_job_qty = fields.Float(string='Job Quantity')
	wrkbk_corrugation_id = fields.Many2one('mrp.bom','Work Book Id')

# color workbook for bill of materials
class workbook_color_bom(models.Model):
	_name = 'workbook_color_bom'
	mrp_color = fields.Char(string='Color')
	mrp_quantity = fields.Float(string='Quantity')
	mrp_remarks = fields.Text(string='Remarks')
	side = fields.Selection([
			('sideone', 'Side 1'),
			('top', 'Top'),
			('front', 'Front'),
			('number', 'Number'),
			('sidetwo', 'Side 2'),
			('bottom', 'Bottom'),
			('back', 'Back'),
			('filter', 'Filter'),
			],default='', string="Side")
	wrkbk_color_id = fields.Many2one('mrp.bom','Work color Id')