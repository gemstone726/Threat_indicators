#import track_detections_to_feather as td2f
#import tracks_to_feather as t2f
import os.path
import glob
cwd = os.getcwd()
def is_there_zip_file():
    if not glob.glob(cwd +'/def*.zip'):
        print('There is not a zip file in this directory')
        bool_zip = False
    else:
        bool_zip = True
    #    for files in zip_files:
    #        dos_zips=files.split(sep = '/')[-1]
    #except:
    #    print('No Zip File Found in location {}'.format(cwd))

    return(bool_zip)

def main():
    print(is_there_zip_file())
    #is is possible to check if file deather file or json file was created before the zip file if so will need to redo them

    #td2f.read_db_dump()
    #t2f.read_dump()

main()
