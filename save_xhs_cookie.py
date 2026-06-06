"""将小红书Raw Cookie转换为Playwright storage_state JSON"""
import json, os, re
from pathlib import Path

raw = "abRequestId=aafa2023-ef99-549e-b807-e32b35d93bd5; a1=19de948907d8kjrql9hp4t2jks993ifnrbgjqkzp050000939742; webId=b600a20c8af882f5437ff6a18d9c956b; x-user-id-creator.xiaohongshu.com=67fd08c0000000000e013be3; customerClientId=368031990396610; x-rednote-datactry=CN; x-rednote-holderctry=CN; x-hng=lang=zh-CN&domain=www.xiaohongshu.com; x-hng=lang=zh-CN&domain=creator.xiaohongshu.com; access-token-creator.xiaohongshu.com=customer.creator.AT-68c517640852454469566466yxhvdyfkb2cqx3vh; galaxy_creator_session_id=7JwFCrRglSo5wfs6nR0Ee6jlWKdXJoqSQr9r; galaxy.creator.beaker.session.id=1779024595439094302261; xsecappid=xhs-pc-web; web_session=040069b6894b886b6bb5ad0225384b451ea32c; id_token=VjEAAKnPYL7hW/f4l48rZ6p35IbmYdu0J4YqF51M4mS/dq8Kc2huPOfVKV+0X4wl5rMfGHFJ4ICmYMYu3Mu3qs5IsfO338jYzdSpKkSTAOus8FxpFHJxQRqjblxXexEkIIxraJ6/; ets=1780447344743; unread={%22ub%22:%226a1d17c20000000036031b44%22%2C%22ue%22:%226a155d7d000000003502452b%22%2C%22uc%22:29}; webBuild=6.15.0; loadts=1780713928763; acw_tc=0ad6fbf217807303630568827e38ede74d99b01205b58523649eab0018209c; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=4d9d8764-138b-46d5-a197-6d3649f5f9b0"

# 解析cookie字符串
cookies = []
for item in raw.split("; "):
    if "=" not in item:
        continue
    name, value = item.split("=", 1)
    name = name.strip()
    value = value.strip()
    
    # 判断domain
    if ".xiaohongshu.com" in name:
        # 有些cookie名含域名后缀，提取域名
        parts = name.rsplit(".", 1)
        domain = ".xiaohongshu.com"
    else:
        domain = ".xiaohongshu.com"
    
    # 判断属性
    secure = True  # 小红书基本都是HTTPS
    http_only = name in ("web_session", "acw_tc", "websectiga", "sec_poison_id", "id_token", "access-token-creator.xiaohongshu.com", "galaxy.creator.beaker.session.id", "galaxy_creator_session_id", "ets", "unread")
    
    cookies.append({
        "name": name,
        "value": value,
        "domain": domain,
        "path": "/",
        "expires": -1,
        "httpOnly": http_only,
        "secure": secure,
        "sameSite": "Lax"
    })

# 添加 creator.xiaohongshu.com 也需要的cookie副本
creator_cookies = []
for c in cookies:
    cc = dict(c)
    cc["domain"] = ".creator.xiaohongshu.com"
    creator_cookies.append(cc)

# 合并
all_cookies = cookies + creator_cookies

state = {
    "cookies": all_cookies,
    "origins": [
        {
            "origin": "https://www.xiaohongshu.com",
            "localStorage": []
        },
        {
            "origin": "https://creator.xiaohongshu.com",
            "localStorage": []
        }
    ]
}

# 写入文件
out_dir = Path("D:/@kaifa/social-auto-upload/cookies")
out_dir.mkdir(exist_ok=True)
out_path = out_dir / "xiaohongshu_玲丽.json"

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"Cookies saved: {out_path}")
print(f"Total cookies: {len(all_cookies)} ({len(cookies)} unique × 2 domains)")
print(f"File size: {os.path.getsize(out_path)} bytes")
