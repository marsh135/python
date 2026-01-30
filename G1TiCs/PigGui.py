import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
WINNING_SCORE = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (100, 100, 100)
GREEN = (50, 200, 50)
RED = (200, 50, 50)
BLUE = (50, 100, 200)
YELLOW = (255, 200, 50)
GOLD = (255, 215, 0)

class Button:
    def __init__(self, x, y, width, height, text, color=BLUE, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.is_hovered = False

    def draw(self, surface, font):
        color = self.color if not self.is_hovered else tuple(min(c + 30, 255) for c in self.color)
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=5)
        
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)

class PigGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The Game of Pig")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        self.reset_game()
        
    def reset_game(self):
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.turn_total = 0
        self.last_roll = 0
        self.game_over = False
        self.winner = None
        self.message = ""
        self.message_timer = 0
        
        self.roll_button = Button(150, 550, 120, 60, "ROLL", GREEN)
        self.hold_button = Button(350, 550, 120, 60, "HOLD", YELLOW)
        self.restart_button = Button(400, 400, 200, 60, "Play Again")
        
    def roll_die(self):
        return random.randint(1, 6)
    
    def process_roll(self):
        if self.game_over:
            return
            
        die = self.roll_die()
        self.last_roll = die
        
        if die == 1:
            self.message = "You rolled a 1! No points for this turn."
            self.turn_total = 0
            self.message_timer = 120
            self.end_turn()
        else:
            self.turn_total += die
            self.message = f"You rolled a {die}! Turn total: {self.turn_total}"
            self.message_timer = 120
    
    def hold(self):
        if self.game_over:
            return
            
        if self.current_player == 1:
            self.player1_score += self.turn_total
            if self.player1_score >= WINNING_SCORE:
                self.game_over = True
                self.winner = 1
                self.message = "Player 1 WINS!"
                return
        else:
            self.player2_score += self.turn_total
            if self.player2_score >= WINNING_SCORE:
                self.game_over = True
                self.winner = 2
                self.message = "Player 2 WINS!"
                return
        
        self.message = f"Player {self.current_player} held and scored {self.turn_total} points!"
        self.message_timer = 120
        self.end_turn()
    
    def end_turn(self):
        self.turn_total = 0
        self.last_roll = 0
        self.current_player = 2 if self.current_player == 1 else 1
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if self.game_over:
                    if self.restart_button.is_clicked(pos):
                        self.reset_game()
                else:
                    if self.roll_button.is_clicked(pos):
                        self.process_roll()
                    elif self.hold_button.is_clicked(pos):
                        self.hold()
            
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if not self.game_over:
                    self.roll_button.update(pos)
                    self.hold_button.update(pos)
                else:
                    self.restart_button.update(pos)
        
        return True
    
    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        
        # Title
        title_surf = self.font_large.render("The Game of Pig", True, BLACK)
        self.screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, 20))
        
        # Player sections
        self.draw_player_section(1, 50)
        self.draw_player_section(2, 550)
        
        # Current turn info
        if not self.game_over:
            turn_text = self.font_medium.render(f"Player {self.current_player}'s Turn", True, BLUE)
            self.screen.blit(turn_text, (SCREEN_WIDTH // 2 - turn_text.get_width() // 2, 100))
            
            # Turn total
            turn_total_text = self.font_medium.render(f"Turn Total: {self.turn_total}", True, BLACK)
            self.screen.blit(turn_total_text, (SCREEN_WIDTH // 2 - turn_total_text.get_width() // 2, 150))
            
            # Last roll display
            if self.last_roll > 0:
                roll_text = self.font_medium.render(f"Last Roll: {self.last_roll}", True, RED)
                self.screen.blit(roll_text, (SCREEN_WIDTH // 2 - roll_text.get_width() // 2, 200))
        
        # Message
        if self.message_timer > 0:
            msg_surf = self.font_small.render(self.message, True, GOLD)
            self.screen.blit(msg_surf, (SCREEN_WIDTH // 2 - msg_surf.get_width() // 2, 250))
            self.message_timer -= 1
        
        # Buttons
        if self.game_over:
            pygame.draw.rect(self.screen, WHITE, (100, 300, 800, 200), border_radius=10)
            pygame.draw.rect(self.screen, BLACK, (100, 300, 800, 200), 3, border_radius=10)
            
            winner_text = self.font_large.render(f"Player {self.winner} WINS!", True, GOLD)
            self.screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, 320))
            
            final_scores = self.font_medium.render(
                f"Final Scores - Player 1: {self.player1_score}  Player 2: {self.player2_score}",
                True, BLACK
            )
            self.screen.blit(final_scores, (SCREEN_WIDTH // 2 - final_scores.get_width() // 2, 380))
            
            self.restart_button.draw(self.screen, self.font_small)
        else:
            self.roll_button.draw(self.screen, self.font_small)
            self.hold_button.draw(self.screen, self.font_small)
        
        pygame.display.flip()
    
    def draw_player_section(self, player_num, y):
        # Background box
        pygame.draw.rect(self.screen, WHITE, (30, y, 940, 100), border_radius=10)
        pygame.draw.rect(self.screen, BLACK, (30, y, 940, 100), 2, border_radius=10)
        
        # Highlight current player
        if not self.game_over and self.current_player == player_num:
            pygame.draw.rect(self.screen, YELLOW, (30, y, 940, 100), 5, border_radius=10)
        
        # Player label
        label_surf = self.font_medium.render(f"Player {player_num}", True, BLUE)
        self.screen.blit(label_surf, (50, y + 10))
        
        # Score
        if player_num == 1:
            score = self.player1_score
        else:
            score = self.player2_score
        
        score_surf = self.font_large.render(str(score), True, BLACK)
        self.screen.blit(score_surf, (800, y + 20))
        
        score_label = self.font_small.render("Score", True, DARK_GRAY)
        self.screen.blit(score_label, (800, y + 60))
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PigGame()
    game.run()