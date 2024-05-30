const express = require("express");
const multer = require("multer");
const amqp = require("amqplib");
const fs = require("fs");
const path = require("path");

const app = express();
const upload = multer({ dest: "uploads/" });

app.set("view engine", "ejs");

let connection, channel, processedData;
const queue = "data_mining_queue";

app.post("/upload", upload.single("csvfile"), async (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  const filePath = path.join(__dirname, req.file.path);
  const fileContent = fs.readFileSync(filePath, "utf8");

  try {
    // send file to queue
    await channel.sendToQueue(queue, Buffer.from(fileContent), {
      persistent: true,
    });

    fs.unlinkSync(filePath);

    res.render("index", {
      result:
        processedData ??
        "File uploaded successfully. Please wait for processing.",
    });
  } catch (error) {
    console.error("Error sending message to queue:", error);
    res.status(500).send("Error processing file.");
  }
});

app.get("/", (req, res) => {
  res.render("index", { result: processedData ?? "" });
});

app.listen(4000, () => {
  console.log("Server started on http://localhost:4000");
  connectRabbitMQ();
});

async function connectRabbitMQ() {
  try {
    connection = await amqp.connect("amqp://localhost");
    channelSetupAndConsumeData();
  } catch (error) {
    console.error("Error connecting to RabbitMQ:", error);
  }
}

async function channelSetupAndConsumeData() {
  channel = await connection.createChannel();
  // add queue
  await channel.assertQueue(queue, { durable: true });
  // consume data
  consumeData();
}

async function consumeData() {
  channel.consume(queue, (msg) => {
    if (msg) {
      processedData = `File processed by Eclat Algorithm: ${msg.content.toString()}`;
    }
  });
}
