 # Exercise 5: Meow on Command

For this exercise, you'll add a conditional so the cat only meows when you 
tell it to, instead of on a fixed schedule.

1. Open your "Meow-Loop" project from Exercise 4. Click "File" > "Save as a 
   copy" and rename it to "Meow-Command".

2. Remove the "repeat (3)" block and everything inside it, so only "when 
   green flag clicked" remains on your canvas.

3. Click the orange "Control" category. Drag the "forever" block onto your 
   canvas and attach it under "when green flag clicked". Notice it's a 
   C-block like "repeat," but it has no number — it repeats without stopping.

4. Still in "Control," drag the "if <> then else" block inside the "forever" 
   block. Notice it has two mouths — one for when the condition is true, one 
   for when it's false.

5. Click the teal "Sensing" category. Drag the "key (space) pressed?" block 
   into the hexagonal slot in the "if" block's condition.

6. From your earlier exercises, drag a "play sound Meow until done" block 
   (Sound category) into the FIRST mouth of the if/else block (the "then" 
   branch).

7. Click the purple "Looks" category. Drag a "say" block into the SECOND 
   mouth (the "else" branch). Change its text to "Press space to hear me meow!"

8. Run your program. Nothing should happen at first. Hold down the space bar 
   — the cat should meow. Release it — the cat should go back to saying 
   "Press space to hear me meow!"

9. Save your project ("File" > "Save now"), then download "Meow-Command.sb3" 
   ("File" > "Save to your computer").