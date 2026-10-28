import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

catalog_map = {
    "delonghi_magnifica_s": "B00400OMU0",
    "krups_essential": "B00INSX904",
    "philips_series_2200": "B07MMSHC4R",
    "cosori_dual_blaze": "B07N8N6C85",
    "ninja_foodi_dualzone": "B08GC1QZ5W",
    "roborock_q8_max": "B0C7VMFRDZ",
    "dreame_d10s_pro": "B0BKGL6V9C",
    "comfee_mddf_20den7": "B07KJX6RDK",
    "pro_breeze_20l": "B077H1MZ35",
    "ecoflow_river_2_pro": "B0BFQD5RMJ",
    "bluetti_eb55": "B0B5RJSPD6",
    "nuki_smart_lock_pro_4": "B0DX2FPQFQ",
    "yale_linus_l2": "B0CRHS6W72"
}

headers = [
    '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    '-H', 'Accept-Language: es-ES,es;q=0.9,de-DE,de;q=0.8'
]

all_ok = True
print("VERIFYING ALL 13 PRODUCTS ACROSS AMAZON.ES AND AMAZON.DE:")
print("-" * 75)
for pid, asin in catalog_map.items():
    url_es = f"https://www.amazon.es/dp/{asin}?tag=shopvseu-21"
    url_de = f"https://www.amazon.de/dp/{asin}?tag=shopvseu-21"
    
    cmd_es = ['curl.exe', '-s', '-L', '-o', 'nul', '-w', '%{http_code}'] + headers + [url_es]
    code_es = subprocess.run(cmd_es, capture_output=True, text=True).stdout.strip()
    
    cmd_de = ['curl.exe', '-s', '-L', '-o', 'nul', '-w', '%{http_code}'] + headers + [url_de]
    code_de = subprocess.run(cmd_de, capture_output=True, text=True).stdout.strip()
    
    status = "OK [200/200]" if code_es == '200' and code_de == '200' else f"FAIL [{code_es}/{code_de}]"
    if code_es != '200' or code_de != '200':
        all_ok = False
    print(f"{pid:<25} | ASIN: {asin} | ES: {code_es} | DE: {code_de} | {status}")

print("-" * 75)
if all_ok:
    print("ALL 13 PRODUCTS 100% VERIFIED ACTIVE (200 OK) ON BOTH MARKETPLACES!")
else:
    print("SOME PRODUCTS FAILED!")
