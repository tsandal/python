from xml.etree import ElementTree as ET
tree = ET.parse("list.xml")
root = tree.getroot()
#zipa = root.findall("zip")
zip_num = root.attrib.get("zip_num")
print("zip包的总数为：" + zip_num)
listall = []
for i in range(int(zip_num)):
    zip_name = root[int(i)].attrib.get("name")
    tar_num = root[int(i)].attrib.get("tar_num")
    print(zip_name + "下tar包的总数为：" + tar_num)
    for j in range(int(tar_num)):
        tar_name = root[int(i)][int(j)].attrib.get("name")
        tar1_num = root[int(i)][int(j)].attrib.get("tar1_num")
#        print(tar_name + "下tar1包的总数为：" + tar1_num)
        for k in range(int(tar1_num)):
            tar1_name = root[int(i)][int(j)][int(k)].attrib.get("name")
            so_num = root[int(i)][int(j)][int(k)].attrib.get("so_num")
            list1 = []
            list1.append(zip_name)
            list1.append(tar_name)
            list1.append(tar1_name)
            for m in range(int(so_num)):
                so_name = root[int(i)][int(j)][int(k)][int(m)].attrib.get("name")
                list1.append(so_name)
            listall.append(list1)
print(listall)