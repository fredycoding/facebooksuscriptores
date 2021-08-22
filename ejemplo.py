import facebook


token='AQUI VA EL TOKEN'
graph = facebook.GraphAPI(token)
profile = graph.get_object("NOMBRE DEL CANAL", fields='fan_count')
print("Fan Count: ", profile['fan_count'])
