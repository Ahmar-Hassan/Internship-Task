import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


nltk.download('stopwords')
nltk.download('wordnet')


faqs = {
"What is artificial intelligence": "Artificial Intelligence enables machines to mimic human intelligence.",
"What is machine learning": "Machine Learning allows systems to learn patterns from data.",
"What is deep learning": "Deep Learning uses deep neural networks for complex tasks."
}


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess(text):
words = nltk.word_tokenize(text.lower())
return " ".join([lemmatizer.lemmatize(w) for w in words if w.isalnum() and w not in stop_words])


questions = [preprocess(q) for q in faqs.keys()]
answers = list(faqs.values())


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)


print("--- Intelligent FAQ Chatbot ---")
user_input = preprocess(input("Ask your question: "))
user_vec = vectorizer.transform([user_input])


similarity = cosine_similarity(user_vec, X)
best_score = similarity.max()


if best_score < 0.3:
print("Sorry, I couldn't understand your question.")
else:
print("Answer:", answers[similarity.argmax()])