#include "internal.h"

int				hash(char *key)
{
    int			hash = 0;
    int			i = 0;

    while (key && key[i])
    {
        hash += key[i];
        i++;
    }
    return (hash % HASH_SIZE);
}