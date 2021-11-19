import os
import sys
import xml.etree.ElementTree as ET


path_str = os.getcwd()
path_list = os.listdir(path_str)

temp = []

target_apk = sys.argv[1]

path_glo = ""


#find apk files
for path in path_list:
    temp_str = path_str + "/" + path
    try:
        temp = os.listdir(temp_str)
        temp_str = ""
        if (temp[0][-4:] != ".apk"):
            temp = ""
        else:
            path_glo = path

    except:
        continue

target_apk_str = "\"" + target_apk + "\""
os.system("apktool" + " d " + target_apk_str)


target_apk = target_apk.strip(".apk")
directory = os.path.join(target_apk + "\\" + "AndroidManifest.xml")
root = ET.parse(directory).getroot()
attr = root.attrib
package = attr.get("package")


directory = os.path.join(target_apk + "\\smali")
path = os.walk(directory + "\\" + package.replace(".", "\\"))

for root, directories, files in path:

    for file in files:

        curr_file = os.path.join(root, file)

        f = open(curr_file, "r")

        for line in f:
            if ("http:") in line or ("FakeHostnameVerifier") in line or ("NaiveHostnameVerifier") in line or ("AcceptAllHostnameVerifier") in line or ("proceed()") in line or ("AllowAllHostnameVerifier") in line:

                with open('output.txt', 'a') as f:

                    print(curr_file + line)
                    f.write("path: " + curr_file + line)

        f.close()


