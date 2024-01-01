#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check for list sycle
 * @list: list to check
 * Return: 1 on cycle 0 on no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = NULL, *tail = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	head = list;
	tail = head->next;

	do
	{

		for (; head != tail && tail != NULL;)
		{

			if (head == tail || head == tail->next)
			{
				return (1);
			}
			tail = tail->next;
		}
		if (head->next == NULL || head == NULL)
			return (0);
		head = head->next;


	} while (head != list);

	return (0);
}
