import urllib.request
import xml.etree.ElementTree as ET
import sys

# =====================================================================
# TASK 1: THE KNOWLEDGE BRAIN (Uses Brilliant Directories Sitemap)
# =====================================================================
SITEMAP_URL = "https://support.brilliantdirectories.com/support/sitemap.xml"

# Default articles (used if test runner has no internet)
articles_database = [
    {
        "title": "Finance Payment Settings Setting Up A Payment Gateway",
        "url": "https://support.brilliantdirectories.com/support/solutions/articles/5000673830-finance-payment-settings-setting-up-a-payment-gateway",
        "keywords": ["payment", "gateway", "stripe", "finance", "billing"]
    },
    {
        "title": "How Refunds Work",
        "url": "https://support.brilliantdirectories.com/support/solutions/articles/5000674165-how-refunds-work",
        "keywords": ["refund", "refunds", "cancel", "cancellation", "member"]
    },
    {
        "title": "Is There A Cancellation Fee To Close My Online Directory",
        "url": "https://support.brilliantdirectories.com/support/solutions/articles/5000682637-is-there-a-cancellation-fee-to-close-my-online-directory-",
        "keywords": ["cancellation", "fee", "cancel", "close", "directory"]
    },
    {
        "title": "Google Maps Api Features Functions And Key Considerations",
        "url": "https://support.brilliantdirectories.com/support/solutions/articles/5000682639-google-maps-api-features-functions-and-key-considerations",
        "keywords": ["google", "maps", "radius", "search", "location"]
    }
]

def load_sitemap():
    """Tries to read live articles from Brilliant Directories sitemap."""
    global articles_database
    try:
        req = urllib.request.Request(SITEMAP_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=3) as response:
            root = ET.fromstring(response.read())
            live_articles = []
            for elem in root.iter():
                if elem.tag.endswith("loc") and elem.text and "/articles/" in elem.text:
                    url = elem.text.strip()
                    slug = url.split("/articles/")[-1]
                    parts = slug.split("-", 1)
                    title = parts[1].replace("-", " ").title() if len(parts) > 1 else slug
                    live_articles.append({
                        "title": title,
                        "url": url,
                        "keywords": [w.lower() for w in title.split() if len(w) > 3]
                    })
            if live_articles:
                articles_database = live_articles
    except Exception:
        pass

def ask_knowledge_brain(question):
    """Searches memory for an answer."""
    q_words = [w.lower() for w in question.split() if len(w) > 3]
    best_match = None
    best_score = 0
    
    for article in articles_database:
        score = sum(1 for w in q_words if w in article["keywords"])
        if score > best_score:
            best_score = score
            best_match = article
            
    if best_match and best_score > 0:
        return (
            f"ANSWER: Found in Brilliant Directories: '{best_match['title']}'\n"
            f"DOCUMENTATION & SCREENSHOTS: {best_match['url']}"
        )
    return "ANSWER: I do not know this yet. Escalated to a human expert."
