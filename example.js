const fs = require("fs");
const axios = require("axios");
const dotenv = require("dotenv");
dotenv.config();

function encodeImage(filePath) {
  const bitmap = fs.readFileSync(filePath);
  return Buffer.from(bitmap).toString("base64");
}

async function generate(prompt, imagePath = null) {
  const url = "http://localhost:8080/completion";
  const headers = { "Content-Type": "application/json" };

  let data = {
    prompt: prompt,
    n_predict: 200,
    temperature: 0.1,
    stop: ["", "[/INST]"],
  };

  if (imagePath) {
    const encodedImage = encodeImage(imagePath);
    data.image_data = [{ data: encodedImage, id: 1 }];
  }

  try {
    const response = await axios.post(url, data, { headers: headers });
    return response.data; // Return the full response data
  } catch (error) {
    console.error("Error:", error.message);
  }
}

const prompt = "USER:[img-1] What is it on the image?\nASSISTANT:\n";

generate(
  prompt
  // "/home/random/Documents/7.png"
).then((response) => {
  console.log("Response:", response);
});
