class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
            
# class Observer:
#     def update(self, message):
#         raise NotImplementedError
class ConcreteObserverA():
    def update(self, message):
        print(f"Observer A received: {message}")
class ConcreteObserverB():
    def update(self, message):
        print(f"Observer B received: {message}")
# Usage
subject = Subject()
observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()
subject.attach(observer_a)
subject.attach(observer_b)
subject.notify("State changed!")
