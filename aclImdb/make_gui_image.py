"""
make_gui_image.py
Generates a crisp visual showcase image of the CineSense Streamlit GUI
to embed in the presentation.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 6.2), dpi=160)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")
ax.axis("off")

# Header banner
header = patches.FancyBboxPatch((0.03, 0.82), 0.94, 0.15, boxstyle="round,pad=0.02", facecolor="#0f172a", edgecolor="#1e293b")
ax.add_patch(header)
ax.text(0.06, 0.90, "CineSense: Movie Review Sentiment Analysis", color="white", fontsize=14, fontweight="bold")
ax.text(0.06, 0.85, "NLP Semester 5 Project  |  TF-IDF + Linear SVM  |  89.90% Test Accuracy", color="#94a3b8", fontsize=9.5)

# Sidebar mockup
sidebar = patches.FancyBboxPatch((0.03, 0.04), 0.25, 0.75, boxstyle="round,pad=0.015", facecolor="#ffffff", edgecolor="#e2e8f0")
ax.add_patch(sidebar)
ax.text(0.05, 0.73, "Quick Samples", color="#0f172a", fontsize=10, fontweight="bold")
btn1 = patches.FancyBboxPatch((0.045, 0.62), 0.22, 0.08, boxstyle="round,pad=0.01", facecolor="#f1f5f9", edgecolor="#cbd5e1")
ax.add_patch(btn1)
ax.text(0.06, 0.655, "Positive Sample", color="#0f172a", fontsize=8.5, fontweight="bold")
btn2 = patches.FancyBboxPatch((0.045, 0.51), 0.22, 0.08, boxstyle="round,pad=0.01", facecolor="#f1f5f9", edgecolor="#cbd5e1")
ax.add_patch(btn2)
ax.text(0.06, 0.545, "Negative Sample", color="#0f172a", fontsize=8.5, fontweight="bold")
btn3 = patches.FancyBboxPatch((0.045, 0.40), 0.22, 0.08, boxstyle="round,pad=0.01", facecolor="#f1f5f9", edgecolor="#cbd5e1")
ax.add_patch(btn3)
ax.text(0.06, 0.435, "Tricky Negation", color="#0f172a", fontsize=8.5, fontweight="bold")

# Main input box
input_box = patches.FancyBboxPatch((0.31, 0.52), 0.66, 0.27, boxstyle="round,pad=0.015", facecolor="#ffffff", edgecolor="#cbd5e1")
ax.add_patch(input_box)
ax.text(0.33, 0.74, "Enter Movie Review:", color="#64748b", fontsize=9, fontweight="bold")
sample_text = "The movie was fantastic! The acting was superb and the story kept me hooked throughout."
ax.text(0.33, 0.65, sample_text, color="#0f172a", fontsize=9.5, style="italic")

# Predict button
btn_pred = patches.FancyBboxPatch((0.31, 0.43), 0.22, 0.065, boxstyle="round,pad=0.01", facecolor="#2563eb", edgecolor="#1d4ed8")
ax.add_patch(btn_pred)
ax.text(0.34, 0.455, "Analyze Sentiment", color="white", fontsize=9.5, fontweight="bold")

# Result card (Positive)
res_card = patches.FancyBboxPatch((0.31, 0.16), 0.66, 0.24, boxstyle="round,pad=0.015", facecolor="#f0fdf4", edgecolor="#22c55e", linewidth=1.5)
ax.add_patch(res_card)
ax.text(0.34, 0.33, "PREDICTED POLARITY", color="#64748b", fontsize=8.5, fontweight="bold")
ax.text(0.34, 0.25, "Positive Sentiment", color="#15803d", fontsize=15, fontweight="bold")
ax.text(0.72, 0.33, "MODEL CONFIDENCE", color="#64748b", fontsize=8.5, fontweight="bold")
ax.text(0.72, 0.25, "81.3%", color="#0f172a", fontsize=16, fontweight="bold")

# Progress bar
prog_bg = patches.Rectangle((0.34, 0.19), 0.60, 0.025, facecolor="#e2e8f0")
ax.add_patch(prog_bg)
prog_fg = patches.Rectangle((0.34, 0.19), 0.60 * 0.813, 0.025, facecolor="#22c55e")
ax.add_patch(prog_fg)

# Diagnostic tabs preview
ax.text(0.31, 0.08, "Tabs: [ Linguistic Preprocessing ]  [ NLP Pipeline Inspection ]  [ Evaluation Evidence ]", color="#64748b", fontsize=9)
ax.text(0.31, 0.04, "Shielded Negations Verified: not, no, never, didn't preserved without data leakage.", color="#15803d", fontsize=8.5, style="italic")

plt.tight_layout()
plt.savefig("gui_showcase.png", dpi=180, bbox_inches="tight")
print("gui_showcase.png generated successfully!")
