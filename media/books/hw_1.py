monday = int(input('рассходы в пн: '))
tuesday= int(input('рассходы в вт: '))
wednesday  = int(input('рассходы в ср: '))
thursday = int(input('рассходы в чт: '))
friday = int(input('рассходы в пт: '))
satirday = int(input('рассходы в сб: '))
sunday = int(input('рассходы в вс: '))
summ = monday + tuesday + wednesday + thursday + friday + satirday + sunday

sr_summ = int(summ // 7)

print(summ)
print(sr_summ)

