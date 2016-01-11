#include <Python.h>
#include "structmember.h"

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

typedef struct {
    PyObject_HEAD
    PyObject *first;
    PyObject *last;
    int number;
} Hi;

static void
Hi_dealloc(Hi* self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    self->ob_type->tp_free((PyObject*)self);
}

static PyObject *
Hi_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Hi *self;

    self = (Hi *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyString_FromString("");
        if (self->first == NULL)
        {
            Py_DECREF(self);
            return NULL;
        }
        self->last = PyString_FromString("");
        if (self->last == NULL)
        {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }
    return (PyObject *)self;
}

static int
Hi_init(Hi *self, PyObject *args, PyObject *kwds)
{
    PyObject *first=NULL, *last=NULL, *tmp;

    static char *kwlist[] = {"first", "last", "number", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_XDECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_XDECREF(tmp);
    }
    return 0;
}

static PyMemberDef Hi_members[] = {
    {"first", T_OBJECT_EX, offsetof(Hi, first), 0,
     "first name"},
    {"last", T_OBJECT_EX, offsetof(Hi, last), 0,
     "last name"},
    {"number", T_INT, offsetof(Hi, number), 0,
     "hi object number"},
    {NULL}  /* Sentinel */
};

static PyObject *
Hi_name(Hi* self)
{
    static PyObject *format = NULL;
    PyObject *args, *result;

    if (format == NULL) {
        format = PyString_FromString("%s %s");
        if (format == NULL)
            return NULL;
    }

    if (self->first == NULL) {
        PyErr_SetString(PyExc_AttributeError, "first");
        return NULL;
    }

    if (self->last == NULL) {
        PyErr_SetString(PyExc_AttributeError, "last");
        return NULL;
    }

    args = Py_BuildValue("OO", self->first, self->last);
    if (args == NULL)
        return NULL;

    result = PyString_Format(format, args);
    Py_DECREF(args);

    return result;
}

static PyMethodDef Hi_methods[] = {
    {"name", (PyCFunction)Hi_name, METH_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject HiType = {
    PyObject_HEAD_INIT(NULL)
    0,                         /*ob_size*/
    "hello.Hi",                /*tp_name*/
    sizeof(Hi),          /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)Hi_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/
    "Hi objects",           /* tp_doc */
    0,                     /* tp_traverse */
    0,                     /* tp_clear */
    0,                     /* tp_richcompare */
    0,                     /* tp_weaklistoffset */
    0,                     /* tp_iter */
    0,                     /* tp_iternext */
    Hi_methods,             /* tp_methods */
    Hi_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Hi_init,      /* tp_init */
    0,                         /* tp_alloc */
    Hi_new,                 /* tp_new */
};

static PyMethodDef HelloMethods[] = {
    {"system", hello_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}
};

#ifndef PyMODINIT_FUNC  /* declarations for DLL import/export */
#define PyMODINIT_FUNC void
#endif
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

    if (PyType_Ready(&HiType) < 0)
        return;
    Py_INCREF(&HiType);
    PyModule_AddObject(m, "Hi", (PyObject *)&HiType);
}
