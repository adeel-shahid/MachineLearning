from keras.datasets import reuters,imdb
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding,SimpleRNN,Dense
from keras.utils import to_categorical
from keras.utils import custom_object_scope
maxitems = 10000
max_len = 500
embedding_size = 128  # change it to 128 to gain more accuracy
output_classes = 46
def Reuters():

    (train_data, train_lbl), (test_data, test_lbl) = reuters.load_data(num_words=maxitems)


    train_data = pad_sequences(train_data, max_len)
    test_data = pad_sequences(test_data, max_len)

    train_lbl = to_categorical(train_lbl)
    test_lbl = to_categorical(test_lbl)
    model = Sequential([
        Embedding(maxitems, embedding_size, input_length=max_len),
        SimpleRNN(embedding_size),
        Dense(output_classes, activation='softmax')
    ])
    print(model.summary())

    # #provide basic settings for neural networks
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics='accuracy')
    # #perform training of neural network
    hist = model.fit(train_data, train_lbl, epochs=20, batch_size=80, verbose=1)
    # #perform testing on the nural network
    model.evaluate(test_data, test_lbl)

# #saves the training model
# model.save('model.hdf5')
# Accuracy
#Sentimetal Analaysis
# Imdb
def IMDB():
    (train_data, train_lbl), (test_data, test_lbl) = imdb.load_data(num_words=maxitems)

    train_data = pad_sequences(train_data, max_len)
    test_data = pad_sequences(test_data, max_len)

    train_lbl = to_categorical(train_lbl)
    test_lbl = to_categorical(test_lbl)
    model = Sequential([
        Embedding(maxitems, embedding_size, input_length=max_len),
        SimpleRNN(embedding_size),
        Dense(1, activation='softmax')
    ])
    print(model.summary())

    # #provide basic settings for neural networks
    model.compile(optimizer='sgd', loss='binary_crossloss', metrics='accuracy')
    # #perform training of neural network
    hist = model.fit(train_data, train_lbl, epochs=20, batch_size=100, verbose=1)
    # #perform testing on the nural network
    score=model.evaluate(test_data, test_lbl)
    print(f'Testing Loss is {score}')

IMDB()