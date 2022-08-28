#include "lists.h"



/**
 * is_palindrome - check if a linkedlist is a palindrome
 * @head: head of the linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */


int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *nhead = NULL, *tmp;

	if (!head)
		return (-1);

	if (!(*head))
		return (1);

	tmp = *head;

	while (tmp != NULL)
	{
		add_nodeint_end(&nhead, tmp->n);
		tmp = tmp->next;
	}


	while (nhead != NULL)
	{
		next = nhead->next;
		nhead->next = prev;
		prev = nhead;
		nhead = next;
	}

	nhead = prev;

	while (*head != NULL)
	{
		if ((*head)->n != nhead->n)
			return (0);
		*head = (*head)->next;
		nhead = nhead->next;
	}

	return (1);
}

