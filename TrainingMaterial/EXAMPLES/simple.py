#!/usr/bin/env python3

class Simple:
	def __init__(self):
		self.msg = "Hello"

	def info(self):
		return self.msg

if __name__ == "__main__":
	s = Simple()
	print(s.info())

