PARAMS = {'legend.fontsize': 'xx-large',
          'figure.figsize': (25, 17),
         'axes.labelsize': 'large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'xx-large'}

CURRENT_TEAMS = ["ATL", "BOS", "BRK", "CHI", "CHO", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHO", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
TEAMS = CURRENT_TEAMS + ["SLH", "TCB", "NJN", "NYN", "CHA", "FWP", "SFW", "SDC", "VAN", "NOK", "NOH", "SEA", "SYR", "KCK", "ROR", "NOJ", "WSB", "CAP", "BAL"]

CURRENT_TEAM_COLORS = ['#E03A3E', '#007A33', '#000000', '#CE1141', '#00788C', '#860038', '#00538C', '#FEC524', '#1D42BA', 
                     '#1D428A', '#CE1141', '#002D62', '#BEC0C2', '#552583', '#5D76A9', '#98002E', '#00471B', '#78BE20',
                     '#85714D', '#F58426', '#007AC1', '#0077C0', '#006BB6', '#E56020', '#E03A3E', '#5A2D81', '#C4CED4', 
                     '#A1A1A4', '#00471B', '#002B5C']

WESTERN_CONF_TEAMS = ["DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM", "MIN", "NOP", "OKC", "PHO", "POR", "SAC", "SAS", "UTA"]
EASTERN_CONF_TEAMS = ["ATL", "BOS", "BRK", "CHI", "CHO", "CLE", "DET", "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR", "WAS"]

ATLANTIC_DIV_TEAMS = ["BOS", "BRK", "NYK", "PHI", "TOR"]
CENTRAL_DIV_TEAMS = ["CHI", "CLE", "DET", "IND", "MIL"]
SOUTHEAST_DIV_TEAMS = ["ATL", "CHO", "MIA", "ORL", "WAS"]
NORTHWEST_DIV_TEAMS = ["DEN", "MIN", "OKC", "POR", "UTA"]
SOUTHWEST_DIV_TEAMS = ["GSW", "LAC", "LAL", "PHO", "SAC"]
PACIFIC_DIV_TEAMS = ["DAL", "HOU", "MEM", "NOP", "SAS"]

ATLANTIC_DIV_TEAMS_COLORS = ["#007A33", "#000000", "#F58426", "#006BB6", "#A1A1A4"]
CENTRAL_DIV_TEAMS_COLORS = ["#CE1141", "#860038", "#1D42BA", "#002D62", "#00471B"]
SOUTHEAST_DIV_TEAMS_COLORS = ["#E03A3E", "#00788C", "#98002E", "#0077C0", "#002B5C"]
NORTHWEST_DIV_TEAMS_COLORS = ["#FEC524", "#78BE20", "#007AC1", "#E03A3E", "#00471B"]
SOUTHWEST_DIV_TEAMS_COLORS = ["#1D428A", "#BEC0C2", "#FDB927", "#E56020", "#5A2D81"]
PACIFIC_DIV_TEAMS_COLORS = ["#00538C", "#CE1141", "#5D76A9", "#85714D", "#C4CED4"]

SEASONS = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
POSITIONS = ["PG", "SG", "SF", "PF", "C"]

TEAM_TO_ABBR = {
    'ATLANTA HAWKS': 'ATL',
    'ST. LOUIS HAWKS': 'SLH',
    'MILWAUKEE HAWKS': 'MIL',
    'TRI-CITIES BLACKHAWKS': 'TCB',
    'BOSTON CELTICS': 'BOS',
    'BROOKLYN NETS': 'BRK',
    'NEW JERSEY NETS' : 'BRK',
    'NEW YORK NETS' : 'NYN',
    'CHICAGO BULLS': 'CHI',
    'CHARLOTTE HORNETS': 'CHO',
    'CHARLOTTE BOBCATS' : 'CHO',
    'CLEVELAND CAVALIERS': 'CLE',
    'DALLAS MAVERICKS': 'DAL',
    'DENVER NUGGETS': 'DEN',
    'DETROIT PISTONS': 'DET',
    'FORT WAYNE PISTONS': 'FWP',
    'GOLDEN STATE WARRIORS': 'GSW',
    'SAN FRANCISCO WARRIORS': 'SFW',
    'PHILADELPHIA WARRIORS': 'PHI',
    'HOUSTON ROCKETS': 'HOU',
    'SAN DIEGO ROCKETS': 'HOU',
    'INDIANA PACERS': 'IND',
    'LOS ANGELES CLIPPERS': 'LAC',
    'SAN DIEGO CLIPPERS': 'SDC',
    'BUFFALO BRAVES': 'BUF',
    'LOS ANGELES LAKERS': 'LAL',
    'MINNEAPOLIS LAKERS': 'MIN',
    'MEMPHIS GRIZZLIES': 'MEM',
    'VANCOUVER GRIZZLIES' : 'MEM',
    'MIAMI HEAT': 'MIA',
    'MILWAUKEE BUCKS': 'MIL',
    'MINNESOTA TIMBERWOLVES': 'MIN',
    'NEW ORLEANS PELICANS' : 'NOP',
    'NEW ORLEANS/OKLAHOMA CITY HORNETS' : 'NOP',
    'NEW ORLEANS HORNETS' : 'NOP',
    'NEW YORK KNICKS' : 'NYK',
    'OKLAHOMA CITY THUNDER' : 'OKC',
    'SEATTLE SUPERSONICS' : 'OKC',
    'ORLANDO MAGIC' : 'ORL',
    'PHILADELPHIA 76ERS' : 'PHI',
    'SYRACUSE NATIONALS' : 'SYR',
    'PHOENIX SUNS' : 'PHO',
    'PORTLAND TRAIL BLAZERS' : 'POR',
    'SACRAMENTO KINGS' : 'SAC',
    'KANSAS CITY KINGS' : 'KCK',
    'KANSAS CITY-OMAHA KINGS' : 'KCK',
    'CINCINNATI ROYALS' : 'CIN',
    'ROCHESTER ROYALS': 'ROR',
    'SAN ANTONIO SPURS' : 'SAS',
    'TORONTO RAPTORS' : 'TOR',
    'UTAH JAZZ' : 'UTA',
    'NEW ORLEANS JAZZ' : 'NOJ',
    'WASHINGTON WIZARDS' : 'WAS',
    'WASHINGTON BULLETS' : 'WAS',
    'CAPITAL BULLETS' : 'CAP',
    'BALTIMORE BULLETS' : 'BAL',
    'CHICAGO ZEPHYRS' : 'CHI',
    'CHICAGO PACKERS' : 'CHI',
    
    # DEFUNCT FRANCHISES
#     'ANDERSON PACKERS': 'AND',
#     'CHICAGO STAGS': 'CHI',
#     'INDIANAPOLIS OLYMPIANS': 'IND',
#     'SHEBOYGAN RED SKINS': 'SRS',
#     'ST. LOUIS BOMBERS': 'SLB',
#     'WASHINGTON CAPITOLS' : 'WAS',
#     'WATERLOO HAWKS': 'WAT',
}

ALL_NEW_ABBR = {
    'ATL': 'ATL',
    'BOS': 'BOS',
    'BRK': 'BRK',
    'NJN' : 'BRK',
    'CHH' : 'CHO',
    'CHI': 'CHI',
    'CHO': 'CHO',
    'CHA' : 'CHO',
    'CLE': 'CLE',
    'DAL': 'DAL',
    'DEN': 'DEN',
    'DET': 'DET',
    'GSW': 'GSW',
    'HOU': 'HOU',
    'IND': 'IND',
    'LAC': 'LAC',
    'SDC': 'LAC',
    'LAL': 'LAL',
    'MEM': 'MEM',
    'VAN' : 'MEM',
    'MIA': 'MIA',
    'MIL': 'MIL',
    'MIN': 'MIN',
    'NOP' : 'NOP',
    'NOK' : 'NOP',
    'NOH' : 'NOP',
    'NYK' : 'NYK',
    'OKC' : 'OKC',
    'SEA' : 'OKC',
    'ORL' : 'ORL',
    'PHI' : 'PHI',
    'PHO' : 'PHO',
    'POR' : 'POR',
    'SAC' : 'SAC',
    'SAS' : 'SAS',
    'TOR' : 'TOR',
    'UTA' : 'UTA',
    'WAS' : 'WAS',
    'WSB' : 'WAS',
    'TOT' : 'TOT'
}

TEAM_STATS = ['G', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA',
       '2P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK',
       'TOV', 'PF', 'PTS', 'W', 'L', 'PW', 'PL', 'MOV', 'SOS', 'SRS', 'ORtg',
       'DRtg', 'NRtg', 'Pace', 'FTr', '3PAr', 'TS%', 'Off_eFG%', 'Off_TOV%',
       'Off_ORB%', 'Off_FT/FGA', 'Def_eFG%', 'Def_TOV%', 'Def_DRB%',
       'Def_FT/FGA', 'Arena', 'Attend.', 'Attend./G']

PLAYER_STATS = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P',
       '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
       'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%',
       'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS',
       'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP', 'Salary']

BENCH_STATS = ['Age', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P',
       '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
       'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PER', 'TS%', '3PAr', 'FTr', 'ORB%',
       'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS',
       'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP', 'Salary', 'Count']

STATS_MAPPER = {
    'MP' : "Usage", 
    'FGA' : "Usage", 
    '3PA' : "Usage", 
    '3P%' : "Shooting", 
    '2PA' : "Usage", 
    '2P%' : "Shooting", 
    'eFG%' : "Shooting", 
    'FT%' : "Shooting", 
    'PF' : "Defensive", 
    'PTS' : "Shooting",
    'PER' : "General", 
    'TS%' : "Shooting", 
    '3PAr' : "Usage", 
    'FTr' : "Usage", 
    'ORB%' : "Rebounding", 
    'DRB%' : "Rebounding", 
    'TRB%' : "Rebounding", 
    'AST%' : "Playmaking", 
    'STL%' : "Defensive",
    'BLK%' : "Defensive", 
    'TOV%' : "Playmaking", 
    'USG%' : "Usage", 
    'OWS' : "General", 
    'DWS' : "General", 
    'WS/48' : "General", 
    'OBPM' : "General", 
    'DBPM' : "General", 
    'BPM' : "General",
    'Salary' : "Salary"
}

COLOR_MAPPER = {
    "Usage" : 'red',
    "Defensive": 'blue',
    "Shooting": 'green',
    "General": 'orange',
    "Rebounding" : 'purple',
    "Playmaking": 'darkgoldenrod',
    "Salary": 'slategray'
}