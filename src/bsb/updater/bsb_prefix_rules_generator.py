from base_generator import BaseGenerator
import os


class BSBPrefixRulesGenerator(BaseGenerator):
    # temporary placeholder, fix after finding info on yaml side
    BSB_PREFIX_PATH = "static/bsb_prefix_rules.csv"

    def __init__(self):
        super().__init__()
        self.file_name = self.latest_file(matching_filename='KEY TO ABBREVIATIONS AND BSB NUMBERS', file_format='.csv')

    def update_bsb_prefix_rules(self):
        # print(self.SB_DIRECTORY_PATH)
        file_path = self.BSB_PREFIX_PATH
        with open(file_path, 'wb') as f:
            self.ftp.retrbinary(f'RETR {self.file_name}', f.write)
            f.close()


# if __name__ == '__main__':
#     dbg = BSBPrefixRulesGenerator()
#     print(dbg.update_bsb_prefix_rules())
