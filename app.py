import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

from scripts.ai_writer import spin_chapter
from scripts.ai_reviewer import review_chapter
from scripts.versioning import save_version, get_version, list_versions
from scripts.web_scraper import scrape_chapter
from scripts.visualization import get_text_stats
from scripts.metadata import get_about_info

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def editor():
    text, feedback, status, url, stats = "", "", "", "", {}
    selected_version = ""
    versions = list_versions()

    if request.method == "POST":
        action = request.form.get("action")
        text = request.form.get("text", "")
        url = request.form.get("url", "")
        selected_version = request.form.get("version_id", "")

        if action == "scrape" and url:
            try:
                text = scrape_chapter(url, "chapter.png")
                status = "✅ Chapter scraped and screenshot saved."
            except Exception as e:
                text, status = "", f"❌ Scraping failed: {e}"

        elif action == "spin":
            text = spin_chapter(text)
            status = "✅ Text spun successfully."

        elif action == "review":
            feedback = review_chapter(text)
            status = "✅ Review generated."

        elif action == "save":
            version_id = f"v{abs(hash(text)) % 100000}"
            status = save_version(text, version_id)
            versions = list_versions()

        elif action == "load":
            text = get_version(selected_version) or "⚠️ Version not found."
            status = f"📂 Loaded version {selected_version}"

    if text:
        stats = get_text_stats(text)

    about = get_about_info()
    return render_template("editor.html", text=text, feedback=feedback,
                           status=status, url=url, stats=stats,
                           versions=versions, selected_version=selected_version,
                           about=about)

if __name__ == "__main__":
    app.run(debug=True)
