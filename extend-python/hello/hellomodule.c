#include <Python.h>

static PyObject *HelloError;

static PyObject *
hello_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(HelloError, "System command failed");
        return NULL;
    }
    return Py_BuildValue("i", sts);
}

static PyMethodDef HelloMethods[] = {
    {"system", hello_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
inithello(void)
{
    PyObject *m;

    m = Py_InitModule("hello", HelloMethods);
    if (m == NULL)
        return;

    HelloError = PyErr_NewException("hello.error", NULL, NULL);
    Py_INCREF(HelloError);
    PyModule_AddObject(m, "error", HelloError);
}
