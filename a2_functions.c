/********* definitions.c ********
    Student Name 	= Kalid Wehbe
    Student Number	= 101259994
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "a2_nodes.h"
#include "a2_functions.h"
#include <stdbool.h>

// Your solution goes here

/*
   Function that creates a new user and adds it to a sorted (ascending order) linked list at
   the proper sorted location. Return the head of the list.
*/
user_t *add_user(user_t *users, const char *username, const char *password)
{

   // Create a new user

   user_t *new_user = (user_t *)malloc(sizeof(user_t));
   if (new_user == NULL)
   {
      printf("malloc failed\n");
      exit(EXIT_FAILURE);
   }

   // Initialize the new user
   strncpy(new_user->username, username, sizeof(new_user->username));
   strncpy(new_user->password, password, sizeof(new_user->password));
   new_user->friends = NULL; // Initialize friends list to empty
   new_user->posts = NULL;   // Initialize posts list to empty
   new_user->next = NULL;    // Initialize next pointer to NULL

   // If the list is empty or the new user should be inserted at the beginning
   if (users == NULL || strcmp(username, users->username) < 0)
   {
      new_user->next = users;
      return new_user;
   }

   // Find the proper location to insert the new user in ascending order
   user_t *current = users;
   while (current->next != NULL && strcmp(username, current->next->username) > 0)
   {
      current = current->next;
   }

   // Insert the new user at the proper location
   new_user->next = current->next;
   current->next = new_user;

   return users;
}
/*
   Function that searches if the user is available in the database
   Return a pointer to the user if found and NULL if not found.
*/
user_t *find_user(user_t *users, const char *username)
{

   user_t *current = users;
   while (current != NULL)
   {
      if (strcmp(current->username, username) == 0)
      {
         // User found, return a pointer to the user
         return current;
      }
      current = current->next;
   }

   // User not found, return NULL
   return NULL;
}
/*
   Function that creates a new friend's node.
   Return the newly created node.
*/
friend_t *create_friend(const char *username)
{

   friend_t *newFriend = (friend_t *)malloc(sizeof(friend_t));
   if (newFriend == NULL)
   {
      printf("malloc failed\n");
      exit(EXIT_FAILURE);
   }

   // Initialize the new friend
   strncpy(newFriend->username, username, sizeof(newFriend->username));
   newFriend->next = NULL;

   return newFriend;
}

/*
   Function that links a friend to a user. The friend's name should be added into
   a sorted (ascending order) linked list.
*/
void add_friend(user_t *user, const char *friend)
{

   friend_t *newFriend = create_friend(friend);

   // If the list is empty or the new friend should be inserted at the beginning
   if (user->friends == NULL || strcmp(friend, user->friends->username) < 0)
   {
      newFriend->next = user->friends;
      user->friends = newFriend;
   }
   else
   {
      friend_t *currentFriend = user->friends;
      friend_t *prevFriend = NULL;

      // Find the proper location to insert the new friend in ascending order
      while (currentFriend != NULL && strcmp(friend, currentFriend->username) > 0)
      {
         prevFriend = currentFriend;
         currentFriend = currentFriend->next;
      }

      // Insert the new friend at the proper location
      newFriend->next = currentFriend;
      prevFriend->next = newFriend;
   }

   printf("Friend %s added successfully.\n", friend);
}

/*
   Function that removes a friend from a user's friend list.
   Return true of the friend was deleted and false otherwise.
*/
_Bool delete_friend(user_t *user, char *friend_name)
{

   friend_t *currentFriend = user->friends;
   friend_t *prevFriend = NULL;

   // Find the friend with the specified name
   while (currentFriend != NULL && strcmp(currentFriend->username, friend_name) != 0)
   {
      prevFriend = currentFriend;
      currentFriend = currentFriend->next;
   }

   // If the friend is found, delete it
   if (currentFriend != NULL)
   {
      // Update pointers to bypass the friend to be deleted
      if (prevFriend != NULL)
      {
         prevFriend->next = currentFriend->next;
      }
      else
      {
         // If the friend is the first in the list, update the head of the list
         user->friends = currentFriend->next;
      }

      free(currentFriend);
      printf("Friend %s deleted successfully.\n", friend_name);
      return true;
   }

   // Friend not found
   printf("Error: Friend %s not found.\n", friend_name);
   return false;
}

/*
   Function that creates a new user's post.
   Return the newly created post.
*/
post_t *create_post(const char *text)
{
   post_t *new_post = (post_t *)malloc(sizeof(post_t));
   if (new_post == NULL)
   {
      printf("malloc failed\n");
      exit(EXIT_FAILURE);
   }

   // Initialize the new post
   strncpy(new_post->content, text, sizeof(new_post->content));
   new_post->next = NULL;

   return new_post;
}

/*
   Function that adds a post to a user's timeline. New posts should be added following
   the stack convention (LIFO) (i.e., to the beginning of the Posts linked list).
*/
void add_post(user_t *user, const char *text)
{

   post_t *new_post = create_post(text);

   // Add the new post to the beginning of the user's posts list (LIFO)
   new_post->next = user->posts;
   user->posts = new_post;
}

