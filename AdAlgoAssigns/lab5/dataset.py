import random


def gen_data(N, i=0):
    dataset = []
    dup = int(N * i * 0.1)
    if dup == 0:
        dup = 1
    base_data = random.sample(range(0, N), N - dup + 1)
    # print(base_data)
    # print(base_data)
    dataset.extend(base_data)
    for d in range(int(dup)):
        random_index = random.randint(0, int(N - dup + 1))
        # print(random_index)
        dataset.append(dataset[random_index])
    random.shuffle(dataset)
    # print(dataset)
    return dataset
