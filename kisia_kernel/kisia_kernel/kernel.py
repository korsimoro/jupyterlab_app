from ipykernel.kernelbase import Kernel
from cli import run_script
from subprocess import check_output
import os.path
import re
import signal

__version__ = '0.7.1'

version_pat = re.compile(r'version (\d+(\.\d+)+)')

with open("/tmp/output",'w+') as outfile:
    print("STARTED",file=outfile)

class KisiaKernel(Kernel):
    implementation = 'bash_kernel'
    implementation_version = __version__

    @property
    def language_version(self):
        m = version_pat.search(self.banner)
        return m.group(1)

    _banner = None

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output(['bash', '--version']).decode('utf-8')
        return self._banner

    language_info = {'name': 'bash',
                     'codemirror_mode': 'shell',
                     'mimetype': 'text/x-sh',
                     'file_extension': '.sh'}

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        with open("/tmp/output",'w+') as outfile:
            print("CREATED",file=outfile)

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        with open("/tmp/output",'w+') as outfile:
            code = code.strip()

            print("CODE:",code,file=outfile)

            if code == "":
                return {'status': 'ok', 'execution_count': self.execution_count,
                        'payload': [], 'user_expressions': {}}

            #output = pexpect.run('python -m cli.__init__ '+code)
            result = run_script(code)
            if type(result) == list:
                body = ""
                for r in result:
                    body = body + r.output
            else :
                body = result.output

            print("RESULT:",body,file=outfile)
            self.send_response(self.iopub_socket,'display_data',
                { 'source':'kisia',
                    'data': { 'text/plain': body },
                    'metadata' : {}})

            if not silent:
                return {'status': 'ok', 'execution_count': self.execution_count,
                                        'payload': [], 'user_expressions': {}}


            print("NO RETURN, SILENT:",silent,file=outfile)


    def do_complete(self, code, cursor_pos):
        code = code[:cursor_pos]
        default = {'matches': [], 'cursor_start': 0,
                   'cursor_end': cursor_pos, 'metadata': dict(),
                   'status': 'ok'}

        if not code or code[-1] == ' ':
            return default

        tokens = code.replace(';', ' ').split()
        if not tokens:
            return default

        matches = []
        token = tokens[-1]
        start = cursor_pos - len(token)

        if token[0] == '$':
            # complete variables
            cmd = 'compgen -A arrayvar -A export -A variable %s' % token[1:] # strip leading $
            output = self.bashwrapper.run_command(cmd).rstrip()
            completions = set(output.split())
            # append matches including leading $
            matches.extend(['$'+c for c in completions])
        else:
            # complete functions and builtins
            cmd = 'compgen -cdfa %s' % token
            output = self.bashwrapper.run_command(cmd).rstrip()
            matches.extend(output.split())

        if not matches:
            return default
        matches = [m for m in matches if m.startswith(token)]

        return {'matches': sorted(matches), 'cursor_start': start,
                'cursor_end': cursor_pos, 'metadata': dict(),
                'status': 'ok'}
