#include "lists.h"

/**
 * is_palindrome - check if the lincked list is palindrome
 * @listint_t: the list
 * Return: return 1 if true, 0 if false
 */

int is_palindrome(listint_t **head)
{
	int count = 0;
	listint_t *current = *head;

	while(current != NULL)
	{
		current = current->next;
		count++;
	}
	if(count % 2 == 0)
		return (1);
	else
		return (0);
}
