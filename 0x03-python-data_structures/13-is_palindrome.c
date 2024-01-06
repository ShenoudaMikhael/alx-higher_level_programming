#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - detect if list is palindrome
 * @head: linked list
 * Return: int 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int list_len = 1;
	listint_t *tmp;
	tmp = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp->next)
	{
		list_len++;
		tmp = tmp->next;
	}
	tmp = *head;

	return (1);
}
