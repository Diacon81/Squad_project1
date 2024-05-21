
#  Create two classes: Subject () and Experiment ()
class Subject():
  """
    Represents an experimental subject.
    Attributes:
    id (str): 9-digit identifier for the subject.
    info (dict): Preliminary data, e.g., sociodemographic details.
    results (dict): Outcomes of the tests conducted on the subject.
    """

  def __init__(self, subject_id: str, info: dict) -> None:
    """
    Initialize a SubjectData instance.

    Args:
    - subject_id (str): The identifier for the subject.
    - info (dict): Information related to the subject.

    Attributes:
    - subject_id (str): The identifier for the subject.
    - info (dict): Information related to the subject.
    - results (dict): A dictionary to store results related to the subject.
    """
    
    self.subject_id = subject_id
    self.info = info
    self.results = {}

  def __repr__(self) -> str:
    """
        Returns a formatted string representation of the subject's data. 
        Use padding (':<20' pads a str) for consistent display width. 
        Returns:
        str: Formatted information and results associated with the subject.
        """

    s = f'Data for ID {self.subject_id:<20}\n\n'
    """ 
        Iterate with two for loops the keys and values of the two 
        dictionaries at disposal (info and results, respectively) 
        to add them to the string object named s:"""

    for k, v in self.info.items():
      s += f"{k:<20} {v:<20}\n"
    for k, v in self.results.items():
      s += f"{k:<20} {v:<20}\n"
    return s


class Experiment():

  def __init__(self,
               subject: Subject,
               exp_name: str = 'Experiment',
               exp_instruction: str = 'Attention!') -> None:
    """
        Initialize a new experiment.
        Parameters:
        subject (Subject): The subject participating in the experiment.
        exp_name (str, optional): The name of the experiment. Default is 
        'Experiment'.
        exp_instructions (str, optional): The guidelines for the experiment. 
        Default is 'Attention!'."""

    self.subject = subject
    self.exp_name = exp_name
    self.exp_instruction = exp_instruction
    self.data = []

  def display_instructions(self) -> None:
    """
        Display the instructions for the experiment"""
    print(self.exp_instruction)

  def correct_data(self) -> None:
    """
        Process and correct the raw data collected during the experiment.
        This method is intended to be overridden by subclasses to provide specific data correction for each experiment."""
    pass

  def conduct_experiment(self) -> None:
    """
        Execute the experimental procedure.
This method is intended to be overridden by subclasses to provide specific steps or details for each experiment."""
    pass
