# Text Summarization System

A web-based Text Summarization System developed using Python, Flask, and Natural Language Processing techniques. The application accepts a long text and generates a concise summary by identifying important sentences.

## Features

* User-friendly web interface
* Accepts long text as input
* Automatically generates a concise summary
* Uses Natural Language Processing techniques
* Extractive text summarization
* Flask-based web application
* Displays the generated summary directly on the webpage

## Technologies Used

* Python
* Flask
* Sumy
* NLTK
* HTML
* CSS
* Natural Language Processing (NLP)

## Project Structure

```text
Text-Summarization-System/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

If required, download the NLTK tokenizer:

```bash
python -c "import nltk; nltk.download('punkt')"
```

## Running the Application

Run:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## How It Works

1. The user enters a long text.
2. The text is sent to the Flask backend.
3. The application divides the text into sentences.
4. The LSA summarization algorithm identifies important sentences.
5. The selected sentences are combined into a summary.
6. The summary is displayed on the webpage.

## Example

### Input

```text
Natural Language Processing is an important field of Artificial Intelligence.
It allows computers to understand and process human language.
NLP is used in search engines, chatbots, translation systems and many other applications.
Text summarization is one of the important applications of NLP.
It helps users understand large documents quickly by producing shorter versions of the original text.
```

### Output

```text
Natural Language Processing is an important field of Artificial Intelligence.
NLP is used in search engines, chatbots, translation systems and many other applications.
It helps users understand large documents quickly by producing shorter versions of the original text.
```

## Applications

Text summarization can be used for:

* News article summarization
* Research paper summarization
* Document summarization
* Report summarization
* Educational content summarization
* Business report analysis

## Purpose

This project demonstrates the application of Natural Language Processing and Text Analysis techniques for automatically generating concise summaries from lengthy text.

## License

This project is licensed under the MIT License.
