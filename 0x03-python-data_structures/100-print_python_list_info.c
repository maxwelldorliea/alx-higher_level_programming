#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>


/**
 * print_python_list_info - prints info about python list
 * @p: python list to be pass
 * Return: Nothing
 */


void print_python_list_info(PyObject *p)
{
	int len = PyList_Size(p), i = 0;
	int allot = (((PyListObject *)p)->allocated);
	
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", allot);

	while (i < len)
	{
		PyObject *ele = PyList_GetItem(p, i);
		char *eleName = Py_TYPE(ele)->tp_name;
		printf("Element %d: %s\n", i, eleName);
		i++;
	}
}
