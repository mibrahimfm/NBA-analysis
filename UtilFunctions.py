import scipy.stats as sts
import pandas as pd

def mean(data):
    return sum(data) / len(data)

def variance(data):
    n = len(data)
    avg = mean(data)
    
    deviations = [(x - avg) ** 2 for x in data]
    
    variance = sum(deviations) / n
    return variance

def std(data):
    var = variance(data)
    std = var ** 0.5
    return std

def round_closest_half(n):
    return round(n * 2) / 2

def growth_rate(data):
    straight_line_growth = []
    
    for i in range(1, len(data)):
        growth = (data[i] - data[i-1]) / data[i-1]
        straight_line_growth.append(growth)
        
    growth_rt = sum(straight_line_growth) / len(straight_line_growth)
    
    return "{:.2f}%".format(growth_rt*100)

def format_season(season):
        #Formats years in season to use in File Name
        #Ex: 2021 turns into 2020-21
        first_year = season-1
        second_year = str(season)[2:]
        
        return first_year, second_year
    
def spearman_rank_corr(rank1, rank2):
    d_square = []
    
    if len(rank1) != len(rank2):
        return
    
    n = len(rank1)
    
    for i in range(n):
        d = rank1[i] - rank2[i]
        d_square.append(d ** 2)
    
    return 1 - ((6 * sum(d_square)) / (n * (n ** 2 - 1)))

def merge_standings(eastern_standings, western_standings):
    standings = pd.concat([western_standings, eastern_standings])
    standings.sort_values(by=["Made_Playoffs", "W", "Rank", "Team"], ascending=[False, False, True, True], inplace=True)
    standings.reset_index(inplace=True)
    standings.drop('index', axis=1, inplace=True)
    standings.index += 1
    teams_ranked = dict(standings["Team"])
    inv_teams_ranked = {v: k for k, v in teams_ranked.items()}
    return inv_teams_ranked

def linear_regression_stat(x, y):
    if len(x) != len(y):
        return
    
    return sts.linregress(x, y)

def spearman_rank_corr(rank1, rank2):
    d_square = []
    
    if len(rank1) != len(rank2):
        return
    
    n = len(rank1)
    
    for i in range(n):
        d = rank1[i] - rank2[i]
        d_square.append(d ** 2)
    
    return 1 - ((6 * sum(d_square)) / (n * (n ** 2 - 1)))