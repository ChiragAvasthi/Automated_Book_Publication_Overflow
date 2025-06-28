# 📘 AI Chapter Spinner

**AI Chapter Spinner** is an intelligent web application that extracts textbook chapters from live URLs and transforms them using AI-powered rewriting and review. Designed for educators, publishers, and content creators, it streamlines content modernization with precision, quality control, and version tracking.

---

## 🚀 Features

- 🔍 **Live Web Scraping** – Extracts chapter content from any webpage in real-time  
- ♻️ **AI-Powered Rewriting** – Rewrites text while preserving original meaning  
- 🧠 **Smart Reviewing** – Uses AI to ensure clarity, tone, and accuracy  
- 🗂️ **Version Control** – Save, track, and revert chapter versions effortlessly  
- 🖼️ **Screenshot Capture** – One-click UI or content snapshot saving  
- 🎨 **Tailwind UI** – Clean, responsive, modular design for smooth UX

---

## 🛠 Tech Stack

- **Frontend:** Tailwind CSS, Jinja2 Templates  
- **Backend:** Python (Flask or FastAPI), OpenAI API  
- **Modules:** Web Scraper, AI Writer/Reviewer, Versioning, Screenshot  
- **Storage:** Local files / ChromaDB

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ai-chapter-spinner.git
cd ai-chapter-spinner

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create a .env file in the root directory with your OpenAI key
echo "OPENAI_API_KEY=your_openai_api_key" > .env

# 5. Run the app
python app.py

# 6. Open in your browser
# Visit http://localhost:5000
