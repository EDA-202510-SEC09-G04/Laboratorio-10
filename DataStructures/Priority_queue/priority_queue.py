from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import index_pq_entry as pqe


def new_heap(is_min_pq=True):
    
    new_list = lt.new_list()
    funcion_comparacion = default_compare_lower_value
    
    if  not is_min_pq:
        
        funcion_comparacion = default_compare_lower_value
        
        
    
    new_heap = {
        
        'elements': new_list,
        'size': 0,
        'cmp_function': funcion_comparacion
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