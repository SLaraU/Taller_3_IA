from algorithms.probability import expected_utility, best_action

actions = {
    "monitorear":   {0: 0,   1: -100},
    "inspeccionar": {0: -8,  1: -25},
    "brigada":      {0: -30, 1: -5},
}

print(expected_utility({0: 0.9, 1: 0.1}, {0: -8, 1: -25}))  # ≈ -9.7

print(best_action({0: 0.9, 1: 0.1}, actions))         # inspeccionar
print(best_action({0: 1/3, 1: 2/3}, actions))         # brigada
print(best_action({0: 0.98844, 1: 0.01156}, actions)) # monitorear

# Empate: debe ganar "a"
print(best_action({0: 0.5, 1: 0.5}, {"a": {0: 1, 1: 1}, "b": {0: 1, 1: 1}}))