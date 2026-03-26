from models.organization import Organization
from models.member import Member
from models.territory import Territory
from models.racket import Racket
from models.relationship import Relationship
from systems.markov_transitions import markov_transition
from systems.ai_decision_engine import choose_action
from systems.combat_resolver import resolve_combat
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
        print("\n--- Simulation Summary ---")
        for org in self.organizations:
            print(f"{org.name}: Treasury=${org.treasury}, Members={len(org.members)}, Territories={len(org.territories)}")
        for relation in self.relationships:
            print(f"{relation.org_a.name} & {relation.org_b.name}: {relation.state} | History: {relation.history}")

    def run_week(self, week):
        for organization in self.organizations:
            organization.collect_income()
            organization.pay_expenses()

        for organization in self.organizations:
            action = choose_action(organization.personality)
            print(f"Week: {week}: {organization.name} chooses to {action}")
            if action == "Attack":
                target = None
                for rel in self.relationships:
                    if rel.org_a == organization and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_b
                    elif rel.org_b == organization and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_a
                if target and len(target.territories) > 0:
                    territory = random.choice(target.territories)
                    winner, winner_casualties, loser_casualties = resolve_combat(organization, target, territory)
                    print(f"Combat: {organization.name} attacks {target.name} for {territory.name} —— {winner.name} wins!")

            elif action == "Expand":
                target_territory = None
                for territory in self.territories:
                    if territory.owner is None:
                        organization.territories.append(territory)
                        territory.owner = organization
                        print(f"Expansion: {organization.name} expands to {territory.name}!")
                        break
            
            elif action == "Recruit":
                name = f"Recruit_{random.randint(1, 1000)}"
                skill = random.randint(30, 70)
                loyalty = random.randint(40, 80)
                new_member = Member(name, skill, loyalty, "Bruiser")
                organization.recruit_members([new_member])
                print(f"Recruitment: {organization.name} recruits new member {new_member.name}!")

            elif action == "Establish":
                type = random.choice(["Protection", "Gambling", "Smuggling"])
                income = random.randint(50, 90)
                heat = random.randint(1, 3)
                new_racket = Racket(type, income, heat)
                organization.rackets.append(new_racket)
                print(f"Growth: {organization.name} establishes new {new_racket.type} racket!")
            
            elif action == "Negotiate":
                target = None
                for rel in self.relationships:
                    if rel.org_a == organization and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_b
                        found_rel = rel
                        break
                    elif rel.org_b == organization and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_a
                        found_rel = rel
                        break
                if target:
                    pressure = random.random()
                    new_state = markov_transition(rel.state, pressure)
                    found_rel.update(new_state)
                    print(f"Negotiation: {organization.name} negotiates with {target.name} —— New state: {new_state}")
                
            elif action == "Lay Low":
                reduction = random.randint(0, 10)
                organization.heat = max(0, organization.heat - reduction)
                if reduction >= 5:
                    print(f"Laying low: {organization.name}'s efforts pay off!'")
                elif reduction < 5:
                    print(f"Laying low: {organization.name}'s efforts are in vain.")


        for relationship in self.relationships:
            old_state = relationship.state
            new_state = markov_transition(relationship.state, random.random() * 2 - 1)
            relationship.update(new_state)
            print(f"Week: {week}: {relationship.org_a.name} and {relationship.org_b.name}: {old_state} -> {new_state}")
        