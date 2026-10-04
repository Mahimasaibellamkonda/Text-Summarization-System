from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words

app = Flask(__name__)


def summarize_text(text, sentences_count=3):

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    summarizer = LsaSummarizer()

    summarizer.stop_words = get_stop_words("english")

    summary = summarizer(
        parser.document,
        sentences_count
    )

    return " ".join(str(sentence) for sentence in summary)


@app.route("/", methods=["GET", "POST"])
def index():

    text = ""
    summary = ""

    if request.method == "POST":

        text = request.form.get("text", "").strip()

        if text:
            summary = summarize_text(text)

    return render_template(
        "index.html",
        text=text,
        summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)
