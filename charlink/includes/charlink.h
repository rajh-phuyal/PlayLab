#ifndef CHARLINK_H
# define CHARLINK_H

// enum that will be used to determine the type of data
typedef enum data_type
{
    INT,
    CHAR,
    BOOL,
    FLOAT,
    DOUBLE,
    STRING
}	data_type;

// structures that will handle the hash table
typedef struct node
{
    char			*key;
    void			*value;
    struct s_node	*next;
}	node;

typedef struct link_table link_table; // forward declaration

// the methods the hash table will have
typedef void    (*datadel)(struct link_table *table, char *key);
typedef void    *(*dataget)(struct link_table *table, char *key);
typedef void    *(*dataset)(struct link_table *table, char *key, void *value);


typedef struct link_table
{
    datadel     del;
    dataget     get;
    dataset     set;
    int		    size;
    node	    **array;
    bool        overwrite;
    data_type   type;
}	link_table;

// create and delete
void            charlink_delete(link_table *table, bool freeval);
link_table      *charlink_create(data_type type, int size, bool overwrite);


# endif