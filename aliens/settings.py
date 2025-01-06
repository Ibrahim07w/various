class Settings:
    def __init__(self):
        self.width = 800
        self.height = 400
        self.bgc = (230, 230, 230)
        self.speed = 1.5
        self.ship_limit = 3
        self.speedup_scale = 1.2

        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
        
        self.alien_speed = 1.0
        self.drop_speed = 25
        self.fleet_direction = 1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_point = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.speedup_scale)