
#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
listint_t *i = list;

if (!list)
return (0);
while (list)
{
list = list->next;
if (i == list)
return (1);
if (!(list->next) || !(list->next->next))
return (0);
i = i->next;
list = list->next->next;
}
return (0);
}
