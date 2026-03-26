from models.organization import Organization
from models.member import Member
from models.territory import Territory
from models.racket import Racket
from models.relationship import Relationship
from systems.markov_transitions import markov_transition
from systems.ai_decision_engine import choose_action
from systems.combat_resolver import resolve_combat
import random
import csv

class Simulation:
    def __init__(self, config):
        self.config = config
        self.organizations = []
        self.territories = []
        self.members = []
        self.relationships = []
        self.rackets = []
        self.territory_names = ["The Docks", "Small Heath", "Canal Street", "Market Square", "Main Street,", "Old Town", "Boardwalk", "Iron Bridge", "Central Avenue", "Park Place", "Whitmore Lane", "Elm Court", "The Railyard", "St. Johns", "Boomtown", "The Garrison", "Johnnie McCracken's", "Diagon Alley", "The Foundry", "Governor's Street"]
        self.territory_types = ["street", "port", "warehouse", "gentleman's club", "plaza", "distillery", "pub", "bookmaker", "factory"]
        self.neighborhoods = ["London", "Birmingham", "Manchester", "Liverpool"]
        self.organization_names = ["Sabini's Gang", "Peaky Blinders", "The Camden Boys", "The Iron Hand", "Kimber's Boys", "Solomon's Bakery"]
        self.personalities = ["Opportunistic", "Territorial", "Vindictive", "Strategic"]
        self.member_names = ["Tommy", "Arthur", "John", "Alfie", "Billy", "Joel", "Ringo", "Curly", "Johnny", "Michael", "Finn", "Isaiah", "Bonnie", "Clyde"]
        self.member_types = ["Bruiser", "Operations", "Accounting", "Protection"]
        self.racket_types = ["Protection", "Gambling", "Smuggling"]
        self.setup()
        self.csv_file = open('data/simulation_output.csv', 'w')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(['Week', 'Organization', 'Treasury', 'Members', 'Territories', 'Heat', 'Active'])
    
    def setup(self):
    
        for i in range(self.config['num_territories']):
            name = self.territory_names[i]
            type = random.choice(self.territory_types)
            income = random.randint(30, 200)
            heat = random.uniform(0.1, 2.0)
            control_requirement = random.randint(2, 5)
            neighborhood = random.choice(self.neighborhoods)
            territory = Territory(name, type, income, heat, control_requirement, "visible", neighborhood)
            self.territories.append(territory)
        
        for i in range(self.config['num_orgs']):
            name = self.organization_names[i]
            personality = random.choice(self.personalities)
            treasury = self.config['starting_treasury'] + random.randint(-1000, 1000)
            organization = Organization(name, treasury, 0, None, None, personality)
            for t in self.territories:
                if t.owner is None:
                    organization.hq = t
                    t.owner = organization
                    organization.territories.append(t)
                    break
        
            for i in range(self.config['members_per_org']):
                name = random.choice(self.member_names)
                skill = random.randint(30, 90)
                loyalty = random.randint(60, 100)
                role = random.choice(self.member_types)
                member = Member(name, skill, loyalty, role)
                organization.recruit_members([member])

            racket = Racket(random.choice(self.racket_types), random.randint(50, 90), random.uniform(0.5, 2.0))
            organization.rackets.append(racket)
            self.organizations.append(organization)

        for i in range(len(self.organizations)):
            for j in range(i + 1, len(self.organizations)):
                rel = Relationship(self.organizations[i], self.organizations[j], "Neutral")
                self.relationships.append(rel)

    def run(self, num_weeks):
        for week in range(num_weeks):
            self.run_week(week)
        print("\n--- Simulation Summary ---")
        for org in self.organizations:
            print(f"{org.name}: Treasury=${org.treasury}, Members={len(org.members)}, Territories={len(org.territories)}")
        for relation in self.relationships:
            print(f"{relation.org_a.name} & {relation.org_b.name}: {relation.state} | History: {relation.history}")
        
        self.csv_file.close()

    def run_week(self, week):
        for organization in self.organizations:
            if not organization.is_active: continue
            organization.collect_income()
            organization.pay_expenses()

        for organization in self.organizations:
            if not organization.is_active: continue
            action = choose_action(organization.personality)
            print(f"Week: {week}: {organization.name} chooses to {action}")
            if action == "Attack":
                target = None
                for rel in self.relationships:
                    if rel.org_a == organization and rel.org_b.is_active and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_b
                    elif rel.org_b == organization and rel.org_a.is_active and (rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_a
                if target and len(target.territories) > 0:
                    territory = random.choice(target.territories)
                    winner, winner_casualties, loser_casualties = resolve_combat(organization, target, territory)
                    print(f"Combat: {organization.name} attacks {target.name} for {territory.name} —— {winner.name} wins!")
                    if len(target.territories) == 0:
                        winner.treasury += target.treasury
                        target.treasury = 0


            elif action == "Expand":
                target_territory = None
                for territory in self.territories:
                    if territory.owner is None:
                        organization.territories.append(territory)
                        territory.owner = organization
                        print(f"Expansion: {organization.name} expands to {territory.name}!")
                        break
            
            elif action == "Recruit":
                name = random.choice(self.member_names)
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
                    if rel.org_a == organization and rel.org_b.is_active and (rel.state == "Tense" or rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_b
                        found_rel = rel
                        break
                    elif rel.org_b == organization and rel.org_a.is_active and (rel.state == "Tense" or rel.state == "Hostile" or rel.state == "War"):
                        target = rel.org_a
                        found_rel = rel
                        break
                if target:
                    pressure = random.random()
                    new_state = markov_transition(found_rel.state, pressure)
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

        betrayals = []
        for organization in self.organizations:
            for member in organization.members:
                if member.check_betrayal():
                    betrayals.append(member)
                    print(f"Betrayal: {member.name} betrays {organization.name}!")
            for member in betrayals:
                organization.members.remove(member)
            betrayals.clear()


        for organization in self.organizations:
            if organization.is_active and (len(organization.territories) == 0 or len(organization.members) == 0):
                organization.eliminate()
                print(f"Elimination: {organization.name} has been eliminated!")
        
        for organization in self.organizations:
            self.writer.writerow([week, organization.name, organization.treasury, len(organization.members), len(organization.territories), organization.heat, organization.is_active])
                
        