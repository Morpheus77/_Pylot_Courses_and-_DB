from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        
        self.load_model('Course')
        self.db = self._app.db

	def index(self):
		return "hello world"
		
	def hello(self):
		return "hello world"
