# Windows Setup Instructions

## Prerequisites
- Python 3.11 or higher (download from https://www.python.org/)
- Windows 10 or later
- Webcam

## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MelihAydinYanibol/Meme-interactive-cam-test.git
   cd Meme-interactive-cam-test
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python maymun_test.py
   ```

## Troubleshooting

### If pip install fails:
- Update pip: `python -m pip install --upgrade pip`
- Try installing with pre-built wheels: `pip install --only-binary :all: opencv-python mediapipe`

### If webcam doesn't work:
- Ensure your webcam is connected and not in use by another application
- Check Windows camera permissions (Settings > Privacy > Camera)

### Dependencies
- **opencv-python 4.8.1.78**: Computer vision library for image processing
- **mediapipe 0.10.9**: MediaPipe for hand and face detection

## Features
- Detects hand gestures and face expressions via webcam
- Displays interactive meme overlays based on gestures
- Press 'Q' to quit the application
