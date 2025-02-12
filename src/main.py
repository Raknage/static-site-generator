from os import path, mkdir, listdir
from shutil import copy, rmtree
from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    source = "./static"
    destination = "./public"
    copy_static_to_public(source, destination)


def copy_static_to_public(source, destination):
    if path.exists(destination):
        print(f"Destination {destination} exists. Deleting...")
        rmtree(destination)
    print(f"Creating new folder: {destination}")
    mkdir(destination)
    copy_files_recursive(source, destination)
    print(f"all files copied from {source} to {destination}")


def copy_files_recursive(source, destination):
    file_list = listdir(source)
    if len(file_list) == 0:
        return
    for file in file_list:
        source_filepath = path.join(source, file)
        destination_filepath = path.join(destination, file)
        if path.isfile(source_filepath):
            print(f"copying file: {source_filepath} to {destination_filepath}")
            copy(source_filepath, destination_filepath)
        else:
            print(f"Copying folder: {source_filepath} to {destination_filepath}")
            mkdir(destination_filepath)
            copy_files_recursive(source_filepath, destination_filepath)
    return


if __name__ == "__main__":
    main()
