import os

class FileSearching():
  def AskUser(self):
    while True:
      try:
        asking = int(input("1. Search 2. Exit [1/2]"))
        if asking == 1:
          folder_path = input("Enter Folder Path: ")
          keyword = input("Enter Keyword:")
          extension = input("Enter File Extension[PRESS ENTER TO SKIP]: ").strip().lower()

          print("Searching...")

          if os.path.exists(folder_path):
            repetition = 0
            for root, subfolders, files in os.walk(folder_path):
              for file in files:

                if extension and os.path.splitext(file)[1].lower() != extension:
                  continue
                file_path = os.path.join(root, file)
                try:          
                  with open(file_path, "r", encoding ="utf-8" ) as read_file:
                    for i, line in enumerate(read_file, start = 1):
                      if keyword.lower().strip() in line.lower():
                        repetition += 1
                        print("[FILE NAME MATCH]")
                        print(f"File: {file_path}\nLine index: {i}\nLine: {line}")
                except Exception as e:
                  print(f"{file_path} not readable: {e}")
            print(f"----------------------------------------\nNo. of result found: {repetition}\n----------------------------------------")

          elif not os.path.isdir(folder_path):
            print("Invalid folder path")
            continue
          
        elif asking == 2:
          return asking
      except ValueError:
        print("please choose between 1 and 2")


def main():
  FS = FileSearching()
  while True:
    print("=========================================\nWELCOME TO FILE SEARCH TOOL\n=========================================\n")

    ask = FS.AskUser()

    if ask == 2:
      print("Thankyou for considering us")
      break

if __name__ == "__main__":
  main()