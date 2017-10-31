import bottle

@bottle.route('/')
def home():
    frutas = ['manzana','naranja','banana']
    return bottle.template('home1',{'usuario':"Luis Arturo",'frutas':frutas})

@bottle.post('/frutafav')
def favorita():
    fruta = bottle.request.forms.get("fruta")
    if(fruta == None or fruta == ""):
        fruta = "No hay ninguna fruta"
    return bottle.template('frutafav',{'fruta':fruta})

bottle.debug(True)
bottle.run(host='localhost', port=8080)