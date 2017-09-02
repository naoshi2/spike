import yaml

with open("data.yaml") as f:
    data = yaml.load(f)

print len(data)
print data['aaa']['text']
print data['aaa']['hashtag']

key_list = data.keys()
print len(key_list)
print key_list[0]