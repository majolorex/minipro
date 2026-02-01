import urllib.request
import ssl

# Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

images = {
    "ประวัติศาสตร์.jpg": "https://images.unsplash.com/photo-1590422892576-9f33ae2ebba3?q=80&w=2070",
    "สถาปัตยกรรม.jpg": "https://images.unsplash.com/photo-1548011270-b6c867ee429f?q=80&w=1887",
    "วิถีชีวิต & อาหาร.jpg": "https://images.unsplash.com/photo-1626509744111-c91895a97576?q=80&w=1974",
    "อนุสา.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/King_Mangrai_Monument_Chiang_Rai.jpg/640px-King_Mangrai_Monument_Chiang_Rai.jpg",
    "วัด.jpg": "https://images.unsplash.com/photo-1599540263690-e5bf7e822008?q=80&w=2070",
    "ดอยสุเทพ.jpeg": "https://images.unsplash.com/photo-1598935898627-66953dd4eb43?q=80&w=1974",
    "เรือนกาแล.jpeg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Traditional_Thai_house_Lanna_style.jpg",
    "วิหาร.jpeg": "https://images.unsplash.com/photo-1627885375533-3e1150499e90?q=80&w=2074",
    "เจดี.jpeg": "https://images.unsplash.com/photo-1587524962295-d261e57c62d0?q=80&w=2062",
    "ประตู.jpeg": "https://images.unsplash.com/photo-1721545625440-cc54cf3c09f3?q=80&w=2070",
    "ข้าวซอยไก่.jpeg": "https://images.unsplash.com/photo-1626804475297-411d8c669143?q=80&w=2070",
    "ไส้อั่ว.jpeg": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Sai_ua.jpg",
    "น้ำพริกอ่อง.jpeg": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Nam_phrik_ong.jpg",
    "น้ำพริกหนุ่ม.jpeg": "https://upload.wikimedia.org/wikipedia/commons/0/06/Nam_phrik_num.jpg",
    "แกงฮังเล.jpeg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Kaeng_hang_le.jpg/1280px-Kaeng_hang_le.jpg",
    "ลาบเหนือ.jpeg": "https://images.unsplash.com/photo-1605333396915-47ed6b68a00e?q=80&w=2070",
    "การแต่งกายชายล้านนา.jpeg": "https://images.unsplash.com/photo-1590497556637-a162232a00c6?q=80&w=2070",
    "ผ้า.jpeg": "https://images.unsplash.com/photo-1579783902614-a3fb39274c50?q=80&w=2094",
    "สันกำแพง.jpeg": "https://images.unsplash.com/photo-1528458909336-e7a0adfed0a5?q=80&w=2070",
    "รมดำ.jpeg": "https://images.unsplash.com/photo-1610419885836-e4277b963cc0?q=80&w=2070"
}

for filename, url in images.items():
    print(f"Downloading {filename}...")
    try:
        # User-agent to avoid 403 on some sites
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req, context=ctx) as response, open(filename, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
