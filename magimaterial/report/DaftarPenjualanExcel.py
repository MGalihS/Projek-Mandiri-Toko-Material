from odoo import api, fields, models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.magimaterial.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    #Laporan dalam 1 Sheet
    tgl_lap = fields.Date.today()
    
    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Penjualan Excel')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'No Nota')
        sheet.write(1, 1, 'Nama')
        sheet.write(1, 2, 'Tanggal Transaksi',)
        sheet.write(1, 4, 'Banyak Barang',)
        sheet.write(1, 5, 'Total Pembayaran')
        row = 2
        col = 0
        for obj in penjualan:
            col = 0
            sheet.write(row, col, obj.name)
            for nama in obj.nama_pembeli:
                sheet.write(row, col+1, str(obj.nama_pembeli))
            sheet.write(row, col+2, str(obj.tgl_penjualan))
            sheet.write(row, col+4, str(obj.qty))
            sheet.write(row, col+5, obj.total_bayar)
            row += 1