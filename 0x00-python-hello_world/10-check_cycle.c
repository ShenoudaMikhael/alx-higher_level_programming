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
	head = list->next->next;
	tail = list->next;
	while (tail && head && head->next)
	{

		if (tail == head)
		{
			return (1);
		}
		head = head->next->next;
		tail = tail->next;
	}

	return (0);
}
