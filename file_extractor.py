import os


def extract_files(paths: list, extensions: list):
    result = []
    path_and_file_gen = ((pathname, filename) for path in paths for pathname, dirnames, filenames in os.walk(path) for
                         filename in filenames)

    for path, filename in path_and_file_gen:
        basename, ext = os.path.splitext(filename)
        if ext in extensions:
            result.append(os.path.join(path, filename))

    return result
