class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


class E(C, B):
    pass


try:

    class F(D, E):
        pass

except TypeError as e:
    print("MRO build failed:", e)
