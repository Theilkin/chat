içe aktarma  günlüğü 
ithalat  zamanı
 Abg  içe  aktarma yamasından

motordan  .​ motor_asyncio  AsyncIOMotorClient'ı MongoCli olarak içe aktar   
 pirogram  içe aktarma  istemcisinden
pirogramdan  .​ ParseMode'u içe aktaran numaralandırmalar  

 yapılandırmayı içe aktar

Kerestecilik . temelYapılandırma (
    format = "[%(asctime)s - %(seviyeadı)s] - %(name)s - %(mesaj)s" ,
    datefmt = "%d-%b-%y %H:%M:%S" ,
    işleyiciler = [ günlüğe kaydetme . FileHandler ( "log.txt" ), günlüğe kaydetme . StreamHandler ()],
    seviye = günlüğe kaydetme . BİLGİ ,
)

Kerestecilik . getLogger ( "pirogram" ). setLevel ( günlüğe kaydetme . HATA )
KAYITÇI  =  günlüğe kaydetme . getLogger ( __isim__ )
önyükleme  =  zaman . zaman ()
mongo  =  MongoCli ( yapılandırma . MONGO_URL )
db  =  mongo . Anonim
SAHİBİ  =  yapılandırma . OWNER_ID

 VenomX sınıfı ( İstemci ):
    def  __init__ ( kendisi ):
        Süper (). __içinde__ (
            isim = "VenomX" ,
            api_id = yapılandırma . API_ID ,
            api_hash = yapılandırma . API_HASH ,
            lang_code = "tr" ,
            bot_token = yapılandırma . BOT_TOKEN ,
            in_memory = Doğru ,
            parse_mode = AyrıştırmaModu . VARSAYILAN ,
        )

    async  def  start ( self ):
         süper () bekliyoruz . başlangıç ​​()
        öz . kimlik  =  öz . Ben . İD
        öz . isim  =  kendisi . Ben . ad  +  " "  + ( kendini . ben . soyadını  veya  "" )
        öz . Kullanıcı adı  =  kendisi . Ben . Kullanıcı adı
        öz . bahsetme  =  kendinden . Ben . değinmek

    async  def  stop ( self ):
         süper () bekliyoruz . durmak ()


VenomX  =  VenomX ()
