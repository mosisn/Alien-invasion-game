class Settings:
    def __init__(self) -> None:
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        self.ship_speed = 2.5

        self.bullet_speed = 4.5
        self.bullet_height = 15
        self.bullet_width = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1