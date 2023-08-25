from keras.datasets import reuters
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding,SimpleRNN
from keras.utils import to_categorical
maxitems = 10000
(train_data,train_lbl),(test_data,test_lbl) = reuters.load_data(num_words=maxitems)
max_len = 500
embedding_size = 100
train_data = pad_sequences(train_data,max_len)
test_data = pad_sequences(test_lbl,max_len)

train_lbl = to_categorical(train_lbl)
test_lbl = to_categorical(test_lbl)
model=Sequential([
    Embedding(max_len,embedding_size),
    SimpleRNN()
])
print(model.summary())