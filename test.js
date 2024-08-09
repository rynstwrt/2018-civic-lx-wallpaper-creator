const fs = require("fs");
const path = require("path");
const sharp = require("sharp");
const sharpBMP = require("sharp-bmp");


const INPUT_DIR = "./images/resized";
const OUTPUT_DIR = "./output/bmp";
const DELETE_OUTPUT_FILES_ON_RUN = true;


function deleteOutputDirContents()
{
    const outputDir = path.join(__dirname, OUTPUT_DIR);
    const fileNamesInOutputDir = fs.readdirSync(outputDir);

    fileNamesInOutputDir.forEach(fileName =>
    {
        const filePath = path.join(outputDir, fileName);
        fs.unlinkSync(filePath);

        console.log(`Deleted ${OUTPUT_DIR}/${fileName}!`);
    });
}


function convertJPGToBMP()
{

}


(async () =>
{
    if (DELETE_OUTPUT_FILES_ON_RUN)
        deleteOutputDirContents();

    const inputFileNames = fs.readdirSync(INPUT_DIR);

    for (const inputFileName of inputFileNames)
    {
        const inputFilePath = path.join(INPUT_DIR, inputFileName);
        const fileName = path.parse(inputFilePath).name;

        const image = sharp(inputFilePath);

        const outputFilePath = path.join(OUTPUT_DIR, `${fileName}.bmp`);
        await sharpBMP.sharpToBmp(image, outputFilePath);

        console.log(`Wrote to ${outputFilePath}!`);
    }
})();