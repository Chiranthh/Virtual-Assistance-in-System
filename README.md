# Virtual-Assistance-in-System
# Hash - AI Voice Assistant 🔊

Hash is a Python-based AI voice assistant that helps users perform various tasks through voice commands. It can open applications, search the web, fetch Wikipedia summaries, play music, tell the time, and even send emails.

## Features ✨
- **Voice Recognition**: Uses SpeechRecognition to process user commands.
- **Text-to-Speech**: Uses pyttsx3 for voice responses.
- **Web Search**: Opens Google searches and Wikipedia results.
- **Application Launcher**: Opens Chrome, Notepad, Calculator, Paint, and more.
- **Email Sending**: Sends emails via Gmail (SMTP).
- **Music Player**: Plays music from a predefined directory.
- **Dynamic Energy Threshold**: Improves speech recognition accuracy.

## Installation 🛠
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/hash-ai-voice-assistant.git
   cd hash-ai-voice-assistant
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the assistant:
   ```sh
   python hash.py
   ```

## Dependencies 📦
Ensure you have the following Python packages installed:
- `pyttsx3`
- `SpeechRecognition`
- `wikipedia`
- `pyaudio`

## Usage 🎙
- Say **"open Chrome"** to launch Chrome.
- Say **"search Python tutorials"** to perform a Google search.
- Say **"wikipedia Elon Musk"** to get a Wikipedia summary.
- Say **"play music"** to play your favorite songs.
- Say **"what's the time"** to get the current time.
- Say **"email to [recipient]"** and dictate your message.
