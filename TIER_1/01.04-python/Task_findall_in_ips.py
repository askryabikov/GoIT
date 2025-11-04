import re

log_file = "Bot activity detected: 192.16.4.162, 69.168.21.343 looks suspicious"

# _, _, _, _  - обычный ip состоит из 4 слотов: 
# 0-255.0-255.0-255.0-255
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}."
# \d - какая-либо цифра
# {1, 3} - от одной до 3 цифр в слоте
# \. - будет искать именно точку (как разделитель слотов)
ips = re.findall(pattern, log_file)
print(ips)