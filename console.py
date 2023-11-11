#!/usr/bin/python3
""" This is the console entry point """

import cmd
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ this is the command console class """

    #updating the public attribute prompt
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

    def do_quit(self, line):
        return True
    
    def help_quit(self):
        print("This is a command to exit.")
        #should return the string as well
        
    def do_EOF(self, line):
        return True
    
    def help_EOF(self):
        print("This is an EndOfFile method that handle Ctrl-D key stroke.")
        #should it be returned?

    # the create command
    def do_create(self, line):
        print("line: {}".format(line))
        if not line:
            print("** class name missing **")
        elif not (line in self.classes):
            print("** class doesn't exist **")
        else:
            # this is still gonna be upated with a conditional statement to
            #look for other classes and operare on them
            #new_model = BaseModel()
            #new_model.save()
            #print(new_model.id)
            obj = eval(line)() # here we can use eval() to create objects of a given class name
            obj.save()
            print(obj.id)
        

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.")

    # the show command
    def do_show(self, line):
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
           all_objects = storage.all()
           spec_class = args[0] + '.' + args[1]
           #print("the key to lok for is: {}".format(spec_class))
           if spec_class in all_objects:
               print(all_objects[spec_class])
           else:
               print("** no instance found **")
           
            
    def help_show(self):
        print("Prints the string representation of an instance based on the class name and id.")

    def do_destroy(self, line):
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            spec_instance = args[0] + '.' + args[1]
            all_objects = storage.all()
            del all_objects[spec_instance]
            storage.save()
            
    def help_destroy(self):
        print("Deletes an instance based on the class name and id (save the change into the JSON file).")

    def do_all(self, line):
        
        all_objects = storage.all()
        output_list = []
        all_obj_list = list(all_objects.values())
        for obj in all_obj_list:
            #print("{}".format(i), end=", ")
            output_list.append(str(obj))
            
        if line:
            if line in self.classes:
                #print("printing the string rep of all the instances by the nme : {}".format(line))
                # this is only done if the system supports the class that the user inputed.
                # this hanels 'all [class name]' we extract every object that has the same class name in it as the user input
                rec_string = '[' + line + ']'
                #print("looking for this: {}".format(rec_string))
                #fr i in output_list:
                    #print(eval(i.__class__.__name__, line))
                selection_list = []
                for obj in all_obj_list:
                    if obj.__class__.__name__ == line:
                        selection_list.append(str(obj))
                print(selection_list)
            else:
                print("** class doesn't exist **")
        else:
           # this is for 'all' -> this means outputting everythong in the json file
            print(output_list)
            
            #print("printing all the existent classes as a list")

    def help_all(self):
        print("Prints all string representation of all instances based or not on the class name.")

    def do_update(self, line):
        args = line.split(" ")
        
        if line is None or len(line) < 1 or line == "":
            print("** class name is missing **")
        elif args[0] not in self.classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objects = storage.all()
            instance = args[0] + '.' + args[1]
            if instance not in all_objects:
                print("** no instance found **")
            else:
                for key, value in all_objects.items():
                    val = args[3]
                    if '"' in val:
                        val = val.strip('"')
                    if instance == key:
                        setattr(value, args[2], val)
                        storage.save()
                        
            

    def help_update(self):
        print("Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)")
        
    #this is to overwrite the emptyline public method
    def emptyline(self):
        pass
    
if __name__ == "__main__":
   HBNBCommand().cmdloop()