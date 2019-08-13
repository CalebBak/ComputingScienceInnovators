import time

from uagame import Window

#def writeString(string, window, x, y):
    #"""
    #Write a string to the window at position. Returns y incremented by one
    #"""
    #window.draw_string(string, x, y)
    #window.update()
    #return y + 1

def main():
    # create window
    window = Window("Hacking", 800, 600)
    window.set_font_color("green")
    window.set_font_name("couriernew")
    window.set_bg_color("black")
    window.set_font_size(12)
    
    # initialize variables
    line_y = 0
    string_height = window.get_font_height()
    attempts = 2
    
    while attempts > 1:
        # display remaining attempts
        window.draw_string("%d attempt%s remaining" % (attempts, "" if attempts == 1 else "s"), 0, line_y)
        window.update()
        time.sleep(0.5)
        line_y += string_height
        
        # display password list (similar to above, copy/paste for each password)
        window.draw_string("PASSWORD", 0, line_y)
        window.update()
        line_y += string_height
        time.sleep(0.5)
        
        window.draw_string("ADMIN", 0, line_y)
        window.update()
        line_y += string_height
        time.sleep(0.5)
        
        
        # prompt user for password
        guess = window.input_string("Enter a password: ", 0, line_y)
        
        
        # create outcome
        if guess == "PASSWORD":
            window.clear()
            # Every character should have the same width in this font
            window.draw_string("SUCCESS!", 0, 0)
        else:
            window.clear()
            window.draw_string("FAILURE", 0, 0)
        window.update()
    
    time.sleep(2)
    
    # clear window
    window.clear()
    
    # prompt for end
    window.input_string("Press 'Enter' to exit game", 0, 0)
    
    # close window
    window.close()

if __name__ == "__main__":
    main()
