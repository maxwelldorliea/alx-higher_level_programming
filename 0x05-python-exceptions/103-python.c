#include <Python.h>
#include <stdio.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	int size, allot, i;
	const char *type;
	PyListObject *list = ((PyListObject *)p);
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allot = list->allocated;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allot);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		setbuf(stdout, NULL);
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
			setbuf(stdout, NULL);
		}

		else if (strcmp(type, "float") == 0) 
		{
			print_python_float(list->ob_item[i]);
		}
	}
}

void print_python_bytes(PyObject *p)
{
	int size, i;
	char *s;
	PyBytesObject *bytes;

	printf("[.] bytes object info\n");
	setbuf(stdout, NULL);

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}
	bytes = (PyBytesObject *)p;
	s = bytes->ob_sval;
	size = ((PyVarObject *)(bytes))->ob_size;
	printf("  size: %d\n", size);
	setbuf(stdout, NULL);
	printf("  trying string: %s\n", s);
	setbuf(stdout, NULL);
	if (size > 10)
		size = 10;
	else if (size < 10)
		size++;
	printf("  first %d bytes: ", size);
	
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", s[i]);
		setbuf(stdout, NULL);
		if (i == (size - 1))
		{
			printf("\n");
			setbuf(stdout, NULL);
		}
		else
		{
			printf(" ");
			setbuf(stdout, NULL);
		}
	}
}


void print_python_float(PyObject *p)
{
	double val;
	char *valf;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = ((PyFloatObject *)p)->ob_fval;
	valf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", valf);
	setbuf(stdout, NULL);
}
