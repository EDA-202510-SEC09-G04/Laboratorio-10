from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as pqe


def new_heap(is_min_pq=True):
    """
    Crea una nueva cola de prioridad indexada.
    """
    new_list = lt.new_list()
    lt.add_last(new_list, None)  # Posición 0 del heap (no se usa realmente)

    cmp_function = default_compare_lower_value
    if not is_min_pq:
        cmp_function = default_compare_higher_value
    
    new_heap = {
        
        'elements': new_list,
        'size': 0,
        'cmp_function': cmp_function
    }

    return new_heap



def default_compare_higher_value(father_node,child_node):
    
    if pqe.get_key(father_node) >= pqe.get_key(child_node):
        
        return True
    
    return False



def default_compare_lower_value(father_node, child_node):
    if pqe.get_key(father_node) <= pqe.get_key(child_node):
     return True
 
    return False



def priority(my_heap,parent,child):
    
    cmp = my_heap["cmp_function"](parent, child)
    if cmp > 0:
        return True
    return False


def insert(my_heap, value, key):
    """
    Inserta una nueva entrada con key como prioridad y value como valor.
    """
    index = my_heap["size"] + 1

    # Crear entrada tipo pq_entry
    entry = pqe.new_pq_entry(key, value)
    pqe.set_index(entry, index)

    # Insertar al final del heap
    lt.add_last(my_heap["elements"], entry)

    # Actualizar tamaño
    my_heap["size"] += 1

    # Restaurar propiedad del heap
    swim(my_heap, index)

    return my_heap

def swim(my_heap, pos):
    """
    Sube un nodo desde la posición `pos` hasta su lugar correcto en el heap.
    """
    while pos > 1:
        parent = pos // 2

        child_node = lt.get_element(my_heap["elements"], pos)
        parent_node = lt.get_element(my_heap["elements"], parent)

        if not priority(my_heap, child_node, parent_node):
            # Ya está en la posición correcta, termina el ciclo naturalmente
            pos = 1  # fuerza la condición de salida sin usar break
        else:
            # Intercambiar posiciones
            lt.change_info(my_heap["elements"], pos, parent_node)
            lt.change_info(my_heap["elements"], parent, child_node)

            # Actualizar los índices internos
            pqe.set_index(child_node, parent)
            pqe.set_index(parent_node, pos)

            # Subir en el heap
            pos = parent
            

def size(my_heap):
    """
    Retorna el número de elementos en el heap (no incluye posición 0).
    """
    return my_heap["size"]

def is_empty(my_heap):
    """
    Retorna True si el heap está vacío.
    """
    return my_heap["size"] == 0

def get_first_priority(my_heap):
    """
    Retorna el valor del elemento con mayor prioridad sin eliminarlo.
    """
    if is_empty(my_heap):
        return None

    first_entry = lt.get_element(my_heap["elements"], 1)
    return pqe.get_value(first_entry)

def remove(my_heap):
    if is_empty(my_heap):
        return None

    root = lt.get_element(my_heap["elements"], 1)
    removed_value = pqe.get_value(root)

    last = lt.get_element(my_heap["elements"], my_heap["size"])
    lt.change_info(my_heap["elements"], 1, last)
    pqe.set_index(last, 1)

    lt.removeLast(my_heap["elements"])
    my_heap["size"] -= 1

    if my_heap["size"] > 0:
        sink(my_heap, 1)

    return removed_value

def sink(my_heap, pos):
    """
    Baja un nodo desde la raíz hasta su posición correcta en el heap.
    """
    size = my_heap["size"]
    while 2 * pos <= size:
        left = 2 * pos
        right = left + 1
        best_child = left

        # Si existe hijo derecho, escoger el que tenga mayor prioridad
        if right <= size:
            left_node = lt.get_element(my_heap["elements"], left)
            right_node = lt.get_element(my_heap["elements"], right)
            if priority(my_heap, right_node, left_node):
                best_child = right

        current_node = lt.get_element(my_heap["elements"], pos)
        child_node = lt.get_element(my_heap["elements"], best_child)

        # Si el hijo no tiene mayor prioridad, estamos listos
        if not priority(my_heap, child_node, current_node):
            pos = size + 1  # fuerza fin del ciclo
        else:
            # Intercambiar
            lt.change_info(my_heap["elements"], pos, child_node)
            lt.change_info(my_heap["elements"], best_child, current_node)

            # Actualizar índices
            pqe.set_index(child_node, pos)
            pqe.set_index(current_node, best_child)

            # Continuar con la nueva posición
            pos = best_child