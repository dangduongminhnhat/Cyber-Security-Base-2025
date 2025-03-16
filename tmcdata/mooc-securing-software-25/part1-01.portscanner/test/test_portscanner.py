#!/usr/bin/env python3

import unittest
from tmc import points
from tmc.utils import load, get_out

import socket
import _thread
import random


def local_dummy_server(server):
	server.accept()


module_name="src.portscanner"
scanner = load(module_name, "get_accessible_ports")


@points('1.1.1 1.1.2 1.1.3 1.1.4 1.1.5')
class PortScanner(unittest.TestCase):

	def test_scan(self):
		for i in range(3):
			port = random.randint(20000, 30000)
			min_port = port - random.randint(0, 10)

			server = socket.socket()
			server.bind(('localhost', port))
			server.listen(1)

			_thread.start_new_thread(local_dummy_server, (server,))

			found = scanner('localhost', min_port, min_port + 10)
			self.assertEqual(found, [port], 'port scanner did not find the correct port')


	def test_first(self):
		port = random.randint(20000, 30000)

		server = socket.socket()
		server.bind(('localhost', port))
		server.listen(1)

		_thread.start_new_thread(local_dummy_server, (server,))

		found = scanner('localhost', port, port + 10)
		self.assertEqual(found, [port], 'port scanner did not test min_port')


	def test_last(self):
		port = random.randint(20000, 30000)

		server = socket.socket()
		server.bind(('localhost', port))
		server.listen(1)

		_thread.start_new_thread(local_dummy_server, (server,))

		found = scanner('localhost', port - 10, port)
		self.assertEqual(found, [port], 'port scanner did not test max_port, check the range of your for-loop')
