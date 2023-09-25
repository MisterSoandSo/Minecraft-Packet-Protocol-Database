import requests
import json
from bs4 import BeautifulSoup

url = input("Url Link: ")
fn = "protocols/"+ input("Version Number: ") + '.json'

def extract_table(h4):
    name = h4.text
    # Find the nearest <table> element following the <h4> element
    table = h4.find_next_sibling('table', class_='wikitable')

    if table:
        # Extract the desired information from the table
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = table.find_all('tr')

        packet_id_index = headers.index('Packet ID')
        cells = rows[1].find_all('td')

        if len(cells) > packet_id_index:
            packet_id = cells[packet_id_index].get_text(strip=True)
            name = name.replace(" ","").replace("(play)","").replace("(clientbound)","").replace("(serverbound)","").replace("(login)","").replace("(configuration)","") + "Packet"
            packet_data = { name : packet_id}
            return packet_data


response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

h2_elements = soup.find_all('h2')[3:-1]     #Handshaking Status Login Configuration Play #Configuration is a 1.20.2 classification
h4_elements = soup.find_all('h4')

packet = []
for h4 in h4_elements:
    packet.append(extract_table(h4))

c=[{},{},{},{},{}]     #Handshake client has no packets
s=[{},{},{},{},{}]

i = 0
mode = True
temp = {}
for p in packet:
    key, value = next(iter(p.items()))
    if value == '0x00':
        if mode:
            c[i].update(temp)
            print("client:", c[i])
            mode = False
        else:
            s[i].update(temp)
            print("server:",s[i])
            mode = True
            i+=1
        temp = {}   #Reset table collection
    temp.update(p)
s[i].update(temp)  #handle last server packets

data = {}
i = 0
for h2 in h2_elements:
    temp = {}
    temp.update({'clientbound':c[i]})
    temp.update({'serverbound':s[i]})
    i += 1
    tittle = h2.text.lower()
    data.update({tittle:temp})

#json_string = json.dumps(data, indent=4)
#print(json_string)

with open(fn, 'w') as json_file:
    json.dump(data, json_file, indent=4)