import json

ruta = "/var/www/html/clientes/tamila/videotutoriales/python/repo/clase_13/"

data = {}

data['post'] = []

falso="""
Y, viéndole don Quijote de aquella manera, con muestras de tanta tristeza, le dijo: Sábete, Sancho, que no es un hombre más que otro si no hace más que otro. Todas estas borrascas que nos suceden son señales de que <hr /> presto ha de serenar el tiempo y han de sucedernos bien las cosas; porque no es posible que el mal ni el bien sean durables, y de aquí se sigue que, habiendo durado mucho el mal, el bien está ya cerca. Así que, no debes congojarte por las desgracias que a mí me suceden, pues a ti no te cabe parte dellas.Y, viéndole don Quijote de aquella manera, con muestras de tanta tristeza, le dijo: Sábete, Sancho, que no es un hombre más que otro si no hace más que otro. Todas estas borrascas que nos suceden son señales de que presto ha de serenar el tiempo y han de sucedernos bien las cosas; porque no es posible que el mal ni el bien sean durables, y de aquí se sigue que, habiendo durado mucho el mal, el bien está ya cerca. Así que, no debes congojarte por las desgracias que a mí me suceden, pues a ti no
"""

for i in range(1, 11):
    data['post'].append({
        'id': i,
        'titulo': f'Título del post con ñandú {i}',
        'slug':f'titulo-del-post-con-nandu-{i}',
        'detalle': falso,
        'fecha':'2020-08-10'
    })

with open(ruta+'ejemplo.json', 'w') as file:
    json.dump(data, file, indent=4)