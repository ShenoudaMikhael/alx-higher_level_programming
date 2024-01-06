#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - detect if list is palindrome
 * @head: linked list
 * Return: int 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int list_len = 1, i, j;
	listint_t *tmp, *rev_tmp;
	tmp = *head;
	rev_tmp = *head;
	while (tmp->next)
	{
		list_len++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < list_len / 2; i++)
	{
		rev_tmp = *head;
		for (j = 0; j < list_len - i - 1; j++)
		{
			rev_tmp = rev_tmp->next;
		}
		if (rev_tmp->n != tmp->n)
		{
			return (0);
		}
		tmp = tmp->next;
	}

	return (1);
}
