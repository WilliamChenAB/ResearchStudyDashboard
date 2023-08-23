import pandas as pd
import re
import os
import shutil

# Create a directory to store the new Excel files
output_directory = "NegativeStorySheets"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create a directory for PsychoPy integration sheets
integration_directory = "PsychopyIntegrationSheets"
if not os.path.exists(integration_directory):
    os.makedirs(integration_directory)

# Load the original Excel file
input_file = "ExportedData.xlsx"
df_original = pd.read_excel(input_file)

# Define the columns for story splitting and NSBs
story_columns = ["Q1", "Q3", "Q5", "Q7", "Q9", "Q11"]
nsb_columns = ["Q2", "Q4", "Q6", "Q8", "Q10", "Q12"]

# Function to split text into sentences without word breaks
def split_into_sentences(text, num_sentences=8):
    words = text.split()
    words_left = len(words)
    # dDivision to get ceiling instead of floor
    words_per_sentence = -(words_left // -num_sentences)
    
    sentences = []
    current_sentence = ""
    sentences_left = num_sentences
    count = 0

    for word in words:
        if count < words_per_sentence:
            if count > 0:
                current_sentence = current_sentence + " " + word
            else:
                current_sentence = word
            count += 1
        else:
            sentences.append(current_sentence)
            sentences_left -= 1
            current_sentence = word
            count = 1
        # Need to update to ensure exactly 8 sentences are made
        if sentences_left > 0:
            words_per_sentence = -(words_left // -sentences_left)
            words_left -= 1

    # Add the last sentence
    if current_sentence:
        sentences.append(current_sentence)

    return sentences

# Get the participant's email as input
participant_id = input("Enter the participant's ID: ")

# Check if the provided email exists in the DataFrame
if participant_id in df_original["ParticipantID"].astype(str).values:
    # Find the row with the matching email
    participant_row = df_original[df_original["ParticipantID"].astype(str) == participant_id].iloc[0]

    # Create a directory for the participant's files
    participant_directory = os.path.join(output_directory, participant_id)
    if not os.path.exists(participant_directory):
        os.makedirs(participant_directory)

    for idx, (story_col, nsb_col) in enumerate(zip(story_columns, nsb_columns), start=1):
        # Split story into sentences
        story_text = participant_row[story_col]
        sentences = split_into_sentences(story_text)

        # Create a new Excel workbook for the participant's Negative sheet
        workbook_negative = pd.ExcelWriter(os.path.join(participant_directory, f"Negative{idx}.xlsx"), engine="xlsxwriter")

        # Create a new sheet for story sentences
        df_story = pd.DataFrame({"StorySentences": sentences})
        df_story.to_excel(workbook_negative, sheet_name="Negative", index=False)
        workbook_negative.save()
        workbook_negative.close()

        # Create a new Excel workbook for the participant's NSB sheet
        workbook_nsb = pd.ExcelWriter(os.path.join(participant_directory, f"NSB{idx}.xlsx"), engine="xlsxwriter")

        # Create a new sheet for NSBs
        nsb_values = [participant_row[f"{nsb_col}_{i}"] for i in range(1, 11)]
        cue_values = ["REACT", "REGULATE"] * 5
        df_nsb = pd.DataFrame({"NSBs": nsb_values, "Cue": cue_values})
        df_nsb.to_excel(workbook_nsb, sheet_name="NSB", index=False)
        workbook_nsb.save()
        workbook_nsb.close()

        # Copy the generated sheets to the PsychoPy integration directory
        shutil.copy(os.path.join(participant_directory, f"Negative{idx}.xlsx"), os.path.join(integration_directory, f"Negative{idx}.xlsx"))
        shutil.copy(os.path.join(participant_directory, f"NSB{idx}.xlsx"), os.path.join(integration_directory, f"NSB{idx}.xlsx"))

    print("Excel files created successfully!")
else:
    print("Participant ID not found in the dataset.")