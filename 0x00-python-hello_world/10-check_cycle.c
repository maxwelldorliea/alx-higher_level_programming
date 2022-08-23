#include "lists.h"


/**
 * check_cycle - check if there is a circle in a linkedlist
 * @list: head of the linkedlist
 * Return 1 if true and 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
