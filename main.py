import json
import os


def guardar_reporte_mensual_json(response_data):
    fecha = response_data['FechaYHoraCorte'].split('T')
    filName = 'D_%s_%s_%s_%s_EXO_JSON.json' % (
    response_data['RfcContribuyente'], response_data['RfcProveedor'], fecha[0], response_data['ClaveInstalacion'])
    data = fecha[0].split('-')
    dir = './ControlVolumetrico/json/%s/Mensales/%s' % (data[0], data[1])

    # Si existe la ruta
    if os.path.isdir(dir):
        print(' ===> La ruta ya existe')
        if not os.path.exists('%s/%s' % (dir, filName)):
            print(' ===> El archivo No existe')
            with open(os.path.join(dir, filName), 'w') as file:
                json.dump(response_data, file)
                print(' ===> Se creo el archivo JSON')
        else:
            print(' ===> El archivo JSON ya existe')
    # En caso contrario
    else:
        # Creamos los archivos
        print(' ===> La ruta no existe')
        os.makedirs(dir, exist_ok=True)
        print(' ===> Se genera la ruta')
        # Generamos el archivo JSON
        with open(os.path.join(dir, filName), 'w') as file:
            json.dump(response_data, file)
            print(' ===> Se creo el archivo JSON')

def guardar_reporte_diario_json(response_data):
    fecha = response_data['FechaYHoraCorte'].split('T')
    filName = 'D_%s_%s_%s_%s_EXO_JSON.json' % ( response_data['RfcContribuyente'], response_data['RfcProveedor'], fecha[0], response_data['ClaveInstalacion'])
    data = fecha[0].split('-')
    dir = './ControlVolumetrico/json/%s/Diarios/%s' % (data[0], data[1])

    # Si existe la ruta
    if os.path.isdir(dir):
        print(' ===> La ruta ya existe')
        if not os.path.exists('%s/%s' %(dir, filName)) :
            print(' ===> El archivo No existe')
            with open(os.path.join(dir, filName), 'w') as file:
                json.dump(response_data,file)
                print(' ===> Se creo el archivo JSON')
        else:
            print(' ===> El archivo JSON ya existe')
    # En caso contrario
    else:
        # Creamos los archivos
        print(' ===> La ruta no existe')
        os.makedirs(dir, exist_ok=True)
        print(' ===> Se genera la ruta')
        # Generamos el archivo JSON
        with open(os.path.join(dir, filName), 'w') as file:
            json.dump(response_data,file)
            print(' ===> Se creo el archivo JSON')

