
import tkinter

MARGIN = 10
GRAPH_WIDTH = 300
GRAPH_HEIGHT = 300

def main():

    name = str(input("Please enter your name: "))



    orig_weight = float(input("Please enter your start weight: "))


    new_weight = float(input("Please enter your current weight: "))

    with open("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + ".txt", "a") as file:
        file.write(str(orig_weight)+"\n"+str(new_weight)+"\n")




    list_of_weights = read_list(name)

    graph_canvas = create_graph_canvas(GRAPH_WIDTH, GRAPH_HEIGHT, "Progress!")

    plot_points(list_of_weights, graph_canvas)


    tkinter.mainloop()



def get_point(graph_width,graph_height, list, x, y):

    scale_y = -(graph_height/200)
    scale_x = (graph_width/ len(list))

    new_x = (scale_x * x)
    new_y = (scale_y * y) + graph_height

    point = {"x":new_x, "y":new_y}
    return point


def plot_points(figures, canvas):

    points = []
    graph_width = GRAPH_WIDTH
    graph_height = GRAPH_HEIGHT

    for index, value in enumerate(figures):
        point = get_point(graph_width, graph_height, figures, index, value)
        points.append(point)

    previous_point = points [0]

    for point in points:
        canvas.create_line(MARGIN+previous_point["x"], MARGIN+previous_point["y"], MARGIN+point["x"], MARGIN+point["y"])
        previous_point = point



def create_graph_canvas(width, height, title):

    """
    Creates a background for the graph image
    width/height = size of graph

    """
    window = tkinter.Tk()
    window.minsize(width=width, height=height)
    window.title(title)
    graph_canvas = tkinter.Canvas(window, width=width + (MARGIN*2), height=height + (MARGIN*2), bg='white')
    graph_canvas.pack(expand="yes", fill="both")

    graph_canvas.create_line(MARGIN, MARGIN, MARGIN, height + MARGIN)
    graph_canvas.create_line(MARGIN, height + MARGIN, width + MARGIN, height + MARGIN)

    return graph_canvas


def read_list(name):
    mylist = []
    with open ("D:/UserFiles/Desktop/Code In Place/Final Project/profiles/" + name + ".txt", "r") as file:
        for line in file:
            line = float(line.strip())
            mylist.append(line)

    return mylist





    ##draw lines
    ##label lines
    ##plot x axis time ideally but in this case just each time they log
    ##plot y axis = weight
    ##plot points on graph
    ##animate the points joining:

if __name__ == '__main__':
    main()
