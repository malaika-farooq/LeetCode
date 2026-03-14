/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head) {
    if (head == NULL || head->next == NULL){
        return head;
    }

    struct ListNode* sorted = head;
    struct ListNode* curr = head->next;
    sorted->next = NULL;

    while (curr != NULL){
        struct ListNode* nextNode = curr->next;
         if(curr->val < sorted->val){
            curr->next = sorted;
            sorted = curr;
         }
         else{
            struct ListNode *temp = sorted;
            while (temp->next !=NULL && temp->next->val < curr->val){
                temp = temp->next;
            }
            curr->next = temp->next;
            temp->next = curr;
            
         }
         curr = nextNode;
    }
    return sorted;
}