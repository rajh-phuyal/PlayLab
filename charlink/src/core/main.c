#include "internal.h"

// get the value of a key
void    *get(link_table *table, char *key)
{
    return NULL;
}

// set the value of a key
void    *set(link_table *table, char *key, void *value)
{
    return NULL;
}

// delete a key and its value
void    del(link_table *table, char *key)
{
    return;
}


link_table  *charlink_create(data_type type, int size, bool overwrite)
{
    link_table *table = malloc(sizeof(link_table));
    table->type = type;
    table->size = size;
    table->overwrite = overwrite;
    table->del = &del;
    table->get = &get;
    table->set = &set;
    return table;
}

void    charlink_delete(link_table *table, bool freeval)
{
    free(table);
    return;
}


int main(void)
{
    link_table *table = charlink_create(CHAR, 10, true);
    printf("Hash %d\n", hash("someshit"));
    printf("Hash %d\n", hash("someshitagain"));
    charlink_delete(table, true);
}