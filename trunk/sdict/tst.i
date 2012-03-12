%module tst

%{
#include "tst.h"
%}

extern tst_db *create_tst_db();
extern void tst_put(tst_db * db, const char *key, PyObject * value);
extern PyObject * tst_get(tst_db * db, const char *key);
extern void tst_prefix(tst_db *db, const char* prefix,
             PyObject* result, int limit,enum SortingOrder);
extern void tst_less(tst_db *db, const char* key,
             PyObject* result, int limit);
extern void tst_greater(tst_db *db, const char* key,
             PyObject* result, int limit);

extern void tst_delete(tst_db *db, const char * key);
extern void free_tst_db(tst_db * db);

