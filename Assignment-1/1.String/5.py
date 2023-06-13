# 5. Again, you have lost your USIS password!! You went to the registrar office and requested for a new password. 
# This time, you need to follow some rules to set your password. Otherwise, they won't change it. The rules are
# At least one lowercase letter
# At least one uppercase letter
# At least one digit (0-9)
# At least one special character (_ , $ , #, @)
# Your task is to find whether a given password follows all those rules. If it breaks any rule, you have to print Lowercase Missing, 
# Uppercase Missing, Digit Missing or Special Missing respective to the missing case. For more than one rule break,
# print all the rules that were broken (order doesn't matter). If the password is ok,

given = "ohmybracu"
upper = "QWETYTYUIOOPASDFGHJKLZXCVBNM"
lower = "qwertyuiopasdfghjklzxcvbnm"
digit = "0123456789"
sp_chr = '_$#@'

upper_count = 0
lower_count = 0
digit_count = 0
sp_chr_count = 0


for i in given:
  if i in upper:
    upper_count += 1
  elif i in lower:
    lower_count += 1
  elif i in digit:
    digit_count += 1
  elif i in sp_chr:
    sp_chr_count += 1

if upper_count ==0:
  print("Uppercase Missing", end=",")
if lower_count ==0:
  print("Lowercase Missing", end=",")
if digit_count ==0:
  print("Digit Missing", end=",")
if sp_chr_count ==0:
  print("Special Missing", end=",")
if upper_count != 0 and lower_count !=0 and digit_count != 0 and sp_chr_count != 0:
  print("OK")