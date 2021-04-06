import os;
import time;
import shutil;

def get_file_or_folder_age(path):
    create_time = os.stat(path).st_ctime;
    print(create_time);

    return create_time;

def remove_folder(path):

    if not (shutil.rmtree(path)):
        print("Folder Removed")

    else:
        print("Unable to delete");    
    
def remove_file(path):
    if not (os.remove(path)):
        print("File removed");

    else:
        print("Unable to delete file");    

    

def main():

    deleted_folder_count = 0;
    deleted_file_count = 0;

    path = 'old_files_folders/';

    days = 1;
#    seconds = time.time() - (days);  * 24 * 60 * 60
    seconds = 0;

    if (os.path.exists(path)):


        for root_folder, folders, files in os.walk(path):

            if (seconds >= get_file_or_folder_age(root_folder)):


                remove_folder(root_folder);
                deleted_folder_count += 1;

                break;

            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder);

                    if (seconds >= get_file_or_folder_age(root_folder)):
                        remove_folder(folder_path);
                        deleted_folder_count += 1;
                        
                        break;

                for file in files:
                    file_path = os.path.join(root_folder, file);

                    if (seconds >= get_file_or_folder_age(root_folder)):
                        remove_file(file_path);
                        deleted_file_count += 1;
                        
                        break;

    else:
        print("File not found");


main();                        
                            

    
