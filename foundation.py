print('랜냥이 키우기')

LoveScore = 0
PlayerFeeling = 10

while True:
   print('1. 밥주기')
   print('2. 놀아주기')
   print('3. 씻기기')
   print('4. 게임종료')
   player = int(input('원하시는 항목을 선택해주세요: '))
   if player in (1, 2, 3):
      if player ==  1:
         print('랜냥이에게 먹일 메뉴를 고르세요.')
         c1 =int(input('1. 일반사료 2. 고급사료 3. 츄르 4. 치킨: '))
            if c1 == 1:
               print( #무난한 표정)
               print('랜냥이가 무난한 반응을 보입니다.')
            elif c1 == 2:
               LoveScore = +1
               print(#만족하는 표정)
               print('랜냥이가 거만한 표정을 짓습니다.')
               print('만족도 상승!')
            elif c1 == 3 :
               LoveScore = +2
               print('#환장하는 표정')
               print('랜냥이의 두 눈이 하트로 가득 차오릅니다.')
               print('만족도 대상승!')
            elif c1 == 4:
               LoveScore = -2
               print('#놀란 표정')
               print('인간이 먹는 음식은 나트륨이 많이 포함되어 있습니다.')
               print('염분 덩어리를 고양이에게 먹이려 하다니... 최악이군요!')
               print('만족도 대폭락!')
      elif player == 2:
         print('랜냥이와 함께할 행동을 고르세요.')
         c2 = int(input('1. 공놀이 2. 쥐 잡기 3. 뜨개실 장난 4. 산책: '))
            if c2 == 1:
               LoveScore = -1
               print('#싫어하는 표정')
               print('랜냥이는 공을 싫어합니다.')
               print('만족도 하락!')
            elif c2 == 2:
               LoveScore = +2
               print('#좋아하는 표정')
               print('당신은 직접 쥐 분장을 하고 랜냥이 앞에서 뛰어다닙니다.')
               print('랜냥이가 몹시 흥분하며 당신에게 뛰어듭니다.')
               print('비록 랜냥이가 당신을 할퀴어 상처가 났지만, 랜냥이의 행복한 표정을 보며 당신은 웃습니다.')
               print('만족도 대상승!')
            elif c2 == 3:
               LoveScore = +1
               print('#좋아하는 표정')
               print('랜냥이의 기분이 좋아 보입니다.')
               print('그러나 뜨개실의 주인인 친구가 그 모습을 보고 당신을 째려 봅니다.')
               print('저런! 인간관계가 무너질 조짐을 보입니다.')
               print('만족도 상승!')
            elif c2 ==4:
               PlayerFeeling = +5
               print('창밖을 보니 미세먼지 때문에 어둡습니다.')
               print('당신은 다시 침대로 돌아갑니다. 랜냥이도 당신의 선택에 동의합니다.')
               print('플레이어 만족도 상승!')
      elif player == 3:
         c3 =int(input('랜냥이를 씻기겠습니까? 예는 1, 아니오는 2를 입력하세요: '))
         if c3 == 1:
            PlayerFeeling = -5
            print('#싫어하는 표정')
            print('랜냥이가 매우 싫어합니다.')
            print('당신은 날뛰는 랜냥이를 씻기다가 친구와의 약속 시간에 늦고 말았습니다.')
            print('당신의 협소한 인간관계가 종말을 향해 나아가고 있습니다.')
            print('플레이어 만족도 하락!')
         else:
   
   elif player == 4:
      break