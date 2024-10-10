class Product:
    products_list=[]
    def __init__(self,p_id,p_name,p_category,p_price):
        
        self.p_id=p_id
        self.p_name=p_name
        self.p_category=p_category
        self.p_price=p_price
        temp=[]
        for i in(p_id,p_name,p_category,p_price):
            temp.append(i)
        Product.products_list.append(temp)
        print(Product.products_list)
    @staticmethod
    def update_byid(p_id,np_id):
           for product in Product.products_list:
               if product[0]==p_id:
                   product[0]=np_id
                   print("P_id has been successfully changed")
    @staticmethod
    def update_bycategory(p_category,np_category):
        for product in Product.products_list:
            if product[2]==p_category:
                product[2]=np_category
                print("category has been changed successfully")
    @staticmethod
    def delete_byid(p_id):
        for i in Product.products_list:
           if p_id in i:
              Product.products_list.remove(i)
        print("removed succesfully")
    @staticmethod
    def get_byid(p_id):
        for i in Product.products_list:
            if p_id in i:
                print(i)
    @staticmethod
    def get_allproducts(products_list):
        print(products_list)
    @staticmethod
    def get_bycategory(p_category):
        for i in Product.products_list:
          if p_category in i:
             print(i[1])
    @staticmethod
    def get_byprices(price1,price2):
        for i in Product.products_list:
            if price1<=i[3] and price2>=i[3]:
                print(i)

if __name__ == '__main__':
    while True:
        choice=int(input(
            """what do you want to do?
            1.Add product
            2.update product
            3.delete product
            4.get by_id
            5.get all products
            6.get products by category
            7.get products by prices"""
        ))
        if choice==1:
            p_id=int(input("enter the id: "))
            p_name=input("enter the name of the product: ")
            p_category=input("enter the category: ")
            p_price=int(input("enter the price: "))
            Product(p_id,p_name,p_category,p_price)
        elif choice==2:
             update=int(input(
                """
                what do you want to update?
                1.update by id
                2.update by category
                """
             ))
             if update==1:
                p_id=int(input("enter old id: "))
                np_id=int(input("enter new input id: "))
                Product.update_byid(p_id,np_id)
             if update==2:
                 p_category=input("enter the old category")
                 np_category=input("enter the new category")
                 Product.update_bycategory(p_category,np_category)      
        elif choice==3:
            delete=int(input(
                """ 
                what do youwant to delete
                1.delete by id
                """
            ))
            if delete==1:
                p_id=int(input("enter id to delete: "))
                Product.delete_byid(p_id)
        elif choice==4:
            get=int(input("enter id to display: "))
            Product.get_byid(p_id)
        elif choice==5:
            Product.get_allproducts(Product.products_list)
        elif choice==6:
            category=input("enter category: ")
            Product.get_bycategory(p_category)
        elif choice==7:
            price1=int(input("enter price between the range : "))
            price2=int(input("enter price between the range : "))
            Product.get_byprices(price1,price2)
        

        