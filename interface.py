# Gabriel Wersebe


class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, member):
        return member in self.__myTeam

    def __iter__(self):
        return iter(self.__myTeam)


def main():
    classmates = Teams(["John", "Steve", "Tim"])
    print(len(classmates))

    # 1) Add the __contains__ protocol and show whether or not  'Tim' and 'Sam' are part of our team.  
    print("Tim" in classmates)
    print("Sam" in classmates)

    # 2) Add the __iter__ protocol and show how you can print each member of the classmates object.
    for member in classmates:
        print(member)

    # 3) Determine if the class classmates implements the __len__ method.
    # Yes it does, its implemented on line 17

    # 4) Explain the difference between interfaces and implementation. 
    # Interfaces define all the properties and methods that a class must have to be an instance of that object. The implentation is the code that is used to instantiate the object.

    # 5) Using both visual and written descriptions, think through the interface-implementation of a large scale storage system.   
    # In many systems today, we have the ability to store information from a single application to a variety of storage devices - local storage (hard drive, usb), the cloud and/or some new medium in the future.   
    # How would you design an interface structure such that all of the possible implementations could store data effectively.

    # To accomplish this i would make an extremely generic interface that focuses on the output of the application rather than the storage medium. In modern operating systems and other cloud services we can leverage pre built 
    # interfaces for things such as files and file systems. One example of an application that leverages this is Microsoft Word, regardless of the platform it is running on, it consitently outputs a .docx file and then the platform 
    # its running on will handle the storage or transmission of that file. This same architecture can be adopted for any application that needs to store data, including a storage system.


    


main()
