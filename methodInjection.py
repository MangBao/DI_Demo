class A:
    def A_Func(txt = "Hello Text") -> None:
        return txt
    
class B:
    def B_Func(txtHalo: str):
        return txtHalo
    
a = A
txt = B.B_Func(txtHalo="Good afternoon")

print(a.A_Func(txt=txt))