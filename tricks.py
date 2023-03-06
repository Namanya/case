class Device:
	def __init__(self, name, connected_by):
		self.name = name
		self.connect = connected_by
		self.connect = True

	def __str__(self) -> str:
		return f'{self.name!r} is connected {self.connect}'


	def disconnect(self):
		self.connect= False
		print('Disconnected')


		
class Printer(Device):
	def __init__(self, name, connected_by, capacity):
		super().__init__(name, connected_by)
		self.capacity = capacity
		self.remaining_pages= capacity


	def __str__(self) -> str:
		return f'{super().__str__()} {self.remaining_pages} pages remaining'

	def print(self, pages):
		if not self.connect:
			print ('printer not connected')
			return
		print(f'printing {pages} pages')
		self.remaining_pages -= pages 
		return self.remaining_pages

printer = Printer('printer', 'bluetooth', 200)
printer.print(100)
print (printer)
printer.disconnect()
