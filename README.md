## Inspiration

-Navigating through the UMass Dining app to find Indian cuisine was frustrating and time-consuming. We were inspired to create a more efficient experience for users who want to easily find food options based on their preferences. We ask the user for their location to suggest a dining common which is nearby by walk.


##What it does
-The UMass Eats chatbot recommends meals to users based on their personal preferences, making it easier to find the food they love.



## What we used 
**Scrapy:**
-We scraped the UMass Dining website using scrapy to gather food attributes and categorize meal options.

**OpenAI:**
- We used the Open AI Assistants API to create the AI Agent for our UMass Eats Chatbot
- We used a VectorDB within OpenAI to store the data required for the chatbot , this included the food menu of all the four dining commons which was scraped. It also included the names of UMass buildings and their distances from the dining commons. 

**Streamlit:**

-Used to create the UI for the chatbot.
- Allowed us to create a simple chat interface for the user

##Challenges we faced

- Facing a steep learning curve when learning about OpenAI agents and using their API.<img width="1121" alt="original" src="https://github.com/user-attachments/assets/e5a9b7b9-ec18-4f15-a058-39e7d154ee22">

- Preventing Hallucinations in the chatbot
- Ensuring that the RAG was implemented properly.

## Accomplishments we are proud of

-We learnt a lot of new technology

-Using a Web scraper 

-Using GenAI agents 

- Using a vectorDB
  
- We are proud of being able to create an MVP in a short time span.

##We learnt how to:
Collaborate and code in a short span of time. Use various new technologies to make an app of our choice.

## What's next for UMass Eats
**Full Health App**

Expanded Features: The next step is to turn UMass Eats into a full-fledged health app.
The app will not only recommend meals but also provide tools for nutrition tracking and fitness.
Users will be able to track their calorie intake and exercise routines in one unified platform.

 **Integrating Multi-Agent System**

Adding a multi-agent system that can handle:

-Food Recommendations based on dietary preferences, restrictions, and goals. (**UMass Eats**)

-Fitness Tracking Agent
- We would add other Agents as required
-LangGraph could be used to create the MultiAgent Structure to allow for better


