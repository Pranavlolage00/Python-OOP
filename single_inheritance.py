class A:
    def __init__(self):
        print("I am a Base Class")
        return
class B(A):
    def __init__(self):
        print("I am a Derived Class")
        super().__init__()
        return

ob=B()
