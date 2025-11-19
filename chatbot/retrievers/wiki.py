import wikipedia

def get_wikipedia_summary(query):
    try:
        results = wikipedia.search(query)
        if results:
            page = wikipedia.page(results[0])
            return page.summary
        else:
            return ""
    except Exception:
        return ""
