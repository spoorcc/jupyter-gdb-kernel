import unittest
from jupyter-gdb-kernel.kernel import GDBKernel

class GDB_calls(unittest.TestCase):

    def test_calling_gdb(self):

        GDBKernel._execute_gdb_call('\n'.join(['import gdb',
                                               'gdb.execute("printf \"Hello world\n\"")',
                                                'gdb.quit()']))


if __name__ == '__main__':
    unittest.main()
