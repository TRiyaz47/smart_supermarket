import mysql.connector as mc

def prt(prd_id):
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='mes_stocks')
        cursor=conn.cursor()

        prd_check_query=f"SELECT * FROM product where prd_id={prd_id};"
        cursor.execute(prd_check_query)
        feedback=cursor.fetchall()
        
        if feedback==[]:
            return False
        else:
            return feedback 
    
    except Exception as e:
        conn.rollback()
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()
    

def add_prd():
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='mes_stocks')
        cursor=conn.cursor()
        conn.start_transaction()


        prd_id=abs(int(input("Product id:")))
        prd_check_query=f"SELECT prd_name FROM product WHERE prd_id={prd_id};"
        cursor.execute(prd_check_query)
        
        feedback=cursor.fetchall()
        print(f"The feedback receive is:{feedback}")
        
        if feedback==[]:
            prd_name=input("Product name:")
            prd_type=input("Product type:")
            prd_price=abs(int(input("Product price:")))
            prd_quantity=abs(int(input("Product Quantity")))
            #INSERT INTO product VALUES(121,"jimjam","A",50,10);
            query_to_add=f"INSERT INTO product (prd_id,prd_name,type,price,quantity) VALUES({prd_id},'{prd_name}','{prd_type}',{prd_price},{prd_quantity});"
            cursor.execute(query_to_add)
            temp_feedback=cursor.fetchall()
        else:
            prd_quantity=abs(int(input("Product Quantity:")))
            query_add_more=f"UPDATE product SET quantity=quantity+{prd_quantity};"
            cursor.execute(query_add_more)
            temp_feedback=cursor.fetchall()
    except Exception as error:
        #print(f"An error occured:",error)
        conn.rollback() 
        return False
    finally:
        cursor.close()
        conn.commit()
        conn.close()

        
#decrease quantity
#remove certain product
#change type,name,price,
def change_details():
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='mes_stocks')
        cursor=conn.cursor()
        conn.start_transaction()
        
        prd_id=abs(int(input("Product id:")))
        prd_check_query=f"SELECT prd_name FROM product WHERE prd_id={prd_id};"
        cursor.execute(prd_check_query)
        feedback=cursor.fetchall()

        if feedback==[]:
            #print("Product with product id doesen't exist")
            return False
        else:
            prd_name=input("Product name:")
            prd_type=input("Product type:")
            prd_price=abs(int(input("Product price:")))
            prd_quantity=abs(int(input("Product Quantity")))
            
            query_to_change=f"UPDATE product SET prd_name='{prd_name}',type='{prd_type}',price={prd_price},quantity={prd_quantity} WHERE prd_id={prd_id};"
            cursor.execute(query_to_change)
            temp_feedback=cursor.fetchall()
            
            if temp_feedback==[]:
                return False
            else:
                return True
        
    except Exception as error:
        #print(f"An error occured:",error) 
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.commit()
        conn.close()

def prd_delete():
    try:
        conn=mc.connect(host='localhost',username='root',password='Tanwar9867@',database='mes_stocks')
        cursor=conn.cursor()
        conn.start_transaction()
        prd_id=abs(int(input("Product id:")))
        confirmation=None
        while True:
            confirmation=input("Are you sure you want to delete this product?(Y/N):")
            if confirmation == "Y":
                break
            else:
                return None
        delete_query=f"DELETE FROM product WHERE prd_id={prd_id};"
        cursor.execute(delete_query)
        temp=cursor.fetchall()
        print("Product deleted successfully")

    except Exception as error:
        #print("An unexpected error occured",error)
        conn.rollback()
        return False
    finally:
        conn.commit()
        cursor.close()
        conn.close()




