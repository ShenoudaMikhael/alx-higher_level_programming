#include "lists.h"
#include <stdio.h>

int check(listint_t *head, listint_t *tail)
{
	int q = 1;

	if (tail->next == NULL)
	{
	}
	else
	{

		q = check(head, tail->next);
		if (q == 0)
		{
			return (0);
		}
		*head = *head->next;
		printf("head:%d  end tail:%d\n", head->n, tail->n);
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

	while (tmp->next)
	{
		list_len++;
		tmp = tmp->next;
	}
	tmp = *head;
	qq = *head;
	printf("===================\n");
	list_len = check(qq, tmp);
	printf("result = %d\n", list_len);

	return (list_len);
}
