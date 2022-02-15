# Move-Uni-File
A Python project designed to make quick and easy transfers from the user's downloads folder into their university folder structure 

# Where to place this script 
For ease of use, the best location to store this script is in the user's directory for mac (**need to add in the equivalent for windows and linux**). This will make the process the most simple when it comes to running the code, as less modification to the script is required to allow it to run.  

# Prior to Running the Script
Before running the script, two variables must be modified to allow for the code to run. 

The `uni_folder_path_name` and the `download_folder_path_name` must be changed on lines 17 and 18 respectively, otherwise the ValueError will trigger, preventing the rest of the code from running. 

Additionally, the `subject_folders`, the `weekly_subfolders` and the `week_folder_numbers` all can be modified to suit however the folder structure is designed. This is to allow the best amount of customisation for the user, while sticking within the guidelines of a strict folder structure. 

# Running the script 
Once everything is setup for the user's machine, simply run `python move-uni-file.py` and follow the prompts to move the file into the correct location. 

Happy file transfers!
- Aidan