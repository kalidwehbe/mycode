/********* definitions.c ********

	Student Name 	= Kalid Wehbe
	Student Number	= 101259994
*/
#include <stdio.h>
#include "a1_data_structures.h"
#include <math.h>
#include "a1_functions.h"


milestone_t init_milestone(char stage_name[], float assigned_budget)
{
	milestone_t newMilestone;

	strcpy(newMilestone.name, stage_name);

	// Initialize other fields
	newMilestone.cost = assigned_budget / 5.0;
	newMilestone.time = 0.0;
	newMilestone.num_employees = 0;
	newMilestone.completed = 0;

	return newMilestone;
}

unsigned short int get_input_usi(void)
{

	int number;

	scanf("%d", &number);

	return number;
}

float get_input_f(void)
{

	float f_num = 0.0;

	do
	{
		scanf("%f", &f_num);

		if (f_num < 0)
		{
			printf("The value you entered is wrong.\n");
			printf("Enter a positive value: ");
		}
	} while (f_num < 0);

	return f_num;
}

void number_of_employees(milestone_t *project_details)
{

	float salary = project_details->time * hours * pay;

	float num_employees = project_details->cost / salary;

	int num_employees_int = round(num_employees);

	printf("The planned number of employees needed is %d\n", num_employees_int);
}

void print_menu(void)
{

	printf("Which milestone you want to update? (0 to exit): \n");
	printf("1.	Technical requirements\n");
	printf("2.	System Design\n");
	printf("3.	Software Development\n");
	printf("4.	Testing\n");
	printf("5.	Product release\n");
}

void print_stats(milestone_t details)
{
	printf("Actual time %.2f\n", details.time);
	printf("Actual number of employees %d\n", details.num_employees);
	printf("Actual cost %.2f $\n", details.cost);
	if (details.completed == 0)
	{

		printf("Completed: No\n");
	}
	else
	{

		printf("Completed: Yes\n");
	}
}

void update_stats(milestone_t milestone_array[], int milestone_num)
{

	printf("Enter the milestone's actual time: ");
	milestone_array[milestone_num].time = get_input_f();
	printf("Enter the milestone's actual number of employees: ");
	milestone_array[milestone_num].num_employees = get_input_usi();
	char choice;
	printf("Is this milestone's complete?: (Y/N) ");
	scanf(" %c", &choice);
	if (choice == 'Y')
	{
		milestone_array[milestone_num].completed = 1;
	}
	else
	{
		milestone_array[milestone_num].completed = 0;
	}
	milestone_array[milestone_num].cost = milestone_array[milestone_num].time * milestone_array[milestone_num].num_employees * hours * pay;
}

void check_project_completion(milestone_t milestone_array[], int num_milestones)
{

	milestone_array[0].completed = 1;
	int i;
	for (i = 1; i < num_milestones; i++)
	{
		if (milestone_array[i].completed == 0)
		{

			milestone_array[0].completed = 0;
			break;
		}
	}
}
