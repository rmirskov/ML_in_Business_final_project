from flask_wtf import Form
from wtforms import IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class DataForm(Form):
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=17, max=85)])
    workclass = SelectField(
        'workclass', choices=[
            'state-gov', 'self-emp-not-inc', 'private', 'federal-gov', 'local-gov',
            'self-emp-inc', 'without-pay', 'never-worked'
            ]
        )
    sex = SelectField('sex', choices=['male', 'female'])
    race = SelectField('race', choices=[
        'white', 'black', 'asian-pac-islander', 'amer-indian-eskimo', 'other'
        ])
    education = SelectField('education', choices=[
        'bachelors', 'hs-grad', '11th', 'masters', '9th', 'some-college', 'assoc-acdm', 'assoc-voc',
        '7th-8th', 'doctorate', 'prof-school', '5th-6th', ' 10th', ' 1st-4th', 'preschool', '12th'
        ])
    education_num = IntegerField('education_num', validators=[DataRequired(), NumberRange(min=0, max=20)])
    marital_status = SelectField('marital_status', choices=[
        'never-married', 'married-civ-spouse', 'divorced', 'married-spouse-absent', 'separated',
        'married-af-spouse', 'widowed'
        ])
    occupation = SelectField('occupation', choices=[
        'adm-clerical', 'exec-managerial', 'handlers-cleaners', 'prof-specialty', 'other-service',
        'sales', 'craft-repair', 'transport-moving', 'farming-fishing', 'machine-op-inspct',
        'tech-support', 'other', 'protective-serv', ' armed-forces', 'priv-house-serv'
        ])
    relationship = SelectField('relationship', choices=[
        'not-in-family', 'husband', 'wife', 'own-child', 'unmarried', 'other-relative'
        ])
    capital_gain = IntegerField('capital_gain', validators=[DataRequired(), NumberRange(min=0)])
    capital_loss = IntegerField('capital_loss', validators=[DataRequired(), NumberRange(min=0)])
    hours_per_week = IntegerField('hours_per_week', validators=[DataRequired(), NumberRange(min=0, max=100)])
    native_country = SelectField('native_country', choices=[
        'united-states', 'cuba', 'jamaica', 'india', 'other', 'mexico', 'south', 'puerto-rico',
        'honduras', 'england', 'canada', 'germany', 'iran', 'philippines', 'italy', 'poland',
        'columbia', 'cambodia', 'thailand', 'ecuador', 'laos', 'taiwan', 'haiti', 'portugal',
        'dominican-republic', 'el-salvador', 'france', 'guatemala', 'china', 'japan', 'yugoslavia',
        'peru', 'outlying-us(guam-usvi-etc)', 'scotland', 'trinadad&tobago', 'greece', 'nicaragua',
        'vietnam', 'hong', 'ireland', 'hungary', 'holand-netherlands'
        ])
