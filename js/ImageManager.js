const config = require("../config");
const Util = require("./Util");
const ImageFormat = require("./enums/ImageFormat");
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");


const ACCEPTED_INPUT_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".bmp"];


class ImageManager
{

    static async resizeAndConvertFileIfNeeded(inputFilePath)
    {
        const inputFileName = path.parse(inputFilePath).name;
        const inputFileExtension = path.extname(inputFilePath);
        const relativePath = `${config.inputDir}${inputFileName}${inputFileExtension}`;

        if (!ACCEPTED_INPUT_IMAGE_EXTENSIONS.includes(inputFileExtension.toLowerCase()))
        {
            const acceptedFileTypesString = Util.convertArrayToReadableList(ACCEPTED_INPUT_IMAGE_EXTENSIONS);
            return console.error(`Could not load ${relativePath}! File extension must be ${acceptedFileTypesString}.`);
        }

        let buffer = fs.readFileSync(inputFilePath);

        const imageMetadata = await sharp(buffer).metadata();
        const imageDimensions = [imageMetadata.width,  imageMetadata.height];
        if (imageDimensions[0] !== config.resizedImageDimensions[0] || imageDimensions[1] !== config.resizedImageDimensions[1])
        {
            buffer = await sharp(buffer).resize({
                width: config.resizedImageDimensions[0],
                height: config.resizedImageDimensions[1],
                fit: config.resizeImageFit,
                position: config.resizePosition
            }).toBuffer();

            console.log(`Resized ${relativePath} to [${config.resizedImageDimensions.toString()}]!`);
        }
        else
        {
            console.log(`Skipped resize for ${relativePath} because it already has the correct dimensions!`);
        }

        const inputImageFormat = ImageFormat[inputFileExtension.replace(".", "").toUpperCase()];
        if (config.outputImageFormat !== inputImageFormat)
        {
            buffer = ImageManager.convertImageFormat(buffer, inputImageFormat, config.outputImageFormat);
            console.log(`Converted ${relativePath} to ${config.outputImageFormat}!`);
        }
        else
        {
            console.log(`Skipped format conversion for ${relativePath} because it is already a ${config.outputImageFormat} file!`);
        }

        return buffer;
    }



    static #convertJPGToBMP(buffer)
    {
        // TODO:
        return buffer;
    }


    static #convertBMPToJPG(buffer)
    {
        // TODO:
        return buffer;
    }


    static convertImageFormat(buffer, inputFormat, outputFormat)
    {
        if (inputFormat === ImageFormat.JPG && outputFormat === ImageFormat.BMP)
            return this.#convertJPGToBMP(buffer);
        else if (inputFormat === ImageFormat.BMP && outputFormat === ImageFormat.JPG)
            return this.#convertBMPToJPG(buffer);
    }
}


module.exports = ImageManager;