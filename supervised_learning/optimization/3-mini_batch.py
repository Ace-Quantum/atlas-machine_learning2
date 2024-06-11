#!/usr/bin/env python3

shuffle_data = __import__('2-shuffle_data').shuffle_data

def create_mini_batches(X, Y, batch_size):
    mini_batches = []
    # data = np.haystack(X, Y)
    # np.random.shuffle(data)
    big_batch = shuffle_data(X, Y)
    n_minibatches = big_batch.shape[0] // batch_size

    i = 0

    for i in range(n_minibatches + 1):
        mini_batch = data[i * batch_size:(i + 1) * batch_size, :]
        X_mini = mini_batch[:, :-1]
        Y_mini = mini_batch[:, -1].reshape((-1, 1))
        mini_batches.append((X_mini, Y_mini))
    if data.shape[0] % batch_size != 0:
        mini_batch = data[i * batch_size:data.shape[0]]
        X_mini = mini_batch[:, :-1]
        Y_mini = mini_batch[:, -1].reshape((-1, 1))
        mini_batches.append((X_mini, Y_mini))

    return mini_batches