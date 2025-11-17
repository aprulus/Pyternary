# Pyternary
A Python Code that can import code into the Geometry Dash Level Deternary.

Hello! I am Aprulus, and I really enjoyed beating Deternary. It found it really fun, so I decided to make this in order
to make it more open for others to want to try it. I added a few nice things to make coding with this easier.

**GRAMMAR:**
  To code with Pyternary, I use a Python Script to read a .txt file and try to practically macro that into GD. Because I am still not a very good programmer, I have some rules that I highly recommend you follow.
    **1.** Type in the order that you see the trites in. In Deternary, there is the Command Selector and the Data Selectors (with both an Upper and Lower one). It goes (Command, Upper, Lower). You are not able to mix those around.
    **2** In order to swap between those specific parts, you must seperate them with a comma.
    **3** However, I do highly recommend you use (Command, Data Selectors) instead, as it is generally a lot more useful when writing your script that way.
    **4** Just as with Deternary, the first line is Line 0, so keep that in mind when deciding what line you want to select.
    **5** To select a Command, I personally recommend using the Command Name (which you can see within the Deternary Documentation, or just within the Python Code)
**Comments**
  To Comment in Pyternary, I only made the code with Inline Comments in mind. To type a comment, at the end of a line, type a colon, and then you can type your comment. (ie: comp,37**:This is a comment**). The Code should automatically remove that when it adjusts it into Deternary, so you should be fine like that.
**Variable Functions**
  To make the Deternary Process easier, I decided to add Variable Functions to it. This allows you to set a specific line to a variable that you are able to call at   any time, even before the function variable is introduced. To Introduce a variable, add a #[varName] to the start of the line (ie: #start,set,30) . To select a variable, at the Data Selector area, type in #[varName], and the code will automatically change it to the variable (ie: jump,#start).
**Unknown Variables**
  If you want to create a variable, but don't have a place in mind for it, use a %[number] format to set it to a free area. What this does is place it [number] away from your final line. Using %0 will put it at the first next free spot, %1 will be the second, etc. This really comes in handy when you are storing things, so I highly recommend you use this for that (ie: set,%0)
**Using**
  To use Pyternary, change the File to the File you need to read, and then hit play. Then, quickly switch over to your GD tab, and focus in on the game. It will then Macro the code into the game. DO NOT HAVE ANY OTHER THING BE FOCUSED ON DURING THIS PROCESS, otherwise it will start spamming all the inputs into that place. I added Time.Sleep() to it to try to minimize that occuring, so I hope that works for now.
**Changing Things**
  I attempted to add plenty of variables to Pyternary, so you could customize it as much as you can. The Main things you can change are the delimiters, Click Speed, File It Checks, and what Keys it Presses to do the things it needs to do. (I set the keys to the default ones) 
**Updating**
  If you want to change anything to this, feel free, if you want me to add anything, feel free to ask me. I just wanted to make this a nice and simple working thing.
**Bugs**
  If you encounter any bugs with this, please tell me, I absolutely did not spend a good enough amount of time Bugfixing this, so I am sure there are plenty of errors within it. I do recommend trying to change things a bit yourself though (if it is not typing in the right amount of things, try making it type stuff a bit slower, etc.)

Anyways, I hope you all are able to use this and enjoy Deternary, I had such a great time playing it, and honestly this might make me want to make projects just for fun in it.

-AP
