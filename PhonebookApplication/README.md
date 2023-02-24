#  Phonebook Application
## Problem Statement

* Write a program that creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

* There should be 4 options available to the user and from the options, users should be able to add, find, delete contacts, or terminate the program as shown below.

* Phonebook has users and their corresponding phone numbers.

* At the beginning of the program the phonebook will be empty and user can choose to add new contacts to the phonebook.

* Program should ask user for the input, after giving information text shown as below.

        Welcome to the phonebook application
        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) :

* Application should be case sensitive and run until the user types 4.

* Example for user inputs and respective outputs.

        Welcome to the phonebook application
        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 2
        Insert name of the person : John
        Insert phone number of the person: ten
        Invalid input format, cancelling operation ...

        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 2
        Insert name of the person : Alex
        Insert phone number of the person: 1234
        Phone number of Alex is inserted into the phonebook

        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 1
        Find the phone number of : Alex
        1234

        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 3
        Whom to delete from phonebook : Alex
        Alex is deleted from the phonebook

        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 1
        Find the phone number of : Alex
        Couldn't find phone number of Alex

        1. Find phone number
        2. Insert a phone number
        3. Delete a person from the phonebook
        4. Terminate
        Select operation on Phonebook App (1/2/3) : 4
        Exiting Phonebook
