#include "lists.h"
#include <stdio.h>
/**
 * check - check list if palindrome
 * @head: start
 * @tail: end
 * Return: 0 or 1
 */
int check(listint_t *head, listint_t *tail)
{
	int q = 1;

	if (tail->next != NULL)
	{

		q = check(head, tail->next);
		if (q == 0)
		{
			return (0);
		}
		*head = *head->next;
		q = head->n == tail->n;
	}

	return (q);
}

/**
 * is_palindrome - detect if list is palindrome
 * @head: linked list
 * Return: int 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int list_len = 1;
	/*int  i, j;*/
	listint_t *tmp;
	listint_t *qq;
	/*listint_t *rev_tmp;*/
	tmp = *head;
	/*rev_tmp = *head;*/

	if (head == NULL || *head == NULL)
		return (1);

	tmp = *head;
	qq = *head;
	list_len = check(qq, tmp);

	return (list_len);
}
