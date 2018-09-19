import facebook

graph = facebook.GraphAPI(access_token="EAAcAZBcJBsTkBALdSZA7jnnJasFhqspDtk7lVjtLaY28fTIm4lj6C25q"
                                       "SloMNh6JloWZBygvZCahYF2ZAOaoMudtkaYSZCjJoZAvqdiizJZByO9gaZ"
                                       "C7ZCw6RBDHhiZAWgeef2YKnWSmEMAH9YAqjcxUJjBHXjVnhgqtKWxbApo8f"
                                       "P9zWJq6zvZB8GGxOPY7AKBuwNYZD", version="3.0")

with open('id.txt', 'r', encoding='utf-8') as mf, open('id_message.txt', 'w', encoding='utf-8') as mf_new:
    for line in mf.readlines():
        id = line.strip()
        comments = graph.get_connections(id=id, connection_name='comments')
        # if post != 0:
        #     mf_new.write(post['message'])
        print(comments)

