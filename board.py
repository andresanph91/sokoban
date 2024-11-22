SPACE = '🤍'
ROBOT = '🚂'
OBSTA = '🟩'
CAJA =  "📦"
DESTINO = "🏴‍☠️"



def leer_tablero(nivel):

    tablero = []
    seccion = ''
    variables = {}

    with open(f'{nivel}.board','r') as f:
        lineas = f.readlines()

        for linea in lineas :
            linea=linea [:-1].strip()

            if linea in ('','\n'):
                continue

            if linea in  ('#variables', '#tablero'):
                seccion = linea 
                continue
            if seccion == '#variables': 
                linea = linea.split('>')
                var  = linea [0].strip()
                tipo = linea [1].strip()

                if tipo == 'SPACE':
                    tipo = SPACE
                elif tipo == 'ROBOT':
                    tipo = ROBOT
                elif tipo == 'OBSTA':
                    tipo = OBSTA


                variables [var]= tipo
            elif seccion  == '#tablero':
                for  var, tipo in variables.items():
                     linea  = linea.replace(var,tipo)
                linea= list(linea)
                tablero.append(linea)
    return tablero   

                # linea = linea.replace ('s',SPACE)
                # linea = linea.replace ('r',ROBOT)
                # linea = linea.replace ('o',OBSTA)

                

if __name__=='__main__':
    leer_tablero('nivel_1')