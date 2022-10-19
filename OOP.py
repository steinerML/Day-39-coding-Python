
class Hamburguer: #Class definition
    

    def __init__(self,meat,origin,protein,bio,temp,stock,price,farmer):

    #Attributions definition
    
        self.meat = meat
        self.origin = origin
        self.protein = protein
        self.bio = bio
        self.temp = temp
        self.stock = stock
        self.price = price
        self.farmer = farmer


    #Methods definition
    def cook(self):
        print("The hamburguer is being cooked at "+self.temp)
    
    def diet(self):
        print("The hamburguer has a % of protein around "+self.protein)
    
    def serve(self):
        print("The hamburguer being served comes from "+self.origin)
    
    def eat(self):
        print("The hamburguer being eaten is "+self.bio)
        
    def review(self):
        print('The hamburguer is being reviewed')

h0 = Hamburguer('Beef','Argentina','98%','Bio','52 C','In Stock','$89/Kg','Harris & Sons Farming Co.')
h1 = Hamburguer('Lamb','Ireland','100%','Bio','53 C','In Stock','$85/Kg','OKean Farming Co.')
h2 = Hamburguer('Lamb','USA','99%','Bio','60 C','In Stock','$78/Kg','Harrisson Lampart Farming Co.')
h3 = Hamburguer('Cow','Germany','100%','Not-Bio','56 C','In Stock','$87/Kg','Meat 200 Gmbh.')
h4 = Hamburguer('Buffalo','Netherlands','99%','Bio','55 C','In Stock','$82/Kg','BroodjeKaas Hoeve Bv')
h5 = Hamburguer('Beef','Belgium','99%','Bio','53 C','In Stock','$83/Kg','Meat Nv')
h6 = Hamburguer('Lamb','Spain','99%','Not-Bio','61 C','In Stock','$81/Kg','Granjas Reunidas S.L')
h7 = Hamburguer('Beef','Spain','99%','Bio','58 C','In Stock','$68/Kg','Los Bueyes Hermanos S.A')
h8 = Hamburguer('Lamb','Mexico','99%','Not-Bio','56 C','In Stock','$72/Kg','Viva Mexico Cabrones S.A')

#Calling Methods
h0.cook()
h0.diet()
h0.serve()
h0.eat()
h0.review()

h1.cook()
h1.diet()
h1.serve()
h1.eat()
h1.review()

h2.cook()
h2.diet()
h2.serve()
h2.eat()
h2.review()

h3.cook()
h3.diet()
h3.serve()
h3.eat()
h3.review()

h4.cook()
h4.diet()
h4.serve()
h4.eat()
h4.review()

h5.cook()
h5.diet()
h5.serve()
h5.eat()
h5.review()

h6.cook()
h6.diet()
h6.serve()
h6.eat()
h6.review()

h7.cook()
h7.diet()
h7.serve()
h7.eat()
h7.review()

h8.cook()
h8.diet()
h8.serve()
h8.eat()
h8.review()

#Random Class calls

print("This meat being served is of "+h1.meat+" type")
print("This meat comes from "+h1.origin)
print("The protein content is around "+h1.protein)