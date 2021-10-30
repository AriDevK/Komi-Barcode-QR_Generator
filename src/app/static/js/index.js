let btnCopyBarcode = document.querySelector('#btn-copy-barcode');
let staticModal = document.querySelector('#staticBackdrop');
let myModal = new bootstrap.Modal(staticModal, {});


window.addEventListener('load', () => {
    myModal.toggle()
});


btnCopyBarcode.addEventListener('click', async () => {
    const barcode = document.querySelector('#barcode').src;

    const request = await fetch(barcode);
    const blob = await request.blob();

    await navigator.clipboard.write([
        new ClipboardItem({
            'image/png': blob
        })
    ]);
});
