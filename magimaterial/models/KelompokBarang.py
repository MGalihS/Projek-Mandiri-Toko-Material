from unicodedata import name
from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'magimaterial.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('bahansemen', 'Semen'),
        ('paku', 'Paku'),
        ('peralon', 'Peralon'),
        ('genting','Genting'),
        ('cat','Cat'),
        ('batako','Batako'),
        ('alattukang','Alat Tukang'),
        ('alatbangunanrumah','Alat Bangunan Rumah'),
        ('lem','Lem'),
        ('bor','Bor')
    ], string='Kelompok Barang')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self):
        if (self.name == 'bahansemen'):
            self.kode_kelompok = 'sm1'
        elif (self.name == 'paku'):
            self.kode_kelompok = 'pk1'
        elif (self.name == 'peralon'):
            self.kode_kelompok = 'prln1'
        elif (self.name == 'genting'):
            self.kode_kelompok = 'gtg1'
        elif (self.name == 'cat'):
            self.kode_kelompok = 'ct1'
        elif (self.name == 'batako'):
            self.kode_kelompok = 'btk'
        elif (self.name == 'alattukang'):
            self.kode_kelompok = 'alttkng'
        elif (self.name == 'alatbangunanrumah'):
            self.kode_kelompok = 'ar'
        elif (self.name == 'lem'):
            self.kode_kelompok = 'lem'
        elif (self.name == 'bor'):
            self.kode_kelompok = 'bor'

    kode_rak = fields.Char(string='Kode Gudang')
    barang_ids = fields.One2many(comodel_name='magimaterial.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['magimaterial.barang'].search([('kelompokbarang_id','=',rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
            