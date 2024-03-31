 eşzamansız içe aktarma
 içe aktarma kütüphanesini içe aktar

 pirogram  içe aktarma  işlemi boştayken

Venom'dan  LOGGER'ı  içe aktarın  , VenomX
Venom'dan  .​ ALL_MODULES modülleri  içe aktar 


eşzamansız  def  anony_boot ():
    denemek :
         VenomX'i bekleyin . başlangıç ​​()
     Örneğin İstisna  hariç :​ 
        AĞAÇ KESİCİSİ . hata ( örn .)
        bırak ( 1 )

     ALL_MODULES içindeki all_module  için : 
        ithalat kütüphanesi import_module ( "Venom.module'lar."  +  all_module )

    AĞAÇ KESİCİSİ . info ( f"@ { VenomX . kullanıcı adı } aktivdir." )
     boşta bekle ()


if  __name__  ==  "__main__" :
    asenkron . get_event_loop (). run_until_complete ( anony_boot ())
    AĞAÇ KESİCİSİ . info ( "Sohbet Botu 
