# 🚀 GitHub Upload Guide for Movie Sentiment Analysis

This document provides exact, crystal-clear instructions on what to upload to GitHub and what to exclude, followed by the exact terminal commands to push your project.

---

## 📋 What to Upload vs. What NOT to Upload

| Folder / File | Action | Why? |
|---|:---:|---|
| **`app.py`** | ✅ **UPLOAD** | Main Streamlit web application. |
| **`train_model.py`** | ✅ **UPLOAD** | Complete model training & evaluation script. |
| **`requirements.txt`** | ✅ **UPLOAD** | Python dependencies required to run the project. |
| **`README.md`** | ✅ **UPLOAD** | Project documentation displayed on GitHub. |
| **`src/`** | ✅ **UPLOAD** | Modular source code (`data_loader.py`, `preprocessing.py`). |
| **`notebooks/`** | ✅ **UPLOAD** | All 5 academic Jupyter notebooks showing EDA & models. |
| **`models/sentiment_pipeline.joblib`** | ✅ **UPLOAD** | Pre-trained model weights (only 4.75 MB, well under GitHub's 100MB limit). Allows anyone to run the GUI immediately. |
| **`confusion_matrix.png`** | ✅ **UPLOAD** | Evaluation chart displayed in the README and Streamlit app. |
| **`Movie_Sentiment_Analysis_Presentation.pptx`**| ✅ **UPLOAD** | Your 14-slide PowerPoint deck for class and viva. |
| **`presentation_speaker_notes.md`** | ✅ **UPLOAD** | Slide-by-slide speaker script for viva preparation. |
| **`.gitignore`** | ✅ **UPLOAD** | Tells Git which large folders to ignore automatically. |
| ❌ **`train/` & `test/`** | 🚫 **DO NOT UPLOAD** | **Contains over 100,000 `.txt` files!** GitHub will freeze or reject the push if you attempt to upload 100k raw files. Anyone downloading the code can obtain the dataset via the official link in `README.md`. |
| ❌ **`.venv/`** | 🚫 **DO NOT UPLOAD** | Virtual environment directory with local machine paths. Others recreate it with `pip install -r requirements.txt`. |
| ❌ **`__pycache__/` & `*.pyc`** | 🚫 **DO NOT UPLOAD** | Temporary compiled Python bytecode. |

*(Note: Our updated `.gitignore` file automatically excludes `train/`, `test/`, and `.venv/` for you!)*

---

## 💻 Exact Terminal Commands to Push to GitHub

Open **PowerShell** or **Command Prompt** in this folder:

```powershell
cd "c:\Users\user\Desktop\SEM - 5 Subjects\NLP\project\movie sentiment analysis\aclImdb"
```

### Step 1: Initialize Git
```powershell
git init
```

### Step 2: Stage the Files (Safely respects `.gitignore`)
```powershell
git add .
```
*(You can verify staged files by running `git status`. You will see around 15 clean files, not 100,000 text files.)*

### Step 3: Create the Initial Commit
```powershell
git commit -m "Initial commit: Movie Sentiment Analysis NLP project with Streamlit GUI & Presentation"
```

### Step 4: Rename Branch to `main`
```powershell
git branch -M main
```

### Step 5: Link to Your GitHub Repository
Replace `<YOUR_GITHUB_REPO_URL>` with your actual repository link (e.g., `https://github.com/your-username/movie-sentiment-analysis.git`):
```powershell
git remote add origin <YOUR_GITHUB_REPO_URL>
```

### Step 6: Push to GitHub
```powershell
git push -u origin main
```

---
All set! Your GitHub repository will look clean, professional, and well-organized.
