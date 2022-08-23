class A:
    variables = "variables"
    def __init__(self) -> None:
        pass
    
class B:
    def B_Func(txt: str):
        return txt
    
a = A
a.variables = B.B_Func("hello world")
print(a.variables)