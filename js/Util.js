const config = require("../config");
const path = require("path");
const fs = require("fs");


class Util
{
    static deleteOutputDirContents()
    {
        const outputDir = path.join(__dirname, "../", config.outputDir);
        const fileNamesInOutputDir = fs.readdirSync(outputDir);

        fileNamesInOutputDir.forEach(fileName =>
        {
            const filePath = path.join(outputDir, fileName);
            fs.unlinkSync(filePath);

            console.log(`Deleted ${config.outputDir}${fileName}!`);
        });
    }


    static convertArrayToReadableList(array)
    {
        if (array.length === 1)
            return array[0];

        if (array.length === 2)
            return `${array[0]} or ${array[1]}`;

        let string = "";
        array.forEach((v, i) =>
        {
            if (i === array.length - 1)
            {
                string += `or ${v}`;
            }
            else
            {
                string += `${v}, `;
            }
        });

        return string;
    }
}


module.exports = Util;