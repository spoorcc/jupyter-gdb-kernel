#!/usr/bin/env python3

import unittest
from jupyter_gdb_kernel.kernel import GDBKernel

class GDB_calls(unittest.TestCase):

    def test_calling_gdb(self):

        script = \
        u'''
        import gdb
        gdb.execute('printf \"Hello world\\n\"')
        gdb.execute('quit')'''

        kernel = GDBKernel()
        result = kernel._execute_gdb_call(script)

        for k, v in result.__dict__.items():
            print('Key {}:{}'.format(k,v))

        self.assertEquals(result, 'Hello world')



if __name__ == '__main__':
    unittest.main()
