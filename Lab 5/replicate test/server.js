// Server.js

const express = require('express');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' }); // Images will be saved in the 'uploads' directory
require('dotenv').config();
const app = express();
const port = process.env.PORT || 3000;

const Replicate = require('replicate');
const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

app.use(express.static('public')); // Serve the HTML file

app.post('/predict', upload.single('image'), async (req, res) => {
  if (!req.file) {
    return res.status(400).send('No image uploaded.');
  }

  // Construct the URI for the uploaded image
  const imageUri = `${req.protocol}://${req.get('host')}/uploads/${req.file.filename}`;

  try {
    let prediction = await replicate.deployments.predictions.create(
      "stanleywalker1",
      "idd-lab5",
      {
        input: {
            scale: 10,
          input_image: imageUri, // Use the URI of the uploaded image
          negative_prompt: "a normal selfie",
          translation_prompts: "a photo of a man made of fruit",
          negative_prompt_alpha: 1,
          feature_injection_threshold: 0.8
        }
      }
    );

    prediction = await replicate.wait(prediction);
    res.json(prediction.output);
  } catch (error) {
    console.error('Error with the Replicate API:', error);
    res.status(500).send('Error processing the prediction.');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
