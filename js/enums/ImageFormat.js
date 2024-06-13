class ImageFormat
{
    static #JPG = ".jpg";
    static #BMP = ".bmp";

    static get JPG () { return this.#JPG }
    static get BMP () { return this.#BMP }
}


module.exports = ImageFormat;