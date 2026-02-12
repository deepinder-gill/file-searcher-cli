import os

class file_searching():
  def ask_user(self):
    while True:
      asking = int(input("1. Search 2. Exit [1/2]"))
      try:
        if asking == 1:
          folder_path = input("Enter Folder Path: ")
          keyword = input("Enter Keyword:")
          extension = input("Enter File Extension[PRESS ENTER TO SKIP]: ").strip().lower()

          print("Searching...")

          if os.path.exists(folder_path):
            for root, subfolders, files in os.walk(folder_path):
              repetition = 0
              for file in files:
                if extension and os.path.splitext(file)[1].lower() != extension:
                  continue
                file_path = os.path.join(root, file)
                try:          
                  with open(file_path, encoding ="utf-18" ) as read_file:
                    for i, line in enumerate(read_file, start = 1):
                      if keyword in line:
                        repetition += 1
                        print(f"keyword found at:\n{i}\nin line:{line}\n")
                except Exception as e:
                  print(f"{file_path} not readable: {e}")
            print(f"----------------------------------------\nNo. of result found: {repetition}\n----------------------------------------")
            break
          elif asking == 2:
            return asking
      except ValueError:
        print("please choose between 1 and 2")


def main():
  while True:
    print("=========================================\nWELCOME TO FILE SEARCH TOOL\n=========================================\n")

    f_s = file_searching()
    ask = f_s.ask_user()

    if ask == 2:
      print("Thankyou for considering us")
      break

if __name__ == "__main__":
  main()