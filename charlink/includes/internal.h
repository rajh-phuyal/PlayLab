
#ifndef INTERNAL_H
# define INTERNAL_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <limits.h>
# include <stdbool.h>

# include "charlink.h"

# define HASH_SIZE 10

// hash function
int				hash(char *key);

// helper functions
void			print_table(link_table *table);
node			*create_node();
void			free_node(node *node);

#endif