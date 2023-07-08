import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")    # this will set dest_Path = f"{dest_dir}/compressed.zip"
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)          # with this we can extract name using filepath.name
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    pass
