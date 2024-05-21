import os

def check_files() -> None:
  """
  Check for the existence of a directory 'Files'. If it doesn't exist, create it.
  Create a file 'Questionnaire.txt' within the 'Files' directory and write questionnaire lines into it.
  """
  if not os.path.exists('Files'):
    os.makedirs('Files')
  
  # Questionnaire.txt
  lines = [
      '1. I feel calm. \n', '2. I feel secure. \n', '3. I am tense. \n',
      '4. I am upset. \n', '5. I feel at ease.'
  ]
  
  with open('Files/Questionnaire.txt', 'w') as file:
    file.writelines(lines)
  