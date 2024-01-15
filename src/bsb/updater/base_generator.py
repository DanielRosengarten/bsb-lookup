import csv
from ftplib import FTP


class BaseGenerator:

    def __init__(self):
        # initialises the ftp connection
        self.ftp = FTP('bsb.hostedftp.com')
        self.ftp.login()

    def close_ftp(self):
        self.ftp.close()

    def latest_file(self, matching_filename, file_format):
        self.ftp.dir()
        self.ftp.cwd('/~auspaynetftp/bsb')

        search_criteria = [matching_filename, file_format]

        try:
            # uses list comprehension to get all files that match the given search criteria
            directory = [file for file in self.ftp.mlsd() if all(x in file[0] for x in search_criteria)]

            # gets the file with the latest timestamp
            current_file = max(directory, key=lambda x: x[1]['modify'])
            file_name = current_file[0]

            return file_name
        except Exception as e:
            raise f"Could not find valid file, raised exception {e}"
