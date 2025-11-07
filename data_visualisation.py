import os

import matplotlib.pyplot as plt

flower_types = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
colors = ['orange', 'cyan', 'pink', 'indigo', 'beige']
explode = [0.05, 0.05, 0.05, 0.05, 0.05]


def count_data():
    dataset_dir = os.path.join(os.getcwd(), 'dataset/train')
    number_of_images = []

    for flower_type in flower_types:
        flower_dir = os.path.join(dataset_dir, flower_type)
        nb_flower = 0
        for filename in os.listdir(flower_dir):
            if filename.endswith('.jpg'):
                nb_flower += 1
        number_of_images.append(nb_flower)

    return dict(zip(flower_types, number_of_images))


def percentage_formatting(percentage):
    return '{:.1f}%\n'.format(percentage)


def visualize_data():
    data = count_data()
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

    ax.set_title('Distribution of flower types in the dataset', size=20, weight='bold')
    ax.legend(wedges, flowers, loc='lower left')

    plt.setp(autotexts, size=10, weight='bold', color='black')
    plt.setp(texts, size=12, weight='bold', color='black')

    plt.show()


def main():
    visualize_data()


if __name__ == '__main__':
    main()
