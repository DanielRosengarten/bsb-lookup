from base_generator import BaseGenerator
import os


class BSBDirectoryGenerator(BaseGenerator):
    # temporary placeholder, fix after finding info on yaml side
    BSB_DIRECTORY_PATH = "static/bsb_directory.csv"

    def __init__(self):
        super().__init__()
        self.file_name = self.latest_file(matching_filename='BSBDirectory', file_format='.csv')

    def update_bsb_directory(self):
        # print(self.SB_DIRECTORY_PATH)
        file_path = self.BSB_DIRECTORY_PATH
        with open(file_path, 'wb') as f:
            self.ftp.retrbinary(f'RETR {self.file_name}', f.write)
            f.close()


# blg = BSBDirectoryGenerator()
# print(blg.update_bsb_directory())
