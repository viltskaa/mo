import pandas as pd
import pathlib
import utils
import json
from pulp import *

BASEDIR = pathlib.Path(__file__).parent.resolve()

capacities = pd.read_csv(BASEDIR / 'csv' / 'capacities.csv')
constrains = pd.read_csv(BASEDIR / 'csv' / 'constraints.csv')
projects = pd.read_csv(BASEDIR / 'csv' / 'projects.csv')

requirements = utils.load_requirements(BASEDIR / 'requirements' / 'real_requirements.json')

problem = LpProblem('Game_Studio_Problem', LpMaximize)
# Constants
T = 120
MaxConcurrent_GM = 12
MaxConcurrent_GR = 10
MaxConcurrent_S = 15

# Requirements NORMAL
MinReqAAA = requirements.get("AAA_RPG", 3)
MinReqAA = requirements.get("AA_RPG", 6)
MinReqRemake = requirements.get("Remake", 6)
MinReqDLC = requirements.get("DLC", 20)
MinReqSinglePlayer = requirements.get("Strat_SP", 5)
MinReqMultiplayer = requirements.get("Strat_MP", 3)
MinReqSimMobile = requirements.get("Sim_Mobile", 6)
MinReqSimNoMobile = requirements.get("Sim_NoMobile", 8)
MinReqSimVR = requirements.get("Sim_VR", 4)

MinReqRPG = MinReqAAA + MinReqAA + MinReqRemake + MinReqDLC
MinReqStrategy = MinReqSinglePlayer + MinReqMultiplayer
MinReqSim = MinReqSimMobile + MinReqSimNoMobile + MinReqSimVR