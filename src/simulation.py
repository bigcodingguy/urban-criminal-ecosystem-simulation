from models.organization import Organization
from models.member import Member
from models.territory import Territory
from models.racket import Racket
from models.relationship import Relationship
from systems.markov_transitions import markov_transition
from systems.ai_decision_engine import choose_action
import random

# TODO build helper methods to keep organization and territory lists in sync
class Simulation:
    def __init__(self):
        self.organizations = []
        self.territories = []
        self.members = []
        self.relationships = []
        self.rackets = []

        # Organizations
        hq1 = Territory("Small Heath", "street", 50, 0.3, 3, "visible", "Birmingham")
        t1 = Territory("The Bookmaker", "Bookmaker", 50, 1, 3, "hidden", "Birmingham")
        org1 = Organization("Peaky Blinders", 1000, 20, hq1, "Tommy", "Opportunistic")
        t1.owner = org1
        m1 = Member("Arthur", 80, 100, "Operations")
        m2 = Member("John", 75, 100, "Bruiser")
        org1.recruit_members([m1, m2])
        org1.territories.append(hq1)
        hq1.owner = org1
        self.organizations.append(org1)
        self.territories.append(hq1)
        self.territories.append(t1)

        hq2 = Territory("Bourbon Street", "street", 100, 0.8, 9, "visible", "Birmingham")
        t2 = Territory("The Warehouse", "Warehouse", 100, 2, 5, "hidden", "Birmingham")
        org2 = Organization("Kimber's Boys", 3000, 40, hq2, "Billy", "Vindictive")
        t2.owner = org2
        m3 = Member("Lee", 90, 50, "Accounting")
        m4 = Member("Matt", 55, 80, "Protection")
        org2.recruit_members([m3, m4])
        org2.territories.append(hq2)
        hq2.owner = org2
        self.organizations.append(org2)
        self.territories.append(hq2)
        self.territories.append(t2)

        hq3 = Territory("Main Street", "street", 200, 1.5, 10, "visible", "London")
        t3 = Territory("The Club", "Gentleman's Club", 200, 1, 12, "hidden", "London")
        org3 = Organization("Solomons", 5000, 20, hq3, "Alfie", "Territorial")
        t3.owner = org3
        m5 = Member("Bowie", 80, 100, "Accounting")
        m6 = Member("Jordan", 45, 35, "Bruiser")
        org3.recruit_members([m5, m6])
        org3.territories.append(hq3)
        hq3.owner = org3
        self.organizations.append(org3)
        self.territories.append(hq3)
        self.territories.append(t3)

        # Relationships
        rel_1_2 = Relationship(org1, org2, "Tense")
        rel_1_3 = Relationship(org1, org3, "Neutral")
        rel_2_3 = Relationship(org2, org3, "Tense")

        self.relationships.append(rel_1_2)
        self.relationships.append(rel_1_3)
        self.relationships.append(rel_2_3)

    def run(self, num_weeks):
        for week in range(num_weeks):
            self.run_week(week)

    def run_week(self, week):
        for organization in self.organizations:
            action = choose_action(organization.personality)
            print(f"Week: {week}: {organization.name} chooses to {action}")
        for relationship in self.relationships:
            old_state = relationship.state
            new_state = markov_transition(relationship.state, random.random() * 2 - 1)
            relationship.update(new_state)
            print(f"Week: {week}: {relationship.org_a.name} and {relationship.org_b.name}: {old_state} -> {new_state}")
        