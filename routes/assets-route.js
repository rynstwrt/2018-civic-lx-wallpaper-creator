const express = require("express");
const router = express.Router();
const path = require("path");


router.get("/", (req, res) =>
{
    const assetName = req.query.fileName;
    if (!assetName)
        return res.send("no asset found");

    console.log("A" + assetName);

    const assetPath = path.join(__dirname, "../", "/tmp", assetName);
    console.log("B" + assetPath)
    res.sendFile(assetPath);
});


module.exports = router;