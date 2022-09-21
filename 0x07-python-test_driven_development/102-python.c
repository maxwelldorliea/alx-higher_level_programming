#include <Python.h>


void print_python_string(PyObject *p)
{
	Py_ssize_t n;

	fflush(stdout);
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	n = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %zd\n", n);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &n));
	
}
