import check50
import glob

@check50.check()
def exists():
    """Ensure at least one .zip or .md file is present"""
    has_zip = len(glob.glob("*.zip")) > 0
    has_md = len(glob.glob("*.md")) > 0
    
    if not (has_zip or has_md):
        raise check50.Failure("Missing required files: You must include all your code as a .zip file with the README in it or make sure a README.md file exists in this folder with your other summer project files.")