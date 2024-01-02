#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert node in sorted list
 * @head: list head
 * @number: number to insert
 * Return: list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	temp = *head;
	if (temp == NULL || temp->n > number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next)
	{
		if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			if (temp->next == NULL)
				return (NULL);
			return (new);
		}
		temp = temp->next;
	}
	return (*head);
}
