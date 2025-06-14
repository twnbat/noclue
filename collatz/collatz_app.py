import collatz_module
import cmd

def parse_arg(arg: str):
    return arg.strip().split()
class cli(cmd.Cmd):
    prompt = 'Command -> '

    def do_howManySteps(self, number):
        collatz_module.howManySteps(int(number), True)
    def do_toplist(self,arg):
        arg = parse_arg(arg)
        try:
            print(collatz_module.TopListOfNumbersToStep(int(arg[0]),int(arg[1]),int(arg[2])))
        except (IndexError,ValueError):
            print("toplist requires 3 integer arguments")
    def help_toplist():
        print("highest_step_count,startingNumber=2, listLength=10,verbose=False")

if __name__ == "__main__":
    cli().cmdloop()