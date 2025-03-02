import os
import xml.etree.ElementTree as ET
import argparse

def extract_notes_from_enex(enex_file):
    """Extracts notes from an Evernote ENEX file and returns them as a list of (title, content) tuples."""
    notes = []
    tree = ET.parse(enex_file)
    root = tree.getroot()

    for note in root.findall(".//note"):
        title = note.find("title").text if note.find("title") is not None else "Untitled"
        content = note.find("content").text if note.find("content") is not None else "<p>No content</p>"
        notes.append((title, content))

    return notes

def process_enex_files(input_dir, output_dir):
    toc_file = os.path.join(output_dir, "ToC.html")
    individual_notes_dir = os.path.join(output_dir, "individual_notes")

    # Ensure output directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(individual_notes_dir, exist_ok=True)

    with open(toc_file, "w", encoding="utf-8") as out:
        out.write("""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Evernote Notes</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&family=Open+Sans:wght@300;400&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Open Sans', sans-serif;
                    max-width: 1000px;
                    margin: 20px auto;
                    background: #f9f9f9;
                    padding: 20px;
                    color: #333;
                }
                h1 {
                    font-family: 'Roboto', sans-serif;
                    color: #444;
                    text-align: center;
                    font-weight: 500;
                    border-bottom: 3px solid #4CAF50;
                    padding-bottom: 15px;
                    margin-bottom: 30px;
                }
                .toc {
                    margin-bottom: 30px;
                    font-size: 18px;
                    list-style-type: none;
                    padding: 0;
                }
                .toc li {
                    margin-bottom: 12px;
                }
                .toc a {
                    text-decoration: none;
                    font-weight: 500;
                    color: #007BFF;
                    transition: color 0.3s ease, text-decoration 0.3s ease;
                }
                .toc a:hover {
                    color: #0056b3;
                    text-decoration: underline;
                }
                .note {
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    margin-bottom: 30px;
                    transition: all 0.3s ease;
                }
                .note:hover {
                    transform: scale(1.02);
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                }
                .note-title {
                    font-size: 24px;
                    font-weight: 500;
                    color: #4CAF50;
                    margin-bottom: 10px;
                }
                .note-content {
                    line-height: 1.8;
                    color: #555;
                    font-size: 16px;
                }
                .note-footer {
                    text-align: center;
                    font-size: 14px;
                    color: #777;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Evernote Notes</h1>
            <h2>Table of Contents</h2>
            <ul class="toc">
        """)

        for filename in os.listdir(input_dir):
            if filename.endswith(".enex"):
                input_filepath = os.path.join(input_dir, filename)
                notes = extract_notes_from_enex(input_filepath)

                individual_html_file = os.path.join(individual_notes_dir, f"{filename.replace('.enex', '.html')}")
                with open(individual_html_file, "w", encoding="utf-8") as individual_out:
                    individual_out.write(f"""
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <title>{filename}</title>
                        <style>
                            body {{
                                font-family: 'Open Sans', sans-serif;
                                max-width: 800px;
                                margin: 20px auto;
                                background: #f9f9f9;
                                padding: 20px;
                                color: #333;
                            }}
                            h1 {{
                                font-family: 'Roboto', sans-serif;
                                color: #444;
                                text-align: center;
                                font-weight: 500;
                                border-bottom: 3px solid #4CAF50;
                                padding-bottom: 15px;
                                margin-bottom: 30px;
                            }}
                            .note-title {{
                                font-size: 24px;
                                font-weight: 500;
                                color: #4CAF50;
                                margin-bottom: 10px;
                            }}
                            .note-content {{
                                line-height: 1.8;
                                color: #555;
                                font-size: 16px;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>{filename}</h1>
                    """)

                    for title, content in notes:
                        individual_out.write(f"""
                        <div class="note">
                            <div class="note-title">{title}</div>
                            <div class="note-content">{content}</div>
                        </div>
                        """)

                    individual_out.write("</body></html>")

                out.write(f'<li><a href="individual_notes/{filename.replace(".enex", ".html")}">{filename}</a></li>\n')

        out.write("<h2>Notes Content</h2>")
        for filename in os.listdir(input_dir):
            if filename.endswith(".enex"):
                input_filepath = os.path.join(input_dir, filename)
                notes = extract_notes_from_enex(input_filepath)

                for title, content in notes:
                    out.write(f"""
                    <div class="note">
                        <div class="note-title">{title}</div>
                        <div class="note-content">{content}</div>
                    </div>
                    """)

        out.write("""
            </ul>
            <div class="note-footer">
                <p>Generated by Python Script | Evernote Notes</p>
            </div>
        </body>
        </html>
        """)

    print(f"✅ All ENEX files have been processed and saved to: {output_dir}")
    print(f"✅ Table of Contents saved as: {toc_file}")
    print(f"✅ Individual notes saved in: {individual_notes_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Evernote .enex files to styled HTML.")
    parser.add_argument("--input-dir", required=True, help="Directory containing .enex files")
    parser.add_argument("--output-dir", required=True, help="Directory to save output HTML files")

    args = parser.parse_args()
    process_enex_files(args.input_dir, args.output_dir)
