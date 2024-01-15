from bsb_directory_generator import BSBDirectoryGenerator
from bsb_prefix_rules_generator import BSBPrefixRulesGenerator

if __name__ == '__main__':
    try:
        dbg = BSBPrefixRulesGenerator()
        dbg.update_bsb_prefix_rules()
        dbg.close_ftp()
    except Exception as e:
        raise f"Unable to update BSB Database, raised exception: {e}"

    try:
        blg = BSBDirectoryGenerator()
        blg.update_bsb_directory()
        blg.close_ftp()
    except Exception as e:
        raise f"Unable to update prefix rules, raised exception: {e}"
