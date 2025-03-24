Solving this problem has been a great learning. 

What have I learnt, to solve an LLD problem, first understand the scenario, 
try to break the problem into entities, find relationship between entities and then define what each entity has to perform.

Here parking lot is an overarching structure, that has parking levels, these parking levels would then have parking spot. We would have different types of vehicles and to model that we can use either of ways, use an enum to store the types of vehicles or use factory method to generate vehicle objects at runtime. 

I used the factory method way because it's a great way to ensure future enhancements, if we want to increase the price of parking for a Truck it's easier to do it when it has it's own object. 
Using a combination of both is the key, use both a enum to store all the types of vehicle types and use that to create new vehicle class. 

This ensures that other entities can access the types of vehicles we support. 

I stored available slots and currently being used slots in deque and dict respectively, this helps us optimize the time time to park and unpark.

Despite me saying all the above there's still a lot of improvement in the code that's needed. 