import os
import shutil

import Augmentor

from constants import augmented_data_dir
from constants import training_set_dir
from constants import flower_types
from constants import dataset_dir


def count_data_in_directory(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            count += 1
    return count


def data_augmentation(flower_type):
    flower_type_path = os.path.join(training_set_dir, flower_type)

    p = Augmentor.Pipeline(flower_type_path)
    p.skew_tilt(probability=0.1)
    p.skew_tilt(probability=0.1)
    p.rotate(probability=0.1, max_left_rotation=20, max_right_rotation=20)
    p.shear(probability=0.1, max_shear_left=20, max_shear_right=20)
    p.crop_random(probability=0.1, percentage_area=0.9)
    p.random_color(probability=0.1, min_factor=0.1, max_factor=0.1)
    p.random_brightness(probability=0.1, min_factor=0.1, max_factor=0.1)
    p.random_contrast(probability=0.1, min_factor=0.1, max_factor=0.1)
    p.flip_random(probability=0.1)
    p.sample(1000 - count_data_in_directory(flower_type_path), multi_threaded=False)


def move_augmented_data(flower_type):
    source_dir = os.path.join(training_set_dir, flower_type)
    source_dir_augmented = os.path.join(source_dir, 'output')
    target_dir = os.path.join(dataset_dir, 'augmented', flower_type)

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    original_files_to_move = os.listdir(source_dir)
    for file in original_files_to_move:
        if file.endswith('.jpg'):
            shutil.copy(os.path.join(source_dir, file), target_dir)
    augmented_files_to_move = os.listdir(source_dir_augmented)
    for file in augmented_files_to_move:
        if file.endswith('.jpg'):
            shutil.move(os.path.join(source_dir_augmented, file), target_dir)


def main():
    if not os.path.exists(augmented_data_dir):
        os.mkdir(augmented_data_dir)
        print('Augmented dataset directory created successfully')
    for flower_type in flower_types:
        data_augmentation(flower_type)
        move_augmented_data(flower_type)


if __name__ == '__main__':
    main()
