import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox, filedialog
import webbrowser
import pyttsx3
import json
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import threading
import time
from PIL import Image, ImageTk

# ----------------- Utility Functions -----------------
def search_law(law_table, section_no):
    conn = sqlite3.connect("law_data.db")
    cur = conn.cursor()

    if law_table == "ipc":
        cur.execute("SELECT Section, section_title, section_desc FROM ipc WHERE Section = ?", (section_no,))
    elif law_table == "crpc":
        cur.execute("SELECT Section, section_title, section_desc FROM crpc WHERE Section = ?", (section_no,))
    else:
        conn.close()
        return "❌ Law not found."

    row = cur.fetchone()
    conn.close()

    if row:
        return f"{law_table.upper()} Section {row[0]} – {row[1]}\n\n{row[2]}"
    else:
        return "❌ Section not found."

def keyword_search(law_table, keyword):
    conn = sqlite3.connect("law_data.db")
    cur = conn.cursor()
    query = f"SELECT Section, section_title FROM {law_table} WHERE section_desc LIKE ?"
    cur.execute(query, ('%' + keyword + '%',))
    results = cur.fetchall()
    conn.close()

    if results:
        return "\n".join([f"🔹 Section {row[0]}: {row[1]}" for row in results])
    else:
        return "❌ No matches found."

def search_constitution(article_no):
    with open("constitution.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for art in data:
        if art['article'].lower() == article_no.lower():
            return f"Article {art['article']} - {art['title']}\n\n{art['text']}"
    return "❌ Article not found."

def export_text_to_pdf(text, filename="output.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    lines = text.split('\n')
    y = height - 50
    for line in lines:
        c.drawString(50, y, line)
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50
    c.save()

# ----------------- GUI App -----------------
app = tb.Window(themename="darkly")
app.title("📘 Personal Law Assistant")
app.geometry("1000x700")
app.state("zoomed")

# ----------------- Animated Background -----------------
canvas_bg = tk.Canvas(app, bg="#1e1e1e", highlightthickness=0)
canvas_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

circles = []
for i in range(40):
    x, y, r = (i * 70) % 1600, (i * 50) % 900, 100
    color = "#3a3a3c"
    circles.append(canvas_bg.create_oval(x, y, x + r, y + r, fill=color, outline=""))

def animate_background():
    while True:
        for circle in circles:
            canvas_bg.move(circle, 0, 1)
            coords = canvas_bg.coords(circle)
            if coords[1] > app.winfo_height():
                canvas_bg.move(circle, 0, -app.winfo_height())
        time.sleep(0.02)

threading.Thread(target=animate_background, daemon=True).start()

# ----------------- Title Animation -----------------
typing_label = tb.Label(app, text="", font=("Segoe UI", 24, "bold"), bootstyle="info")
typing_label.place(relx=0.5, rely=0.07, anchor="center")
heading_text = "⚖️ Personal Law Assistant"

def animate_text():
    for i in range(len(heading_text)+1):
        s = heading_text[:i]
        typing_label.config(text=s)
        time.sleep(0.05)

threading.Thread(target=animate_text, daemon=True).start()

# ----------------- Input Frame -----------------
frame = tb.Frame(app, bootstyle="dark")
frame.place(relx=0.5, rely=0.18, anchor="center", relwidth=0.8)
frame.configure(borderwidth=0)

law_var = tk.StringVar(value="ipc")
law_menu = tb.Combobox(frame, textvariable=law_var, values=["ipc", "crpc", "constitution"], width=12, bootstyle="primary")
law_menu.grid(row=0, column=0, padx=5, pady=10)

entry = tb.Entry(frame, font=("Segoe UI", 12), bootstyle="info")
entry.grid(row=0, column=1, padx=5, pady=10, sticky="ew")
entry.bind("<Return>", lambda event: search())
frame.columnconfigure(1, weight=1)

entry.configure(validate="focus", validatecommand=lambda: entry.after(100, lambda: entry.configure(bootstyle="info")))

# ----------------- Output Box -----------------
output_box = tk.Text(app, wrap="word", font=("Segoe UI", 11), bg="#2b2b2b", fg="white", insertbackground="white", relief="flat", bd=10)
output_box.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.85, relheight=0.35)
output_box.config(highlightbackground="#444", highlightcolor="#444")

# ----------------- Button Actions -----------------
def search():
    law_type = law_var.get().lower()
    query = entry.get().strip()
    if not query:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "❗ Please enter a section or keyword.")
        return
    if law_type == "constitution" and (query.isdigit() or query.lower().startswith("art")):
        result = search_constitution(query)
    elif law_type in ["ipc", "crpc"] and query.isdigit():
        result = search_law(law_type, query)
    else:
        result = keyword_search(law_type, query)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result)

def export():
    content = output_box.get(1.0, tk.END).strip()
    if not content:
        messagebox.showwarning("Empty", "Nothing to export.")
        return
    file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file:
        export_text_to_pdf(content, file)
        messagebox.showinfo("Success", "Exported to PDF!")

def open_kanoon():
    query = entry.get().strip()
    if query:
        url = f"https://indiankanoon.org/search/?formInput={query}"
        webbrowser.open(url)

def read_law():
    engine = pyttsx3.init()
    text = output_box.get(1.0, tk.END)
    engine.say(text)
    engine.runAndWait()

# ----------------- Sidebar and Icons -----------------
sidebar = tb.Frame(app, bootstyle="dark", width=60)
sidebar.place(relx=0.01, rely=0.5, anchor="w")
sidebar.configure(borderwidth=0)

icons = [
    ("🔍", search),
    ("📄", export),
    ("🌐", open_kanoon),
    ("🔊", read_law)
]

for idx, (icon, cmd) in enumerate(icons):
    tb.Button(sidebar, text=icon, command=cmd, width=3, bootstyle="secondary-outline", padding=6).grid(row=idx, column=0, pady=10)

# ----------------- Rounded Icon Buttons -----------------
button_frame = tb.Frame(app)
button_frame.place(relx=0.5, rely=0.92, anchor="center", relwidth=0.9)
button_frame.columnconfigure((0, 1, 2, 3), weight=1)
button_frame.configure(borderwidth=0)

btn_search = tb.Button(button_frame, text="🔍 Search", command=search, bootstyle="success-outline", width=20)
btn_search.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btn_export = tb.Button(button_frame, text="📄 Export PDF", command=export, bootstyle="info-outline", width=20)
btn_export.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

btn_kanoon = tb.Button(button_frame, text="🌐 Indian Kanoon", command=open_kanoon, bootstyle="warning-outline", width=20)
btn_kanoon.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

btn_read = tb.Button(button_frame, text="🔊 Read Aloud", command=read_law, bootstyle="secondary-outline", width=20)
btn_read.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

app.mainloop()