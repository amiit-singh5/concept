from gensim.models import Word2Vec

sentences = [["This", "is", "Amiit"]]

model = Word2Vec(
    sentences=sentences,
    vector_size=4,
    window=2,
    min_count=1,
    workers=1
)

# Get vector for a word
vector = model.wv["is"]
model.wv.most_similar("amiit")

print(vector)