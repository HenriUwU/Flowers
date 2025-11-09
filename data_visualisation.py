import os

import matplotlib.pyplot as plt

from constants import flower_types
from constants import training_set_dir
from constants import augmented_data_dir

colors = ['orange', 'cyan', 'pink', 'indigo', 'beige']
explode = [0.05, 0.05, 0.05, 0.05, 0.05]


def count_data(augmented: bool):
    number_of_images = []

    for flower_type in flower_types:
        if augmented:
            flower_dir = os.path.join(augmented_data_dir, flower_type)
        else:
            flower_dir = os.path.join(training_set_dir, flower_type)
        nb_flower = 0
        if os.path.exists(flower_dir):
            for filename in os.listdir(flower_dir):
                if filename.endswith('.jpg'):
                    nb_flower += 1
        number_of_images.append(nb_flower)

    return dict(zip(flower_types, number_of_images))


def percentage_formatting(percentage):
    return '{:.1f}%\n'.format(percentage)


def visualize_data(augmented: bool):
    data = count_data(augmented)
    flowers = list(data.keys())
    nb_flowers = list(data.values())

    fix, ax = plt.subplots(figsize=(12, 10))
    wedges, texts, autotexts = ax.pie(nb_flowers,
                                      labels=flowers,
                                      shadow=False,
                                      autopct=lambda p: percentage_formatting(p),
                                      startangle=90,
                                      colors=colors,
                                      explode=explode,
                                      wedgeprops=dict(linewidth=2, edgecolor='lightgreen'))

    if augmented:
        title = 'Distribution of flower types (augmented)'
    else:
        title = 'Distribution of flower types'

    ax.set_title(title, size=20, weight='bold')
    ax.legend(wedges, flowers, loc='lower left')

    plt.setp(autotexts, size=10, weight='bold', color='black')
    plt.setp(texts, size=12, weight='bold', color='black')

    plt.show()


def main():
    visualize_data(False)
    if os.path.exists(augmented_data_dir):
        visualize_data(True)


if __name__ == '__main__':
    main()
