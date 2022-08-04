from src.shapes import *

# t1 = Test()

# t1.test_cir()
# t1.test_tri()
# t1.test_sq()
# t1.test_rec()

while True:
    print("__shape program__\n\n")

    def select_area():
        if inp.get_algo() == "area":
            return True

    def again():
        if inp.ask_again() == "y":
            return True 
        else:
            return False

    inp = Input()
    shape = inp.get_shape()
    
    if shape == "cir":
        cir = Circle()
        if select_area():
            print("___area of cir___\n   (radius)\n")
            cir.get_area()
        else:
            print("___perim of cir___\n   (diameter)\n")
            cir.get_perim()
    elif shape == "tri":
        print("___area of tri___\n (base/height)\n")
        tri = Triangle()
        tri.get_area()
    elif shape == "sq":
        sq = Square()
        if select_area():
            print("___area of sq___\n   (length)\n")
            sq.get_area()
        else:
            print("___perim of sq___\n   (length)\n")
            sq.get_perim()
    elif shape == "rec":
        rec = Rectangle()
        if select_area():
            print("___area of rec___\n (length/height)\n")
            rec.get_area()
        else:
            print("___perim of rec___\n (length/height)\n")
            rec.get_perim()
    
    if not again():
        break
