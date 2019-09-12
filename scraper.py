import json
import urllib
import urllib.request
import os




with open('personasdesaparecidas.json', 'r', encoding="utf8") as f:
        datastore = json.load(f)
#print(datastore[280])
#for i in range(280,len(datastore)):
#    url = datastore[i]['foto']['url']
#    name = "Imagenes/foto" + str(i)+".jpg"
#    if url != "":
#        urllib.request.urlretrieve(url, name)

for i in range(len(datastore)):
    url = datastore[i]['foto']['url']
    prim_nombre = datastore[i]['versiones'][0]['prim_nombre']
    seg_nombre = datastore[i]['versiones'][0]['seg_nombre']
    apellido_pat = datastore[i]['versiones'][0]['apellido_pat']
    apellido_mat = datastore[i]['versiones'][0]['apellido_mat']
    nombre = prim_nombre + "_" + seg_nombre + "_" + apellido_pat + "_" + apellido_mat
    dir = "Imagenes/" + nombre
    if not os.path.exists(dir):
        os.makedirs(dir)
    name = dir + "/" + nombre + ".jpg"
    if url != "":
        urllib.request.urlretrieve(url, name)
