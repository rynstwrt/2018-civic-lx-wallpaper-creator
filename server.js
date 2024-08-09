// REQUIRES
const express = require("express");
const expressFileUpload = require("express-fileupload");
const path = require("path");


// CONSTANTS
const DEV_PORT = 3099;


// EXPRESS SETUP
const app = express();
app.set("view-engine", "pug")
app.use(express.static(path.join(__dirname, "/public")));
app.use(expressFileUpload({
    limits: { fileSize: 1024 * 1024 * 10 },
    useTempFiles: true,
    // tempFileDir: path.join(__dirname, "/tmp")
}));


// EXPRESS ROUTES SETUP
const homeRoute = require("./routes/home-route");
app.use("/", homeRoute);
app.use("/home", homeRoute);

app.use("/upload", require("./routes/upload-route"));

app.use("/assets", require("./routes/assets-route"));

app.use("/results", require("./routes/results-route"));

// START EXPRESS LISTENER
app.listen(DEV_PORT, () =>
{
    console.log(`2018 Honda Civic Wallpaper Util is listening on port ${DEV_PORT}`);
});