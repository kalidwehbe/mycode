/**
 * A Heater models a simple space-heater. The operations provided by a Heater
 * object are:
 * 1. Increase and decrease the temperature setting by a set amount.
 * 2. Return the current temperature setting.
 * 3. Change the set amount by which the temperature is increased and lowered.
 * 
 * @author L.S. Marshall, SCE, Carleton University
 * (incomplete implementation for SYSC 2004 Lab 2)
 * @author Kalid Wehbe
 * @version 1.03 January 17th, 2024
 */
public class Heater
{
    /** The temperature setting that the heater should maintain. */
    private int temperature;
    
    /** The temperature setting for a newly created heater. */
    private static final int INITIAL_TEMPERATURE = 15;
    
    /** 
     * The amount by which the temperature setting is raised/lowered when
     * warmer() and cooler() are invoked.
     */
     private int increment;
    
    /** 
     * The default amount by which the temperature setting is 
     * increased when warmer() is invoked and decreased when cooler()
     * is invoked.
     */
    private static final int DEFAULT_INCREMENT = 5;
    
    /** 
     * The default max and min values set for the temperature range 
     */
    
    private static final int MAX_TEMP = 100;
    private static final int MIN_TEMP = 0;
    /** 
     * max and min temperature of the heater
     */
    
    private int max;
    
    private int min;
    
    /**
     * Constructs a new Heater with an initial temperature setting of 15
     * degrees, and which increments and decrements the temperature
     * setting in increments of 5 degrees.
     */
    public Heater()
    {
        temperature = INITIAL_TEMPERATURE;
        increment = DEFAULT_INCREMENT;
        min = MIN_TEMP;
        max = MAX_TEMP;
        
    }
 
    /**
     * construct with parameters that will be the values for max and min
     */    
    public Heater(int minTemp, int maxTemp)
    {
        temperature = INITIAL_TEMPERATURE;
        increment = DEFAULT_INCREMENT;
        min = minTemp;
        max = maxTemp;
    }

    /**
     * Returns the heaters current temperature.
     */    
    public int temperature()
    {
        return temperature;
    }
    
    /**
     * Increase the heater by a the value in increment
     */
    public void warmer()
    {
     if (max >= temperature + increment){
         temperature = temperature + increment;
        }
        
    }

    /**
     * Decrease the heater by the value in increment
     */    
    public void cooler()
    { 
        if (min <= temperature - increment){
         temperature = temperature - increment;
        }
    }
    
    
    /**
     * Sets up a new increment for changing the temperature
     */    
    public void setIncrement(int newIncrement)
    { 
        if (newIncrement > 0 ){
            increment = newIncrement;
        }
    }
}
