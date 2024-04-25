import cmd
from SynFlood import synflood, conf_iface


class AttackCLI(cmd.Cmd):
    prompt = 'Prepare attack >>'
    intro = 'Welcome to Attack CLI. Type "help" for available commands.'

    def do_syn_flood(self, line):
        synflood('127.0.0.1', 8000, '0.0.0.0', 8080, b'abc', conf_iface)

    def do_brute_force(self, line):
        pass

    def do_quit(self, line):
        #TODO:
        pass


AttackCLI().cmdloop()
