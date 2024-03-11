from config import OWNER_USERNAME, SUPPORT_GRP
from Venom import VenomX

START = f"""
**๏ Salam👋 Mənim Adım {VenomX.name}**
**Qruplar üçün yaradılmış Çat Botuyam.**
**──────────────**
**➻ İstifadəsi /chatbot [on/off]**
<b>||๏ @IlkinOwner hazırlamışdır !||</b>
"""

HELP_READ = f"""
<u>**{VenomX.name}- üçün**</u>
<u>**Əmrlər aşağıda verilmişdir!**</u>
**Bütün əmrləri / ilə istifadə edə bilərsiniz**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

TOOLS_DATA_READ = f"""
<u>**{VenomX.name}- üçün alətlər:**</u>
**➻ Kommand /ping {VenomX.name}- un pingini yoxlayın**
**──────────────**
**➻ öz istifadəçi id, söhbət id və öz id - ni əldə etmək üçün /id komutu ilə istifadə edin.**
**──────────────**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

CHATBOT_READ = f"""
<u>**{VenomX.name}- üçün əmr**</u>
**➻ /chatbot (on/off) ilə aktiv edə bilərsiniz**
**๏ Qeyd yuxarıdakə əmr sadəcə qruplar üçün etibarlıdır!!**
<b>||©️ @{OWNER_USERNAME}||</b>
"""

SOURCE_READ = f"**Salam, [{VenomX.name}](https://t.me/{VenomX.username})- in mənbə kodu aşağıda verilmişdir.**\n**XAHIŞ EDİRƏM REPO-Nİ FORK EDİN VƏ YILDIZI VERİN ✯**\n**──────────────────**\n**MƏNBƏ KODU [burada](https://github.com/venombolteop/ChatbotV2)**\n**──────────────────**\n**ƏGƏR HANSI-SA PROBLEMİ BAŞ VERƏRSƏ, ONDAN SONRA [DƏSTƏK QURULUŞUNA](https://t.me/{SUPPORT_GRP}) MÜRACİƏT EDİN.\n<b>||©️ @{OWNER_USERNAME}||</b>"

ADMIN_READ = f"Yenidir"

ABOUT_READ = f"""
**➻ [{VenomX.name}](https://t.me/{VenomX.username})- in bir çat-botdur.**
**➻ [{VenomX.name}](https://t.me/{VenomX.username})- avtomatik olaraq istifadəçiyə cavab verir.**
**➻ Qruplarınızı aktivləşdirməyinizə kömək edir.**
**➻ [Python](https://www.python.org) ilə yazılıb [MongoDB](https://www.mongodb.com) kimi verilənlər bazası ilə.**
**➻ [{VenomX.name}](https://t.me/{VenomX.username})- haqqında əsas kömək və məlumat üçün aşağıda verilmiş düymələrə basın**
"""
