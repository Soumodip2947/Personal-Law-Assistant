import sqlite3
import json

def search_law(law_table, section_no):
    conn = sqlite3.connect("law_data.db")
    cur = conn.cursor()

    if law_table == "ipc":
        cur.execute("SELECT Section, section_title, section_desc FROM ipc WHERE Section = ?", (section_no,))
    elif law_table == "crpc":
        cur.execute("SELECT Section, section_title, section_desc FROM crpc WHERE Section = ?", (section_no,))
    else:
        return "❌ Law not found."

    row = cur.fetchone()
    conn.close()

    if row:
        return f"{law_table.upper()} Section {row[0]} – {row[1]}\n\n{row[2]}"
    else:
        return "❌ Section not found."

def search_constitution(article_no):
    with open("constitution.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for art in data:
        if art['article'] == article_no:
            return f"Article {art['article']} - {art['title']}\n\n{art['text']}"
    return "❌ Article not found."

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