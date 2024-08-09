const express = require("express");
const router = express.Router();
const fs = require("fs");
const path = require("path");


router.post("/", (req, res) =>
{
    if (!req.files || Object.keys(req.files).length === 0)
        return res.status(400).send("No files were uploaded.");

    let files = req.files["image-files"];
    if (!(files instanceof Array))
        files = [files];

    console.log(files);
    console.log(files[0]);

    const fileNames = [];
    for (let i = 0; i < files.length; ++i)
    {
        const file = files[i];
        console.log(file);
        const tempFilePath = file.tempFilePath;
        const tempFileName = path.parse(tempFilePath).name;
        fileNames.push(tempFileName);
    }

    const arrayString = encodeURIComponent(JSON.stringify(fileNames));
    console.log(arrayString);




    // const imageType = file.mimetype.replace('image/', '.')
    // const imagePath = file.tempFilePath + imageType
    // fs.renameSync(file.tempFilePath, imagePath)



    // const f = fs.readdirSync("/tmp");
    // console.log(f);

    res.redirect("/results?filePathsString=" + arrayString);

    // res.send("File uploaded!");
});


module.exports = router;