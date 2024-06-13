const ImageFormat = require("./ImageFormat.js");
const sharp = require("sharp");


class ImageManager
{
    #dimensions;
    #format;
    #clearOutput


    constructor(imageDimensions, imageFormat, clearOutputFolder)
    {
        this.#dimensions = imageDimensions;
        this.#format = imageFormat;
        this.#clearOutput = clearOutputFolder;
    }


    async resizeImage()
    {

    }
}


module.exports = ImageManager;