import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required resources (only once)
nltk.download("punkt")
nltk.download("stopwords")

def parse_resume(text: str):
    # Tokenize text into words
    tokens = word_tokenize(text)

    # Convert to lowercase and filter out stopwords/punctuation
    stop_words = set(stopwords.words("english"))
    keywords = [t.lower() for t in tokens if t.isalpha() and t.lower() not in stop_words]

    return keywords

# Example usage
if __name__ == "__main__":
    sample_text = "Experienced Python developer with FastAPI and PostgreSQL skills."
    print(parse_resume(sample_text))
