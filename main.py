import turtle
import pandas
screen = turtle.Screen()
screen.title("Indian States and Union Territories")
image = "blank_states_image.gif"
screen.addshape(image)
turtle.shape(image)
# for getting co-ordinates of each state on map
#
#
# def get_mouse_click_coor(x, y):
#     print(f"{x},{y}")
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()    # another way of keeping screen open
data = pandas.read_csv("28_states_8_union_territories.csv")
all_regions = data.region.to_list()
guessed = []
while len(guessed) < 36:
    answer = screen.textinput(f"{len(guessed)}/36 regions guessed", "What is the state or ut?").title()
    if answer == "Exit":
        missing_regions = [region for region in all_regions if region not in guessed]    # List Comprehension
        new_data = pandas.DataFrame(missing_regions)
        new_data.to_csv("regions_to_learn.csv")
        break
    if answer in all_regions and answer not in guessed:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        region_data = data[data.region == answer]
        t.goto(int(region_data.x.iloc[0]), int(region_data.y.iloc[0]))
        t.write(region_data.region.item())    # item() gets first element in underlying data
