import random
import checks
from general_classes import Subject,Experiment
from subclasses import ReactionTime, Questionnaire,Memory_Numbers
from report import Report

# Randomizing subject ID
random.seed(42)
subject_id = str(random.random())[2:]

# Creating a subject for the experiments
spock = {
    'name': 'Spock Vulkan',
    'age': 162,
    'birth_date': '06-01-2230',
    'years_of_education': 60
}
# Instantiating the subject class
spock_subject = Subject(subject_id, spock)
# Instanciating the experiment
general_exp = Experiment(spock_subject)

# Printing the details of the subject
print(spock_subject.__repr__())
# Create the format string
format_string = "{:<15}{:>10}"
# Print the details using the format string
print('An instance for the abstract Experiment class:')
print(format_string.format("Name:", general_exp.exp_name))
print(format_string.format("Instructions:", general_exp.exp_instruction))
print(format_string.format("List:", str(general_exp.data)))
print()
print('For the subject instance:')
print("subject:", general_exp.subject)


# Instantiating the reaction time experiment
reaction_experiment = ReactionTime(spock_subject,'Reaction Time','Press ENTER as quickly as possible!')
# Calling the methods conduct_experiment and correct_data
reaction_experiment.conduct_experiment(n_trials=3, pause_range=10)
reaction_experiment.correct_data()

# Printing the results of the experiment
print(reaction_experiment.subject)
print(reaction_experiment.subject.results)


# The Second Experiment: a Questionnaire
# The experiment will be conduced by a subclass of the Experiment class, called Questionnaire. The subclass will inherit all the methods and attributes of the Experiment class.

# Calling the check_files function to check if the files containing the questions are present
checks.check_files()

# Defining the instructions for the experiment
questionnaire_instructions = '''Below are some statements that people use to describe themselves.
Read each statement and press the number that indicates how you feel right now, being:
0 = NO, 1 = A LITTLE, 2 = QUITE A BIT, 3 = VERY MUCH.'''

# Instantiating the questionnaire experiment
questionnaire_experiment = Questionnaire('Files/Questionnaire.txt', spock_subject, 'Questionnaire',questionnaire_instructions) 

# Calling the method conduct_experiment
questionnaire_experiment.conduct_experiment()

# Printing the results of the experiment
print(questionnaire_experiment.subject.results)

memory_experiment = Memory_Numbers(spock_subject,'Memory Numbers', 'Remember the numbers displayed in the screen!')

memory_experiment.conduct_experiment()

# Printing the results of the experiment
print(questionnaire_experiment.subject.results)

report = Report(spock_subject, questionnaire_experiment)
report.create_graphics()
report.generate_report()