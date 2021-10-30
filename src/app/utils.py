import barcode, qrcode, time
from secrets import token_hex
from os import path, listdir, remove, stat
from barcode.writer import ImageWriter


BASE_DIR = path.abspath(path.dirname(__file__))
IMAGES_DIR = path.abspath(path.join(BASE_DIR, 'static', 'images')).replace('\\', '/')


def write_barcode(barcode_type: str, data: str) -> str:
    try:
        filename = None
        error_message = None
        bc = barcode.get(barcode_type, data, writer=ImageWriter())
        filename = f'{barcode_type}-{token_hex(3)}'
        bc.save(f'{IMAGES_DIR}/{filename}')
    except Exception as e:
        error_message = e.__str__()

    return filename, error_message


def write_qr(data: str) -> str:
    filename = f'QR-{token_hex(3)}'
    qr = qrcode.make(data)
    qr.save(f'{IMAGES_DIR}/{filename}.png')

    return filename


def get_provided_barcodes() -> str:
    return barcode.PROVIDED_BARCODES


def clean_barcodes() -> None:
    one_day_ago = time.time() - 86400

    for barcode in listdir(IMAGES_DIR):
        file_path = path.join(IMAGES_DIR, barcode)

        if stat(file_path).st_mtime <= one_day_ago:
            remove(file_path)