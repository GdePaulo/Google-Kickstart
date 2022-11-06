def main():
  test_cases = int(input())
  for test_case in range(1, test_cases + 1):
    N, R, C, Sr, Sc = map(int, input().split())
    instructions = input()

    final_r, final_c = end_position(N, R, C, Sr, Sc, instructions)
    print(f'Case #{test_case}: {final_r} {final_c}')

def end_position(N, R, C, Sr, Sc, instructions):
  # TODO: Complete this function and return the final position (row, column) of
  # the robot
  final_r, final_c = 0, 0

  # history = [[0 for x in range(C)] for y in range(R)]
  r, c = Sr - 1, Sc - 1
  history = {getPairId(r, c)}
  row_history = [[] for x in range(R)]
  columns_history = [[] for x in range(C)]

  row_history[r].append((c, c))
  columns_history[c].append((r, r))
  
  for d in instructions:
    print("Going", d)
    r, c, row_history, columns_history = getPosition(r, c, d, row_history, columns_history)
    # history_string = str(r) + "x" + str(c)
    # history_id = getPairId(r, c)
    # while history_id in history:
    #   
    #   r, c = getPosition(r, c, d)
    #   history_id = getPairId(r, c)
    #   # history_string = str(r) + "x" + str(c)
    # 
    # history.add(history_id)
    print("Now at", r, c)
    
  final_r, final_c = r + 1, c + 1
  return final_r, final_c


def getPairId(k1, k2): 
  return (k1 + k2) * (k1 + k2 + 1) // 2 + k2


def positiveUpdate(p, ph):
  next_p = p + 1
  print(f"initial ph {ph}")
  found_i = -1
  for i, (pl, pr) in enumerate(ph):
    # if next_p == pl or :
    if next_p == pl or (p >= pl and p <= pr):
      p = pr + 1
      next_p = p
      found_i = i
      break
  if found_i >= 0:
    if found_i == len(ph) - 1:
      ph[found_i] = (ph[found_i][0], p)
    else:
      if ph[found_i + 1][0] == p + 1:
        ph[found_i + 1] = (ph[found_i][0], ph[found_i + 1][1])
        ph.pop(found_i)
      else:
        ph[found_i] = (ph[found_i][0], p)
  else:
    ph.append((p, next_p))
    ph = sorted(ph, key=lambda x: x[0])
  print(f"p{p} next_p{next_p} ph{ph}")
  return next_p, ph

def negativeUpdate(p, ph):
  next_p = p - 1
  print(f"initial ph {ph}")
  found_i = -1
  for i, (pl, pr) in enumerate(reversed(ph)):
    # if next_p == pl or :
    if next_p == pr or (p >= pl and p <= pr):
      p = pl - 1
      next_p = p
      found_i = len(ph) - i - 1
      break
  if found_i >= 0:
    if found_i == 0:
      ph[found_i] = (p, ph[found_i][1])
    else:
      if ph[found_i - 1][1] == p - 1:
        ph[found_i - 1] = (ph[found_i - 1][0], ph[found_i][1])
        ph.pop(found_i)
      else:
        ph[found_i] = (p, ph[found_i][1])
  else:
    ph.append((next_p, p))
    ph = sorted(ph, key=lambda x: x[0])
  print(f"p{p} next_p{next_p} ph{ph}")
  return next_p, ph

def getPosition(r, c, instruction, rh, ch):
  if instruction == "E":
    c, rh[r] = positiveUpdate(c, rh[r])
  if instruction == "W":
    c, rh[r] = negativeUpdate(c, rh[r])
  if instruction == "N":
    r, ch[c] = negativeUpdate(r, ch[c])
  if instruction == "S":
    r, ch[c] = positiveUpdate(r, ch[c])


  return r, c, rh, ch

if __name__ == '__main__':
  main()
