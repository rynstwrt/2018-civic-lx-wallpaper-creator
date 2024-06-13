class ImageFormat
{
    static #JPG = 0;
    static #BMP = 1;

    static get JPG () { return this.#JPG }
    static get BMP () { return this.#BMP }
}


module.exports = ImageFormat;