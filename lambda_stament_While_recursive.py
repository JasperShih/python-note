def locate_on_arena(self, creature, character):
		#1
        random_x = random.randrange(0, self.arena.x_limit)
        random_y = random.randrange(0, self.arena.y_limit)
        spawn_location = self.arena.array[random_x][random_y]
        if spawn_location == '_':
            spawn_location = character
        else:
            self.locate_on_arena(creature, character)

		#2
        (spawn_location = character if (spawn_location == '_')else 
         self.locate_on_arena(creature, character))
        
		#3
        def ass():
            spawn_location = character
        (ass() if (spawn_location == '_') else
         self.locate_on_arena(creature, character))
		 
""""
python的lambda不允許assign操作, 因為他們認為函數式編程是不應該有狀態的,
我原本想寫成第2種簡潔的語法, 無奈無法assign, 只好回到第1種, 
因為實在不想寫成第3種
"""


def locate_on_arena2(self, creature, character):
        spawn = False
        while spawn is False:
            random_x = random.randrange(0, self.arena.x_limit)
            random_y = random.randrange(0, self.arena.y_limit)
            spawn_location = self.arena.array[random_x][random_y]
            if spawn_location == '_':
                spawn_location = character
                spawn = True
				

				
def get_action(self):
        action_buffer = None
        while Player.is_not_valid_action(action_buffer):
            print "Input valid action:"
            action_buffer = msvcrt.getch()
        self.action = action_buffer


def get_action2(self):
	action_buffer = None
	if Player.is_not_valid_action(action_buffer):
		self.action = action_buffer
	else:
		self.get_action2()				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				