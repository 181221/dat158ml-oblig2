taxi = load_taxi_data()
csv_path = os.path.join(TAXI_PATH, "test.csv")
test_set = pd.read_csv(csv_path)

taxi_samples = taxi.sample(frac=0.10)

taxi.info()

taxi_samples.info()

taxi_samples.head()


data_labels = list(taxi_samples)
data_y = {'Duraton': taxi_samples.iloc[:,10]}

X = pd.DataFrame(data=taxi_samples.iloc[:, :-1].values, columns=data_labels[:10])
y = pd.DataFrame(data_y)
X.head()

y.head()


from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.3, random_state=42)

X_train['passenger_count'].hist()

import seaborn as sns
sns.heatmap(X_train.corr(), cmap='Blues')


#Pickup location for train dataset
import folium # goelogical map
newyork_map = folium.Map(location=[40.767937,-73.982155 ], tiles='OpenStreetMap', zoom_start=12)

def createMap(geo_map, data, i=10):
    for each in X_train[:i].iterrows():
    p1 = [each[1]['pickup_latitude'] ,each[1]['pickup_longitude']]
    p2 = [each[1]['dropoff_latitude'], each[1]['dropoff_longitude']]
    folium.CircleMarker(p1,
                        radius=3,
                        color='blue',
                        popup=str(each[1]['pickup_latitude'])+','+str(each[1]['pickup_longitude']),
                        fill_color='#FD8A6C'
                        ).add_to(geo_map)
    folium.CircleMarker(p2,
                        radius=3,
                        color='red',
                        popup=str(each[1]['dropoff_latitude'])+','+str(each[1]['dropoff_longitude']),
                        fill_color='#FD8A6C'
                        ).add_to(map_1)
    folium.PolyLine(locations=[p1, p2], color='green').add_to(geo_map)
    
createMap(newyork_map, X_train)

newyork_map


import mpu

def calculateDistances(data, distances):
    for each in data.iterrows():
        lat1 = float(each[1]['pickup_latitude'])
        lon1 = float(each[1]['pickup_longitude'])
        lat2 = float(each[1]['dropoff_latitude'])
        lon2 = float(each[1]['dropoff_longitude'])
        dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
        distances.append(dist)
        

distances = []
calculateDistances(X_train, distances)

distances = np.array(distances)
X_train['Distance'] = distances
X_train.head()









