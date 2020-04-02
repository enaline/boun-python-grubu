import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def game_of_life(size, seed, ticks):
    np.random.seed(seed)   # seed is for pseudo-randomness
    array = np.random.randint(0, 2, size=(size, size))

    generational_array = np.zeros((ticks + 1, array.shape[0], array.shape[1]))  # initialization of final array
    generational_array[0, :, :] = array  # adding the initial array to final array
    a_placeholder = np.zeros((array.shape[0], array.shape[1]))  # initialization of placeholder array to store each tick
    for t in range(1, ticks):
        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                slice_matrix = array[max(0, i - 1):(i + 2), max(0, j - 1):(j + 2)]  # slicing for filtering neighbors
                if array[i, j] == 1:
                    if np.sum(slice_matrix) == 3 or np.sum(slice_matrix) == 4:  # sum of elements in slicing_matrix
                        a_placeholder[i, j] = 1
                    else:
                        a_placeholder[i, j] = 0
                else:
                    if np.sum(slice_matrix) == 3:
                        a_placeholder[i, j] = 1
                    else:
                        a_placeholder[i, j] = 0
        generational_array[t, :, :] = a_placeholder  # store array to its respective tick
        array = a_placeholder  # update array for following ticks
        a_placeholder = np.zeros((array.shape[0], array.shape[1]))  # reset placeholder array

    images = []  # empty array to hold plotted patches
    fig = plt.figure(figsize=(generational_array.shape[1], generational_array.shape[2]))  # base of plotting
    for i in range(0, len(generational_array)):  # for loop to plot patches
        im = plt.imshow(generational_array[i], cmap='Blues')  # used for plotting
        images.append([im])  # appending plotted patches
    ani = animation.ArtistAnimation(fig, images, interval=500)  # gif creation from plotted patches
    ani.save('game_of_life_full.gif', dpi=40, writer='imagemagick')  # saving the gif, imagemagick is tricky

    return generational_array


# game_of_life(10, 1, 100)
# game_of_life(10, 2, 100)
# game_of_life(20, 1, 100)
# game_of_life(20, 2, 100)
# game_of_life(30, 1, 100)
# game_of_life(30, 2, 100)
z = game_of_life(6, 1, 10)
print(z)
