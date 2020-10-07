
# import csv as commaz

class App:
    def __init__(self):
        print("Select an option::\n1. New File\n2. Read File\n3. File-to-CSV\n\n*********EXPERIMENTAL******\n4. hshr1\n4a. Decrypt hshr1(might be or might not be possible at this time)\n********\n\n5. Create List\n6. Add to List\n7. Read List")
        print("**type the method as you see it above**\n")
        user_select = input("<USER_SELECT>...")

        if user_select == "New File":
           txt_for_file = input("Compose a message for the file.>>")
           file_name = input("What ould you like to name this file?>>")
           self.new_file(txt_for_file, file_name)
        if user_select == 'Read File':
            file_to_read = input('Specify the name of the file you want to read?')
            self.read_file(file_to_read)
        # CSV to be added (**maybe have the method look in list files and convert to csv(title,descr,[...,points,..n.])

        if user_select == "hshr1":
            filename = input("file name>>")
            msg = input("Message>>")
            self.hshr1(filename, msg)
        if user_select == "Decryp hshr1":
            filename = input("file name>>")
            self.dh(filename)

        if user_select == 'Create List':
            list_to_create = input('Specify the name of the file for the list?')
            list_title = input("Header/Title for the list>>")
            list_descr = input("Brief description for list>>")
            self.create_list(list_to_create, list_title, list_descr)
        if user_select == 'Add to List':
            listname = input("Enter the name of the list to add to>>")
            self.add_to_list(listname)
        if user_select == 'Read List':
            list_to_read = input('Specify the name of the list file you want to read?')
            self.read_list(list_to_read)



    
    # new file
    def new_file(self, txt, filename):
        with open(f"txt_files/{filename}.txt" , 'x') as f:
            f.write(txt)
            f.close()
        if not txt or not filename:
            print('An error occured ...')
        else: print('File Created!')

    # read file
    def read_file(self, filename):
        with open('txt_files/'+filename, 'r') as f:
            cntnt = f.read()
            f.close()
            print(cntnt)
    # file to csv
    #hshr1
    def hshr1(self, file_name, txt):
        arr = []
        arr2 = []
        for i in file_name:
            arr.append(i)
        for j in txt:
            arr2.append(j)
        tg = arr+arr2
        for k in tg:
            ln = len(tg)
            h0 = k[:7]
            h1 = k[8:14]
            fusion = h0+str(ln)+h1
        msg = txt
        msg = fusion.join(h0+str(ln)+h1)
        # str(msg)
        try:
            with open("hshr1_files/"+file_name+".txt", 'x') as hfile:
                hfile.write(msg)
                hfile.close()
        except FileNotFoundError:
            print("ERROR::404<<File!found.")
        else:
            print("hshr1 succeeded!")
    # decrypt^^^^^^^^
    # def dh(self, filename):
    # REALLY COOL IF I CAN SOMEDAY FIGURE OUT HOW TO REVERSE THIS....MAYBE IT CAN OR CANT but the unique value returned each time can be used for stuff


    # create a list file
    def create_list(self, filename, title, descr):
        with open(f"list_files/{filename}.txt", 'x') as lf:
            lf.write(f"Title::{title}\nDescription::{descr}\n**********POINTS**********") # Points will be>>'Add to List'
            lf.close()
        if not title or not filename or not descr:
            print('An error occured ...')
        else: print('List File Created!')
    # add to list^
    def add_to_list(self, filename):
        count = 0
        while count < 5:
            adding_txt = input('Task/Note to add>>')
            with open('list_files/'+filename+'.txt', 'a') as lfile:
                    lfile.write('\n> '+adding_txt)
                    count+=1
                    if count == 5:
                        ask = input('add more to the list? ***(y/n)??')
                        if ask == 'y':
                            count = 0
                        else:
                            break
                            lfile.close()
    # read list [?^^?]
    def read_list(self, filename):
        with open('list_files/'+filename+".txt", 'r') as f:
            cntnt = f.read()
            f.close()
            print("\n\n"+cntnt+"\n\n")

a1 = App()