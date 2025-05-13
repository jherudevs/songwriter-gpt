import unicodedata

def normalize_text(text: str) -> str:
    """Convert smart quotes and non-ASCII characters to plain text."""
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
