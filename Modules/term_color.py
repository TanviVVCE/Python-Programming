import termcolor
import pyfiglet 

message = input('What message do you want to print ? : ')
color = input('What color ? : ')

f = termcolor.colored(color=color, text = pyfiglet.figlet_format(message, font="slant"))
print(f)

