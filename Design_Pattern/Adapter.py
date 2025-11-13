class OldSystem:
    def old_request(self):
        return "Old system request"
    
    
class NewSystem:
    def new_request(self):
        return "New system request"
    
    
class Adapter:
    def __init__(self, old_system):
        self._old_system = old_system
    def old_request(self):
        return self._old_system.old_request()
    def new_request(self):
        return self._old_system.new_request()
    
    
# Client code
old_obj = OldSystem()
adapter = Adapter(old_obj)
print(adapter.old_request())

new_sys = NewSystem()
adapter = Adapter(new_sys)
print(adapter.new_request())
