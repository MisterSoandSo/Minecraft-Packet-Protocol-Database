import requests
import json
from bs4 import BeautifulSoup

def extract_packet_data(h4):
    name = h4.text
    table = h4.find_next_sibling('table', class_='wikitable')

    if table:
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = table.find_all('tr')
        packet_id_index = headers.index('Packet ID')
        cells = rows[1].find_all('td')

        if len(cells) > packet_id_index:
            packet_id = cells[packet_id_index].get_text(strip=True)
            name = name.replace(" ", "").replace("(play)", "").replace("(clientbound)", "").replace("(serverbound)", "").replace("(login)", "").replace("(configuration)", "") + "Packet"
            return {name: packet_id}

def main():
    url = input("Url Link: ")
    version_number = input("Version Number: ")
    fn = f"protocols/{version_number}.json"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    h2_elements = soup.find_all('h2')[3:-1]
    h4_elements = soup.find_all('h4')

    packet_data = []
    for h4 in h4_elements:
        packet = extract_packet_data(h4)
        if packet:
            packet_data.append(packet)

    c, s = [{}, {}, {}, {}, {}], [{}, {}, {}, {}, {}]
    i, mode = 0, True
    temp = {}
    
    for p in packet_data:
        key, value = next(iter(p.items()))
        if value == '0x00':
            if mode:
                c[i].update(temp)
                print("client:", c[i])
                mode = False
            else:
                s[i].update(temp)
                print("server:", s[i])
                mode = True
                i += 1
            temp = {}
        temp.update(p)
    s[i].update(temp)

    data = {}
    i = 0
    for h2 in h2_elements:
        temp = {'clientbound': c[i], 'serverbound': s[i]}
        i += 1
        title = h2.text.lower()
        data[title] = temp

    with open(fn, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()
