# Evernote ENEX to HTML Converter  

Convert Evernote `.enex` files into beautifully styled HTML with a **Table of Contents** and **individual note pages**.  

## 🚀 Features  
- Parses and converts Evernote `.enex` files to HTML.  
- Generates a **Table of Contents (ToC)** linking to individual notes.  
- Preserves original filenames for easy reference.  
- Uses **modern fonts & styling** for readability.  
- Command-line support for flexible input/output directory selection.  

## 🛠 Installation  
Ensure you have **Python 3.x** installed, then clone the repository:  
```bash
git clone https://github.com/your-username/enex-to-html.git
cd enex-to-html
```

## 📌 Usage  
Run the script with your input and output directories:  
```bash
python3 convert_enex_to_html.py --input-dir "/path/to/enex/files" --output-dir "/path/to/output"
```

## 📂 Output Structure  
```
output-dir/
│── ToC.html          # Merged file with Table of Contents + all notes  
│── individual_notes/  # Folder containing separate HTML files per .enex  
│   ├── note1.html  
│   ├── note2.html  
│   ├── ...  
```

## 📝 Example  
After running the script, open `ToC.html` in your browser to view all notes in an organized format.

## 📚 License  
MIT License  

---
💡 **Tip:** Customize the CSS in the script to tweak the design as needed!

