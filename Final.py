
import pygame , time


# screen saver class
class ScreenSaver:

    # constructer
    def __init__(self , screen):
        
        self.screen = screen

    # a method for create first logo
    def create_logo_one(self):

        logo_speed = [10,10]
        logo = pygame.image.load('circle.png')
        logo = pygame.transform.scale(logo , (40,40))
        logo_rect = logo.get_rect()

        return logo , logo_rect , logo_speed

    # a method for create seccond logo
    def create_logo_seccond(self):

        logo_speed_two = [5,5]
        logo_two = pygame.image.load('square.png')
        logo_two = pygame.transform.scale(logo_two , (40,40))
        logo_rect_two = logo_two.get_rect()
        
        return logo_two , logo_rect_two , logo_speed_two


    # a method for create third logo
    def create_logo_third(self):

        logo_speed_three = [7,2]
        logo_three = pygame.image.load('triangle.png')
        logo_three = pygame.transform.scale(logo_three , (40,40))
        logo_rect_three = logo_three.get_rect()
        
        return logo_three , logo_rect_three , logo_speed_three
    



# Check Not In Another Function
def check(logo_rect , logo_rect_two , logo_speed_two , logo_speed):

    if  logo_rect.left - 50 < logo_rect_two.left < logo_rect.left + 50:

            if logo_rect.right - 50 < logo_rect_two.right < logo_rect.right + 50:

                if logo_rect.top - 50 < logo_rect_two.top < logo_rect.top + 50 :

                    if logo_rect.bottom - 50 < logo_rect_two.bottom < logo_rect.bottom + 50:

                        logo_speed_two[0] = -logo_speed_two[0]

                        logo_speed_two[1] = -logo_speed_two[1]

                        logo_speed[0] = -logo_speed[0]

# Main Function
def main():

    pygame.init()

    screenwidth , screenheight = 800 , 600
    background_color = 0,0,0
    screen = pygame.display.set_mode((screenwidth , screenheight))

    bot = ScreenSaver(screen)

    # first logo
    logo , logo_rect , logo_speed = bot.create_logo_one()

    # seccond logo
    logo_two , logo_rect_two , logo_speed_two = bot.create_logo_seccond()

    # third logo
    logo_three , logo_rect_three , logo_speed_three = bot.create_logo_third()

    # four logo
    logo_four , logo_rect_four , logo_speed_four  = bot.create_logo_one()


    while True : 

        screen.fill(background_color)

        # first logo
        screen.blit(logo , logo_rect)
        logo_rect = logo_rect.move(logo_speed)

        # seccond logo
        screen.blit(logo_two , logo_rect_two)
        logo_rect_two = logo_rect_two.move(logo_speed_two)


        # third logo
        screen.blit(logo_three , logo_rect_three)
        logo_rect_three = logo_rect_three.move(logo_speed_three)

        # four logo
        screen.blit(logo_four , logo_rect_four)
        logo_rect_four = logo_rect_four.move(logo_speed_four)


         # FOR LOGO ONE
        if logo_rect.left < 0 or logo_rect.right > screenwidth : 

            logo_speed[0] = -logo_speed[0]

        if logo_rect.top < 0 or logo_rect.bottom > screenheight :

            logo_speed[1] = -logo_speed[1]

        # FOR LOGO TWO
        if logo_rect_two.left < 0 or logo_rect_two.right > screenwidth : 

            logo_speed_two[0] = -logo_speed_two[0]

        if logo_rect_two.top < 0 or logo_rect_two.bottom > screenheight :

            logo_speed_two[1] = -logo_speed_two[1]

        # FOR LOGO THREE
        if logo_rect_three.left < 0 or logo_rect_three.right > screenwidth : 

            logo_speed_three[0] = -logo_speed_three[0]

        if logo_rect_three.top < 0 or logo_rect_three.bottom > screenheight :

            logo_speed_three[1] = -logo_speed_three[1]

        # FOR LOGO FOUR
        if logo_rect_four.left < 0 or logo_rect_four.right > screenwidth : 

            logo_speed_four[0] = -logo_speed_four[0]

        if logo_rect_four.top < 0 or logo_rect_four.bottom > screenheight :

            logo_speed_four[1] = -logo_speed_four[1]
        


        # FOR LOGO ONE AND TWO
        check(logo_rect , logo_rect_two ,logo_speed_two ,logo_speed)
        
        # FOR LOGO ONE AND THREE
        check(logo_rect , logo_rect_three ,logo_speed_two ,logo_speed_three)

        # FOR LOGO ONE AND FOUR
        check(logo_rect , logo_rect_four ,logo_speed_two ,logo_speed_four)

        # FOR LOGO TWO AND THREE
        check(logo_rect_two , logo_rect_three ,logo_speed_three ,logo_speed_two)

        # FOR LOGO TWO AND FOUR
        check(logo_rect_two , logo_rect_four ,logo_speed_three ,logo_speed_four)

        # FOR LOGO THREE AND FOUR
        check(logo_rect_three , logo_rect_four ,logo_speed_three ,logo_speed_four)


        pygame.display.flip()

        time.sleep(10/1000)


if __name__ == '__main__':main()