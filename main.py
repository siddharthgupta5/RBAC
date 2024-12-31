from src.core.rbac_system import RBACSystem
from src.cli.command_line import CommandLineInterface

def main():
    rbac = RBACSystem()
    cli = CommandLineInterface(rbac)
    cli.run()

if __name__ == "__main__":
    main()