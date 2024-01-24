/********* main.c ********

    Student Name 	= Kalid Wehbe
    Student Number	= 101259994
*/

#include <stdio.h>
#include "a1_data_structures.h"
#include "a1_functions.h"
int main()
{

    //Printing out the introduction and asking the user to input the correct details

    printf("Welcome to ABC Project Tracker\n");
    printf("Enter total project's budget: ");

    milestone_t project_info;

    project_info.cost = get_input_f();

    printf("Enter total project's duration in weeks: ");
    project_info.time = get_input_f();

    //finding out the amount of employees needed 

    number_of_employees(&project_info);

    printf("\n");

    //making a array for the milestones and innitializing them
    milestone_t milestones[6];

    milestones[0].cost = project_info.cost;
    milestones[0].time = project_info.time;
    milestones[0].completed = 0;

    char stage_one[] = "Technical requirements";
    milestones[1] = init_milestone(stage_one, project_info.cost);
    char stage_two[] = "System Desigm";
    milestones[2] = init_milestone(stage_two, project_info.cost);
    char stage_three[] = "Software Development";
    milestones[3] = init_milestone(stage_three, project_info.cost);
    char stage_four[] = "Testing";
    milestones[4] = init_milestone(stage_four, project_info.cost);
    char stage_five[] = "Product release";
    milestones[5] = init_milestone(stage_five, project_info.cost);

    //printing the menu for the user and allowing him to choose an otion

    printf("--------------------------\n");
    printf("\n");
    print_menu();
    printf("\n");
    printf("Your choice is: ");
    int choice;
    int exit_flag = 0;
    choice = get_input_usi();
    printf("\n");

    //while the exit_flag isn't raised then continue this loop
    while (!exit_flag)
    {


        while (choice < 0 || choice > 5)
        {
            printf("----------------------------------------\n");
            printf("The value you entered is wrong\n");
            printf("Enter a value between 0 and 5: ");
            choice = get_input_usi();
            printf('\n');
        }
        if (choice > 0 && choice <= 5)
        {
            printf("--------------Milestone Stats------------\n");
            printf("Below is \"%s\" current stats\n", milestones[choice].name);
            printf("-----------------------------------------\n");
            print_stats(milestones[choice]);

            if (milestones[choice].completed == 1)
            {

                printf("%s is complete \n", milestones[choice].name);
                printf("cannot be updated\n");
            }
            else
            {
                printf("------------Update Stats--------------\n");
                update_stats(milestones, choice);
                printf("Stats updated!\n");
                printf("--------------Milestone Stats------------\n");
                printf("Below is '%s' current stats\n", milestones[choice].name);
                printf("-----------------------------------------\n");
                print_stats(milestones[choice]);
            }
            printf("--------------------------\n");
            print_menu();
            printf("Your choice is: ");
            choice = get_input_usi();
        }
        if (choice == 0)
        {

            check_project_completion(milestones, sizeof(milestones) / sizeof(milestones[0]));

            if (milestones[0].completed == 0)
            {

                printf("-----------------------------------------------\n");
                printf("------------Project's Preformance---------------\n");
                printf("-----------------------------------------------\n");
                printf("---------------Milestones Stats------------------\n");
                printf("Below is \"Planned Details\" current stats\n");
                printf("-----------------------------------------------\n");
                print_stats(milestones[choice]);
                printf("Do you want to finish the remaining milestones? (Y/N)");
                while (1)
                {
                    char letter;
                    scanf(" %c", &letter); // Read a single character

                    if (letter == 'Y' || letter == 'y')
                    {
                        // Perform action for 'Y'
                        printf("You chose to proceed. Performing action for 'Y'.\n");

                        printf("--------------------------\n");
                        print_menu();

                        printf("Your choice is: ");
                        choice = get_input_usi();

                        break; // Exit the inner loop
                    }
                    else if (letter == 'N' || letter == 'n')
                    {
                        int total_cost = milestones[1].cost + milestones[2].cost + milestones[3].cost + milestones[4].cost + milestones[5].cost;
                        if (milestones[0].cost > total_cost)
                        {

                            printf("The project's cost is below budget!\n");
                            printf("Planned budget: %.2f\n", milestones[0].cost);
                            printf("Actual Cost: %d\n", total_cost);
                        }
                        else
                        {

                            printf("The project's cost is over budget!\n");
                            printf("Planned budget: %.2f\n", milestones[0].cost);
                            printf("Actual Cost: %d\n", total_cost);
                        }
                        printf("The program will quit now! Goodbye!\n");
                        printf("Process exited with status 0\n");
                        exit_flag = 1;
                        break;
                    }
                    else
                    {
                        printf("Invalid input. Please enter 'Y' or 'N': ");
                    }
                }
            }else{
                
                printf("--------------Final Project's Performance-------------------\n");
                int total_cost = milestones[1].cost + milestones[2].cost + milestones[3].cost + milestones[4].cost;
                if (milestones[0].cost > total_cost)
                {

                    printf("The project's cost is below budget!\n");
                    printf("Planned budget: %.2f\n", milestones[0].cost);
                    printf("Actual Cost: %d\n", total_cost);
                }
                else
                {

                    printf("The project's cost is over budget!\n");
                    printf("Planned budget: %.2f\n", milestones[0].cost);
                    printf("Actual Cost: %d\n", total_cost);
                }

                printf("The program will quit now! Goodbye!\n");
                printf("Process exited with status 0\n");

                break;



            }
        }
    }
}
