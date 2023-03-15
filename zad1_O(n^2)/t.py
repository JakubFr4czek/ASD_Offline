def My_tests(n):
  tab = []
  for i in range(n):
    test = "./my_tests/in/test" + str(i) +".txt"
    ans = "./my_tests/out/test" + str(i) +".txt"
    fo = open(test, "r")
    t = fo.read()
    fo.close()
    fo = open(ans, "r")
    a = fo.read()
    tab.append({'arg':[t],'hint':int(a)})
  return tab
