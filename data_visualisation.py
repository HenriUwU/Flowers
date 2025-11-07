import matplotlib.pyplot as plt
import os

from matplotlib.pyplot import title

flower_types = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
colors = ['orange', 'cyan', 'pink', 'indigo', 'beige']
explode = [0.1, 0.1, 0.1, 0.1, 0.1]

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

def visualize_data():
    data = count_data()
    flowers = list(data.keys())
    nb_flowers = list(data.values())

    # plt.pie(list(data.values()), labels=list(data.keys()))
    fix, ax = plt.subplots(figsize=(12, 12))
    ax.pie(nb_flowers,
           labels=flowers,
           shadow=True,
           startangle=90,
           colors=colors,
           explode=explode)
    ax.set_title("Distribution of flower types")
    plt.show()

def main():
    visualize_data()

if __name__ == '__main__':
    main()