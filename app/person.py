from pydantic import BaseModel, Field


class Person(BaseModel):
    age: int = Field(..., description="Age in years")
    workclass: str = Field(..., description="valid values are Private, Local-gov, Self-emp-not-inc, Federal-gov, State-gov, Self-emp-inc, Without-pay, Never-worked, use '?' if unknown")
    education: str = Field(..., description="valid values are 11th, HS-grad, Assoc-acdm, Some-college, 10th, Prof-school, 7th-8th, Bachelors, Masters, Doctorate, 5th-6th, Assoc-voc, 9th, 12th, 1st-4th, Preschool")
    education_num: int = Field(..., description="Education in years")
    marital_status: str = Field(
        ..., description="valid values are Never-married, Married-civ-spouse, Widowed, Divorced, Separated, Married-spouse-absent, Married-AF-spouse")
    occupation: str = Field(..., description="valid values are Machine-op-inspct, Farming-fishing, Protective-serv, Other-service, Prof-specialty, Craft-repair, Adm-clerical, Exec-managerial, Tech-support, Sales, Priv-house-serv, Transport-moving, Handlers-cleaners, Armed-Forces, use '?' if unknown")
    relationship: str = Field(
        ..., description="valid values are Own-child, Husband, Not-in-family, Unmarried, Wife, Other-relative")
    race: str = Field(..., description="valid values are Black, White, Asian-Pac-Islander, Other, Amer-Indian-Eskimo")
    sex: str = Field(..., description="valid values are Male, Female")
    capital_gain: int = Field(..., description="Capital Gain")
    capital_loss: int = Field(..., description="Capital Loss")
    hours_per_week: int = Field(..., description="Hours per week")
    native_country: str = Field(..., description="valid values are United-States, Peru, Guatemala, Mexico, Dominican-Republic, Ireland, Germany, Philippines, Thailand, Haiti, El-Salvador, Puerto-Rico, Vietnam, South, Columbia, Japan, India, Cambodia, Poland, Laos, England, Cuba, Taiwan, Italy, Canada, Portugal, China, Nicaragua, Honduras, Iran, Scotland, Jamaica, Ecuador, Yugoslavia, Hungary, Hong, Greece, Trinadad & Tobago, Outlying-US(Guam-USVI-etc), France, use '?' if unknown")

    class Config:
        schema_extra = {
            "example": {'age': 25,
                        'workclass': 'Private',
                        'education': '11th',
                        'education_num': 7,
                        'marital_status': 'Never-married',
                        'occupation': 'Machine-op-inspct',
                        'relationship': 'Own-child',
                        'race': 'Black',
                        'sex': 'Male',
                        'capital_gain': 0,
                        'capital_loss': 0,
                        'hours_per_week': 40,
                        'native_country': 'United-States'}
                 }
