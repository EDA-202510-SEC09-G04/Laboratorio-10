"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import csv
import time
import os

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


# ___________________________________________________
#  Importaciones
# ___________________________________________________

from DataStructures.List import single_linked_list as lt
from DataStructures.Priority_queue  import priority_queue as pq
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = new_analyzer()
    return analyzer

def new_analyzer():
    """ Inicializa el analizador

   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
            'stops': {},
            'connections': None,
            'components': None,
            'paths': None,
            'pq': pq.new_heap(True)
        }

     


        return analyzer
    except Exception as exp:
        return exp

# ___________________________________________________
#  TODO Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def load_services(analyzer, file):
    try:
        with open(file, encoding="utf-8") as csvfile:
            input_file = csv.DictReader(csvfile)

            for row in input_file:
                stop_code = row['BusStopCode']
                distance = float(row['Distance'])
                if stop_code not in analyzer['stops']:
                    analyzer['stops'][stop_code] = {
                        'services': [],
                        'min_distance': distance
                    }
                else:
                    if distance < analyzer['stops'][stop_code]['min_distance']:
                        analyzer['stops'][stop_code]['min_distance'] = distance
                analyzer['stops'][stop_code]['services'].append(row)
                pq.insert(analyzer['pq'], row, distance)

        print("Datos cargados: {} paradas.".format(len(analyzer['stops'])))
        return analyzer

    except Exception as e:
        print("Error al cargar los datos:", e)
        return analyzer 




    

#Funciones para la medición de tiempos

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def delta_time(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed








