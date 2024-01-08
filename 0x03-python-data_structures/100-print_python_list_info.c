#include "python3.11/Python.h"
/**
 * print_python_list_info - print oython list info
 * @p: list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{

		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
