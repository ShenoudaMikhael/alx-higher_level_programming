#include "python3.11/Python.h"
void print_python_list_info(PyObject *p)
{

    Py_ssize_t n = PyList_Size(p);
    

    printf("[*] Size of the Python List = %ld\n", n);


    return;
}