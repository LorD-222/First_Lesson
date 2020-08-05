def convert(seconds):
   days = seconds // (60*60*24)
   seconds %= 60*60*24 
   hours = seconds // (60*60)
   seconds %= 60*60 
   minutes = seconds // 60
   seconds %= 60
   print(f'{days}:{hours}:{minutes}:{seconds}')

convert(437325)