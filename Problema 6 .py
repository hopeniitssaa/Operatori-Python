n = int(input("dati n: "))
if n<= 10000:
    n= str(n)
    a=(len(n))
    b=a-1
    
    print("ultima cifra a acestui numar: ", n[b])
    print("suma tuturor cifrelor:", sum(map(int,list(n))))
    n= int(n)
    print("restul impartirii acestui numar la 9: ",n%9)
    print("catul acestui numar imparti la 9: ", n//9)
    n=str(n)
    
    if(b>0):
        print("penultima cifra a acestui numar: ", n[b-1])
        i=n[::-1]
        print("acest numar scris invers: ", i)
        
    else:
 
 
  
      print("acest numar este format dintr-o cifra")
       
      
      
      

     





    
    
    

else:
     print("acest numar este prea mare")
     