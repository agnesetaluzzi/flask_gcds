## Quick Start

### Prerequisites
- Python 3.6 or higher
- OpenAI API Key

### Installation
Open a terminal and navigate to the project directory.

Optionally, create a virtual environment:
```
$ python -m venv venv
$ source venv/bin/activate
```

Install the dependencies and run the server:
```
$ pip install -r requirements.txt
$ export OPENAI_API_KEY=YOUR_API_KEY
$ flask run
```

## Example Usage
Here is an example of how to use the MemorAI Web App.

In the first image, during a chat with the assistant, the user uploads a PDF file and then provides incorrect information about the file content.
![First Image](images/Screenshot1.png)

In the image below, you can see the assistant correcting the user and providing the correct information, along with a rhyme to help the user remember the incorrect information they provided.
![Second Image](images/Screenshot2.png)

## Other Functionalities
This demo was developed in a short period of time and has some limitations.

The use of Whisper AI for speech transcription to make the spoken interaction with the assistant possible is not implemented in this version.

You can find a PoC of a Node.js server containing the PoC of the use of the Whisper AI API for audio transcription [here](https://github.com/agnesetaluzzi/whisperAPI_gdsc/). It provides a REST endpoint that accepts a POST request with an audio file and returns the transcription of the audio file.
