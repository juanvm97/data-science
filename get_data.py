import twint

accion_popular = ['coco_ancachi', 'DarwinEspinozaV', 'wilsonsotop']
alianza_progreso = ['LuchoPiconQ', 'robertochiabra', 'SalhuanaE']
avanza_pais = ['1DianaGonzales', 'adrianatudelag', 'AlejandroCavero', 'Gral_Williams', 'RosselliAmuruz']
fuerza_popular = ['A_Aguinaga', 'CesarManuelRev1', 'ErnesBustamante', 'hventuraangel', 'LizarzaburuJuan', 'marthamoyano', 'NanoGuerra4', 'patty_juarez_', 'rosangelak8']
juntos_peru = ['chabelita2020', 'EdgardReymundo', 'ruthlib_', 'sigridbazan']
partido_morado = ['EdMalagaTrillo', 'FlorPabloMedina', 'suselparedes', 'RodolfoPerez_2']
peru_libre = ['bermejo_rojas', 'flaviocruzmaman', 'GonzaAmerico', 'GuidoPuka', 'Mariaagueroguti', 'segundoquirozb']
podemos_peu = ['EnriqueWong4', 'JoseLunaGalvez']
renovacion_popular = ['Alm_Montoya', 'AMunante11', 'DiegoBazCal', 'JoseCuetoAservi', 'NormaYarrow4', 'EsdrasMinaya']
somos_peru = ['alfredoazurin15', 'MartinVizcarraC']

partidos = {'accion_popular': accion_popular,
    'alianza_progreso': alianza_progreso,
    'avanza_pais': avanza_pais,
    'fuerza_popular': fuerza_popular,
    'juntos_peru': juntos_peru,
    'partido_morado': partido_morado,
    'peru_libre': peru_libre,
    'podemos_peu': podemos_peu,
    'renovacion_popular': renovacion_popular,
    'somos_peru': somos_peru}

for partido, lista in partidos.items():
    for congresista in lista:
        c = twint.Config()
        c.Username = congresista
        c.Since = "2021-01-01"
        c.Until = "2021-04-12"
        c.Pandas = True
        c.Hide_output = True
        twint.run.Search(c)
        df = twint.storage.panda.Tweets_df
        df.to_csv('data/' + partido + '/' + congresista + '.csv', index=False)

