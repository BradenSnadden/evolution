import numpy as np
import matplotlib.pyplot as plt

# Function to read the optimal tour from a file
def read_optimal_tour(file_path):
    optimal_tour = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            city_id = int(line.strip())
            optimal_tour.append(city_id)
    return optimal_tour

# Read city coordinates from a file
city_coordinates_file = "pcb442.tsp"  # Replace with the path to your TSP file
with open(city_coordinates_file, "r") as file:
    lines = file.readlines()

city_coordinates = {}
for line in lines:
    parts = line.strip().split()
    if len(parts) == 3 and parts[0].isdigit():
        city_id = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
        city_coordinates[city_id] = (x, y)

# Read the best tour found by the Inver-Over algorithm
# Replace this with the best tour you obtained from your algorithm
best_tour = [141, 389, 387, 130, 119, 108, 384, 120, 390, 142, 155, 143, 156, 167, 180, 195, 194, 193, 204, 205, 206, 216, 192, 191, 203, 215, 224, 232, 255, 256, 257, 418, 259, 258, 421, 304, 303, 302, 327, 328, 344, 329, 305, 330, 331, 332, 431, 333, 426, 436, 274, 422, 419, 271, 437, 301, 300, 299, 324, 325, 326, 430, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 337, 336, 335, 334, 306, 267, 415, 263, 262, 235, 261, 260, 411, 407, 408, 403, 412, 217, 207, 196, 181, 182, 197, 208, 218, 413, 236, 264, 409, 410, 225, 219, 209, 198, 183, 170, 159, 147, 169, 158, 146, 168, 157, 145, 132, 122, 110, 90, 91, 26, 25, 58, 59, 27, 28, 29, 30, 375, 376, 32, 31, 64, 95, 63, 62, 61, 60, 93, 92, 100, 435, 94, 378, 379, 96, 97, 383, 382, 112, 124, 134, 111, 123, 133, 144, 131, 121, 109, 89, 57, 88, 55, 54, 86, 85, 84, 83, 380, 381, 377, 87, 56, 24, 23, 22, 21, 20, 19, 53, 52, 51, 18, 17, 50, 49, 48, 16, 15, 14, 13, 12, 11, 10, 43, 9, 8, 41, 40, 7, 6, 5, 38, 70, 39, 71, 72, 73, 42, 74, 75, 76, 44, 45, 46, 47, 78, 77, 98, 104, 105, 106, 99, 79, 80, 81, 82, 438, 107, 118, 129, 117, 128, 140, 139, 138, 127, 116, 115, 388, 150, 161, 149, 136, 386, 114, 440, 103, 67, 66, 34, 2, 3, 4, 37, 69, 68, 36, 35, 1, 0, 441, 33, 65, 101, 102, 113, 385, 126, 125, 135, 148, 160, 171, 184, 399, 404, 226, 233, 237, 265, 268, 269, 238, 405, 400, 185, 172, 173, 395, 398, 186, 210, 220, 228, 211, 402, 174, 151, 391, 137, 392, 152, 162, 175, 187, 163, 153, 164, 176, 188, 201, 401, 213, 200, 396, 199, 212, 221, 229, 245, 244, 243, 423, 287, 313, 312, 286, 311, 285, 284, 310, 309, 283, 282, 279, 425, 242, 241, 240, 406, 227, 234, 239, 266, 270, 273, 276, 272, 275, 278, 280, 340, 341, 427, 281, 439, 307, 308, 338, 345, 346, 347, 432, 348, 349, 339, 350, 351, 342, 352, 353, 354, 433, 355, 356, 357, 434, 358, 429, 359, 360, 343, 428, 298, 297, 323, 322, 296, 277, 295, 321, 320, 294, 293, 319, 318, 292, 291, 317, 316, 290, 289, 315, 314, 288, 424, 420, 246, 247, 248, 414, 249, 250, 230, 222, 251, 416, 417, 252, 253, 254, 231, 223, 214, 202, 189, 190, 397, 178, 177, 165, 394, 179, 166, 393, 154]  # Example tour for illustration

# Read the optimal tour for pcb442.tsp
optimal_tour_file = "OptTour.txt"  # Replace with the path to your optimal tour file
optimal_tour = read_optimal_tour(optimal_tour_file)

# Plot the city locations (Not Needed)
# x_coords = [city_coordinates[city_id][0] for city_id in range(1, len(city_coordinates))]
# y_coords = [city_coordinates[city_id][1] for city_id in range(1, len(city_coordinates))]
# plt.scatter(x_coords, y_coords, s=15, color='seagreen', label='Cities')

# Plot the optimal tour for pcb442.tsp
optimal_tour_x = [city_coordinates[city_id][0] for city_id in optimal_tour]
optimal_tour_y = [city_coordinates[city_id][1] for city_id in optimal_tour]
optimal_tour_x.append(optimal_tour_x[0])  # Connect the last city to the starting city
optimal_tour_y.append(optimal_tour_y[0])
plt.plot(optimal_tour_x, optimal_tour_y, marker='o', markersize=1.5, color='cornflowerblue', label='Optimal Tour')

# Plot the best tour found by the Inver-Over algorithm
best_tour_x = [city_coordinates[city_id][0] for city_id in range(1, len(best_tour))]
best_tour_y = [city_coordinates[city_id][1] for city_id in range(1, len(best_tour))]
best_tour_x.append(best_tour_x[0])  # Connect the last city to the starting city
best_tour_y.append(best_tour_y[0])
plt.plot(best_tour_x, best_tour_y, marker='o', markersize=1, color='darkorange',linewidth=1, label='Inver-Over Best Tour')

# Set plot labels and legend
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('TSP Comparison: Inver-Over Best Tour vs. Optimal Tour')
plt.legend()

# Show the plot
plt.show()