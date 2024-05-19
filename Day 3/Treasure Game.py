print('''
H=============================================================================H
H                     _______                            CAPTAIN -FUTURE-     H
H                 ,--'       `--._                                            H
H                (                `-.                         __              H
H              ,-' _                 )                     ,-'  `-.           H
H             /     `.   ,           |                   ,'        `.         H
H             |     -.\_(_      __   |                 ,'    .,,     )        H
H             |      /\)  `----' (   )               ,'   _((((\    (         H
H             |     /  _____   ___| (               ( ---'      )\   \        H
H             |,-.  \ <_____) (__ ; /                `. |(  )   '.      H
H             |)  ) (   (o)    (o| (                   ) \  i   )/      '.    H
H            ( | |   )        .  | ;                  (   \-=- ((         :   H
H             \ \|  (        __) |(                    \   `--' \)\  .     :  H
H              )  `--'    _____ (__)                    `. _'      '-'`---.;  H
H              `-.| `.    `---- /                       ,-' /    ,'        `. H
H                |`-._`-.      (                       /   |  , /            \H
H             ___|    `- `--^--'         (`.          | ,'  \: /              H
H   ,-. ,-.--'   |            |-._.-...  _`.`.        ;/     \/               H
H_,'\  \\  \     `-._       __|   \ \\ \__    )      | \      \               H
H.   \  \\  \        `-----__,'    \ \\ \ `.  \      |  `.     \        /    ,H
H `.  \  U   )    ___,----'         \ V /,-'\ /`-.   ;    `.  =|=-.__,-'    / H
H`-'   )    /,---'_,---._            \-' \,,-\    `-;     ;\  =|=        _,' (H
H      '----/  ,',-----._`.  [III]    '.   \,-\          ;  \  |   ,----'     H
H         /// ; /        \ \            \    ,-\`.       ;   ) |   `.______ ,'H
H       _//| | |          | |            \   \,|  `._   |   ;--|___,------.'-.H
H _,: _/ | | | |          ; |  [III]      \-.   \    `--'  ;--._()_,------|   H
H'  :/   | |  : \        ; ;              /  \__/         ;              (    H
H   ;     \ \  `.'.____,' /   [MEPH]     /     \         ;                \   H
H  ;       \ `.  `--.__,-'              / )     \       ; \                \  H
H /         `._`.____________________,-' /       |     ;   \         _.-----| H
H/\            `-._________________     /        |    ;     \     ,-'    |==| H
H  \            _,-'|          \   `-. |         |   ;       \   /       |==| H
H   `.  _    ,-'    |           |     ||         (  ;         \_/        |==| H
H     )/ \  |       |           |     |(\         \;          ; |        |==| H
H    ||   | |       |           |     | )\    ____(          ;  |         ``| H
H    ||   | |       |           |     |/  \,-'     \        ;   |           ; H
H     \)  \/        |           |     |   (         \      ;    |          |  H
H       |           |           |     |    \         \    ;     :          ;  H
H       |           |           |     |     \         \  ;       |        ;   H
H       |           |           |     |      \         \;        |       ;    H
H=======================================================================H

      ''')

print('''
Welcome to Treasure Island.
Your mission is to find the treasure.
      ''')

direction = input("You are at a cross road. Where do you want to go? Type left or right ").lower()
if direction == "left":
     action = input("You come to a lake. Do you want to swim or wait? ").lower()
     if action == "wait":
      door = input("You have arrived at a door. Which door do you want to choose? Red, Blue, or Yellow? ").lower()
      if door == "yellow":
         print("You won!")
      elif door == "blue":
          print("Eaten by beast. Game over.")
      elif door == "red":
          print("Burned by fire. Game over.")
      else:
         print("Game over. Try again.")
         
     else:
      print("Attacked by trouts. Game over.")

else:
     print("Fall into a hole. Game over.")
