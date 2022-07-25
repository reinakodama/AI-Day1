# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        #json.load(file)
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        name = input("Enter full name: ")
        age = input("Enter age: ")
        print("Creating ...")
        account = Person(name, age)
        self.list_of_people.append(account)
        print("Your account has been recorded")
        pass


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(person_object)
        pass

    def send_message(self):
        #implement sending message to friend here
        recieving = input("Who are you sending the message to?: ")
        message = input("Type message here: ")
        print(recieving, "has recieved the message: ", message)
        pass

    def edit_details(self):
        edit_details_choice = social_network_ui.manageEditDetails()
        if edit_details_choice == "1":
            self.id = input("Enter edited name: ")
        elif edit_details_choice == "2":
            self.year = input("Enter edited age: ")
        elif edit_details_choice == "3":
            username = input("Enter edited username: ")
        else:
            print("invalid input")
            edit_details_choice = social_network_ui.manageEditDetails()

    def all_messages(self):
        print(message)



        


