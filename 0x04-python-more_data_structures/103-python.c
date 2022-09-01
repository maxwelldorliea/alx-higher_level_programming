#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	int size, allot, i;
	const char *type;
	PyListObject *list;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);
	allot = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", allot);
	list =  ((PyListObject *)p);
	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
	printf("Element 0: %s\n", type);
	/**print_python_bytes(p);**/
}

void print_python_bytes(PyObject *p)
{
	int size, i;
	PyBytesObject *bytes;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	//s = PyBytes_AsString(p);
	size = PyBytes_Size(p);
	bytes = (PyBytesObject *)p;
	printf("  size: %d\n", size);
	if (size > 10)
		size = 10;
	else if (size < 10)
		size++;
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
