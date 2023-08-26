import time
 
pkmn_left = """
`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \\
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
jgs      (_,'"""
pkmn_right = """
       ,___          .-;'
       `"-.`\_...._/`.`
    ,      \        /
 .-' ',    / ()   ()\\
`'._   \  /()    .  (|
    > .' ;,     -'-  /
   / <   |;,     __.;
   '-.'-.|  , \    , \\
      `>.|;, \_)    \_)
       `-;     ,    /
          \    /   <
           '. <`'-,_)
        jgs '._)"""
 
clock_1 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .      /  . \\
 |; .      /   . |;
 ||45    ()    15||
 |; .          . |;
  \\ .         . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_2 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .         . \\
 |; .          . |;
 ||45    ()----15||
 |; .          . |;
  \\ .         . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_3 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .         . \\
 |; .          . |;
 ||45    ()    15||
 |; .     \\    . |;
  \\ .      \\  . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_4 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .         . \\
 |; .          . |;
 ||45    ()    15||
 |; .     |    . |;
  \\ .     |   . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_5 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .         . \\
 |; .          . |;
 ||45    ()    15||
 |; .   /      . |;
  \\ .  /      . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_6 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .         . \\
 |; .          . |;
 ||45----()    15||
 |; .          . |;
  \\ .         . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_7 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // . \\       . \\
 |; .   \\      . |;
 ||45    ()    15||
 |; .          . |;
  \\ .         . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
clock_8 = """
        .--.
   .-._;.--.;_.-.
  (_.'_..--.._'._)
   /.' . 60 . '.\\
  // .   |     . \\
 |; .    |     . |;
 ||45    ()    15||
 |; .          . |;
  \\ .         . //
   '._' 30 '_.'//
    '-._'--'_.-' jgs
        `""`
"""
 
check = True
counter = 0
counter_pkmn = 0
counter_1 = 100
time_spent = 0
frame_pkmn = [pkmn_left,pkmn_left,pkmn_right,pkmn_right]
frame = [clock_1,clock_2,clock_3,clock_4,clock_5,clock_6, clock_7, clock_8]
fps = 0.1
dash = "|"
 
while check:
 if time_spent > 50 and time_spent < 60:
  time.sleep(fps)
  if counter_pkmn == 4:
   counter_pkmn -= 4
  print("\n"*180)
  print("WILD PIKACHU APPEARED!!!!\n\nHP:\n")
  print(dash*(counter_1))
  counter_1 -= 1
  print("{}".format(frame_pkmn[counter_pkmn]))
  print("\nTime spent: {} seconds\n".format(time_spent))
  print("\nFPS: {}\n".format(fps*100))
  time_spent += fps
  counter_pkmn += 1
 elif time_spent > 120 and time_spent < 130:
  time.sleep(fps)
  if counter_pkmn == 4:
   counter_pkmn -= 4
  print("\n"*180)
  print("WILD PIKACHU APPEARED!!!!\n\nHP:\n")
  print(dash*(counter_1))
  counter_1 -= 1
  print("{}".format(frame_pkmn[counter_pkmn]))
  print("\nTime spent: {} seconds\n".format(time_spent))
  print("\nFPS: {}\n".format(fps*100))
  time_spent += fps
  counter_pkmn += 1
 elif time_spent > 200 and time_spent < 210:
  time.sleep(fps)
  if counter_pkmn == 4:
   counter_pkmn -= 4
  print("\n"*180)
  print("WILD PIKACHU APPEARED!!!!\n\nHP:\n")
  print(dash*(counter_1))
  counter_1 -= 1
  print("{}".format(frame_pkmn[counter_pkmn]))
  print("\nTime spent: {} seconds\n".format(time_spent))
  print("\nFPS: {}\n".format(fps*100))
  time_spent += fps
  counter_pkmn += 1
 else:
  counter_1 = 100
  counter_pkmn = 0
  time.sleep(fps)
  if counter == 8:
   counter -= 8
  print("\n"*180)
  print("{}".format(frame[counter]))
  print("\nTime spent: {} seconds\n".format(time_spent))
  print("\nFPS: {}\n".format(fps*100))
  time_spent += fps
  counter += 1
 