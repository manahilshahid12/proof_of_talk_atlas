from pydantic import BaseModel
from typing import List

class Profile(BaseModel):
    id: str
    name: str
    capital_role: str                  # allocator / builder / service
    capital_direction: str             # deploying / raising / facilitating
    industry_focus: List[str]          # sectors they care about
    regulatory_exposure: List[str]     # MiCA, SEC, local laws, etc.
    primary_constraint: str            # main limitation (e.g., liquidity, compliance)
    strategic_goal: str                # what they want to achieve in the event
    urgency_level: str                 # high / medium / low
    geography_focus: List[str]         # regions of interest
