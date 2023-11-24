import os
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
import requests
import json
import uvicorn
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# (mostrar todos los de un año)
app = FastAPI()



def mostrar_por_año():
    años={}
    for feature in archivo_json["features"]:
        atributos = feature["attributes"]
        nombre_patrimonio=atributos["Nombre"]

        año=atributos["Año_inscripción"]
        if año not in años:
            años[año]=[]
            años[año].append(nombre_patrimonio)
        else:
            años[año].append(nombre_patrimonio)

    return json.dumps(años)

    
    


#mostrar todos los culturales o naturales


def mostrar_naturales():
    naturales=[]
    for feature in archivo_json["features"]:
        atributos = feature["attributes"]
        nombre_patrimonio=atributos["Nombre"]
        tipo=atributos["Tipo"]
        if tipo =="Natural":
            naturales.append(nombre_patrimonio)

    return json.dumps({"naturales": naturales})

    


#mostrar de insertados por año

def numero_patrimonios():
    numero=0
    for feature in archivo_json["features"]:
        numero+=1
    print(numero)
    return json.dumps({"numero_patrimonios": numero})    



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # o especifica tus dominios permitidos
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


url="https://services1.arcgis.com/nCKYwcSONQTkPA4K/arcgis/rest/services/Patrimonio_de_la_unesco/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
response= requests.get(url)

archivo_json=response.json()




@app.get("/")
async def get_index_html():
    html_file_path = os.path.join("static", "index.html")
    return FileResponse(html_file_path)

@app.get("/mostrar_anyo")
async def get_mostrar_por_año():
    return mostrar_por_año()

@app.get("/mostrar_naturales")
async def get_mostrar_naturales():
    return mostrar_naturales()

@app.get("/mostrar_Numpatrimonios")
async def get_numero_patrimonios():
    return numero_patrimonios()


