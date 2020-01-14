//21.c Merge two sorted lists.

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode *merged = l1;
	struct ListNode *prev = NULL;
	struct ListNode *tmp = NULL;

	if(l1 == NULL)
		return l2;
	else if(l2 == NULL)
		return l1;

	if((l1->val) > (l2->val)) 
		merged = l2;
	else
		merged = l1;

	while((l1 != NULL) && (l2 != NULL))
	{
		if((l1->val) > (l2->val)) {
			tmp = l2;
			l2 = l2->next;
			tmp->next = l1;
			if(prev == NULL) {
				prev = tmp;
			} else {
				prev->next = tmp;
				prev = tmp;
			}
		} else {
			prev = l1;
			l1 = l1->next;
		}
	}

	if(l1 == NULL && l2 != NULL) {
		prev->next = l2;
	}
	return merged;
}

void print(struct ListNode *head)
{
	while(head != NULL) {
		printf("%d ", head->val);
		head = head->next;
	}
}

int main(int argc, char **argv)
{
	struct ListNode *l1;
	struct ListNode *l2;

	l1 = malloc(sizeof(struct ListNode));
	l1->val = 1;

	l1->next = malloc(sizeof(struct ListNode));
	l1->next->val = 2;

	l1->next->next = malloc(sizeof(struct ListNode));
	l1->next->next->val = 4;

	l1->next->next->next = NULL;

	l2 = malloc(sizeof(struct ListNode));
	l2->val = 1;

	l2->next = malloc(sizeof(struct ListNode));
	l2->next->val = 3;

	l2->next->next = malloc(sizeof(struct ListNode));
	l2->next->next->val = 4;

	l2->next->next->next = NULL;

	print(mergeTwoLists(l1,l2));

	return 0;
}
