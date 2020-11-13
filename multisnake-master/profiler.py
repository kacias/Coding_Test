import pstats
stream = open('readable_local_snake_profiling.txt', 'w');
stats = pstats.Stats('local_snake_profiling', stream=stream)
stats.strip_dirs()
stats.sort_stats('time', 'calls')
stats.print_stats()
