# GAN Learning Platform

Welcome to the **GAN Learning Platform**, an educational and interactive application designed to make Generative Adversarial Networks (GANs) more accessible and engaging. This project provides a simple interface for users to adjust GAN parameters, train the model, and generate black-and-white images.

---

<img width="955" alt="GAN" src="https://github.com/user-attachments/assets/92a29567-9332-4099-91de-c39be3d438c1" />


---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Folder Structure](#folder-structure)
6. [Technical Details](#technical-details)
7. [Optimization Tips](#optimization-tips)
8. [Future Improvements](#future-improvements)

---

## Introduction

This platform allows users to:
- Experiment with GAN parameters such as **learning rate** and **batch size**.
- Train a GAN model interactively.
- Generate and download images.
- View the last generated image on the platform.
- Track progress and points using a built-in leaderboard system.

---

## Features

1. **Interactive Web Interface**:
   - Adjustable learning rate and batch size.
   - Real-time training updates.

2. **Image Generation**:
   - Generate black-and-white images based on user inputs.
   - Download and view the last generated image.

3. **Leaderboard System**:
   - Track user progress and reward points for training completion.

4. **Customization**:
   - Modify GAN parameters for personalized experiments.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iamfahad43/GAN.git
   cd gan-learning-platform
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

4. Run the application:
   ```bash
   flask run
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

### Web Interface

![Web Interface Screenshot](GAN.png)

- **Learning Rate**: Input a value to define the step size for model optimization (e.g., 0.001).
- **Batch Size**: Specify the number of training samples per batch (e.g., 64).
- **Train GAN**: Start the training process and monitor real-time updates.
- **Text Input**: Describe the desired image for context-based generation.
- **Generate Image**: Create an image based on the input text and parameters.
- **Download Image**: Save the generated image locally.
- **View Last Generated Image**: See the most recent image output.

---

## Folder Structure

```
├── app.py                # Main application script
├── dcgan_model.py        # GAN model architecture and logic
├── templates/            # HTML files for web interface
│   ├── index.html        # Main page
│   ├── last_generated_image.html
├── static/               # Static files (CSS, JS, images)
├── migrations/           # Database migrations
├── requirements.txt      # Python dependencies
└── site.db               # SQLite database (auto-generated)
```

---

## Technical Details

- **Backend**: Flask framework for API and web services.
- **Frontend**: HTML and CSS for a user-friendly interface.
- **GAN Architecture**: A pre-trained DCGAN model with options for parameter tuning.
- **Database**: SQLite for storing GAN parameters and user progress.
- **Image Generation**: Utilizes the GAN model to create black-and-white images based on textual input.

---

## Optimization Tips

To improve the platform's performance and output quality:

1. **Experiment with Parameters**:
   - **Learning Rate**: Start with 0.001 and test values between 0.0001 and 0.005.
   - **Batch Size**: Try values like 16, 32, or 128 for better training speed.

2. **Enhance GAN Model**:
   - Add more layers to the generator and discriminator.
   - Use advanced optimizers like Adam or RMSprop.

3. **Data Augmentation**:
   - Include transformations like cropping or rotation to improve training data diversity.

4. **Logging**:
   - Integrate TensorBoard for visualizing training progress and losses.

---

## Future Improvements

- Add color image generation capabilities.
- Enable cloud-based training for faster processing.
- Incorporate pre-trained text-to-image models for enhanced results.
- Develop a more sophisticated leaderboard system with user authentication.

---
