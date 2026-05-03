import requests

API_KEY = "67978f691b0412f948d92228861f04465ccc7e7f71d869e7dd3eef74755da85a"

def check_file(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {
        "x-apikey": API_KEY
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
      
        malicious_count = data['data']['attributes']['last_analysis_stats']['malicious']
        return f"Topilgan xavflar: {malicious_count}"
    else:
        return "Fayl bazada topilmadi yoki xatolik yuz berdi."

