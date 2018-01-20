import simplegui

# define global variables
time_passed = 0
A = 0
B = 0
C = 0
D = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global A, B, C, D, time_passed
    seconds = time_passed // 10
    A = seconds // 60
    B = (seconds % 60) // 10
    C = (seconds % 60) % 10
    D = time_passed % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

#helper function to determine score
def score():
    global x, y
    return str(x) + "/" + str(y)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global x, y, D
    if timer.is_running() == True:
        y += 1
        if D == 0:
            x += 1
    timer.stop()

def reset():
    global time_passed, x, y
    time_passed = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_passed
    time_passed += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(), [120, 160], 30, 'Red')
    canvas.draw_text(score(), [250, 30], 30, 'Blue')

# create frame
frame = simplegui.create_frame("timer", 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
