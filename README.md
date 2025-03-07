# Viral Transmition Model

This is a simple model of viral transmission in a population. 
Red represents infected and green represents healthy. 
The program calculates frames based on the specified parameters and then creates an animation.

### Example Frame
![Example frame from animation](src/Transmition%20Example.png)

### Methodology
this program works by creating multiple points, programs their movement 
based of numerous available methods, and then calculates if each point is within range of an infected point.
If a point is in range of an infected point there is a chance that it will become infected.
### Potential Features

 - progress bar for the animation
 - different path finding algorithms
 - fix double counting of infections
 - produce plot of infected over time