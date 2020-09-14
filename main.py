import gzip
import shutil
import os
import platform


def main():
    logs_directory = input("Please specify the logs directory: ")
    search_phrase = input("Enter the search phrase: ")
    temp_directory = 'temp'
    slash = '\\' if platform.system() == 'Windows' else '/'

    print(f"\nSearching for \"{search_phrase}\" in {logs_directory}...")
    os.mkdir(temp_directory)
    os.chdir(temp_directory)

    print("Extracting the logs...")
    for file in os.listdir(logs_directory):
        if os.path.splitext(file)[1] == '.gz':
            with gzip.open(f'{logs_directory}{slash}{file}', 'rb') as f_in:
                with open(os.path.splitext(file)[0] + ' RAW.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

    print("Reading files...")
    for file in os.listdir(os.getcwd()):
        with open(file) as f_out:
            log_lines = f_out.readlines()
            for line in log_lines:
                if search_phrase in line:
                    print(f"> FOUND! \"{search_phrase}\" in {file.split(' ')[0]}")
                    print(f"  {line}")

    print("Cleaning up...")
    os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    shutil.rmtree(temp_directory)

    input("\nDone. Press Enter to terminate.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
