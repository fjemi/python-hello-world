"""helloworld.py"""

from dataclasses import dataclass

@dataclass
class HelloWorld:
  '''Simple class to print Hello World!'''
  string: str = 'Hello World!'
  
  def __post_init__(self):
    print(self.string)
  
if __name__ == '__main__':
  HelloWorld()
