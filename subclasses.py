# Importing libraries and classes needed for the experiment
from general_classes import Experiment
import random
import time
import os
from typing import List

# Creating the first experiment
class ReactionTime(Experiment):
  """ 
    A subclass derived from the “Experiment” class, tailored to measure a participant's reaction time. Inherits all methods and attributes of the parent class. (You have to document the attributes)"""

  def __init__(self, *args) -> None:
    """
      Initialize the “ReactionTime” subclass. 
      Utilizes the super() function to inherit the properties and behaviors from the parent          "Experiment" class"""

    super().__init__(*args)

  def correct_data(self) -> None:
    """
      Process and correct the raw data obtained from the “conduct_experiment” method, i.e. the reaction time experiment.
      Computes the mean and variance of the gathered data, and updates the associated subject's “results” (dict) with these statistical values.
    """
    # Overwrite the super class method for additional funcionality
    # Now we calculate the mediun and variance of the reaction time data
    mu = sum(self.data) / len(self.data)
    var = sum([(x - mu)**2 for x in self.data]) / len(self.data)
    self.subject.results.update({
        'MeanReaction': round(mu, 2),
        'VarianceReaction': round(var, 2)
    })

  def conduct_experiment(self, n_trials: int, pause_range: int = 10) -> None:
    """
    Administer the reaction time experiment. 
      The experiment flow is as follows: 
      1. Introduce a random pause. 
      2. Display a prompt to the participant with the instructions. 
      3. Measure the time taken by the participant to respond (by pressing ENTER). 
    Parameters: 
      n_trials (int): Specifies the number of repetitions of the experiment.
      pause_range (int, optional): Sets the average duration (in seconds) for the random pause       before each prompt. Defaults to 10 seconds.
    """

    for _ in range(n_trials):
      # Generate a random number between 0 and pause_range
      time.sleep(random.random() * pause_range)
      time_0 = time.time()
      input("Press ENTER as quickly as possible!")
      time_1 = time.time()

      self.data.append(time_1 - time_0)

# Creating the second experiment
class Questionnaire(Experiment):
  """
    A subclass derived from the "Experiment" abstract class. Inherits all methods and attributes of the parent class. (You have to document the attributes and any information you consider) """

  def __init__(self, path_questionnaires: str, *args) -> None:
    """
      Initialize the Questionnaire subclass.
After the inheritance, execute the “load_questions()” method, using the correct path, to load the questions into the self.questions attribute (attribute defined within the “load_questions()” method).
Args (apart from the inherited from Experiment):
path_questionnaire (str): Path to file containing questions."""
    super().__init__(*args)
    # Calling the load_questions method
    self.questions = self.load_questions(path_questionnaires)

  def load_questions(self, path_questionnaires: str) -> List:
    """ 
      Load questions from a specified file path and store them in the self.questions attribute.
Each line in the file is treated as a separate question. The method reads the file, splits it by lines, and assigns the resulting list of questions to “self.questions” attribute.
Args:
path (str): Path to the file containing the questions."""

    if os.path.exists(path_questionnaires):
      with open(path_questionnaires, "r") as file:
        list = file.readlines()
        return list
    else:
      print("This file doesn't exist!")
      return []

  def correct_data(self) -> None:
    """
      Process and correct the raw data collected during the questionnaire. This method calculates the total score by summing all the responses (stored in data by the conduct_experiment method). The subject's results (dict) are then updated with this total score."""

    totalscore = sum(self.data)
    self.subject.results.update({f'total_{self.exp_name}': totalscore})

  def conduct_experiment(self) -> None:
    """
      Administer the questionary experiment."""

    self.display_instructions()

    # Iterate through the questions
    while len(self.data) < 5:
      try:
        answer = int(input(f'In a range from 0 to 3, how would you rate the following question? {self.questions[len(self.data)]}'))
        if answer >= 0 and answer <= 3:
          self.data.append(answer)
        else:
          print('Invalid input! Try again.')

      except ValueError:
        print('Invalid input! Try again.')
    self.correct_data()

# Creating the third experiment
class Memory_Numbers(Experiment):
  """
    A subclass derived from the "Experiment" abstract class. Inherits all methods and attributes of the parent class. (You have to document the attributes and any information you consider) """

  def __init__(self, *args) -> None:
    """
      Initialize the Memory_Numbers subclass. 
      Utilizes the super() function to inherit the properties and behaviors from the parent          "Experiment" class
      """
    super().__init__(*args)

  def correct_data(self) -> None:
    """
       Update the results dictionary with the total correctly guessed numbers.
      """
    total_guessed = 0
    
    for v in self.data:
      if v == True:
        total_guessed += 1
      
    self.subject.results.update({'Memory numbers':total_guessed})

  def conduct_experiment(self) -> None:
    """
      Run the memory numbers experiment.
      """
      
    self.display_instructions()
    
    # Creating a random number list
    number_list = [random.randint(1,9) for _ in range(5)]
    print(f'Remember this numbers! {number_list}')
    
    # Waiting 3 seconds to give time to the subject to memorize the numbers
    time.sleep(3)
    # Cleaning the screen for better user experience
    print("\033[H\033[J")
    
    while len(self.data) < 5:
      try:
        # Ask the participant to input the next number in the sequence
        answer = int(input(f'Introduce the next number in the sequence: '))
        # Check if the entered number is within the range of 1 to 9
        if answer >= 1 and answer <= 9:
           # Compare the entered number with the next number in the generated sequence
          if answer == number_list[len(self.data)]:
            # If the entered number matches the sequence, add True to self.data
            self.data.append(True)
          else:
            self.data.append(False)
          
        else:
          # If the entered number is not within the valid range, display an error message
          print('Invalid input! Try again.')
        
      except ValueError:
        # If the entered input is not an integer, display an error message
        print('Invalid input! Try again.')
    
    # Calling the correct_data method    
    self.correct_data()