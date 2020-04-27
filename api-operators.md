```py
guild = discord.utils.get(client.guilds, name=GUILD)
```
Finds a specified server `GUILD` name out of all servers the bot is on.

```py
guild.name
guild.id
```
Outputs Guild Name and ID of the specified Server (obove)  

```py
client.user
```
Name of the Client (the Bot)

```py
message.author
```
Name of the Person who triggered the Bot (chris#1234)

```py
message.channel.send
```
Send message in the channel the bot is triggered

```py
@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
		f'Hi {member.name}, welcome to Hell!'
		)
```
Messages a Member private when joined

```py
if message.content == "Hi!":
```
Checks if a Messsage contains a certain string


### Functions pt 2
You can input a function as an argument for an other function  
```py
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")
    ```
```py
>>> greet_bob(say_hello)
'Hello Bob'

>>> greet_bob(be_awesome)
'Yo Bob, together we are the awesomest!'
```

It's possible to define a function in a function.  
The inner function is only defined inside that function. It can't be called from outside and is only a local variable.  

```py
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
```

```py
first = parent(1)
first()
```
Enables to call the exectution of an inner function outside  

Functions can be collected in a list and the be exectuted by
```py
my_functions = [func1, func2]

my_functions[1]("Arguement")
```
- Calls the second function with the given arguements

### Decorators
To input an other function in a function you can decorate it

*In a library*  
```py
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

*In the actual code*  
```py
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
```
The code will say Whee two times

### Save a return value of a function
```py
ret_val = function_with_return(args)
```












