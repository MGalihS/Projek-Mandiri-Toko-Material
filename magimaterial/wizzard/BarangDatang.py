from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'magimaterial.barangdatang'

    barang_id = fields.Many2one(comodel_name='magimaterial.barang', string='Nama Barang', required=True)
    jumlah = fields.Integer(
        string='Jumlah', required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['magimaterial.barang'].search([('id', '=', line.barang_id.id)]).write(
                {'stok': line.barang_id.stok +  line.jumlah}
            )