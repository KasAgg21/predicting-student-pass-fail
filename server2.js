const express = require("express");
const fileUploader = require("express-fileupload");
const { spawn } = require("child_process");

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(fileUploader());

app.listen(2006, function () {
    console.log("Server Live");
});

app.use(express.static("public"));

app.get("/", function (req, resp) {
    resp.sendFile(__dirname + "/public/index.html");
});

app.post("/submit", function (req, resp) {
    try {
        // Extract custom data from the request body
        const customData = {
            gender: req.body.gender,
            'race/ethnicity': req.body.ethnicity,
            'parental level of education': req.body.education,
            lunch: req.body.lunch,
            'test preparation course': req.body.testPrep
        };

        // Run the machine learning script using a child process
        console.log(`Executing: python3 scriptv2.py ${JSON.stringify(customData)}`);
const pythonScript = spawn("python3", ["scriptv2.py", JSON.stringify(customData)]);
        let result = '';

        // Capture the output of the script
        pythonScript.stdout.on("data", (data) => {
            result += data.toString();
            console.log(`Script output: ${data}`);
        });

        // Handle the end of the script execution
        pythonScript.on("close", (code) => {
            if (code === 0) {
                // Parse the result as JSON
                const parsedResult = JSON.parse(result);

                // Send the prediction back to the client
                resp.json({ prediction: parsedResult.prediction });
            } else {
                console.error(`Script execution failed with code ${code}`);
                resp.status(500).send("Internal Server Error");
            }
        });
    } catch (error) {
        console.error(error);
        resp.status(500).send("Internal Server Error");
    }
});
