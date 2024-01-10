
/*#include <python3.11/Python.h>*/
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - get py list info.
 * @p: PyObject.
 */
void print_python_list(PyObject *p)
{
	int size, allocated, i;
	const char *type;

	/* subtype of PyObject represents a Python list object */
	PyListObject *list_ptr = (PyListObject *)p;

	/*extension of PyObject that adds the ob_size field*/
	PyVarObject *var = (PyVarObject *)p;

	/* 1 - got size */
	size = var->ob_size;
	/* 2 - got allocated */
	allocated = list_ptr->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list_ptr->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list_ptr->ob_item[i]);
	}
}

/**
 * print_python_bytes - print python bytes.
 * @p: A PyObject.
 */
void print_python_bytes(PyObject *p)
{
	char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}