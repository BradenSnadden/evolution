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
best_tour = [283 ,228 ,403 ,178 ,289 ,339 ,70 ,360 ,200 ,222 ,405 ,424 ,370 ,270 ,358 ,100 ,206 ,227 ,423 ,174 ,36 ,113 ,28 ,204 ,299 ,131 ,433 ,382 ,372 ,78 ,421 ,420 ,65 ,295 ,300 ,340 ,301 ,67 ,132 ,320 ,29 ,323 ,103 ,16 ,177 ,57 ,55 ,107 ,50 ,85 ,33 ,354 ,89 ,383 ,224 ,243 ,385 ,43 ,73 ,60 ,95 ,240 ,80 ,109 ,197 ,225 ,61 ,316 ,333 ,437 ,40 ,302 ,428 ,399 ,386 ,201 ,94 ,192 ,64 ,39 ,130 ,337 ,117 ,294 ,37 ,63 ,164 ,409 ,397 ,162 ,167 ,155 ,21 ,139 ,338 ,25 ,236 ,171 ,121 ,101 ,216 ,390 ,82 ,373 ,308 ,105 ,235 ,282 ,429 ,147 ,180 ,436 ,321 ,149 ,136 ,268 ,275 ,129 ,5 ,330 ,159 ,68 ,247 ,198 ,356 ,238 ,35 ,127 ,53 ,264 ,284 ,213 ,9 ,26 ,96 ,254 ,369 ,34 ,303 ,11 ,52 ,310 ,145 ,347 ,47 ,115 ,440 ,187 ,163 ,97 ,165 ,191 ,309 ,248 ,314 ,217 ,426 ,190 ,281 ,202 ,255 ,379 ,352 ,371 ,407 ,62 ,210 ,135 ,151 ,169 ,161 ,124 ,304 ,311 ,355 ,199 ,363 ,185 ,266 ,418 ,214 ,230 ,75 ,357 ,315 ,209 ,76 ,7 ,86 ,229 ,259 ,376 ,332 ,140 ,434 ,6 ,146 ,313 ,410 ,120 ,116 ,252 ,91 ,143 ,381 ,170 ,274 ,419 ,142 ,317 ,342 ,344 ,378 ,336 ,431 ,111 ,1 ,184 ,319 ,368 ,249 ,119 ,183 ,404 ,22 ,359 ,223 ,288 ,269 ,19 ,327 ,306 ,2 ,325 ,211 ,366 ,3 ,231 ,257 ,125 ,110 ,88 ,273 ,188 ,387 ,392 ,138 ,233 ,181 ,114 ,20 ,329 ,435 ,312 ,251 ,108 ,218 ,362 ,389 ,205 ,15 ,175 ,215 ,267 ,27 ,265 ,322 ,219 ,160 ,148 ,221 ,343 ,287 ,326 ,66 ,417 ,377 ,393 ,144 ,90 ,176 ,106 ,411 ,226 ,123 ,402 ,13 ,58 ,152 ,253 ,92 ,194 ,168 ,241 ,56 ,81 ,51 ,87 ,400 ,203 ,239 ,285 ,324 ,153 ,83 ,246 ,133 ,59 ,401 ,193 ,72 ,42 ,32 ,438 ,220 ,258 ,263 ,48 ,207 ,196 ,49 ,365 ,18 ,361 ,335 ,126 ,118 ,374 ,158 ,271 ,256 ,297 ,8 ,425 ,427 ,278 ,128 ,104 ,12 ,71 ,351 ,157 ,38 ,244 ,24 ,46 ,234 ,237 ,172 ,413 ,350 ,293 ,291 ,17 ,10 ,345 ,262 ,166 ,331 ,305 ,334 ,41 ,154 ,272 ,277 ,292 ,341 ,364 ,14 ,245 ,173 ,408 ,346 ,391 ,260 ,416 ,141 ,179 ,394 ,189 ,261 ,422 ,375 ,328 ,439 ,134 ,186 ,232 ,398 ,77 ,298 ,349 ,414 ,182 ,102 ,137 ,367 ,84 ,242 ,99 ,156 ,432 ,212 ,79 ,44 ,54 ,31 ,122 ,412 ,406 ,45 ,348 ,318 ,69 ,395 ,279 ,112 ,208 ,384 ,442 ,441 ,280 ,250 ,307 ,296 ,388 ,430 ,150 ,30 ,74 ,396 ,276 ,4 ,195 ,93 ,98 ,23 ,353 ,286 ,415 ,290 ,380]  # Example tour for illustration

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

# Plot the best tour found by Algorithm #1
best_tour_x = [city_coordinates[city_id][0] for city_id in best_tour]
best_tour_y = [city_coordinates[city_id][1] for city_id in best_tour]
best_tour_x.append(best_tour_x[0])  # Connect the last city to the starting city
best_tour_y.append(best_tour_y[0])
plt.plot(best_tour_x, best_tour_y, marker='o', markersize=1, color='darkmagenta',linewidth=0.5, label='Algorithm #1')

# Set plot labels and legend
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('TSP Comparison: Algorithm #1 vs. Optimal Tour')
plt.legend()

# Show the plot
plt.show()