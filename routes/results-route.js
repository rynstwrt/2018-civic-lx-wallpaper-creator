const express = require("express");
const router = express.Router();
const path = require("path");


router.get("/", (req, res) =>
{
    const filePathsString = req.query.filePathsString;

    const fileNames = JSON.parse(decodeURIComponent(filePathsString));
    console.log(fileNames);

    res.render(path.join(__dirname, "../", "public", "views", "results.pug"), { fileNames: fileNames });
});


module.exports = router;