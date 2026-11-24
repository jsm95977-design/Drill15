world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_pair(o)
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()

def clear():
    for layer in world:
        layer.clear()

def collide(a,b):
    a.left, a.bottom, a.right, a.top = a.get_bb()
    b.left, b.bottom, b.right, b.top = b.get_bb()

    if a.left > b.right: return False
    if a.top < b.bottom: return False
    if a.right < b.left: return False
    if a.bottom > b.top: return False

    return True

collision_pairs = {}
def add_collision_pair(group, a, b):
    if group not in collision_pairs:    
        collision_pairs[group] = [[],[]] 

    if a: collision_pairs[group][0].append(a)
    if b: collision_pairs[group][1].append(b)

def handle_collisions():
    for group,pair in collision_pairs.items():
        for a in pair[0]:
            for b in pair[1]:
                if collide(a,b):
                    a.handle_collision(group,b)
                    b.handle_collision(group,a)

def remove_pair(o):
    for pair in collision_pairs.values():
        if o in pair[0]:
            pair[0].remove(o)
        if o in pair[1]:
            pair[1].remove(o)
