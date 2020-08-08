from datetime import datetime

def formateaFecha(fecha):#2020-08-04
    fechaArray=fecha.split('-')
    objeto_datetime = datetime.strptime(fecha, "%Y-%m-%d")
    dia_semana=datetime.weekday(objeto_datetime)
    
    if dia_semana==0:
        dia="Lunes"
    elif dia_semana==1:
        dia="Martes"
    elif dia_semana==2:
        dia="Miércoles"
    elif dia_semana==3:
        dia="Jueves"
    elif dia_semana==4:
        dia="Viernes"
    elif dia_semana==5:
        dia="Sábado"
    elif dia_semana==6:
        dia="Domingo"
    
        
    mes=''
    if fechaArray[1] =='01':
        mes = 'Enero'
    elif fechaArray[1] =='02':
        mes = 'Febrero'
    elif fechaArray[1] =='03':
        mes = 'Marzo'
    elif fechaArray[1] =='04':
        mes = 'Abril'
    elif fechaArray[1] =='05':
        mes = 'Mayo'
    elif fechaArray[1] =='06':
        mes = 'Junio'
    elif fechaArray[1] =='07':
        mes = 'Julio'
    elif fechaArray[1] =='08':
        mes = 'Agosto'
    elif fechaArray[1] =='09':
        mes = 'Septiembre'
    elif fechaArray[1] =='10':
        mes = 'Octubre'
    elif fechaArray[1] =='11':
        mes = 'Noviembre'
    elif fechaArray[1] =='12':
        mes = 'Diciembre'
    return f'{dia} {fechaArray[2]} de {mes} de {fechaArray[0]}'