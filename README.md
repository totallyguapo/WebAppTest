James Ford 
CART 498 
Prof. Vigliensoni 

LINKS
https://jungiandreaims.onrender.com
https://github.com/totallyguapo/WebAppTest

The process of creating this app was long and tedious—I made many mistakes. My first mistake was thinking ChatGPT would simply code the project for me. The main problem was that since the API has been updated after its knowledge cut off point—it was generating useless API code. I ended up going through the endpoint manuals myself. On top of this, I’m highly unexperienced in git, python, and html—so everything went very slowly. Learning about git codespace was a revelation (it makes the possibility of making my own websites seem much less daunting, since its highly integrated and does not require to create my own server to monitor the results). Once I had the app generating images and text, I needed to fine tune everything. At first the dream interpretation was outputting the beginning of a description of what Jungian analysis is, although the images were very effective—if not a bit too on-the-nose.  
Figure 1. first iteration
 
Figure 2. midpoint
 
Figure 3. updated iteration
I switched from dalle 3 to dalle 2 because I couldn’t figure out how to adjust the temperature for image generation and I wanted a less polished looking image. I used internet blog posts to define how the bot should interpret dreams in a Jungian style. I initially experimented with just Twin Peaks quotes, but it just started outputting more quotes, mostly unrelated to the user prompt. Since the images generated were still too closely related to the user prompt, I instead chose to use the ChatGPT interpretation of the dream as the prompt for the image. Finally, I specified a word cutoff to limit the number of tokens while also ensuring a complete response. I should add protections so that nefarious users don’t constantly refresh and drain my API tokens—but I trust the people I’ve given the link to…for now…
 
Figure 4. final images, properly surreal
I tried to personify the website as a virtual entity: thus, its displayed text is written in the first person. It addresses the user as a fellow person, but embodies the liminal ‘backroom’ aesthetic of broken webpages which send data into the virtual abyss. Liminal spaces were touched on by Jung during his reflections on the disconnect experienced between dreams and reality. It is hoped that the user will be encouraged by the aesthetic to ‘enter the liminal space, thereby forgetting their everyday identity, and gaining new insights on their archetypal one. 

USER GUIDE
Describe your dream in as much detail as possible and input the description as text into the page textbox. Next, click ‘Back from whence it came…”
Textual and visual interpretations of the dream should follow.
