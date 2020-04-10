import urllib.parse
import urllib.request
import json
from selenium import webdriver
driver = webdriver.Chrome()

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    #Escribimos el lugar
    address = input('Entrar ciudad: ')
    #Se abre la página de la sede catastro
    url = "https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx"
    driver.get(url)
    if len(address) < 1 : break
    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address,'key':''})
    print('Recuperando los datos de la ciudad', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Recuperados',len(data),'caracteres')
    try: js = json.loads(data)
    except: js = None
    if "status" not in js or js['status'] != 'OK':
        print('==== Fallo de recuperación ====')
        print(data)
        continue
    print(json.dumps(js, indent=4))
    coord = driver.find_element_by_link_text("COORDENADAS")
    #Click coordenadas
    coord.click()
    #Selecciona latitud y longitud
    lat=driver.find_element_by_id("ctl00_Contenido_txtLatitud")
    lon=driver.find_element_by_id("ctl00_Contenido_txtLongitud")
    latitud = js["results"][0]["geometry"]["location"]["lat"]
    longitud = js["results"][0]["geometry"]["location"]["lng"]
    from selenium.webdriver.common.action_chains import ActionChains
    driver.implicitly_wait(30)
    #Convertimos los String de json a reales e introducimos en la url del catastro
    ActionChains(driver).move_to_element(lat).click(lat) # Para provocar el click en la caja y que salte el JavaScript
    lat.send_keys(json.dumps(float(latitud)))
    ActionChains(driver).move_to_element(lon).click(lon) # Para provocar el click en la caja y que salte el JavaScript
    lon.send_keys(json.dumps(float(longitud)))
    #Hacemos click en el boton datos
    datos = driver.find_element_by_id("ctl00_Contenido_btnDatos")
    datos.click()

    
    
