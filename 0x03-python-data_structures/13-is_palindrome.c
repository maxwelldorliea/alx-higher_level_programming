#include "lists.h"
#include <stdlib.h>

/**
 * get_len - get the length of a linkedlist
 * @head: head of the linkedlist
 * Return: the length of a linkedlist
 */

int get_len(listint_t *head)
{
	listint_t *tmp = head;
	int len = 0;

	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}

	return (len);
}

/**
 * is_palindrome - check if a linkedlist is a palindrome
 * @head: head of the linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */


int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int *arr, len, i = 0, j = 0;

	if (!head)
		return (-1);

	if (!(*head))
		return (1);
	len = get_len(*head);
	arr = malloc(sizeof(*arr) * len);

	tmp = *head;

	while (tmp != NULL)
	{
		arr[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	i -= 1;
	while (i >= j)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
		i--;
		j++;
	}

	free(arr);

	return (1);
}
