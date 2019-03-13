from cli import main_cli_entry_point
import shlex
import sys

sys.argv = shlex.split("tool " + "--help")
main_cli_entry_point()

sys.argv = shlex.split("tool " + "config docptr --help")
main_cli_entry_point()

