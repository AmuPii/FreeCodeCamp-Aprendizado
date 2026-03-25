distance_mi = input("qual a distancia à percorrer em Milhas?")

is_raining = input("está chovendo? (sim/não)").lower() == "sim"
has_bike = input("tem bicicleta? (sim/não)").lower() == "sim"
has_car = input("tem carro? (sim/não)").lower() == "sim"
has_ride_share_app = input("tem app de transporte? (sim/não)").lower() == "sim"

if not distance_mi:                    
    print(False)
elif float(distance_mi) <= 1:          
    print(not is_raining)              
elif float(distance_mi) <= 6:          
    print(has_bike and not is_raining)
else:                                  
    print(has_car or has_ride_share_app)

