from . import app
from .utils import write_qr, write_barcode, get_provided_barcodes, clean_barcodes
from flask import render_template, request


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html')


@app.route('/')
def index():
    barcode = None
    error_message = None
    data = request.args.get('data')
    barcode_type = request.args.get('barcode-type')
    provided_barcodes = get_provided_barcodes()

    if data is not None and barcode_type is not None:
        if barcode_type == 'qr':
            barcode = write_qr(data)
        else:
            barcode, error_message = write_barcode(barcode_type, data)

    return render_template('index.html', provided_barcodes=provided_barcodes, barcode=barcode, barcode_type=barcode_type, error_message=error_message)


@app.before_request
def index_before_request():
    clean_barcodes()