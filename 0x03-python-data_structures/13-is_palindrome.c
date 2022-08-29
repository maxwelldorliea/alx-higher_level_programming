#include "lists.h"
#include <stdlib.h>

/**
 * reverse - reverse a linkedlist
 * @head: head of the linkedlist
 * Return: the head of the reverse linkedlist
 */

listint_t *reverse(listint_t *head)
{
	listint_t *tmp = head, *prev = NULL, *next;

	while (tmp != NULL)
	{
		next = tmp->next;
		tmp->next = prev;
		prev = tmp;
		tmp = next;
	}

	tmp = prev;

	return (prev);
}

/**
 * is_palindrome - check if a linkedlist is a palindrome
 * @head: head of the linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */


int is_palindrome(listint_t **head)
{
	listint_t *tmp, *fast, *slow, *nhead;

	if (!head)
		return (-1);

	if (!(*head) || !(*head))
		return (1);

	slow = *head;
	fast = *head;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	nhead = reverse(slow);
	tmp = *head;

	while (nhead != NULL)
	{
		if (nhead->n != tmp->n)
			return (0);
		tmp = tmp->next;
		nhead = nhead->next;
	}

	return (1);
}
