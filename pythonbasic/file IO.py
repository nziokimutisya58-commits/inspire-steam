    # musa majjid
    # 24/2/2026
    # program to perform file operation

# create new file
new_file = open("student_data.txt","r+")

#write to  new file
new_file.write("{students Name : Asoman , ID:  4527868 , email:gooner@gmail.com}")
new_file.close()




# read from the file
new_file = open("student_data.txt","r+")


data = new_file.read()

print(data)


 # delete file
 # us os module 
import os
os.remove("remove.txt")

# delete folder
os.rmdir("folder")