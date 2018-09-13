def create_cast_list(filename):
    cast_list = []

    with open(filename) as f:
        for actor in f:
            actor_data = actor.split(',')
            cast_list.append(actor_data[0])

    return cast_list

print(create_cast_list('flying_circus_cast.txt'))
