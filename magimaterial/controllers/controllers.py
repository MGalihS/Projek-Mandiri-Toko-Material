from odoo import http, models, fields
from odoo.http import request
import json


class magimaterial(http.Controller):
    @http.route('/magimaterial/getbarang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        # Mengambil semua barang dari table barang
        barang = request.env['magimaterial.barang'].search([])
        isi = []

        for bb in barang:
            isi.append({
                'nama_barang': bb.name,
                'harga_jual': bb.harga_jual,
                'stok': bb.stok
            })
        
        return json.dumps(isi)
    
    @http.route('/magimaterial/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['magimaterial.supplier'].search([])
        sup = []

        for s in supplier:
            sup.append({
                'nama_perusahaan': s.name,
                'alamat': s.alamat,
                'no_telepon': s.no_telp,
                'barang_id': s.barang_id[0].name
            })
        
        return json.dumps(sup)