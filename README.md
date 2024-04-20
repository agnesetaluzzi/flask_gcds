# Threddy

This is a simple Flask + HTMX demo of chatting with PDF files using the new OpenAI Assistants API.

## Quick Start

If you want to use your personal assistant, create a ```settings.json``` file with:
```
{
    "assistant_id": "<assistant_id>"
}
```
Otherwise a standard assistant will be created.

(Optional: create a virtual environment).

In the command line run:
```
$ pip install requirements.txt
$ export OPENAI_API_KEY=YOUR_API_KEY
$ flask run
```
