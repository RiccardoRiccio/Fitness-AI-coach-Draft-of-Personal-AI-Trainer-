# Fitness AI Coach

This project is an AI application that utilizes Computer Vision technology, Pose Estimation, and Speech Recognition to provide accurate tracking of exercise repetitions during gym workouts. By doing so, it aims to enhance users' fitness routines.
## Demo

Watch the Fitness AI Coach gameplay demo below:

[![Fitness AI Coach Gameplay Demo](https://img.youtube.com/vi/T-vpCzy17ik/0.jpg)](https://youtu.be/T-vpCzy17ik "Fitness AI Coach Gameplay Demo")


## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Features](#features)
4. [Technologies Used](#technologies-used)


## Project Structure

- `main.py`: The main Python script that runs the Streamlit app.
- `ExerciseAiTrainer`: Pose estimation logic specific for each exercise.
- `AiTrainer_utils.py`: utils functions (resize image, calculate distance)
- `PoseModule2.py`: Body Pose estimation logic
- `requirements.txt`: List of Python libraries required for this project.
- mp3 files: Voice of the AI trainer
- mp4 files: Demo video of exercises (push up, curl, squat, etc)


## Getting Started

### Prerequisites

- Ensure you have Python installed on your machine.
- It's advisable to create a virtual environment to manage dependencies for this project.

### Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/RiccardoRiccio/Fitness-AI-coach.git


## How to Run

To run the application, open your terminal and execute the following command:

      ```bash
      streamlit run main.py


## Features

- **Exercise Tracking**: Accurately tracks repetitions for various exercises like Bicep Curls, Push-Ups, Squats, and Shoulder Press.
- **Voice Commands**: Uses speech recognition to start and stop the exercise tracking.

## Technologies Used

- **Computer Vision**: For pose estimation and exercise tracking.
- **Speech Recognition**: For voice-activated controls.
- **Streamlit**: For the web application interface.
- **Technologies**: Python, OpenCV, Streamlit, mediapipe, Speech Recognition API
