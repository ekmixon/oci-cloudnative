import os
import unittest
from util.Docker import Docker

class GoServices(unittest.TestCase):
    def test_go(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        code_dir = f"{script_dir}/.."
        goPath = os.environ['GOPATH']
        command = [
            'docker',
            'run',
            '--rm',
            '-v',
            f'{goPath}:/go/',
            '-v',
            f'{code_dir}:/go/src/github.com/microservices-demo/payment',
            '-w',
            '/go/src/github.com/microservices-demo/payment',
            '-e',
            'GOPATH=/go/',
            'golang:1.7',
            'go',
            'test',
            '-v',
            '-covermode=count',
            '-coverprofile=coverage.out',
        ]


        print(Docker().execute(command, dump_streams=True))


if __name__ == '__main__':
    unittest.main()