/*
   Function that removes a post from a user's list of posts.
   Return true if the post was deleted and false otherwise.
*/
_Bool delete_post(user_t *user, int number)
{

   if (user != NULL)
   {
      post_t *currentPost = user->posts;
      post_t *prevPost = NULL;
      int currentPosition = 1;

      // Find the post at the specified position
      while (currentPost != NULL && currentPosition < number)
      {
         prevPost = currentPost;
         currentPost = currentPost->next;
         currentPosition++;
      }

      // If the post is found, delete it
      if (currentPost != NULL)
      {
         // Update pointers to bypass the post to be deleted
         if (prevPost != NULL)
         {
            prevPost->next = currentPost->next;
         }
         else
         {
            // If the post is the first in the list, update the head of the list
            user->posts = currentPost->next;
         }

         free(currentPost);
         return true;
      }
   }

   // Post not found or user is NULL
   return false;
}

/*
   Function that  displays a specific user's posts
*/
void display_user_posts(user_t *user)
{
   if (user != NULL)
   {
      printf("-------------------------------------------\n");
      printf("%s's posts:\n", user->username);

      // Iterate through the user's posts and print each one
      post_t *currentPost = user->posts;
      int postNum = 1;
      while (currentPost != NULL)
      {
         printf("%d- %s\n", postNum, currentPost->content);
         currentPost = currentPost->next;
         postNum++;
      }

      // Check if there are no posts
      if (user->posts == NULL)
      {

         printf("No posts available for user %s\n", user->username);
      }
      printf("-------------------------------------------\n");
   }
   else
   {
      printf("-------------------------------------\n");
      printf("           User not found.           \n");
      printf("-------------------------------------\n");
   }
}

/*
   Function that displays a specific user's friends
*/
void display_user_friends(user_t *user)
{

   friend_t *currentFriend = user->friends;

   if (currentFriend == NULL)
   {
      printf("No friends available for %s.\n", user->username);
   }
   else
   {
      int friendNumber = 1;

      printf("-----------------------------------\n");

      printf("List of %s's friends\n", user->username);

      // Display the list of user's friends
      while (currentFriend != NULL)
      {
         printf("%d- %s\n", friendNumber++, currentFriend->username);
         currentFriend = currentFriend->next;
      }
   }
}
/*
   Function that displays all the posts of 2 users at a time from the database.
   After displaying 2 users' posts, it prompts if you want to display
   posts of the next 2 users.
   If there are no more post or the user types “n” or “N”, the function returns.
*/
void display_all_posts(user_t *users)
{

   int userCount = 0;
   user_t *current = users;

   while (current != NULL)
   {
      // Display the posts of the current user
      display_user_posts(current);
      userCount++;

      // Move to the next user
      current = current->next;

      // If two users' posts have been displayed, prompt the user
      if (userCount % 2 == 0)
      {
         char choice;

         printf("\nDo you want to display posts of the next 2 users? (Y/N): ");
         scanf(" %c", &choice);

         if (choice == 'N' || choice == 'n')
         {
            printf("All posts have been displayed.\n");
            return;
         }
      }
   }

   // If there are fewer than 2 users or the user chooses to display more posts after all have been displayed
   printf("All posts have been displayed.\n");
}

/*
   Fucntion that free all users from the database before quitting the application.
*/
void teardown(user_t *users)
{

   user_t *current = users;
   user_t *next;

   while (current != NULL)
   {
      // Free friends linked list
      friend_t *currentFriend = current->friends;
      friend_t *nextFriend;

      while (currentFriend != NULL)
      {
         nextFriend = currentFriend->next;
         free(currentFriend);
         currentFriend = nextFriend;
      }

      // Free posts linked list
      post_t *currentPost = current->posts;
      post_t *nextPost;

      while (currentPost != NULL)
      {
         nextPost = currentPost->next;
         free(currentPost);
         currentPost = nextPost;
      }

      // Move to the next user and free the current user
      next = current->next;
      free(current);

      current = next;
   }
}

/*
   Function that prints the main menu with a list of options for the user to choose from
*/
void print_menu()
{
   printf("**********************************\n");
   printf("           MAIN MENU:             \n");
   printf("**********************************\n");
   printf("1. Register a new User\n");
   printf("2. Manage a user's profile (change passwird)\n");
   printf("3. Manage a user's posts (display/add/remove)\n");
   printf("4. Manage a user's friends (display/add/remove)\n");
   printf("5. Display All Posts\n");
   printf("6. Exit\n");

   printf("Enter your choice: ");
}

/*
   ******** DONT MODIFY THIS FUNCTION ********
   Function that reads users from the text file.
   IMPORTANT: This function shouldn't be modified and used as is
   ******** DONT MODIFY THIS FUNCTION ********
*/
user_t *read_CSV_and_create_users(FILE *file, int num_users)
{
   user_t *users = NULL;
   char buffer[500];
   fgets(buffer, sizeof(buffer), file); // Read and discard the header line
   int count = 0;
   for (int i = 0; i < num_users; i++)
   {
      fgets(buffer, sizeof(buffer), file);
      buffer[strcspn(buffer, "\r\n")] = 0; // Remove newline characters

      char *token = strtok(buffer, ",");
      char *token2 = strtok(NULL, ",");
      users = add_user(users, token, token2);
      char *username = token;

      token = strtok(NULL, ",");

      user_t *current_user = users;
      for (; current_user != NULL && strcmp(current_user->username, username) != 0; current_user = current_user->next)
         ;

      while (token != NULL && strcmp(token, ",") != 0 && count < 3)
      {
         if (strcmp(token, " ") != 0)
         {
            add_friend(current_user, token);
         }
         token = strtok(NULL, ",");
         count++;
      }
      count = 0;

      // token = strtok(NULL, ",");
      while (token != NULL && strcmp(token, ",") != 0)
      {
         add_post(current_user, token);
         token = strtok(NULL, ",");
      }
   }
   return users;
}
