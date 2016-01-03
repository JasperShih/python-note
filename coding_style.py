# -*- coding: utf8 -*-
def is_corrected_key(key):
    directions = ['w','s','a','d']
    attack_directions = ['\x17', '\x13', '\x01', '\x04']
    result = False
    if key in (directions + attack_directions):
        result = True
    return result

def is_corrected_key(key):
    directions = ['w','s','a','d']
    attack_directions = ['\x17', '\x13', '\x01', '\x04']
    if key in (directions + attack_directions):
        return True
    else:
        return False

def is_corrected_key(key):
    directions = ['w','s','a','d']
    attack_directions = ['\x17', '\x13', '\x01', '\x04']
    if key in (directions + attack_directions):
        result = True
    else:
        result = False
    return result
	
第三種寫法明顯比第一種好:
1. if-else區塊一定會有一者被執行(explicit), 不用檢驗去想該區塊是否被執行(implicit)
2. 格式更加對稱, 更易閱讀

第三種寫法明顯比第二種好:
1. function只有一個出口, 那就是在function最下方; 
   這樣不用再去專注於function的所有出口(只看1行對比要看整個function),降低頭腦trace負擔

   
def run(self):
	turns_counter = 0#
	while ~self.is_game_end():
		acted_role = Game.get_acted_role(turns_counter)#
		result = turn_act(acted_role)
		update_game_states(result)
	display_score()
	
   
def run(self):
	while ~self.is_game_end():
		outcome = turn_act()
		update_game_states(outcome)
	display_score()

第一種寫法感覺很複雜, 因為他混雜了兩種概念, 在run中我們是想描述出各個flow stage,
而在第一種卻混雜了variable概念進來(turns_counter, acted_role, Game.get_acted_role()都是)


def turn(self):
	if acted_role == "player":
		player_act()
	else:
		wumpus_act()
	update_game_states()#

有if else似乎else下面要有東西, 才不會造成可讀性差?


def turn(self):
	if acted_role == "player":
		player_act()
	else:
		wumpus_act()
	update_game_states()
	show_score()

instructive programming應該要先平行的寫player_act(),wumpus_act(),update_game_states(),show_score();
而不是先寫player_act()及player_act()的子孫functions後(完全的完成player_act()), 再來寫wumpus_act(),update_game_states(),show_score(),
除非像show_score()和其他平行的functions明顯沒有聯繫, 則可以不用先寫.

if self.active_role is None or self.active_role == "wumpus":
	pass

if self.active_role in (None, "wumpus"):
	pass

@staticmethod
def is_not_valid_action(action_buffer):
	return (True if (action_buffer not in (Player.move_directions +
										   Player.attack_directions))else
			False)

第一種寫法好, 雖然他長, 但他正確的表達出程式的意思; 第三種則是適當的用法


if (self.game.wumpus is None or
            self.game.player is None):
            result = True
        else:
            result = False
        return result

result = True \
	if (self.game.wumpus is None or
		self.game.player is None) \
	else False
return result

return (True 
		if (self.game.wumpus is None or
			self.game.player is None) 
		else False)


1. 閱讀代碼就是人腦解譯代碼, 越易解譯代表可讀性高

2. 寫出來的代碼就是要讓他儘量被執行(explicit), 而不是被省略(implicit); 
   儘量寫一定會被執行的代碼, 而不是先default在optional skip的代碼

3. 光看父function,就要能看到或能預期,其所有子孫function的outputs
   (當然是要當這些outputs的生命週期>=父function時);
   只看function A代碼, 就要看到所有A及其inner functions的所有output
   (當然是在其inner functions的output有需要外傳時), 而不應該發生越級呈報的現象;
   比如將inner functions的output賦值給class object, 達成傳遞inner functions的output的效果,
   這樣的output是光看父function看不出來的.
 
4. 如果當一個method過於複雜, 應該想到是否有辦法藉由member來降低method複雜度

5. Procedure flow function就應該是純粹描述該procedure的各個flow stage; 
   而不應該混雜operational function的task進來.
   
   

		
return (1 if (self.game.wumpus is None or
			  self.game.player is None)
		  else 
		2 if (self.game.wumpus is "GG" and 
			  self.game.player is "KK")
		  else 
		3)

return (1 if (self.game.wumpus is None or
			  self.game.player is None)else
		2 if (self.game.wumpus is "GG" and
			  self.game.player is "KK")else 
		3)






