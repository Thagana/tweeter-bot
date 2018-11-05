data="saddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsaddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsadddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"

info = (data[:75] + '..') if len(data) > 75 else data

print(info)