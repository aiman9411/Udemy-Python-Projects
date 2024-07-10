# Pomodoro Timer

## Introduction
The Pomodoro Timer is a simple, yet effective time management tool built with Python and Tkinter. It helps you to utilize the Pomodoro Technique, which breaks work into intervals, traditionally 25 minutes in length, separated by short breaks. This method is proven to improve productivity by maintaining a high level of concentration.

## Features
- **Customizable Times**: Set work, short break, and long break durations.
- **Visual and Textual Countdown**: Displays time remaining in an easy-to-read format.
- **Automatic Session Transitions**: Automatically switches between work and break periods.
- **Progress Tracking**: Shows checkmarks for completed work periods.

## Requirements
- Python 3.x
- Tkinter library (usually comes with Python)
- PIL library for image handling

## Setup and Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. **Install PIL:**
   - The Python Imaging Library (PIL) is required for handling images. It can be installed via pip if not already included in your Python installation.
   ```bash
   pip install pillow
   ```

3. **Add your own tomato image:**
   - Ensure you have a `tomato.png` image in the project directory. This image is used as the background for the timer.

## Running the Application
To run the Pomodoro Timer, execute the following command from the terminal:
```bash
python pomodoro.py
```

## How to Use
- **Start Timer**: Click the "Start" button to begin the Pomodoro cycle.
- **Reset Timer**: Use the "Reset" button to stop the current cycle and reset the timer.
