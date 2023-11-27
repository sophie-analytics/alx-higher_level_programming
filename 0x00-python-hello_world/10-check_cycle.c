#include "lists.h"
#include <stddef.h>

/**
* check_cycle - checks if there is a cycle
* @list: The head pointed to the linkedlist
* Return: 0 for no cycle 1 for cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *second_ptr;
	listint_t *first_ptr;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	second_ptr = list;
	first_ptr = list->next;

	while (first_ptr != NULL && first_ptr->next != NULL)
	{
		if (first_ptr == second_ptr)
		{
			return (1);
		}

		first_ptr = first_ptr->next->next;
		second_ptr = second_ptr->next;
	}
	return (0);
}
