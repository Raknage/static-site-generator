import re
import sys
from os import path, mkdir, listdir, makedirs
from shutil import copy, rmtree
from markdown_to_htmlnode import markdown_to_html_node

separator = "----------------------------------------------------"


def main():
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    source = "./static"
    template_path = "template.html"
    dir_path_content = "./content"
    dest_dir_path = "./docs"
    copy_static_to_public(source, dest_dir_path)
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)


def copy_static_to_public(source, destination):
    if path.exists(destination):
        print(f"Destination {destination} exists. Deleting...")
        rmtree(destination)
    print(f"Creating new folder: {destination}")
    mkdir(destination)
    copy_files_recursive(source, destination)
    print(f"all files copied from {source} to {destination}")
    print(separator)


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


def extract_title(markdown):
    try:
        title = re.match(r"^#{1} (.{1,})", markdown).group(1)
        return title.strip()
    except:
        raise ValueError("Heading missing from markdown")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_page = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_string)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    if path.exists(path.dirname(dest_path)):
        print(f"Path {path.dirname(dest_path)} exists")
    else:
        print(f"Path does not exist. Creating folder {path.dirname(dest_path)}")
        makedirs(path.dirname(dest_path))
    with open(dest_path, "w") as f:
        print(f"writing HTML to file {dest_path}")
        f.write(html_page)
    print(separator)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    file_list = listdir(dir_path_content)
    if len(file_list) == 0:
        return
    for file in file_list:
        source_filepath = path.join(dir_path_content, file)
        if path.isfile(source_filepath):
            destination_filepath = path.join(dest_dir_path, "index.html")
            print(f"Generating HTML: {source_filepath} to {destination_filepath}")
            generate_page(
                source_filepath, template_path, destination_filepath, basepath
            )
        else:
            destination_filepath = path.join(dest_dir_path, file)
            print(f"New folder: {source_filepath} to {destination_filepath}")
            mkdir(destination_filepath)
            generate_pages_recursive(
                source_filepath, template_path, destination_filepath, basepath
            )
    return


if __name__ == "__main__":
    main()
