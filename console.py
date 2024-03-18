#!/usr/bin/python3
"""
This is the console base for the unit
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import json


class RestCommand(cmd.Cmd):
    """Defines the Restaurant command line interpreter"""
    prompt = '(hbnb) '
    my_dict = {
            'BaseModel': BaseModel
            }

    def emptyline(self):
        """Do nothing when an empty line is received"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to end the program"""
        return True

    def do_create(self, arg):
        """ Creates a new instance of the basemodel class
        saves it and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] not in RestCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        new_instance = RestCommand.my_dict[my_data[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in RestCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        save the change into the JSON file
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        cmd_input = shlex.split(arg)
        if len(cmd_input) == 0:
            print("** class name missing **")
            return
        if cmd_input[0] not in RestCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(cmd_input) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        obj_dict = storage.all()
        cmd_key = cmd_input[0] + "." + cmd_input[1]
        if cmd_key in obj_dict:
            del obj_dict[cmd_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based on the class name
        """
        storage.reload()
        my_json = []
        objs_dict = storage.all()
        if not arg:
            for key in objs_dict:
                my_json.append(str(objs_dict[key]))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in RestCommand.my_dict.keys():
            for key in objs_dict:
                if token[0] in key:
                    my_json.append(str(objs_dict[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        cmd_input = shlex.split(arg)
        if len(cmd_input) == 0:
            print('** class name missing **')
            return
        if cmd_input[0] not in RestCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(cmd_input) == 1:
            print('** instance id missing **')
            return
        storage.reload()
        objs_dict = storage.all()
        obj_key = cmd_input[0] + '.' + cmd_input[1]
        if obj_key not in objs_dict:
            print('** no instance found **')
            return
        if len(cmd_input) == 2:
            print('** attribute name missing **')
            return
        if len(cmd_input) == 3:
            print('** value missing **')
            return

        obj_instance = objs_dict[obj_key]

        """Get the attribute name and value"""

        attr_name = cmd_input[2]
        attr_value = cmd_input[3]

        """Check if the attribute exists in the object"""

        if hasattr(obj_instance, attr_name):

            """Get the current type of the attribute and cast the value"""

            attr_type = type(getattr(obj_instance, attr_name))
            try:
                casted_value = attr_type(attr_value)
            except ValueError:
                print('** value missing **')
                return

            """ Update the attribute value and save changes"""

            setattr(obj_instance, attr_name, casted_value)
            obj_instance.save()
        else:
            print('** attribute name missing **')


if __name__ == '__main__':
    RestCommand().cmdloop()
