var express = require("express");
var fileuploader = require("express-fileupload");

var app = express();
app.use(express.urlencoded(true));
app.listen(2003, function () {
    console.log("Server Live");
});

app.use(express.static("public"));
app.use(fileuploader());

app.get("/", function (req, resp) {
    resp.sendFile(process.cwd() + "/public/index.html");
})
