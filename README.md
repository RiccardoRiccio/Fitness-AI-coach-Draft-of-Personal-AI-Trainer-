# Fitness AI Coach

This project is an AI application that utilizes Computer Vision technology, Pose Estimation, and Speech Recognition to provide accurate tracking of exercise repetitions during gym workouts. By doing so, it aims to enhance users' fitness routines.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Main Code](#main-code)
6. [Contributors](#contributors)

## Project Structure

- `main.py`: The main Python script that runs the Streamlit app.
- `ExerciseAiTrainer`: Pose estimation logic specific for each exercise.
- `AiTrainer_utils.py`: utils functions (resize image, calculate distance)
- `PoseModule2.py`: Body Pose estimation logic
- mp3 files: Voice of the AI trainer
- mp4 files: Demo video of exercises (push up, curl, squat, etc)
  
- `requirements.txt`: List of Python libraries required for this project.

## Getting Started

### Prerequisites

- Ensure you have Python installed on your machine.
- It's advisable to create a virtual environment to manage dependencies for this project.

### Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/RiccardoRiccio/Fitness-AI-coach.git