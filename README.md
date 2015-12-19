# homefieldadvantage
Everything here is written in Python and uses BurntSushi's nflgame package for Python. 
Everything is designed to be compatible with the commandline, and there will be examples in this file.

make_game_files.py 
  Retrieves and stores a year(s) worth of NFL games in a .csv file(s) in the game directory.
  Multiple games can be "get"ed at once. Once games have been retrieved, different years can be "combine"d.
  
  example: python make_game_files.py get 2011
  example: python make_game_files.py combine onlyevenyears 2010 2012 2014

make_dat_files.py
  Reads .csv game files and makes .dat files to be used with plot_box_and_hist.py and plot_ppg.py.
  
  example: python make_dat_files.py homeppg games/games_all.csv
  example: python make_dat_files.py spread games/games_2014.csv
  
plot_ppg.py
  Reads 'data/home_ppg.dat', 'data/away_ppg.dat', and 'data/total_ppg.dat' and creates either a box plot
  or a histogram.
  You'll have to use make_dat_files.py to change what is stored in the .dat files, or modify the code to be more flexible.
  
  example: python plot_ppg.py box
  
plot_box_and_hist.py
  Reads 'data/home_win_rating.dat', or 'data/home_spread.dat' and creates a combined box plot and histogram.
  You'll have to use make_dat_files.py to change what is stored in the .dat files, or modify the code to be more flexible.
  
  example: python plot_box_and_hist.py winrating
  
comp_teams.py
  Reads .csv game files to determine a handful of statistics for each team. 
  Statistics include at-home points per game, points allowed per game, spread per game, and win rating;
  the ratio of the at-home to away statistic for the previously mentioned statistics;
  and the difference of the at-home to away statistics for the previously mentioned statistics.
  This will sort the list by that statistic and display the best N of them.
  The "make" command will make .dat files for each statistic type.
  
  example: python comp_teams.py ppg 2015 5  # this will print the top 5 teams from 2015 with the best at-home ppg.
  example: python comp_teams.py make 2015 16  # this will make .dat files for each statistic for 2015. Each .dat file will contain the 16 best teams. 

plot_stats.py
  Reads the .dat files created by comp_teams.py. You'll need to use comp_teams.py to change what is plotted, or you can modify this file to be more flexible.
  'plot' will plot wins vs statistic for each team. wins can be either at-home wins, or total wins.
  'compare' will plot two statistics against each other.
  
  example: python plot_stats.py plot 2012 papgratio total  # plots total wins vs papg ratio for 2012.
  example: python plot_stats.py compare all ppg 2015 ppg  # plots the ppg for all years since 2009 with the ppg for 2015.
