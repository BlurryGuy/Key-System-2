from colorama import *
import time
import sys

this_is_my_array = {hash("key1"), hash("key2"), hash("key3")}

def print01(chat):
    for i in chat:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)

print01(Fore.GREEN + "> " + Fore.RESET + "Enter your key: ")

user_input = input("")

try:

   if hash(user_input) in this_is_my_array:
   
      print01(Fore.GREEN + "> " + Fore.RESET + "Valid Key!")
      
      input()
   else:

      print01(Fore.GREEN + "> " + Fore.RESET + "Invalid Key!")
      
      input()
except:
      print01("You tried to check if a string exists in a non-existing array or put wrong variable / array name!")
      
      input()
