# Example 8: Extracting an Archive 
import shutil

# Extract the archive created in Example 7
shutil.unpack_archive('archive.zip', 'extracted_files')

print('Archive "archive.zip" extracted to "extracted_files" directory.')