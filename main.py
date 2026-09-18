from textblob import TextBlob

def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positive 😀"
    elif sentiment < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

    if __name__ == "__main__":
        print("Welcome to the AI Sentiment Analyzer!")
        while True:
            user_input = input("Enter a sentence (or type 'quit' to exit): ")

            if user_input.lower() == 'quit':
                break
            print(f"Sentiment: {analyze_sentiment(user_input)}\n")