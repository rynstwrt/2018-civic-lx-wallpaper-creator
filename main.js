const config = require("./config");
const Util = require("./js/Util");
const ImageManager = require("./js/ImageManager");
const fs = require("fs");
const path = require("path");


async function run(inputFileName)
{
    const inputDirPath = path.join(__dirname, config.inputDir);
    const inputFilePath = path.join(inputDirPath, inputFileName);

    const outputBuffer = await ImageManager.resizeAndConvertFileIfNeeded(inputFilePath);
    if (!outputBuffer)
        return;

    const fileName = path.parse(inputFilePath).name;
    const outputFileExtension = config.outputImageFormat;
    const outputFilePath = path.join(__dirname, config.outputDir, `${fileName}${outputFileExtension}`);
    console.log(outputFilePath);
    fs.writeFileSync(outputFilePath, outputBuffer);
}


(async () =>
{
    if (config.clearOutputDirOnRun)
        Util.deleteOutputDirContents();

    const inputDirPath = path.join(__dirname, config.inputDir);
    const inputFiles = fs.readdirSync(inputDirPath);
    for (const v of inputFiles)
    {
        const i = inputFiles.indexOf(v);
        await run(v);
    }

    // await run(inputFiles[0]);
})();