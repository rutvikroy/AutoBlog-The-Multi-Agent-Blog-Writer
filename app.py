from flask import Flask, render_template, request, jsonify, send_file
from main import crew
import markdown2
import io
from docx import Document
import os 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Just render the UI
    return render_template("index.html")

@app.route("/", methods=["POST"])
def generate_blog():
    try:
        data = request.get_json()
        topic = data.get("topic") if data else None

        if not topic:
            return jsonify({"error": "No topic provided"}), 400

        # Generate blog
        blog_content = crew.kickoff(inputs={"topic": topic}).raw

        # Remove leading/trailing triple backticks and "markdown" if present
        if blog_content.startswith("```"):
            blog_content = blog_content.strip("`")  # remove backticks
            # Also remove "markdown" if it was included in ```markdown
            if blog_content.lower().startswith("markdown"):
                blog_content = blog_content[len("markdown"):].lstrip()

        clean_blog_text = blog_content  # plain text for download
        blog_html = markdown2.markdown(clean_blog_text)  # HTML for frontend

        return jsonify({
            "topic": topic,
            "blog": blog_html,
            "blog_text": clean_blog_text  # send plain text for downloads
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional: backend Word download route if you want server-generated .docx
@app.route("/download-word", methods=["POST"])
def download_word():
    data = request.get_json()
    text = data.get("text", "")
    doc = Document()
    for para in text.split("\n\n"):
        doc.add_paragraph(para)
    f = io.BytesIO()
    doc.save(f)
    f.seek(0)
    return send_file(f, as_attachment=True, download_name="blog.docx", mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


# Use Azure Web Apps PORT env variable for deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)