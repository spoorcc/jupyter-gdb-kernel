from ipykernel.kernelbase import Kernel
from subprocess import run

class GDBKernel(Kernel):
    implementation = 'GDB'
    implementation_version = '1.0'
    language = 'gdb'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }

    _banner = None

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output(['gdb', '--version']).decode('utf-8')
        return self._banner


    @staticmethod
    def _execute_gdb_call(commands):

        with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as tmp_file:
            print(commands, tmp_file.name)
            return run(['gdb', '-q', '-x', tmp_file.name]).stdout

    def do_execute(self, code, silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):

        if not silent:
            stream_content = {'name': 'stdout', 'text': code}

            result = self._execute_gdb_call(code)

            self.send_response(self.iopub_socket, 'stream', result)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
                }
