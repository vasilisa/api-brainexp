"""User model"""
from sqlalchemy import Column, Integer, ForeignKey, DATETIME, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject

class ParticipantsQuestionDataFollowUp(BaseObject, Model):

    '''
        This is the table where we put the collected QUESTIONNAIRE data from the participants in the RLVARTASK: this only contains the responses but not the question content which is stored in the JS object on the server. 
        
    '''
    id = Column(Integer, primary_key=True)

    participant_id          = Column(Integer,nullable=False)
    prolific_id             = Column(VARCHAR(length=200))
    date_time_survey_start  = Column(VARCHAR(length=200))
    date_time_survey_end    = Column(VARCHAR(length=200))
    date_time               = Column(VARCHAR(length=200)) # date time start of the experiment 
    block_number            = Column(Integer,nullable=False) # the questionnaire has parts and each part is stored as a separate row in the table
    block_name              = Column(VARCHAR(length=1000), nullable=False) # the questionnaire has parts and each part is stored as a separate row in the table
    question_ids            = Column(VARCHAR(length=1000), nullable=False)  # the survey block name /tag for the section 
    answers                 = Column(VARCHAR(length=10000), nullable=False) # an array with the string answers to each of the question items in the questionnaire block    
    completed               = Column(VARCHAR(length=100), nullable=False) # whether the survey has been completed, uncompleted or "aborted"
    
    def get_id(self):
        return str(self.id)

    def get_participant_id(self):
        return str(self.participant_id)

    def get_prolific_id(self):
        return str(self.prolific_id)

    def get_block_number(self):
        return str(self.block_number)

    def get_block_name(self):
        return str(self.block_name)

    def get_question_ids(self): 
        return str(self.question_ids)

    def get_answers(self): 
        return str(self.answers)

    def get_completed(self): 
        return str(self.completed)
    
    def get_date_time_survey_start(self): 
        return str(self.date_time_survey_start)

    def get_date_time(self): 
        return str(self.date_time)

    def get_date_time_survey_end(self): 
        return str(self.date_time_survey_end)
    
    
    def errors(self):
        errors = super(ParticipantsQuestionDataFollowUp, self).errors()
        return errors
 
     

