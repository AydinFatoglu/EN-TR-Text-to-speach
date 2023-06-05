# Multilingual Text-to-Speech

The Multilingual Text-to-Speech application is a program that converts text input into speech output in various languages. It uses the gTTS (Google Text-to-Speech) library to generate speech from the entered text and the ffplay command-line audio player to play the generated speech.

## Features

- Text input: Enter the desired text to be converted into speech.
- Language selection: Choose the language for the speech output from the available options (English and Turkish by default).
- Speech generation: The program utilizes gTTS to generate the speech audio file based on the entered text and selected language.
- Playback: The generated speech is played using the ffplay command-line audio player.
- Stop functionality: The program provides a stop button to halt the speech playback if needed.
- Right-click context menu: The input text box supports cut, copy, paste, and select all operations through a right-click context menu.
- Text wrapping and scrollbars: The input text box wraps the entered text at word boundaries and includes scrollbars for easy navigation.

## Prerequisites

- Python 3.x: Make sure you have Python 3.x installed on your system.
- gTTS: Install the gTTS library using pip: `pip install gtts`.
- ffplay: The ffplay command-line audio player should be accessible from the command line. Install FFmpeg or the appropriate package for your operating system to get ffplay.

## Usage

1. Clone the repository or download the source code to your local machine.
2. Install the required dependencies (gTTS and FFmpeg if not already installed).
3. Run the program: `python text_to_speech.py`.
4. Enter the desired text in the input box.
5. Select the language from the dropdown menu.
6. Click the "Submit" button to generate and play the speech.
7. To stop the speech playback, click the "Stop" button.
8. Right-click inside the input box for additional options like cut, copy, paste, and select all.

## Limitations

- The program requires a working internet connection to use the gTTS library for speech generation.
- Make sure the ffplay command-line audio player is installed and accessible for speech playback.
- Some languages may not be supported or may have limitations with the gTTS library.

## Contributing

Contributions to the Multilingual Text-to-Speech program are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
