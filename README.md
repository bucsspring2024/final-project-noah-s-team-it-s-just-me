[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588413&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Crusty Crusade: The Quest for Toastination
## CS110 Final Project - Spring, 2024 

## Team Members

Noah Gallagher


***

## Project Description

A piece of bread will attempt to navigate through obstacles to get to the magical Volcano in under a minute in order to become toast!

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu
2. Moveable Character
3. Obstacle/Enemy Collisions
4. Scrolling Background
5. Game Over Screen

### Classes

- Bread: Bread is the movable character in the game. He is able to move left, right, and he can jump... somehow.
- Obstacle: A multitude of stationary objects will be in the game.
- Movable Obstacle: Some moving obstacles will also be featured in the game.

## ATP
- Test Case 1: Player Movement
    - Test Description: Verify that the bread moves left, right, and can jump as expected.
    - Test Steps:
    1. Start the game
    2. Press the left arrow key/a
    3. Verify that the bread moves left
    4. Press the right arrow key/d
    5. Verify that the bread moves right
    6. Press the up arrow key/spacebar
    7. Verify that the bread moves up/jumps
    - Expected Outcome: The player’s bread should move left, right, and jumps in response to the keys

- Test Case 2: Collision Detection
    - Test Description: Ensure that collisions between the bread and obstacles are detected correctly.
    - Test Steps:
    1. Start the game
    2. Run into a wall
    3. Verify that the bread is stopped by the obstacle
    4. Run around and don’t touch anything
    5. Verify that no collision is detected
    - Expected Outcome: Moving around should correctly collide or not collide with something.

- Test Case 3: Biome Transitions
    - Test Description: Ensure that the transition between biomes occurs
    - Test Steps:
    1. Start the game
    2. Reach the end of one biome
    3. Verify that the transition to the next biome occurs smoothly
    - Expected Outcome:  When the bread reaches the end of each biome, the transition occurs.

- Test Case 4: Toast Transformation
    - Test Description: Test the condition for the bread to become toast at the end of the game.
    - Test Steps:
    1. Start the game
    2. Navigate through all of the biomes to the end of the game
    3. Reach the volcano at the end of the final biome to become toast
    - Expected Outcome: When the bread reaches the volcano at the end of the final biome, it should transform the bread into toast. This means that you've completed the game.

- Test Case 5: User Interface
    - Test Description: Ensure that the user interface elements function normally. Test the navigation through the game's menu.
    - Test Steps:
    1. Start the game
    2. Navigate through the main menu options (Start, quit, and options)
    3. Verify that each option is selectable and leads to the expected actions
    - Expected Outcome: The main menu should allow the player to navigate through options and select them.