if __name__ == '__main__':
    response_data = {
                "Bitacora": [
                    {
                        "DescripcionEvento": "Cambio en la configuración",
                        "FechaYHoraEvento": "2022-06-23T19:01:11-05:00",
                        "NumeroRegistro": 1,
                        "TipoEvento": 5,
                        "UsuarioResponsable": "GASOMARSHAL"
                    },
                    {
                        "DescripcionEvento": "Inactividad en el programa informático",
                        "FechaYHoraEvento": "2022-06-24T15:08:04-05:00",
                        "NumeroRegistro": 2,
                        "TipoEvento": 5
                    },
                    {
                        "DescripcionEvento": "Toma de muestra",
                        "FechaYHoraEvento": "2022-06-24T15:08:16-05:00",
                        "NumeroRegistro": 3,
                        "TipoEvento": 5
                    },
                    {
                        "DescripcionEvento": "Toma de muestra",
                        "FechaYHoraEvento": "2022-06-24T15:08:38-05:00",
                        "NumeroRegistro": 4,
                        "TipoEvento": 5
                    },
                    {
                        "DescripcionEvento": "Toma de muestra",
                        "FechaYHoraEvento": "2022-06-24T17:37:03-05:00",
                        "NumeroRegistro": 5,
                        "TipoEvento": 5
                    }
                ],
                "Caracter": "permisionario",
                "ClaveInstalacion": "EDS-0001",
                "DescripcionInstalacion": "Estación de combustible",
                "FechaYHoraCorte": "2022-01-24T18:59:59-05:00",
                "Geolocalizacion": [
                    {
                        "GeolocalizacionLatitud": 20.4129782,
                        "GeolocalizacionLongitud": -90.6526069
                    }
                ],
                "ModalidadPermiso": "PER2",
                "NumPermiso": "PL/19735/EXP/ES/2016",
                "NumeroDispensarios": 2,
                "NumeroDuctosEntradaSalida": 0,
                "NumeroDuctosTransporteDistribucion": 0,
                "NumeroPozos": 0,
                "NumeroTanques": 3,
                "Producto": [
                    {
                        "ClaveProducto": "PR07",
                        "ClaveSubProducto": "SP16",
                        "ComposOctanajeGasolina": 87,
                        "Dispensario": [
                            {
                                "ClaveDispensario": "DISP-0003",
                                "Manguera": [
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T23:00:29-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1651.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.398
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:07:39-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1654.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.614
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:23:08-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1658.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:26:55-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1670.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.489
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:43:24-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1708.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 37.499
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:46:09-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1712.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:54:00-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1717.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:01:18-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1722.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:08:29-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1724.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:21:40-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1729.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:26:20-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1739.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:30:08-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1754.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:36:34-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1760.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:06:47-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1762.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:11:21-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1766.85
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:35:57-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1784.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:43:51-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1788.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:50:04-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1791.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:52:06-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1808.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:57:51-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1810.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:59:53-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1828.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:09:13-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1831.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:16:13-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1886.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 55.146
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:18:48-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1899.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:28:54-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1902.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:35:09-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1919.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:37:43-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1937.48
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:40:41-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1942.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.083
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:43:35-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1947.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:51:50-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2009.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 61.864
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:55:01-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2017.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:58:08-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2039.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.376
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:00:06-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2040.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:01:34-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2049.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:04:41-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2059.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:06:55-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2072.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:08:59-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2081.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:13:27-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2124.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 43.008
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:15:46-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2125.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.122
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:19:34-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2178.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 53.024
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:21:04-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2183.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:21:56-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2184.57
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:22:47-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2186.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:23:39-05:00",
                                                    "NumeroDeRegistro": 44,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2188.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:24:20-05:00",
                                                    "NumeroDeRegistro": 45,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2189.89
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.901
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:25:54-05:00",
                                                    "NumeroDeRegistro": 46,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2198.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:26:59-05:00",
                                                    "NumeroDeRegistro": 47,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2200.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:27:56-05:00",
                                                    "NumeroDeRegistro": 48,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2204.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.783
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:30:30-05:00",
                                                    "NumeroDeRegistro": 49,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2217.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:34:30-05:00",
                                                    "NumeroDeRegistro": 50,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2226.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:41:25-05:00",
                                                    "NumeroDeRegistro": 51,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2248.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:45:37-05:00",
                                                    "NumeroDeRegistro": 52,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2258.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:47:08-05:00",
                                                    "NumeroDeRegistro": 53,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2261.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:52:44-05:00",
                                                    "NumeroDeRegistro": 54,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2267.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:59:39-05:00",
                                                    "NumeroDeRegistro": 55,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2302.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:04:42-05:00",
                                                    "NumeroDeRegistro": 56,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2307.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:10:52-05:00",
                                                    "NumeroDeRegistro": 57,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2337.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:13:43-05:00",
                                                    "NumeroDeRegistro": 58,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2348.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:18:22-05:00",
                                                    "NumeroDeRegistro": 59,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2353.07
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:20:09-05:00",
                                                    "NumeroDeRegistro": 60,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2355.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:25:54-05:00",
                                                    "NumeroDeRegistro": 61,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2372.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:31:56-05:00",
                                                    "NumeroDeRegistro": 62,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2373.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:37:31-05:00",
                                                    "NumeroDeRegistro": 63,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2391.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.424
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:41:18-05:00",
                                                    "NumeroDeRegistro": 64,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2431.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:45:35-05:00",
                                                    "NumeroDeRegistro": 65,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2435.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:55:27-05:00",
                                                    "NumeroDeRegistro": 66,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2444.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:58:43-05:00",
                                                    "NumeroDeRegistro": 67,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2448.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:02:27-05:00",
                                                    "NumeroDeRegistro": 68,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2451.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:11:07-05:00",
                                                    "NumeroDeRegistro": 69,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2473.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:15:41-05:00",
                                                    "NumeroDeRegistro": 70,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2484.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:17:57-05:00",
                                                    "NumeroDeRegistro": 71,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2488.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:19:46-05:00",
                                                    "NumeroDeRegistro": 72,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2490.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:27:05-05:00",
                                                    "NumeroDeRegistro": 73,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2510.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:37:16-05:00",
                                                    "NumeroDeRegistro": 74,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2514.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:39:44-05:00",
                                                    "NumeroDeRegistro": 75,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2523.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:50:22-05:00",
                                                    "NumeroDeRegistro": 76,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2536.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:03:13-05:00",
                                                    "NumeroDeRegistro": 77,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2545.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:19:10-05:00",
                                                    "NumeroDeRegistro": 78,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2547.89
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:21:58-05:00",
                                                    "NumeroDeRegistro": 79,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2549.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:25:23-05:00",
                                                    "NumeroDeRegistro": 80,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2553.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:33:58-05:00",
                                                    "NumeroDeRegistro": 81,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2571.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:38:25-05:00",
                                                    "NumeroDeRegistro": 82,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2580.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:49:14-05:00",
                                                    "NumeroDeRegistro": 83,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2584.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:52:45-05:00",
                                                    "NumeroDeRegistro": 84,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2593.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.21
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:59:28-05:00",
                                                    "NumeroDeRegistro": 85,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2648.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 55.497
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:06:38-05:00",
                                                    "NumeroDeRegistro": 86,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2668.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.32
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:12:35-05:00",
                                                    "NumeroDeRegistro": 87,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2682.07
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:18:51-05:00",
                                                    "NumeroDeRegistro": 88,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2704.13
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:25:09-05:00",
                                                    "NumeroDeRegistro": 89,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2708.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:33:25-05:00",
                                                    "NumeroDeRegistro": 90,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2718.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:35:03-05:00",
                                                    "NumeroDeRegistro": 91,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2727.36
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:45:23-05:00",
                                                    "NumeroDeRegistro": 92,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2749.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:48:10-05:00",
                                                    "NumeroDeRegistro": 93,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2769.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:52:52-05:00",
                                                    "NumeroDeRegistro": 94,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2771.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:54:07-05:00",
                                                    "NumeroDeRegistro": 95,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2780.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:55:56-05:00",
                                                    "NumeroDeRegistro": 96,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2781.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.502
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:58:12-05:00",
                                                    "NumeroDeRegistro": 97,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2795.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:00:04-05:00",
                                                    "NumeroDeRegistro": 98,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2804.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:05:14-05:00",
                                                    "NumeroDeRegistro": 99,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2826.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:14:42-05:00",
                                                    "NumeroDeRegistro": 100,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2870.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:16:46-05:00",
                                                    "NumeroDeRegistro": 101,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2876.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:18:43-05:00",
                                                    "NumeroDeRegistro": 102,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2881.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:20:10-05:00",
                                                    "NumeroDeRegistro": 103,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2890.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:29:30-05:00",
                                                    "NumeroDeRegistro": 104,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2893.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:45:15-05:00",
                                                    "NumeroDeRegistro": 105,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2902.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:48:38-05:00",
                                                    "NumeroDeRegistro": 106,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2905.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.138
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:51:14-05:00",
                                                    "NumeroDeRegistro": 107,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2915.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:53:49-05:00",
                                                    "NumeroDeRegistro": 108,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2935.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:01:55-05:00",
                                                    "NumeroDeRegistro": 109,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2936.89
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.672
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:16:01-05:00",
                                                    "NumeroDeRegistro": 110,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2939.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:19:56-05:00",
                                                    "NumeroDeRegistro": 111,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2947.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:22:00-05:00",
                                                    "NumeroDeRegistro": 112,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2952.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:26:29-05:00",
                                                    "NumeroDeRegistro": 113,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2961.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:28:36-05:00",
                                                    "NumeroDeRegistro": 114,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2969.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:30:51-05:00",
                                                    "NumeroDeRegistro": 115,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2972.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:36:26-05:00",
                                                    "NumeroDeRegistro": 116,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2976.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:38:30-05:00",
                                                    "NumeroDeRegistro": 117,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2977.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.329
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:40:48-05:00",
                                                    "NumeroDeRegistro": 118,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2999.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:43:06-05:00",
                                                    "NumeroDeRegistro": 119,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3004.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:49:43-05:00",
                                                    "NumeroDeRegistro": 120,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3006.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:52:43-05:00",
                                                    "NumeroDeRegistro": 121,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3015.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:09:04-05:00",
                                                    "NumeroDeRegistro": 122,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3025.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.37
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:11:40-05:00",
                                                    "NumeroDeRegistro": 123,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3027.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.208
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:17:08-05:00",
                                                    "NumeroDeRegistro": 124,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3071.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:23:10-05:00",
                                                    "NumeroDeRegistro": 125,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3109.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 37.494
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:27:45-05:00",
                                                    "NumeroDeRegistro": 126,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3114.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.79
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:44:25-05:00",
                                                    "NumeroDeRegistro": 127,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3115.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:52:42-05:00",
                                                    "NumeroDeRegistro": 128,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3135.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:00:43-05:00",
                                                    "NumeroDeRegistro": 129,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3139.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:04:31-05:00",
                                                    "NumeroDeRegistro": 130,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3148.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:10:01-05:00",
                                                    "NumeroDeRegistro": 131,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3150.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:27:23-05:00",
                                                    "NumeroDeRegistro": 132,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3154.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:31:02-05:00",
                                                    "NumeroDeRegistro": 133,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3159.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:35:46-05:00",
                                                    "NumeroDeRegistro": 134,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3168.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:45:20-05:00",
                                                    "NumeroDeRegistro": 135,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3198.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:52:51-05:00",
                                                    "NumeroDeRegistro": 136,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3218.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 19.85
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:57:01-05:00",
                                                    "NumeroDeRegistro": 137,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3226.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:02:34-05:00",
                                                    "NumeroDeRegistro": 138,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3288.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 61.756
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:05:22-05:00",
                                                    "NumeroDeRegistro": 139,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3297.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:08:09-05:00",
                                                    "NumeroDeRegistro": 140,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3299.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:11:48-05:00",
                                                    "NumeroDeRegistro": 141,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3321.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:16:10-05:00",
                                                    "NumeroDeRegistro": 142,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3326.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:18:02-05:00",
                                                    "NumeroDeRegistro": 143,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3337.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:28:16-05:00",
                                                    "NumeroDeRegistro": 144,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3381.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:35:44-05:00",
                                                    "NumeroDeRegistro": 145,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3385.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:39:47-05:00",
                                                    "NumeroDeRegistro": 146,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3395.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:42:13-05:00",
                                                    "NumeroDeRegistro": 147,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3396.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:47:46-05:00",
                                                    "NumeroDeRegistro": 148,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3398.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.544
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:57:56-05:00",
                                                    "NumeroDeRegistro": 149,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3424.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.467
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:16:10-05:00",
                                                    "NumeroDeRegistro": 150,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3447.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:18:17-05:00",
                                                    "NumeroDeRegistro": 151,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3469.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:23:06-05:00",
                                                    "NumeroDeRegistro": 152,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "A",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3479.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:27:28-05:00",
                                                    "NumeroDeRegistro": 153,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3484.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.293
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:37:48-05:00",
                                                    "NumeroDeRegistro": 154,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3506.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:39:21-05:00",
                                                    "NumeroDeRegistro": 155,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3515.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:43:35-05:00",
                                                    "NumeroDeRegistro": 156,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3528.51
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:47:34-05:00",
                                                    "NumeroDeRegistro": 157,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3535.13
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:56:13-05:00",
                                                    "NumeroDeRegistro": 158,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3548.36
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:04:31-05:00",
                                                    "NumeroDeRegistro": 159,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3552.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:26:30-05:00",
                                                    "NumeroDeRegistro": 160,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3554.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:30:26-05:00",
                                                    "NumeroDeRegistro": 161,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3559.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.239
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:35:26-05:00",
                                                    "NumeroDeRegistro": 162,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3612.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 53.053
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:39:33-05:00",
                                                    "NumeroDeRegistro": 163,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3621.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:45:24-05:00",
                                                    "NumeroDeRegistro": 164,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3641.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:48:38-05:00",
                                                    "NumeroDeRegistro": 165,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3645.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:54:13-05:00",
                                                    "NumeroDeRegistro": 166,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3658.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:57:57-05:00",
                                                    "NumeroDeRegistro": 167,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3676.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.43
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:05:25-05:00",
                                                    "NumeroDeRegistro": 168,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3711.45
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.289
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:07:48-05:00",
                                                    "NumeroDeRegistro": 169,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3713.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:08:48-05:00",
                                                    "NumeroDeRegistro": 170,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3715.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:19:21-05:00",
                                                    "NumeroDeRegistro": 171,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3720.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:36:58-05:00",
                                                    "NumeroDeRegistro": 172,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3729.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:42:31-05:00",
                                                    "NumeroDeRegistro": 173,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3733.51
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:44:23-05:00",
                                                    "NumeroDeRegistro": 174,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3738.51
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:48:58-05:00",
                                                    "NumeroDeRegistro": 175,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3742.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:51:27-05:00",
                                                    "NumeroDeRegistro": 176,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3751.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:54:46-05:00",
                                                    "NumeroDeRegistro": 177,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3762.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.587
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:00:49-05:00",
                                                    "NumeroDeRegistro": 178,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3766.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 46052.54,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 2031.238
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 178
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0004"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:14:29-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655061.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.529
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:27:02-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655063.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:34:15-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655066.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:42:05-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655070.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:47:52-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655083.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.582
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T20:04:50-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655084.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T20:16:17-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655086.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T20:43:11-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655087.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.588
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:30:35-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655094.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:41:17-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655099.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:44:44-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655101.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:46:01-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655103.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:48:36-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655126.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 23.39
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:58:42-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655128.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:01:32-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655129.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:07:07-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655131.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.496
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:13:30-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655138.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:24:16-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655140.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.104
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:27:36-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655142.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:39:33-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655143.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:46:20-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655147.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:51:07-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655171.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 23.353
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:53:37-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655173.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.837
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:55:10-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655176.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:57:58-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655177.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:59:19-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655181.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.113
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:08:35-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655185.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:16:31-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655194.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:22:38-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655214.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.32
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:24:34-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655217.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:28:02-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655225.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:30:31-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655228.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:32:10-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655234.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:36:52-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655236.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:40:24-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655256.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 19.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:44:39-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655260.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:53:04-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655262.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:54:36-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655265.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:59:58-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655300.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.938
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:03:20-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655303.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:05:01-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655309.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:31:47-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655358.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 48.522
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:40:38-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655360.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:41:47-05:00",
                                                    "NumeroDeRegistro": 44,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655362.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:47:17-05:00",
                                                    "NumeroDeRegistro": 45,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655382.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:53:17-05:00",
                                                    "NumeroDeRegistro": 46,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655384.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:09:26-05:00",
                                                    "NumeroDeRegistro": 47,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655404.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:20:53-05:00",
                                                    "NumeroDeRegistro": 48,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655413.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:32:06-05:00",
                                                    "NumeroDeRegistro": 49,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655435.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:43:03-05:00",
                                                    "NumeroDeRegistro": 50,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655437.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:44:00-05:00",
                                                    "NumeroDeRegistro": 51,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655438.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:55:53-05:00",
                                                    "NumeroDeRegistro": 52,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655440.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:19:03-05:00",
                                                    "NumeroDeRegistro": 53,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655444.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.97
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:21:20-05:00",
                                                    "NumeroDeRegistro": 54,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655454.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:26:51-05:00",
                                                    "NumeroDeRegistro": 55,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655459.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:33:20-05:00",
                                                    "NumeroDeRegistro": 56,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655463.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:37:32-05:00",
                                                    "NumeroDeRegistro": 57,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655488.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:40:43-05:00",
                                                    "NumeroDeRegistro": 58,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655497.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:50:01-05:00",
                                                    "NumeroDeRegistro": 59,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655506.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:07:30-05:00",
                                                    "NumeroDeRegistro": 60,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655514.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:09:15-05:00",
                                                    "NumeroDeRegistro": 61,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655520.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.083
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:13:32-05:00",
                                                    "NumeroDeRegistro": 62,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655522.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:14:56-05:00",
                                                    "NumeroDeRegistro": 63,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655524.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:25:24-05:00",
                                                    "NumeroDeRegistro": 64,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655531.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:33:01-05:00",
                                                    "NumeroDeRegistro": 65,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655533.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:40:50-05:00",
                                                    "NumeroDeRegistro": 66,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655537.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:11:42-05:00",
                                                    "NumeroDeRegistro": 67,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655577.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:21:06-05:00",
                                                    "NumeroDeRegistro": 68,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655589.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.913
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:30:12-05:00",
                                                    "NumeroDeRegistro": 69,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655591.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:37:01-05:00",
                                                    "NumeroDeRegistro": 70,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655593.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.103
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:39:41-05:00",
                                                    "NumeroDeRegistro": 71,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655619.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.467
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:49:32-05:00",
                                                    "NumeroDeRegistro": 72,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655628.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:51:09-05:00",
                                                    "NumeroDeRegistro": 73,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655629.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:54:44-05:00",
                                                    "NumeroDeRegistro": 74,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655636.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:55:48-05:00",
                                                    "NumeroDeRegistro": 75,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655637.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:07:36-05:00",
                                                    "NumeroDeRegistro": 76,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655639.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:17:35-05:00",
                                                    "NumeroDeRegistro": 77,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655641.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:21:44-05:00",
                                                    "NumeroDeRegistro": 78,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655643.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:27:38-05:00",
                                                    "NumeroDeRegistro": 79,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655648.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:36:41-05:00",
                                                    "NumeroDeRegistro": 80,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655659.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:46:52-05:00",
                                                    "NumeroDeRegistro": 81,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655661.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:55:41-05:00",
                                                    "NumeroDeRegistro": 82,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655670.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:57:40-05:00",
                                                    "NumeroDeRegistro": 83,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655674.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:58:36-05:00",
                                                    "NumeroDeRegistro": 84,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655676.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:14:06-05:00",
                                                    "NumeroDeRegistro": 85,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655680.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:25:20-05:00",
                                                    "NumeroDeRegistro": 86,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655689.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:29:19-05:00",
                                                    "NumeroDeRegistro": 87,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655693.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:37:40-05:00",
                                                    "NumeroDeRegistro": 88,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655700.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:48:05-05:00",
                                                    "NumeroDeRegistro": 89,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655701.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:49:51-05:00",
                                                    "NumeroDeRegistro": 90,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655711.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:54:49-05:00",
                                                    "NumeroDeRegistro": 91,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655724.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:59:57-05:00",
                                                    "NumeroDeRegistro": 92,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655735.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:11:04-05:00",
                                                    "NumeroDeRegistro": 93,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655744.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:18:32-05:00",
                                                    "NumeroDeRegistro": 94,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655746.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:23:13-05:00",
                                                    "NumeroDeRegistro": 95,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655760.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:28:17-05:00",
                                                    "NumeroDeRegistro": 96,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655764.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:34:48-05:00",
                                                    "NumeroDeRegistro": 97,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655777.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:41:52-05:00",
                                                    "NumeroDeRegistro": 98,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655779.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.515
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:43:19-05:00",
                                                    "NumeroDeRegistro": 99,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655780.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:50:17-05:00",
                                                    "NumeroDeRegistro": 100,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655785.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:53:47-05:00",
                                                    "NumeroDeRegistro": 101,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655786.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:55:17-05:00",
                                                    "NumeroDeRegistro": 102,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655795.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:58:30-05:00",
                                                    "NumeroDeRegistro": 103,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655799.66
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:00:50-05:00",
                                                    "NumeroDeRegistro": 104,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655801.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:13:36-05:00",
                                                    "NumeroDeRegistro": 105,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655804.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.576
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:15:45-05:00",
                                                    "NumeroDeRegistro": 106,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655812.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.612
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:19:03-05:00",
                                                    "NumeroDeRegistro": 107,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655823.85
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:34:37-05:00",
                                                    "NumeroDeRegistro": 108,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655828.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:37:49-05:00",
                                                    "NumeroDeRegistro": 109,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655837.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:40:41-05:00",
                                                    "NumeroDeRegistro": 110,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655843.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:44:45-05:00",
                                                    "NumeroDeRegistro": 111,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655869.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:08:18-05:00",
                                                    "NumeroDeRegistro": 112,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655876.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:43:09-05:00",
                                                    "NumeroDeRegistro": 113,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655891.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:44:39-05:00",
                                                    "NumeroDeRegistro": 114,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655911.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:55:41-05:00",
                                                    "NumeroDeRegistro": 115,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655913.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:11:35-05:00",
                                                    "NumeroDeRegistro": 116,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655922.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:20:11-05:00",
                                                    "NumeroDeRegistro": 117,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655923.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:26:56-05:00",
                                                    "NumeroDeRegistro": 118,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655928.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:39:28-05:00",
                                                    "NumeroDeRegistro": 119,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655932.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:09:54-05:00",
                                                    "NumeroDeRegistro": 120,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655947.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.95
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:15:36-05:00",
                                                    "NumeroDeRegistro": 121,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655956.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:17:45-05:00",
                                                    "NumeroDeRegistro": 122,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655958.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:20:58-05:00",
                                                    "NumeroDeRegistro": 123,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655980.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.376
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:22:22-05:00",
                                                    "NumeroDeRegistro": 124,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655984.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:24:07-05:00",
                                                    "NumeroDeRegistro": 125,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655986.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.715
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:26:07-05:00",
                                                    "NumeroDeRegistro": 126,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655991.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:35:00-05:00",
                                                    "NumeroDeRegistro": 127,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656001.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:44:26-05:00",
                                                    "NumeroDeRegistro": 128,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656003.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:45:49-05:00",
                                                    "NumeroDeRegistro": 129,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656007.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:49:20-05:00",
                                                    "NumeroDeRegistro": 130,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656020.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:59:05-05:00",
                                                    "NumeroDeRegistro": 131,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656025.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:01:30-05:00",
                                                    "NumeroDeRegistro": 132,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656050.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.613
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:16:34-05:00",
                                                    "NumeroDeRegistro": 133,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656053.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:18:29-05:00",
                                                    "NumeroDeRegistro": 134,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656057.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:21:27-05:00",
                                                    "NumeroDeRegistro": 135,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656064.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:30:00-05:00",
                                                    "NumeroDeRegistro": 136,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656068.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:31:41-05:00",
                                                    "NumeroDeRegistro": 137,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656069.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:42:51-05:00",
                                                    "NumeroDeRegistro": 138,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656079.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:46:09-05:00",
                                                    "NumeroDeRegistro": 139,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656080.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:50:17-05:00",
                                                    "NumeroDeRegistro": 140,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656095.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:54:16-05:00",
                                                    "NumeroDeRegistro": 141,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656098.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:03:33-05:00",
                                                    "NumeroDeRegistro": 142,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656123.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.101
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:10:59-05:00",
                                                    "NumeroDeRegistro": 143,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656128.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:18:55-05:00",
                                                    "NumeroDeRegistro": 144,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656132.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:23:03-05:00",
                                                    "NumeroDeRegistro": 145,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656134.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:24:35-05:00",
                                                    "NumeroDeRegistro": 146,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656139.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:39:22-05:00",
                                                    "NumeroDeRegistro": 147,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656148.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:47:50-05:00",
                                                    "NumeroDeRegistro": 148,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656157.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:49:01-05:00",
                                                    "NumeroDeRegistro": 149,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656159.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:55:15-05:00",
                                                    "NumeroDeRegistro": 150,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656164.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:01:38-05:00",
                                                    "NumeroDeRegistro": 151,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656166.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:03:10-05:00",
                                                    "NumeroDeRegistro": 152,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656175.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:06:06-05:00",
                                                    "NumeroDeRegistro": 153,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656183.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:08:28-05:00",
                                                    "NumeroDeRegistro": 154,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656205.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:13:25-05:00",
                                                    "NumeroDeRegistro": 155,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656207.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.628
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:15:43-05:00",
                                                    "NumeroDeRegistro": 156,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656220.85
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:17:19-05:00",
                                                    "NumeroDeRegistro": 157,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656229.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:19:28-05:00",
                                                    "NumeroDeRegistro": 158,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656234.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:26:07-05:00",
                                                    "NumeroDeRegistro": 159,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656235.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:32:18-05:00",
                                                    "NumeroDeRegistro": 160,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656238.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:53:33-05:00",
                                                    "NumeroDeRegistro": 161,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 656260.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.278
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 24962.79,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 1100.936
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 161
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0006"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:59:06-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671507.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 14.846
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:27:05-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671529.56
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:29:12-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671538.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:38:18-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671560.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:49:58-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671564.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:51:49-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671575.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:00:52-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671580.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:02:36-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671582.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:07:34-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671604.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:14:08-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671606.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.563
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:24:36-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671619.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:38:25-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671620.31
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.972
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:42:55-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671660.57
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.261
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:48:38-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671706.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 45.629
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:56:16-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671719.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:57:56-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671722.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.615
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:59:28-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671725.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.435
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:04:29-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671727.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:14:48-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671732.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.864
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:34:55-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671829.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 97.066
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:38:27-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671834.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:41:53-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671835.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:55:16-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671838.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:59:43-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671884.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 46.036
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:11:19-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671891.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:16:17-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671926.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.531
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:19:06-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671951.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.256
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:30:25-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671996.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:03:12-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672011.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.439
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:15:19-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672051.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:41:24-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672066.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:46:59-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672070.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:13:08-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672100.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:29:06-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672103.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.088
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:30:35-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672106.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:43:15-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672123.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:44:32-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672128.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:05:31-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672141.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:21:46-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672167.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.478
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:25:17-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672172.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.79
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:27:37-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672177.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:29:37-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672186.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:45:47-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672190.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:55:13-05:00",
                                                    "NumeroDeRegistro": 44,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672200.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:06:19-05:00",
                                                    "NumeroDeRegistro": 45,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672211.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:27:34-05:00",
                                                    "NumeroDeRegistro": 46,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672267.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 56.322
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:32:55-05:00",
                                                    "NumeroDeRegistro": 47,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672281.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:35:42-05:00",
                                                    "NumeroDeRegistro": 48,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672285.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:42:09-05:00",
                                                    "NumeroDeRegistro": 49,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672294.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:46:00-05:00",
                                                    "NumeroDeRegistro": 50,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672301.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:58:55-05:00",
                                                    "NumeroDeRegistro": 51,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672335.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 34.421
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:02:11-05:00",
                                                    "NumeroDeRegistro": 52,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672348.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:50:01-05:00",
                                                    "NumeroDeRegistro": 53,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672357.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:51:39-05:00",
                                                    "NumeroDeRegistro": 54,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672367.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:02:31-05:00",
                                                    "NumeroDeRegistro": 55,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672376.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:17:32-05:00",
                                                    "NumeroDeRegistro": 56,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672432.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 56.42
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:26:41-05:00",
                                                    "NumeroDeRegistro": 57,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672502.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 70.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:23:27-05:00",
                                                    "NumeroDeRegistro": 58,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672511.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:45:07-05:00",
                                                    "NumeroDeRegistro": 59,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672515.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:04:30-05:00",
                                                    "NumeroDeRegistro": 60,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672529.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:12:26-05:00",
                                                    "NumeroDeRegistro": 61,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672542.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:18:28-05:00",
                                                    "NumeroDeRegistro": 62,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672546.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:19:42-05:00",
                                                    "NumeroDeRegistro": 63,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672550.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.682
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:28:24-05:00",
                                                    "NumeroDeRegistro": 64,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672591.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 41.143
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:33:14-05:00",
                                                    "NumeroDeRegistro": 65,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672635.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 43.685
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:51:38-05:00",
                                                    "NumeroDeRegistro": 66,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672679.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:03:36-05:00",
                                                    "NumeroDeRegistro": 67,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672701.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:05:58-05:00",
                                                    "NumeroDeRegistro": 68,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672723.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:13:49-05:00",
                                                    "NumeroDeRegistro": 69,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672760.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 36.442
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:19:34-05:00",
                                                    "NumeroDeRegistro": 70,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672780.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:23:22-05:00",
                                                    "NumeroDeRegistro": 71,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672790.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:56:33-05:00",
                                                    "NumeroDeRegistro": 72,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "A",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672810.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:40:21-05:00",
                                                    "NumeroDeRegistro": 73,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672832.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:50:45-05:00",
                                                    "NumeroDeRegistro": 74,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672849.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:06:30-05:00",
                                                    "NumeroDeRegistro": 75,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672871.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:11:39-05:00",
                                                    "NumeroDeRegistro": 76,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672874.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:30:33-05:00",
                                                    "NumeroDeRegistro": 77,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672896.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:40:32-05:00",
                                                    "NumeroDeRegistro": 78,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672916.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:52:54-05:00",
                                                    "NumeroDeRegistro": 79,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672936.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:01:11-05:00",
                                                    "NumeroDeRegistro": 80,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672958.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:20:53-05:00",
                                                    "NumeroDeRegistro": 81,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672959.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:34:47-05:00",
                                                    "NumeroDeRegistro": 82,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672979.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:38:27-05:00",
                                                    "NumeroDeRegistro": 83,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 672989.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:52:54-05:00",
                                                    "NumeroDeRegistro": 84,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673011.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:05:34-05:00",
                                                    "NumeroDeRegistro": 85,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673020.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:30:02-05:00",
                                                    "NumeroDeRegistro": 86,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673024.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:40:42-05:00",
                                                    "NumeroDeRegistro": 87,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673037.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:07:29-05:00",
                                                    "NumeroDeRegistro": 88,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673046.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:10:52-05:00",
                                                    "NumeroDeRegistro": 89,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673060.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 14.12
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:19:12-05:00",
                                                    "NumeroDeRegistro": 90,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673062.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.006
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:32:36-05:00",
                                                    "NumeroDeRegistro": 91,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673075.45
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.535
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:52:02-05:00",
                                                    "NumeroDeRegistro": 92,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 673084.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 35481.96,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 1565.095
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 92
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0008"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T22:04:46-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653774.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T22:15:09-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653778.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T22:16:42-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653787.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T22:25:03-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653797.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T23:17:49-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653802.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T23:41:32-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653813.13
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.398
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:09:36-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653831.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.87
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:48:19-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653844.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.597
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:03:58-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653847.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.45
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:07:30-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653849.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:11:59-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653850.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.573
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:18:03-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653865.18
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 14.343
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:21:13-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653867.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:26:12-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653875.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.386
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:28:58-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653893.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:55:55-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653894.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:07:55-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653896.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:10:44-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653898.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:12:15-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653903.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:15:21-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653905.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:17:19-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653912.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 7.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:24:08-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653943.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.878
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:26:48-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653952.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:32:07-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653953.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:33:57-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653962.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:42:31-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653966.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:53:23-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653975.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:55:51-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 653995.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:58:58-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654004.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:59:57-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654005.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:01:55-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654007.31
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:04:09-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654011.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:05:42-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654012.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:07:52-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654017.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:09:55-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654019.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:17:09-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654032.45
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:24:55-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654036.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.265
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:26:39-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654038.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:28:37-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654041.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.511
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:30:50-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654050.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:33:16-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654056.88
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:36:13-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654063.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:39:19-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654085.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.376
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:40:45-05:00",
                                                    "NumeroDeRegistro": 44,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654087.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:44:17-05:00",
                                                    "NumeroDeRegistro": 45,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654109.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:53:49-05:00",
                                                    "NumeroDeRegistro": 46,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654118.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:55:33-05:00",
                                                    "NumeroDeRegistro": 47,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654123.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:00:57-05:00",
                                                    "NumeroDeRegistro": 48,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654189.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 66.171
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:03:04-05:00",
                                                    "NumeroDeRegistro": 49,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654190.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:04:07-05:00",
                                                    "NumeroDeRegistro": 50,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654192.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:05:38-05:00",
                                                    "NumeroDeRegistro": 51,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654196.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:09:50-05:00",
                                                    "NumeroDeRegistro": 52,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654240.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:11:51-05:00",
                                                    "NumeroDeRegistro": 53,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654250.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 7.79
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:13:43-05:00",
                                                    "NumeroDeRegistro": 54,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654257.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.176
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:21:10-05:00",
                                                    "NumeroDeRegistro": 55,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654267.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:23:30-05:00",
                                                    "NumeroDeRegistro": 56,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654272.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:26:49-05:00",
                                                    "NumeroDeRegistro": 57,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654307.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.289
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:28:10-05:00",
                                                    "NumeroDeRegistro": 58,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654311.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:32:51-05:00",
                                                    "NumeroDeRegistro": 59,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654333.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:34:59-05:00",
                                                    "NumeroDeRegistro": 60,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654338.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:40:44-05:00",
                                                    "NumeroDeRegistro": 61,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654346.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:45:41-05:00",
                                                    "NumeroDeRegistro": 62,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654351.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:50:19-05:00",
                                                    "NumeroDeRegistro": 63,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654356.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:51:01-05:00",
                                                    "NumeroDeRegistro": 64,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654360.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:01:38-05:00",
                                                    "NumeroDeRegistro": 65,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654365.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:02:43-05:00",
                                                    "NumeroDeRegistro": 66,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654366.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:13:26-05:00",
                                                    "NumeroDeRegistro": 67,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654380.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:15:56-05:00",
                                                    "NumeroDeRegistro": 68,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654382.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:22:22-05:00",
                                                    "NumeroDeRegistro": 69,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654397.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.439
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:28:19-05:00",
                                                    "NumeroDeRegistro": 70,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654437.56
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 39.7
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:33:45-05:00",
                                                    "NumeroDeRegistro": 71,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654450.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:36:05-05:00",
                                                    "NumeroDeRegistro": 72,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654459.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:40:34-05:00",
                                                    "NumeroDeRegistro": 73,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654503.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:43:37-05:00",
                                                    "NumeroDeRegistro": 74,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654508.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:46:30-05:00",
                                                    "NumeroDeRegistro": 75,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654519.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:54:57-05:00",
                                                    "NumeroDeRegistro": 76,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654529.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:57:40-05:00",
                                                    "NumeroDeRegistro": 77,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654551.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:59:36-05:00",
                                                    "NumeroDeRegistro": 78,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654553.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.214
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:01:26-05:00",
                                                    "NumeroDeRegistro": 79,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654562.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:06:41-05:00",
                                                    "NumeroDeRegistro": 80,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654571.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:08:55-05:00",
                                                    "NumeroDeRegistro": 81,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654575.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:17:49-05:00",
                                                    "NumeroDeRegistro": 82,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654586.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:21:42-05:00",
                                                    "NumeroDeRegistro": 83,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654588.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:25:33-05:00",
                                                    "NumeroDeRegistro": 84,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654610.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:27:00-05:00",
                                                    "NumeroDeRegistro": 85,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654618.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:29:06-05:00",
                                                    "NumeroDeRegistro": 86,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654620.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:38:17-05:00",
                                                    "NumeroDeRegistro": 87,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654634.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:40:34-05:00",
                                                    "NumeroDeRegistro": 88,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654637.31
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.088
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:44:04-05:00",
                                                    "NumeroDeRegistro": 89,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654641.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:46:26-05:00",
                                                    "NumeroDeRegistro": 90,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654650.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:49:42-05:00",
                                                    "NumeroDeRegistro": 91,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654651.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:56:48-05:00",
                                                    "NumeroDeRegistro": 92,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654656.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:11:37-05:00",
                                                    "NumeroDeRegistro": 93,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654658.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:13:34-05:00",
                                                    "NumeroDeRegistro": 94,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654663.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:24:30-05:00",
                                                    "NumeroDeRegistro": 95,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654676.57
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:33:29-05:00",
                                                    "NumeroDeRegistro": 96,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654698.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.376
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:42:54-05:00",
                                                    "NumeroDeRegistro": 97,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654711.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.393
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:49:34-05:00",
                                                    "NumeroDeRegistro": 98,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654721.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.37
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:55:46-05:00",
                                                    "NumeroDeRegistro": 99,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654724.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:00:43-05:00",
                                                    "NumeroDeRegistro": 100,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654728.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:03:24-05:00",
                                                    "NumeroDeRegistro": 101,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654731.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.754
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:05:13-05:00",
                                                    "NumeroDeRegistro": 102,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654733.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:09:49-05:00",
                                                    "NumeroDeRegistro": 103,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654768.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.289
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:10:36-05:00",
                                                    "NumeroDeRegistro": 104,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654770.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:20:45-05:00",
                                                    "NumeroDeRegistro": 105,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654779.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:22:01-05:00",
                                                    "NumeroDeRegistro": 106,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654784.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:23:52-05:00",
                                                    "NumeroDeRegistro": 107,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654797.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:27:20-05:00",
                                                    "NumeroDeRegistro": 108,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654832.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.289
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:32:00-05:00",
                                                    "NumeroDeRegistro": 109,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654834.89
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:33:10-05:00",
                                                    "NumeroDeRegistro": 110,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654837.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:36:36-05:00",
                                                    "NumeroDeRegistro": 111,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654841.51
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:38:01-05:00",
                                                    "NumeroDeRegistro": 112,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654843.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:41:36-05:00",
                                                    "NumeroDeRegistro": 113,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654874.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.878
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:44:45-05:00",
                                                    "NumeroDeRegistro": 114,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654876.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:46:55-05:00",
                                                    "NumeroDeRegistro": 115,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654879.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:49:19-05:00",
                                                    "NumeroDeRegistro": 116,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654881.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:55:21-05:00",
                                                    "NumeroDeRegistro": 117,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654887.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:00:44-05:00",
                                                    "NumeroDeRegistro": 118,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654890.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:06:15-05:00",
                                                    "NumeroDeRegistro": 119,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654898.85
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:09:24-05:00",
                                                    "NumeroDeRegistro": 120,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654907.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:12:03-05:00",
                                                    "NumeroDeRegistro": 121,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654909.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.33
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:23:04-05:00",
                                                    "NumeroDeRegistro": 122,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654931.06
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:24:20-05:00",
                                                    "NumeroDeRegistro": 123,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654933.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:27:30-05:00",
                                                    "NumeroDeRegistro": 124,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654945.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.426
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:34:13-05:00",
                                                    "NumeroDeRegistro": 125,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654950.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:39:16-05:00",
                                                    "NumeroDeRegistro": 126,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654954.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:44:29-05:00",
                                                    "NumeroDeRegistro": 127,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654963.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:56:56-05:00",
                                                    "NumeroDeRegistro": 128,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654967.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:57:45-05:00",
                                                    "NumeroDeRegistro": 129,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 654968.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:12:23-05:00",
                                                    "NumeroDeRegistro": 130,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655012.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:26:39-05:00",
                                                    "NumeroDeRegistro": 131,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655017.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:30:32-05:00",
                                                    "NumeroDeRegistro": 132,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655061.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 44.111
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:38:21-05:00",
                                                    "NumeroDeRegistro": 133,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655066.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:48:41-05:00",
                                                    "NumeroDeRegistro": 134,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655072.88
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:51:23-05:00",
                                                    "NumeroDeRegistro": 135,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655078.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.734
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:00:20-05:00",
                                                    "NumeroDeRegistro": 136,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655088.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:05:35-05:00",
                                                    "NumeroDeRegistro": 137,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655097.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:18:13-05:00",
                                                    "NumeroDeRegistro": 138,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655115.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:21:36-05:00",
                                                    "NumeroDeRegistro": 139,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655119.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:33:42-05:00",
                                                    "NumeroDeRegistro": 140,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655122.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.088
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:38:49-05:00",
                                                    "NumeroDeRegistro": 141,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655123.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:49:47-05:00",
                                                    "NumeroDeRegistro": 142,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655153.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:55:49-05:00",
                                                    "NumeroDeRegistro": 143,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655160.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:59:36-05:00",
                                                    "NumeroDeRegistro": 144,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655164.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:02:56-05:00",
                                                    "NumeroDeRegistro": 145,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655173.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:06:29-05:00",
                                                    "NumeroDeRegistro": 146,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655179.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.083
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:12:51-05:00",
                                                    "NumeroDeRegistro": 147,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655183.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:14:55-05:00",
                                                    "NumeroDeRegistro": 148,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655203.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:25:45-05:00",
                                                    "NumeroDeRegistro": 149,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655221.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:37:41-05:00",
                                                    "NumeroDeRegistro": 150,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655240.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 19.609
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:41:12-05:00",
                                                    "NumeroDeRegistro": 151,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655245.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:46:06-05:00",
                                                    "NumeroDeRegistro": 152,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655246.44
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:48:05-05:00",
                                                    "NumeroDeRegistro": 153,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655248.65
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:52:08-05:00",
                                                    "NumeroDeRegistro": 154,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655258.65
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:05:52-05:00",
                                                    "NumeroDeRegistro": 155,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655261.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:06:42-05:00",
                                                    "NumeroDeRegistro": 156,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655263.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:10:43-05:00",
                                                    "NumeroDeRegistro": 157,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655265.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:31:27-05:00",
                                                    "NumeroDeRegistro": 158,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655267.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:34:52-05:00",
                                                    "NumeroDeRegistro": 159,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655269.24
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:36:03-05:00",
                                                    "NumeroDeRegistro": 160,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655270.56
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:38:13-05:00",
                                                    "NumeroDeRegistro": 161,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655272.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.544
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:41:08-05:00",
                                                    "NumeroDeRegistro": 162,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655276.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:42:03-05:00",
                                                    "NumeroDeRegistro": 163,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655277.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.103
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:46:26-05:00",
                                                    "NumeroDeRegistro": 164,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655282.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:48:31-05:00",
                                                    "NumeroDeRegistro": 165,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655283.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.768
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:50:26-05:00",
                                                    "NumeroDeRegistro": 166,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655286.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:55:06-05:00",
                                                    "NumeroDeRegistro": 167,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655294.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:01:31-05:00",
                                                    "NumeroDeRegistro": 168,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655298.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:09:47-05:00",
                                                    "NumeroDeRegistro": 169,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655301.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:10:57-05:00",
                                                    "NumeroDeRegistro": 170,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655302.36
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:16:16-05:00",
                                                    "NumeroDeRegistro": 171,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655303.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:18:46-05:00",
                                                    "NumeroDeRegistro": 172,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655305.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:20:31-05:00",
                                                    "NumeroDeRegistro": 173,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655306.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:22:36-05:00",
                                                    "NumeroDeRegistro": 174,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655316.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:25:10-05:00",
                                                    "NumeroDeRegistro": 175,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655325.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:33:00-05:00",
                                                    "NumeroDeRegistro": 176,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655326.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.334
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:38:02-05:00",
                                                    "NumeroDeRegistro": 177,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655328.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.764
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:40:19-05:00",
                                                    "NumeroDeRegistro": 178,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655330.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:41:57-05:00",
                                                    "NumeroDeRegistro": 179,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655333.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.088
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:43:57-05:00",
                                                    "NumeroDeRegistro": 180,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655336.42
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:45:53-05:00",
                                                    "NumeroDeRegistro": 181,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655338.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:49:37-05:00",
                                                    "NumeroDeRegistro": 182,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655343.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:57:08-05:00",
                                                    "NumeroDeRegistro": 183,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655345.24
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:06:14-05:00",
                                                    "NumeroDeRegistro": 184,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655349.65
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:08:21-05:00",
                                                    "NumeroDeRegistro": 185,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655351.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:10:45-05:00",
                                                    "NumeroDeRegistro": 186,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655371.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:23:24-05:00",
                                                    "NumeroDeRegistro": 187,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655376.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:24:45-05:00",
                                                    "NumeroDeRegistro": 188,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655377.38
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.105
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:26:30-05:00",
                                                    "NumeroDeRegistro": 189,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655388.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.398
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:29:28-05:00",
                                                    "NumeroDeRegistro": 190,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655406.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.384
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:32:27-05:00",
                                                    "NumeroDeRegistro": 191,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655414.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:46:05-05:00",
                                                    "NumeroDeRegistro": 192,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655445.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.897
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:47:47-05:00",
                                                    "NumeroDeRegistro": 193,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655448.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:48:33-05:00",
                                                    "NumeroDeRegistro": 194,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655450.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.776
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:50:04-05:00",
                                                    "NumeroDeRegistro": 195,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655454.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:53:30-05:00",
                                                    "NumeroDeRegistro": 196,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655456.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:59:06-05:00",
                                                    "NumeroDeRegistro": 197,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655478.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:04:07-05:00",
                                                    "NumeroDeRegistro": 198,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655483.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:07:34-05:00",
                                                    "NumeroDeRegistro": 199,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655503.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:09:24-05:00",
                                                    "NumeroDeRegistro": 200,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655508.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:11:34-05:00",
                                                    "NumeroDeRegistro": 201,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655515.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 7.367
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:16:05-05:00",
                                                    "NumeroDeRegistro": 202,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655524.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:24:51-05:00",
                                                    "NumeroDeRegistro": 203,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655526.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:27:33-05:00",
                                                    "NumeroDeRegistro": 204,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655530.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.146
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:30:25-05:00",
                                                    "NumeroDeRegistro": 205,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655539.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:36:21-05:00",
                                                    "NumeroDeRegistro": 206,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655548.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:37:53-05:00",
                                                    "NumeroDeRegistro": 207,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655550.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.765
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:43:25-05:00",
                                                    "NumeroDeRegistro": 208,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655575.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:47:18-05:00",
                                                    "NumeroDeRegistro": 209,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655584.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:52:59-05:00",
                                                    "NumeroDeRegistro": 210,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655588.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:56:37-05:00",
                                                    "NumeroDeRegistro": 211,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 655592.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 38173.22,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 1683.592
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 211
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0002"
                                    }
                                ],
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionDispensario": 0.001,
                                        "LocalizODescripSistMedicionDispensario": "Sistema de desplazamiento positivo por manguera del dispensario DISP-0003",
                                        "SistemaMedicionDispensario": "SMD-DISP-0003",
                                        "VigenciaCalibracionSistMedicionDispensario": "2021-02-25"
                                    }
                                ]
                            },
                            {
                                "ClaveDispensario": "DISP-0004",
                                "Manguera": [
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:22:50-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341670.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:27:06-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341679.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:38:36-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341706.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.467
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:57:06-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341742.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 36.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:59:57-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341764.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:12:28-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341803.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 39.757
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:15:58-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341804.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:22:10-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341807.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:22:24-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341815.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:35:29-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341825.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:55:36-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341829.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.97
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:23:47-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341847.48
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:26:23-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341864.68
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:29:01-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341877.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:31:27-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341887.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:42:49-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341888.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.882
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:55:57-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341893.21
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:58:43-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341897.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:11:25-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341902.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:12:10-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341904.24
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:19:58-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341907.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.253
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:26:31-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341912.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:30:16-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341934.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:44:12-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 341961.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.46
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:50:10-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342029.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 68.593
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:57:17-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342032.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.088
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:05:32-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342037.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:25:45-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342072.39
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 35.289
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:45:10-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342073.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.323
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:48:41-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342075.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:54:47-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342078.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:58:13-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342131.28
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 53.161
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:16:25-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342143.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.295
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:29:12-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342159.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 16.138
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:34:57-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342161.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:35:38-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342166.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:57:37-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342168.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:18:56-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342190.59
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:20:37-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342195.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:21:38-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342196.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.103
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:24:15-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342209.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 13.233
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:42:46-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342231.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:17:07-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342235.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:19:46-05:00",
                                                    "NumeroDeRegistro": 44,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342243.81
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.58
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:00:55-05:00",
                                                    "NumeroDeRegistro": 45,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342248.22
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:19:52-05:00",
                                                    "NumeroDeRegistro": 46,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342252.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:58:03-05:00",
                                                    "NumeroDeRegistro": 47,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342259.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:10:34-05:00",
                                                    "NumeroDeRegistro": 48,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342268.07
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.402
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:21:28-05:00",
                                                    "NumeroDeRegistro": 49,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342272.48
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:30:20-05:00",
                                                    "NumeroDeRegistro": 50,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342294.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:33:39-05:00",
                                                    "NumeroDeRegistro": 51,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342304.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:51:27-05:00",
                                                    "NumeroDeRegistro": 52,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342358.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 53.896
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:59:08-05:00",
                                                    "NumeroDeRegistro": 53,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342373.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:18:51-05:00",
                                                    "NumeroDeRegistro": 54,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342375.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.768
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:22:10-05:00",
                                                    "NumeroDeRegistro": 55,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342381.82
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.617
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:29:59-05:00",
                                                    "NumeroDeRegistro": 56,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342382.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.88
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:40:40-05:00",
                                                    "NumeroDeRegistro": 57,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342398.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.439
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:55:15-05:00",
                                                    "NumeroDeRegistro": 58,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 342409.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 17036.2,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 751.471
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 58
                                        },
                                        "IdentificadorManguera": "DISP-0004-MGA-0002"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:11:16-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335586.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.222
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:13:56-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335587.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.174
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:27:30-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335702.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 114.875
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:43:25-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335726.75
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 24.4
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:13:16-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335774.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 47.412
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:21:16-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335782.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:24:09-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335784.98
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:27:04-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335796.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 11.028
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:00:47-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335816.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:36:16-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335870.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 54.963
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:56:25-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335888.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.644
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:53:25-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 335962.72
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 74.107
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:24:36-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336015.65
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 52.933
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:08:31-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336035.65
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:14:12-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336040.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.647
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:00:01-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336060.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:01:27-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336061.85
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.544
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:30:07-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336064.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.206
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:50:12-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336086.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:59:00-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336106.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:27:10-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336134.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 28.213
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:55:07-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336137.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.084
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:20:06-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336177.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 39.7
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:32:26-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336185.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:49:25-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336327.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 141.156
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:14:22-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336347.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:27:16-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336351.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:30:50-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336371.49
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:33:31-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336380.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.822
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:46:22-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336436.63
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 56.31
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:56:15-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336467.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 30.878
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:01:18-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336489.56
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:15:29-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336511.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 22.056
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:36:41-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "A",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336531.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:41:24-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336552.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.173
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:56:41-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 22.67,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 336557.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.411
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 22060.74,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 973.125
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 36
                                        },
                                        "IdentificadorManguera": "DISP-0004-MGA-0004"
                                    }
                                ],
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionDispensario": 0.001,
                                        "LocalizODescripSistMedicionDispensario": "Sistema de desplazamiento positivo por manguera del dispensario DISP-0004",
                                        "SistemaMedicionDispensario": "SMD-DISP-0004",
                                        "VigenciaCalibracionSistMedicionDispensario": "2021-02-25"
                                    }
                                ]
                            }
                        ],
                        "GasolinaConCombustibleNoFosil": "No",
                        "MarcaComercial": "MAGNA",
                        "Tanque": [
                            {
                                "CapacidadFondajeTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 1000.0
                                },
                                "CapacidadOperativaTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 49500.0
                                },
                                "CapacidadTotalTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 60000.0
                                },
                                "CapacidadUtilTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 58500.0
                                },
                                "ClaveIdentificacionTanque": "STQ-EDS-0001",
                                "Entregas": {
                                    "SumaVolumenEntregado": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalEntregas": 0
                                },
                                "EstadoTanque": "O",
                                "Existencias": {
                                    "FechaYHoraEstaMedicion": "2022-06-24T19:00:00-05:00",
                                    "FechaYHoraMedicionAnterior": "2022-06-23T19:00:00-05:00",
                                    "HoraEntregaAcumulado": "19:00:00-05:00",
                                    "HoraRecepcionAcumulado": "19:00:00-05:00",
                                    "VolumenAcumOpsEntrega": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 8055.457
                                    },
                                    "VolumenAcumOpsRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "VolumenExistencias": 22285.574,
                                    "VolumenExistenciasAnterior": 30341.031
                                },
                                "Localizaciony/oDescripcionTanque": "MAGNA",
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionTanque": 0.001,
                                        "LocalizODescripSistMedicionTanque": "Sistema de medición estático para el tanque STQ-EDS-0001",
                                        "SistemaMedicionTanque": "SME-STQ-EDS-0001",
                                        "VigenciaCalibracionSistMedicionTanque": "2021-02-25"
                                    }
                                ],
                                "Recepciones": {
                                    "SumaVolumenRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalRecepciones": 0
                                },
                                "VigenciaCalibracionTanque": "2021-02-25",
                                "VolumenMinimoOperacion": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 1500.0
                                }
                            }
                        ]
                    },
                    {
                        "ClaveProducto": "PR03",
                        "ClaveSubProducto": "SP18",
                        "DieselConCombustibleNoFosil": "No",
                        "Dispensario": [
                            {
                                "ClaveDispensario": "DISP-0004",
                                "Manguera": [
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:44:17-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955524.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 65.91
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:01:33-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955705.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 168.917
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:49:36-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955771.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 65.132
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:12:00-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955823.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 52.044
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:22:41-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955824.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.253
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:54:38-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 955866.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 41.754
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:15:15-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956166.1
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 300.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:42:50-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956180.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 14.614
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:34:28-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956199.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.159
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:36:58-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956205.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.173
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:22:53-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956420.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 215.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:24:15-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956430.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:32:42-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956463.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 32.241
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:54:47-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956627.01
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 164.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:25:25-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956649.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.155
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:03:57-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956708.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 58.23
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:22:35-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956760.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 52.197
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:39:01-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956841.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 81.592
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:53:10-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 956925.99
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 84.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:34:42-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 957005.32
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 79.332
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:35:36-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 957011.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.097
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:44:22-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 957060.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 48.861
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:21:29-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 957135.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 75.157
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 38915.8,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 1624.818
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 23
                                        },
                                        "IdentificadorManguera": "DISP-0004-MGA-0001"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:36:11-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 827557.34
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 90.649
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:52:48-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 827648.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 91.356
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:38:44-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 827732.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 83.51
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:40:01-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 827753.08
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.157
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:58:15-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 827811.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 52.185
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:11:44-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828011.54
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 200.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:20:33-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828086.91
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 75.37
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:29:14-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828504.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 417.119
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:34:45-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828635.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 131.124
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:24:54-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828662.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.156
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:32:41-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828707.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 45.66
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:20:53-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 828734.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.207
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:45:58-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829134.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 400.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:01:23-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829534.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 400.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:09:29-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829734.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 200.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:28:23-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829755.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.157
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:37:06-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829807.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 52.484
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:39:31-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829850.12
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 36.322
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:14:36-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 829934.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 83.934
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:40:18-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 830056.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 122.618
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:48:57-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 830139.67
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 83.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:36:58-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 830171.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.463
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:50:52-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 23.95,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 830249.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 77.712
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 64839.03,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 2707.183
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 23
                                        },
                                        "IdentificadorManguera": "DISP-0004-MGA-0003"
                                    }
                                ],
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionDispensario": 0.001,
                                        "LocalizODescripSistMedicionDispensario": "Sistema de desplazamiento positivo por manguera del dispensario DISP-0004",
                                        "SistemaMedicionDispensario": "SMD-DISP-0004",
                                        "VigenciaCalibracionSistMedicionDispensario": "2021-02-25"
                                    }
                                ]
                            }
                        ],
                        "MarcaComercial": "DIESEL",
                        "Tanque": [
                            {
                                "CapacidadFondajeTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 2000.0
                                },
                                "CapacidadOperativaTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 38000.0
                                },
                                "CapacidadTotalTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 40000.0
                                },
                                "CapacidadUtilTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 36000.0
                                },
                                "ClaveIdentificacionTanque": "STQ-EDS-0003",
                                "Entregas": {
                                    "SumaVolumenEntregado": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalEntregas": 0
                                },
                                "EstadoTanque": "O",
                                "Existencias": {
                                    "FechaYHoraEstaMedicion": "2022-06-24T19:00:00-05:00",
                                    "FechaYHoraMedicionAnterior": "2022-06-23T18:59:00-05:00",
                                    "HoraEntregaAcumulado": "19:00:00-05:00",
                                    "HoraRecepcionAcumulado": "19:00:00-05:00",
                                    "VolumenAcumOpsEntrega": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 4332.001
                                    },
                                    "VolumenAcumOpsRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "VolumenExistencias": 12463.278,
                                    "VolumenExistenciasAnterior": 16795.279
                                },
                                "Localizaciony/oDescripcionTanque": "DIESEL",
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionTanque": 0.001,
                                        "LocalizODescripSistMedicionTanque": "Sistema de medición estático para el tanque STQ-EDS-0003",
                                        "SistemaMedicionTanque": "SME-STQ-EDS-0003",
                                        "VigenciaCalibracionSistMedicionTanque": "2021-02-25"
                                    }
                                ],
                                "Recepciones": {
                                    "SumaVolumenRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalRecepciones": 0
                                },
                                "VigenciaCalibracionTanque": "2021-02-25",
                                "VolumenMinimoOperacion": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 4000.0
                                }
                            }
                        ]
                    },
                    {
                        "ClaveProducto": "PR07",
                        "ClaveSubProducto": "SP17",
                        "ComposOctanajeGasolina": 92,
                        "Dispensario": [
                            {
                                "ClaveDispensario": "DISP-0003",
                                "Manguera": [
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:16:33-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941855.52
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.5
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:39:38-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941880.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 16.821
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:18:07-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941884.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:25:04-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941886.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.261
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:40:34-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941906.2
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:48:01-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941921.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.055
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:46:31-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941931.77
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.209
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:59:08-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941935.97
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:35:58-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941937.23
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.261
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:29:28-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941958.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:34:21-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 941979.26
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:46:33-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942018.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 39.192
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:15:34-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942064.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 46.247
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:44:33-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942077.31
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.61
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:29:03-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942078.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.586
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:42:00-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942091.51
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.21
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:11:04-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942141.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 50.441
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:23:36-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942166.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:27:09-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942200.58
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 33.633
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:57:47-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942217.4
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.214
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:00:58-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942223.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.831
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:05:05-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942243.33
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:22:57-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942247.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:33:43-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942260.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.61
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:56:39-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942288.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 28.794
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:59:48-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942313.93
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:14:48-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942365.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 51.497
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:20:07-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942407.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 42.034
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:22:52-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942427.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:40:23-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942467.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:49:25-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942482.47
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:33:15-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942503.48
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:45:36-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942509.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.305
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:54:08-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942511.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.261
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:06:53-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942526.05
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:10:08-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942542.86
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.214
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:20:54-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942551.27
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:24:21-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942572.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:28:43-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942584.9
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.41
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:02:14-05:00",
                                                    "NumeroDeRegistro": 40,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942616.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 31.945
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:12:22-05:00",
                                                    "NumeroDeRegistro": 41,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942618.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:18:28-05:00",
                                                    "NumeroDeRegistro": 42,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942626.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:32:34-05:00",
                                                    "NumeroDeRegistro": 43,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 942712.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 85.221
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 19163.0,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 805.548
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 43
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0003"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:04:37-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594280.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 7.9
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-23T19:10:13-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594300.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:43:47-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594306.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 6.305
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:10:02-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594314.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 7.566
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:34:55-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594339.03
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:38:15-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594340.29
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.261
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:56:04-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594342.39
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:05:57-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594344.5
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:28:46-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594386.53
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 42.034
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:48:17-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594390.73
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:54:56-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594392.83
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:31:33-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594394.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:20:47-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594404.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:22:33-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594424.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.2
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:27:24-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594445.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:52:12-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594457.95
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:06:16-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594484.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 26.067
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:11:23-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594499.02
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:12:54-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594507.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:45:45-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 594550.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 43.0
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 6217.58,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 261.368
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 20
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0005"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T01:23:53-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670640.78
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.801
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T03:19:34-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670653.39
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.21
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:26:47-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670678.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 24.957
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:43:35-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670693.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 15.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:58:54-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670730.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 37.025
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:30:21-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670735.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:58:40-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670755.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.333
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:26:12-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670756.55
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 0.848
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:40:17-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670764.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:02:50-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670807.0
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 42.043
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:18:13-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670827.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.597
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:28:26-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670867.6
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 40.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:53:34-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670871.8
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:31:30-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670884.41
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.61
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:01:59-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670888.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:25:13-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670908.62
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 17.9
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:37:29-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670928.79
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.178
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:25:31-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670945.61
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 16.814
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:47:51-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670966.64
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.033
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:11:18-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 670979.25
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 12.61
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T17:56:20-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671029.69
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 50.441
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T18:17:39-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 671050.71
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 9521.31,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 400.23
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 22
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0007"
                                    },
                                    {
                                        "Entregas": {
                                            "Entrega": [
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T00:39:10-05:00",
                                                    "NumeroDeRegistro": 1,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627647.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.635
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:14:05-05:00",
                                                    "NumeroDeRegistro": 2,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627648.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.009
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:28:35-05:00",
                                                    "NumeroDeRegistro": 3,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627652.35
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:39:17-05:00",
                                                    "NumeroDeRegistro": 4,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627677.57
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.221
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T02:49:53-05:00",
                                                    "NumeroDeRegistro": 5,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627712.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 34.572
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:17:36-05:00",
                                                    "NumeroDeRegistro": 6,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627763.19
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 51.051
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T04:48:28-05:00",
                                                    "NumeroDeRegistro": 7,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627803.48
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 33.99
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:05:47-05:00",
                                                    "NumeroDeRegistro": 8,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627820.3
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 16.814
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:18:48-05:00",
                                                    "NumeroDeRegistro": 9,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627828.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 8.407
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:30:28-05:00",
                                                    "NumeroDeRegistro": 10,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627833.7
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 5.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T05:42:42-05:00",
                                                    "NumeroDeRegistro": 11,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627858.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 25.221
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T06:33:48-05:00",
                                                    "NumeroDeRegistro": 12,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627868.92
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 10.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:06:36-05:00",
                                                    "NumeroDeRegistro": 13,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627889.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:19:50-05:00",
                                                    "NumeroDeRegistro": 14,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627894.94
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.9
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:38:04-05:00",
                                                    "NumeroDeRegistro": 15,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627915.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:53:59-05:00",
                                                    "NumeroDeRegistro": 16,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627924.37
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.207
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:56:58-05:00",
                                                    "NumeroDeRegistro": 17,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627928.57
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T07:59:05-05:00",
                                                    "NumeroDeRegistro": 18,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627932.56
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.993
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:14:24-05:00",
                                                    "NumeroDeRegistro": 19,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627936.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T08:48:20-05:00",
                                                    "NumeroDeRegistro": 20,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627938.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:15:44-05:00",
                                                    "NumeroDeRegistro": 21,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627958.87
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T09:58:15-05:00",
                                                    "NumeroDeRegistro": 22,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 627960.13
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.265
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:20:18-05:00",
                                                    "NumeroDeRegistro": 23,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628034.76
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 74.63
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:55:19-05:00",
                                                    "NumeroDeRegistro": 24,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628038.96
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T10:57:51-05:00",
                                                    "NumeroDeRegistro": 25,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628043.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:31:16-05:00",
                                                    "NumeroDeRegistro": 26,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628063.17
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 20.0
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:42:50-05:00",
                                                    "NumeroDeRegistro": 27,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628066.11
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.942
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T11:54:05-05:00",
                                                    "NumeroDeRegistro": 28,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628108.14
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 42.034
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:27:49-05:00",
                                                    "NumeroDeRegistro": 29,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628112.36
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.217
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T12:34:27-05:00",
                                                    "NumeroDeRegistro": 30,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628114.46
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:14:18-05:00",
                                                    "NumeroDeRegistro": 31,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628143.89
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 29.424
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:28:19-05:00",
                                                    "NumeroDeRegistro": 32,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628148.09
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T13:52:13-05:00",
                                                    "NumeroDeRegistro": 33,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628151.45
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 3.363
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:04:59-05:00",
                                                    "NumeroDeRegistro": 34,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628153.74
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.292
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T14:36:22-05:00",
                                                    "NumeroDeRegistro": 35,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628155.43
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 1.69
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:01:53-05:00",
                                                    "NumeroDeRegistro": 36,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628163.84
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.207
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:14:02-05:00",
                                                    "NumeroDeRegistro": 37,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628168.04
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 4.203
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T15:20:39-05:00",
                                                    "NumeroDeRegistro": 38,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628170.15
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 2.102
                                                    }
                                                },
                                                {
                                                    "FechaYHoraEntrega": "2022-06-24T16:02:17-05:00",
                                                    "NumeroDeRegistro": 39,
                                                    "PrecioVentaTotalizadorInsta": 23.79,
                                                    "TipoDeRegistro": "D",
                                                    "VolumenEntregadoTotalizadorAcum": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 628191.16
                                                    },
                                                    "VolumenEntregadoTotalizadorInsta": {
                                                        "UnidadDeMedida": "UM03",
                                                        "ValorNumerico": 21.017
                                                    }
                                                }
                                            ],
                                            "SumaVentas": 12581.38,
                                            "SumaVolumenEntregado": {
                                                "UnidadDeMedida": "UM03",
                                                "ValorNumerico": 528.862
                                            },
                                            "TotalDocumentos": 0,
                                            "TotalEntregas": 39
                                        },
                                        "IdentificadorManguera": "DISP-0003-MGA-0001"
                                    }
                                ],
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionDispensario": 0.001,
                                        "LocalizODescripSistMedicionDispensario": "Sistema de desplazamiento positivo por manguera del dispensario DISP-0003",
                                        "SistemaMedicionDispensario": "SMD-DISP-0003",
                                        "VigenciaCalibracionSistMedicionDispensario": "2021-02-25"
                                    }
                                ]
                            }
                        ],
                        "GasolinaConCombustibleNoFosil": "No",
                        "MarcaComercial": "PREMIUM",
                        "Tanque": [
                            {
                                "CapacidadFondajeTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 1000.0
                                },
                                "CapacidadOperativaTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 29500.0
                                },
                                "CapacidadTotalTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 40000.0
                                },
                                "CapacidadUtilTanque": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 39000.0
                                },
                                "ClaveIdentificacionTanque": "STQ-EDS-0002",
                                "Entregas": {
                                    "SumaVolumenEntregado": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalEntregas": 0
                                },
                                "EstadoTanque": "O",
                                "Existencias": {
                                    "FechaYHoraEstaMedicion": "2022-06-24T19:01:00-05:00",
                                    "FechaYHoraMedicionAnterior": "2022-06-23T19:00:00-05:00",
                                    "HoraEntregaAcumulado": "19:01:00-05:00",
                                    "HoraRecepcionAcumulado": "19:01:00-05:00",
                                    "VolumenAcumOpsEntrega": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 1996.008
                                    },
                                    "VolumenAcumOpsRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "VolumenExistencias": 16176.9,
                                    "VolumenExistenciasAnterior": 18172.908
                                },
                                "Localizaciony/oDescripcionTanque": "PREMIUM",
                                "Medidores": [
                                    {
                                        "IncertidumbreMedicionSistMedicionTanque": 0.001,
                                        "LocalizODescripSistMedicionTanque": "Sistema de medición estático para el tanque STQ-EDS-0002",
                                        "SistemaMedicionTanque": "SME-STQ-EDS-0002",
                                        "VigenciaCalibracionSistMedicionTanque": "2021-02-25"
                                    }
                                ],
                                "Recepciones": {
                                    "SumaVolumenRecepcion": {
                                        "UnidadDeMedida": "UM03",
                                        "ValorNumerico": 0.0
                                    },
                                    "TotalDocumentos": 0,
                                    "TotalRecepciones": 0
                                },
                                "VigenciaCalibracionTanque": "2021-02-25",
                                "VolumenMinimoOperacion": {
                                    "UnidadDeMedida": "UM03",
                                    "ValorNumerico": 1000.0
                                }
                            }
                        ]
                    }
                ],
                "RfcContribuyente": "CGL1402138J1",
                "RfcProveedor": "GTE090907184",
                "RfcRepresentanteLegal": "OICG751003FV3",
                "Version": "1.0"
    }

    guardar_reporte_diario_json(response_data)
