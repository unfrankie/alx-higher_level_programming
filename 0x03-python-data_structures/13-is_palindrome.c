#include "lists.h"

/**
  * is_palindrome - check if a singly linked list is a palindrome
  * @head: **head of list
  * Return: 0 itsnt a palindrome || (1 if its a palindrome | empty list
  */

int is_palindrome(listint_t **head)
{
	int arr[2048];
	int value;
	listint_t *mem;
	int i; 

	if (!head || !*head)
		return (1);
	mem = *head;
	while (mem)
	{
		value++;
		arr[value - 1] = mem->n;
		mem = mem->next;
	}
	for (i = 0; i < value / 2; i++)
	{
		if (arr[i] != arr[value - 1 - i])
			return (0);
	}
	return (1);
}
