## move-uni-file is a program used to automate the process of moving selected contents from the downloads folder
# straight into the selected folder structure in the uni folder
# This program works in the terminal by invoking 'python move-uni-file' before a series of questions determines where to move the file to.
# This is designed to make the process of moving weekly content into folders much more efficient. 

# Uni Folder Path - note that for security reasons, this variable will remain an empty string
# and should be filled out prior to executing this code

# Imports for Value Error, os
from multiprocessing.sharedctypes import Value
import os
import shutil

BASE_DIR = os.getcwd()

# Folder Path names (change these variables to reflect where the folder structure and download folder exists)
uni_folder_path_name = ''
download_folder_path_name = ''

# The full folder structure and download folder paths
uni_folder_structure_path = os.path.join(BASE_DIR, uni_folder_path_name)
download_folder_path = os.path.join(BASE_DIR, download_folder_path_name)

# Checking to see if a university folder structure was given. If not, raise a ValueError to stop the program before breaking
if uni_folder_path_name == '' or download_folder_path_name == '':
    raise ValueError('Path to the Folder Structure has not been set. Change the code on Line 17 and Line 18 to specify their respective paths. This code will not work correctly without it.')

# Subject Folders for the user to input 
subject_folders = [] 

# Giving subfolders to navigate to
weekly_subfolders = []

if len(subject_folders) == 0 or len(weekly_subfolders) == 0:
    raise ValueError('Folder Structure has not been specified. Change the code on Line 29 and Line 32 to describe the university folder structure. This code will not work correct without it.')

# Setting up the weekly folders by creating a range of numbers and appending it to a list
week_folder_numbers = range(14)
weekly_folders = []

for week in week_folder_numbers:
    weekly_folders.append(f'Week {week}')

# Finding all items in the download folder
current_download_folder_items = os.listdir(download_folder_path)

# Checking  to see if the DS_Store exists in the download folder. If so, remove it from the list to ensure no movement of that file
checking_for_ds_store = any('.DS_Store' in current_download_folder_item for current_download_folder_item in current_download_folder_items)
if checking_for_ds_store:
    current_download_folder_items.remove('.DS_Store')

# Checking if any files exist in downloads folder
if len(current_download_folder_items) != 0:
    # For every item found in the download folder, move it to a specified location by the user
    for item in current_download_folder_items:

        # New File is detected
        incorrect_subject = True
        while incorrect_subject:
            print(f'New Item Detected: File "{item}"')

            # Prompting the user which unit the file is for
            for index, subject in enumerate(subject_folders):
                print(f'Enter {index + 1} for {subject}')
            
            # Receive input from user to check which unit to put it in 
            get_unit_input = input('')

            # Check if the unit input by the user was valid. If so, run the correct code and return the incorrect object as false
            # If not, keep while loop running until valid response given
            if get_unit_input == "1" or get_unit_input == "2":
                print(f'Unit {get_unit_input} Selected')

                print(f'Current working directory: \n{os.getcwd()}')
                incorrect_subject = False
            else:
                print(f'You selected {get_unit_input}! :/')
                print('Incorrect Option. Try Again.')

        incorrect_week_number = True
        while incorrect_week_number:
            get_week_number = input('Which week folder would you like to put the file into?\n')
            
            if int(get_week_number) > 13 or int(get_week_number) < 0:
                print('Cannot have a number greater than 13 or less than 0. Repeat Number.')
            else:
                incorrect_week_number = False

        # Selecting whether the material is lecture or workshop material type
        incorrect_option = True
        while incorrect_option:
            print('Is the file Lecture or Workshop Material\nEnter 1 for Lecture Material\nEnter 2 for Workshop Material')

            get_material_type = input('')

            if int(get_material_type) == 1 or int(get_material_type) == 2:
                print('Valid Entry! Moving File...\n')

                # Setting the variable of the preferred destination
                print(f'University Folder Structure Path: \n\n{uni_folder_structure_path}\n')

                # Creating variables to direct the new file destination (and simplify code)
                selected_subject_folder = subject_folders[int(get_unit_input) - 1]
                selected_week_folder = f'Week {get_week_number}'
                selected_material_folder = weekly_subfolders[int(get_material_type) - 1]

                # Selected File Destination for moving the file from the downloads folder
                selected_file_destination = os.path.join(uni_folder_structure_path, f'{selected_subject_folder}/{selected_week_folder}/{selected_material_folder}')

                print(f'Desired new file path: \n\n{selected_file_destination}')

                print(f'Item to be moved: \n\n{item} \nFile Destination:\n\n{selected_file_destination}')

                # Changing the current working directory to the downloads folder
                os.chdir(download_folder_path)

                # move the file to requested destination inside the university folder structure
                shutil.move(item, selected_file_destination)

                print(f'File Moved to Week Folder {get_week_number}!')

                incorrect_option = False
            else:
                print('Incorrect Option. Try Again')

    print('No More Files Detected!')

print('No Files Found in Downloads Folder')