import cmd

from attacks import create_multithreaded_attack, syn_flood_attack, url_buster_attack, http_flood_attack


class AttackCLI(cmd.Cmd):
    prompt = 'Prepare attack >>'
    intro = 'Welcome to Attack CLI. Type "help" for available commands.'

    def do_syn_flood(self, line):
        create_multithreaded_attack(syn_flood_attack)

    def do_url_brute_force(self, line):
        create_multithreaded_attack(url_buster_attack)

    def do_http_flood(self, line):
        create_multithreaded_attack(http_flood_attack)

    def do_quit(self, line):
        quit()


AttackCLI().cmdloop()
