commands = {}

def register_command(command_name, callback):
    commands[command_name] = callback

def run_prompt():
    while True:
        user_input = input("> ").strip()
        input_parts = user_input.split()

        if not input_parts:
            continue

        command = input_parts[0]
        args = input_parts[1:]

        if command in commands:
            commands[command](*args)
        elif command == '?':
            print("registered commands")
            for command_name in commands:
                print("[",command_name,"], ")
        else:
            print("invalid command")

def sample_command(*args):
    if not args:
        return
    if args[0] == '?':
        print('usage: sample print')
    elif args[0] == 'print':
        print("execute sample command: ", args[1])
    else:
        print("invalid arg")

def quit_command(*args):
    print("bye")
    exit()

if __name__ == "__main__":
    register_command('sample', sample_command)
    register_command('quit', quit_command)
    run_prompt()
