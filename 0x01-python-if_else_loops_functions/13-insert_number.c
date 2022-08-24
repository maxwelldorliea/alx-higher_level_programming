#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;
	
	if (!head)
		return (NULL);

	node = malloc(sizeof(*node));

	if (node == NULL)
	{
		free(node);
		return (NULL);
	}


	node->n = number;
	node->next = NULL;

	if (!(*head))
	{
		*head = node;
		return (*head);
	}

	if ((*head)->n > node->n)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}

	tmp = *head;

	while (tmp->next != NULL)
	{
		if (tmp->next->n > node->n)
		{
			listint_t *tmp1 = tmp->next;
			tmp->next = node;
			node->next = tmp1;
			return (*head);
		}

		tmp = tmp->next;
	}

	tmp->next = node;

	return (*head);
}

