# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user38_jtwUkJAB4Z_7.py
import simplegui

# define global variables
interval = 100
counter = 0
ticks = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t // 600
    B = t % 600 / 100
    C = t % 100 / 10
    D = t % 10
    return str(A) + ":" + str(B)+str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
   
def stop():
    timer.stop
    global wins, ticks, running
    if timer.is_running():
        timer.stop()
        ticks += 1
        if not counter % 50:
            wins += 1
    
def reset():
    global counter, wins, ticks
    timer.stop()
    counter = 0
    wins =0
    ticks =0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global counter
    counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (60,125), 40, "Blue")
    canvas.draw_text(str(wins) + "/" + str(ticks), [200,25], 15, "Yellow")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 250, 250)
timer = simplegui.create_timer(interval, time_handler)
frame.set_draw_handler(draw_handler)

# register event handlers
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)

# start frame
frame.start()

