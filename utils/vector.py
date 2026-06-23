from pygame.math import Vector2

def limit(vector, max_value):
    if vector.length() > max_value:
        vector.scale_to_length(max_value)
    return vector