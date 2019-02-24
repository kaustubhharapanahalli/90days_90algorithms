count = int(input())

ph_no = {}
for i in range(count):
    name, num = list(input().split())
    ph_no[name.lower()] = num


for i in range(count):
    search_name = input()
    if search_name.lower() in ph_no.keys():
        print("{}={}".format(search_name, ph_no[search_name]))
    else:
        print("Not found")
