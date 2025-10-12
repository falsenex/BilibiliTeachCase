import requests
import json

# 准备数据
data = {
    "currentQueryType": "FLIGHT_LIST",
    "currentSegIndex": 0,
    "selectedRoutes": [],
    "productType": "CASH",
    "routes": [
        {
            "arrCode": "UYN",
            "depCode": "SIA",
            "flightDate": "20250625",
            "arrCodeType": "1",
            "depCodeType": "1",
            "depCityName": "西安",
            "arrCityName": "榆林",
            "segIndex": 0
        }
    ],
    "tripType": "OW",
    "cabinGrade": "",
    "zoneCode": "STRANGE_SHOPPING",
    "salesChannel": "7701",
    "moduleX": "mShopping",
    "os": "M",
    "appVersion": "99.0.0",
    "transactionId": "05202506240857418869"
}

# 发送请求
response = requests.post(
    'http://localhost:3000/api/encrypt',
    json=data
)

# 处理响应
if response.status_code == 200:
    result = response.json()
    print("加密结果:", result['encryptedData'])
else:
    print(f"请求失败: {response.status_code}")
    print("错误详情:", response.json())
# 'yX67CAY2RrMSJ1TxneWBANxXBK5wL6Rvk2bDRa+DKUspUee9v69x1s3TH1rv8tP4wG6sJnnrJmZfMM7TEqmnisgTL6BdEeeLi7oyL6S3MwvEjGQlqs0iPesluloSgPHLd9fQCwbcvjzG10olmLTRo9VwZnF7QDWNq76Wtwmtq+w/A8TjPEkM7+ZmuIAyA6ViSr2N0lDaS9CLIvm3hjONU96wVfhI5yC0CLuUveWCDcdMutEPyUcBYm/8yAUwvJN48Gh9O8eapCtfdXXiHvzjfy4ueZ8Z5sIsXhzRmxy2mF/uKc1XiQpqRrKn9IeRW0vu1objX/DsMVARb0F3MP2ddef45JCHiQ4JN4BfAqdg+ZkfN8oH2S/h5Z/71v6HvEfbl383/DiE8c/Jp7X9zo7C7fz8ReNK7q7nrZgYd1s7e7/zj8oVfsRs617b6BqT/eeBV9ILbPTsGqTMHgHp1iUrotSa5Wz5u2ZGyF/wf0voIJrOl3ogUdD2GAp3GngGZ5joucKPcEh8RolFNvFEn6W/NunE8fjWm/HqpnHDFbpGb8hLHwleOP8qXcehmSF4pquynX+rxP+7N0fcIVtQzGlUrA=='
#  yX67CAY2RrMSJ1TxneWBANxXBK5wL6Rvk2bDRa+DKUspUee9v69x1s3TH1rv8tP4wG6sJnnrJmZfMM7TEqmnisgTL6BdEeeLi7oyL6S3MwvEjGQlqs0iPesluloSgPHLd9fQCwbcvjzG10olmLTRo9VwZnF7QDWNq76Wtwmtq+w/A8TjPEkM7+ZmuIAyA6ViSr2N0lDaS9CLIvm3hjONU96wVfhI5yC0CLuUveWCDcdMutEPyUcBYm/8yAUwvJN48Gh9O8eapCtfdXXiHvzjfy4ueZ8Z5sIsXhzRmxy2mF/uKc1XiQpqRrKn9IeRW0vu1objX/DsMVARb0F3MP2ddef45JCHiQ4JN4BfAqdg+ZkfN8oH2S/h5Z/71v6HvEfbl383/DiE8c/Jp7X9zo7C7fz8ReNK7q7nrZgYd1s7e7/zj8oVfsRs617b6BqT/eeBV9ILbPTsGqTMHgHp1iUrotSa5Wz5u2ZGyF/wf0voIJrOl3ogUdD2GAp3GngGZ5joucKPcEh8RolFNvFEn6W/NunE8fjWm/HqpnHDFbpGb8hLHwleOP8qXcehmSF4pquynX+rxP+7N0fcIVtQzGlUrA==