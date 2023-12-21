import os as sys

sys.system("cls")
FXVersion = "FX 1.0.0"
print(FXVersion)
#App Data
def Cln():
 sys.system("cls")
 Cursor_univ()
def FolderView():
 sys.system("cls")
 sys.system("dir")
 Cursor_univ()
def Settings():
 def Settings_Main_Menu():
  sys.system("cls")
  print("#Settings>#############################")
  print("Help = How to Move Around The Settings app")
  print("Programs = Program List")
  print("Exit = Exit The Settings App.")
  Settings_Input = input("Settings|>")
  if Settings_Input == "Help":
   def Settings_help():
    sys.system("cls")
    print("#Settings>Help>########################")
    print("Type In the Command Displayed before the = sign.")
    print("Back = Back")
    Set_Hlp_Input = input("Settings|>")
    if Set_Hlp_Input == "Back":
     Settings_Main_Menu()
   Settings_help()
 Settings_Main_Menu()
def Shutdwn():
  sys.system("cls")
  exit("Shutting Down Python and FX...")
def Cursor_univ():
 curuni = input("|>")
 if curuni == "FolderView":
  FolderView()
 elif curuni == "Cleanup":
  Cln()
 elif curuni == "CLEANUP":
  Cln()
 elif curuni == "CleanUp":
  Cln()
 elif curuni == "cleanup":
  Cln()
 elif curuni == "fxdb":
  FXDB()
 elif curuni == "FXDB":
  FXDB()
 elif curuni == "exitFX":
  Shutdwn()
 elif curuni == "Version":
  sys.system("cls")
  print(FXVersion)
 elif curuni == "version":
  sys.system("cls")
  print(FXVersion)
 elif curuni == "settings":
  Settings()
 Cursor_univ()
def FXDB():
 sys.system("cls")
 print("Enable Developer Logging?")
 DBInput = input("|>")
 if DBInput == "y":
  DevLog = True
  print("[INFO]: Variable Devlog changed from  to True")
  print("[PROCESS_INFO]: Defining the FXDB_Main_Menu function")
  def FXDB_Main_Menu():
   DBInput = input("FXDB|>")
   if DBInput == "exit":
    sys.system("cls")
    Cursor_univ()
   elif DBInput == "EXIT":
    sys.system("cls")
    Cursor_univ()
   elif DBInput == "Exit":
    sys.system("cls")
    Cursor_univ()
   elif DBInput == "ExIt":
    sys.system("cls")
    Cursor_univ()
   FXDB_Main_Menu()
  FXDB_Main_Menu()
Cursor_univ()
