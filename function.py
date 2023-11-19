def make_shrirt(size,message):
    print(f"this is {size.title()} size shirt with {message.title()} printed on it")

make_shrirt("medium","awesome")

def make_shrirt(size="Large",message="I Love Python"):
    print(f"this is {size.title()} size shirt with {message.title()} printed on it")

make_shrirt("small","Belive")

def city_country(city,country):
    country_city = f"{city},{country}"
    return country_city

city = city_country("Hyderabad","India")
print(city)
city = city_country("Delhi","India")
print(city)
city = city_country("Dhaka","Bangladesh")
print(city)

def make_album(artist_name,album_title,movie_name=''):
    music_album = {'artist': artist_name, 'album': album_title}
    if movie_name:
        music_album = {'artist' : artist_name,'album' : album_title,'movie': movie_name}
    return music_album

album = make_album("Arjit Singh","Aashique")
print(album)
album = make_album("Reshimiyya","Ashique banaya apne",'arya')
print(album)

# passing the list to the function
def show_message(messages):
    print("List of Mesaages are :")
    for message in messages:
        print(f"\t {message}")

mess = ['Belive in your self','Never Give Up','Work Hard']
show_message(mess)

def send_message(messages):
    new_messages = []
    while messages:
        current_message = messages.pop()
        print(current_message)
        new_messages.append(current_message)
    print(new_messages)
    print(messages)

mess = ['Belive in your self','Never Give Up','Work Hard']
send_message(mess[:])
