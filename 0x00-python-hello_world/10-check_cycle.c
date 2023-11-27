#include "lists.h"

/**
  * check_cycle - check if a singly linked list has a cycle in it
  * @list: list to be checked
  * Return: 0 if there is no cycle ||  1 if there is
  */

int check_cycle(listint_t *list)
{
	listint_t *step_1, *step_2;

	step_1 = step_2 = list;
	while (step_2 && step_2->next)
	{
		step_2 = step_2->next->next;
		step_1 = step_1->next;
		if (step_2 == step_1)
			return (1);
	}
	return (0);
}
