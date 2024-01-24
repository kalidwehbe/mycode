/********* main.c ********
    Student Name 	= Kalid Wehbe
    Student Number	= 101259994
*/

// Includes go here
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "a2_nodes.h"
#include "a2_functions.h"

int main()
{
    /******** DONT MODIFY THIS PART OF THE CODE ********/
    /* THIS CODE WILL LOAD THE DATABASE OF USERS FROM THE FILE
       AND GENERATE THE STARTING LINKED LIST.
    */
    FILE *csv_file = fopen("user_details.csv", "r");
    if (csv_file == NULL)
    {
        perror("Error opening the CSV file");
        return 1;
    }
    // Parse CSV data and create users
    user_t *users = read_CSV_and_create_users(csv_file, 50);

    fclose(csv_file);
    /******** DONT MODIFY THIS PART OF THE CODE ********/

    /* IMPORTANT: You must use the users linked list created in the code above.
                  Any new users should be added to that linked list.
    */

    // Your solution goes here

    // Introduction to the program
    printf("**********************************\n");
    printf("Welcome to Text-Based Facebook  \n");
    printf("**********************************\n");

    // Prints out the menu

    print_menu();

    // storing user input

    int option;

    scanf("%d", &option);

    // while loop if the option is invalid

    while (option > 6 || option < 1)
    {

        printf("Invalid choice. Please try again.\n");

        // reprints menu and asks for option again

        print_menu();

        scanf("%d", &option);
    }
    while (option <= 6 && option >= 1)
    {

        if (option == 1)
        {

            char username[30];
            char password[16];

            printf("Enter your username: ");
            scanf("%29s", username);

            printf("Enter an up to 15 character password: ");
            scanf("%15s", password);

            add_user(users, username, password);
        }

        if (option == 2)
        {

            char username[30];

            printf("Enter username to update there password: ");
            scanf("%29s", username);

            user_t *if_found = find_user(users, username);

            if (if_found != NULL)
            {

                char password[30];
                printf("Enter a new password that is up to 15 characters: ");
                scanf("%29s", password);

                printf("Old password: %s\n", if_found->password);
                strncpy(if_found->password, password, sizeof(if_found->password));
                printf("New password: %s\n", if_found->password);
            }
            else
            {
                printf("-------------------------------------\n");
                printf("           User not found.           \n");
                printf("-------------------------------------\n");
            }
        }

        if (option == 3)
        {

            char username[30];
            printf("Enter username to manage their posts: ");
            scanf("%29s", username);

            user_t *if_found_posts = find_user(users, username);

            display_user_posts(if_found_posts);

            if (if_found_posts != NULL)
            {

                printf("1. Add a new user post\n");
                printf("2. Remove a users post\n");
                printf("3. Return to main menu\n\n");

                int choice_posts = 0;
                printf("Your choice: ");
                scanf("%d", &choice_posts);

                while (choice_posts >= 1 && choice_posts <= 3)
                {
                    if (choice_posts == 1)
                    {

                        char sentence[250]; // Assuming the sentence won't be longer than 250 characters

                        printf("Enter your post content: ");

                        scanf(" %[^\n]s", sentence);

                        printf("Post added to your profile.");

                        add_post(if_found_posts, sentence);

                        printf("--------------------------------------");

                        printf("\n");

                        display_user_posts(if_found_posts);
                    }
                    else if (choice_posts == 2)
                    {
                        printf("Which post do you want to delete? ");

                        int numPost;

                        scanf("%d", &numPost);

                        bool did_it_delete = delete_post(if_found_posts, numPost);

                        if (did_it_delete == true)
                        {

                            printf("Post %d was deleted successfully!", numPost);

                            display_user_posts(if_found_posts);
                        }
                        else
                        {

                            printf("Invalid post's number\n");

                            break;
                        }
                    }
                    else if (choice_posts == 3)
                    {
                        break;
                    }

                    printf("1. Add a new user post\n");
                    printf("2. Remove a users post\n");
                    printf("3. Return to main menu\n\n");

                    printf("Your choice: ");
                    scanf("%d", &choice_posts);
                }
            }
        }

        if (option == 4)
        {

            char username[30];

            printf("Enter username to manage their friends: ");

            scanf("%29s", username);

            user_t *if_found_user = find_user(users, username);

            if (if_found_user != NULL)
            {

                printf("-------------------------------------\n");
                printf("           %s's friends        \n", username);
                printf("-------------------------------------\n");
                printf("\n");
                printf("1. Display all user's friends\n");
                printf("2. Add a new friend\n");
                printf("3. Delete a friend\n");
                printf("4. Return to main menu\n");

                printf("Your choice: ");
                int choice_friend;
                scanf("%d", &choice_friend);

                while (choice_friend >= 1 && choice_friend <= 4)
                {

                    if (choice_friend == 1)
                    {

                        display_user_friends(if_found_user);
                    }
                    if (choice_friend == 2)
                    {

                        char friend[30];
                        printf("Enter a new friends' name: ");
                        scanf("%29s", friend);
                        add_friend(if_found_user, friend);
                    }
                    if (choice_friend == 3)
                    {

                        char friend[30];
                        printf("Enter a new friends' name: ");
                        scanf("%29s", friend);

                        bool did_it_delete = delete_friend(if_found_user, friend);
                        if (did_it_delete == true)
                        {

                            display_user_friends(if_found_user);
                        }
                    }
                    if (choice_friend == 4)
                    {

                        break;
                    }

                    printf("\n");
                    printf("------------------------------\n");

                    printf("1. Display all user's friends\n");
                    printf("2. Add a new friend\n");
                    printf("3. Delete a friend\n");
                    printf("4. Return to main menu\n");

                    printf("Your choice: ");
                    scanf("%d", &choice_friend);
                }
            }
            else
            {

                printf("-------------------------------------\n");
                printf("           User not found.           \n");
                printf("-------------------------------------\n");
            }
        }
        if (option == 5)
        {

            display_all_posts(users);
        }
        if (option == 6)
        {

            printf("************************\n");
            printf("Thank you for using \nText-Based Facebook Bye!");
            printf("************************\n");
            teardown(users);
            return 0;
        }
        print_menu();
        scanf("%d", &option);
        while (option > 6 || option < 1)
        {

            printf("Invalid choice. Please try again.\n");

            // reprints menu and asks for option again

            print_menu();

            scanf("%d", &option);
        }
    }
}