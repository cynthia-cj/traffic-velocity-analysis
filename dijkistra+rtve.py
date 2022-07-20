import sys
import pandas as pd
data=pd.read_csv("C&N-MANHATTAN_updated.csv")
#objID=data['Region ID'].tolist()
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V,
        there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path,pickup_nodes,dropoff_nodes,start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    #print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    #print(" -> ".join(reversed(path)))
    path.reverse()
    return path
    #print(path)
    '''
    start_end=path[0]+','+path[-1]
    for i in range(0,len(pickup_nodes)):
        path_dict[start_end]=[]
    path_dict[start_end]=path
    print(path_dict)
    '''    
    
    

#nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
objID = data['Region ID'].tolist()
for i in range(0,len(objID)):
    objID[i]=str(objID[i])
print(objID)
#init_graph={153: {}, 127: {128: 0.57061681}, 128: {127: 0.57061681}, 243: {127: 2.23354958, 128: 1.871803926, 120: 0.789295102, 244: 0.778762051}, 120: {127: 1.632750351, 244: 1.328343302, 42: 0.855748682}, 244: {120: 1.328343302, 116: 0.949165557}, 116: {244: 0.949165557, 152: 0.652663211, 42: 1.518839206}, 152: {116: 0.652663211, 42: 2.129230627, 166: 0.876229483}, 42: {120: 0.855748682, 116: 1.518839206, 152: 2.129230627, 41: 1.659665728, 74: 0.752155127}, 166: {152: 0.876229483, 41: 1.467224965, 24: 0.516563281}, 41: {42: 1.659665728, 166: 1.467224965, 74: 1.841940212, 24: 1.908808766, 75: 1.072454057, 43: 1.893719216}, 74: {42: 0.752155127, 41: 1.841940212, 75: 1.008879625}, 24: {166: 0.516563281, 151: 0.379850781, 43: 0.672747826}, 151: {24: 0.379850781, 238: 0.401932377, 43: 0.743548419}, 75: {41: 1.072454057, 74: 1.008879625, 43: 2.745290819, 236: 1.714428393, 263: 0.9676856, 262: 0.353001684}, 238: {151: 0.401932377, 239: 1.038804566, 43: 0.905482208}, 239: {238: 1.038804566, 143: 0.808808909, 142: 0.424776448, 43: 1.856639868}, 143: {239: 0.808808909, 142: 0.877859227, 50: 0.864562981}, 142: {239: 0.424776448, 143: 0.877859227, 43: 1.784337547, 48: 0.987386783}, 43: {41: 1.893719216, 24: 0.672747826, 151: 0.743548419, 75: 2.745290819, 238: 0.905482208, 239: 1.856639868, 142: 1.784337547, 236: 1.041418012, 237: 0.411360028, 163: 1.448410859}, 236: {75: 1.714428393, 43: 1.041418012, 263: 0.772601069, 237: 1.015246199, 141: 0.558407954}, 263: {75: 0.9676856, 236: 0.772601069, 262: 0.746371937, 141: 1.176796651}, 262: {75: 0.353001684, 263: 0.746371937, 140: 1.430814307}, 237: {43: 0.411360028, 236: 1.015246199, 141: 0.623623414, 163: 1.458355385}, 141: {236: 0.558407954, 263: 1.176796651, 237: 0.623623414, 140: 0.491272133, 229: 0.553559177}, 140: {262: 1.430814307, 141: 0.491272133, 229: 0.984424012}, 202: {}, 50: {143: 0.864562981, 48: 0.773946522, 246: 1.301641977}, 48: {142: 0.987386783, 50: 0.773946522, 230: 0.717165657, 163: 1.338997121, 246: 1.961901418, 68: 1.162850323, 100: 0.33349863}, 230: {163: 0.644279379, 100: 0.52542821}, 163: {43: 1.448410859, 237: 1.458355385, 230: 0.644279379}, 161: {230: 0.776417301, 163: 0.286200079, 164: 0.869939744, 170: 0.332850699}, 162: {237: 0.856220785, 163: 0.736216213, 229: 0.927720686, 170: 0.689766532, 233: 0.462876179}, 229: {141: 0.553559177, 140: 0.984424012, 233: 0.655406975}, 246: {50: 1.301641977, 48: 1.961901418, 158: 0.483166619}, 68: {48: 1.162850323, 246: 0.842284374, 100: 1.325642529, 186: 0.951232502, 90: 0.458001574, 158: 1.157947263, 249: 0.524252799}, 100: {230: 0.52542821, 68: 1.325642529, 186: 0.39365868, 164: 0.465694503}, 186: {68: 0.951232502, 100: 0.39365868, 90: 0.567516684, 164: 0.80632758, 234: 0.352228548}, 90: {68: 0.458001574, 186: 0.567516684, 234: 0.74555897, 249: 0.745340558}, 164: {100: 0.465694503, 186: 0.80632758, 170: 0.717337117, 234: 0.662046472}, 170: {164: 0.717337117, 233: 0.972432621, 107: 0.741094789, 137: 0.578769834}, 233: {229: 0.655406975, 170: 0.972432621, 137: 0.539303266}, 234: {186: 0.352228548, 90: 0.74555897, 164: 0.662046472, 107: 0.656656916, 113: 0.506456956}, 107: {170: 0.741094789, 234: 0.656656916}, 137: {170: 0.578769834, 233: 0.539303266, 107: 1.162314985, 224: 0.200247694}, 158: {246: 0.483166619, 68: 1.157947263, 249: 0.828769279, 125: 0.383201938}, 249: {68: 0.524252799, 90: 0.745340558, 158: 0.828769279, 113: 0.989004863, 114: 0.706060794, 125: 0.69407917}, 113: {234: 0.506456956, 249: 0.989004863, 114: 0.333839335, 79: 0.872343963}, 114: {249: 0.706060794, 113: 0.333839335, 79: 1.165316508, 211: 0.594743743, 144: 0.206812372}, 224: {107: 1.116707325, 137: 0.200247694, 79: 1.360546658, 4: 0.257939776}, 79: {107: 0.392320645, 113: 0.872343963, 114: 1.165316508, 224: 1.360546658, 4: 1.257194097, 148: 0.587055692}, 4: {224: 0.257939776, 79: 1.257194097, 232: 0.916972809}, 125: {158: 0.383201938, 249: 0.69407917, 211: 0.750991381, 231: 0.237330556}, 211: {114: 0.594743743, 125: 0.750991381, 144: 0.618209327, 231: 0.866902949}, 144: {114: 0.206812372, 211: 0.618209327, 148: 0.612403195, 231: 1.469770854, 45: 0.326205477}, 148: {79: 0.587055692, 144: 0.612403195, 232: 0.93002779, 45: 0.786840474}, 232: {4: 0.916972809, 148: 0.93002779, 45: 1.679627818}, 231: {125: 0.237330556, 211: 0.866902949, 144: 1.469770854, 45: 1.334312913, 209: 0.906468007, 13: 0.876809868, 261: 0.574365766}, 45: {148: 0.786840474, 232: 1.679627818, 231: 1.334312913, 209: 0.479701503}, 209: {231: 0.906468007, 45: 0.479701503, 87: 0.381798653}, 13: {231: 0.876809868, 261: 0.376494064, 12: 0.304267091}, 261: {231: 0.574365766, 13: 0.376494064, 87: 0.941670575, 12: 0.233645158, 88: 0.306945803}, 87: {209: 0.381798653, 261: 0.941670575, 88: 0.703676244}, 12: {13: 0.304267091, 261: 0.233645158, 88: 0.40849985}, 88: {261: 0.306945803, 87: 0.703676244, 12: 0.40849985}}
#init_graph = {'153': {}, '127': {'128': 0.57061681}, '128': {'127': 0.57061681}, '243': {'127': 2.23354958, '128': 1.871803926, '120': 0.789295102, '244': 0.778762051}, '120': {'127': 1.632750351, '244': 1.328343302, '42': 0.855748682}, '244': {'120': 1.328343302, '116': 0.949165557}, '116': {'244': 0.949165557, '152': 0.652663211, '42': 1.518839206}, '152': {'116': 0.652663211, '42': 2.129230627, '166': 0.876229483}, '42': {'120': 0.855748682, '116': 1.518839206, '152': 2.129230627, '41': 1.659665728, '74': 0.752155127}, '166': {'152': 0.876229483, '41': 1.467224965, '24': 0.516563281}, '41': {'42': 1.659665728, '166': 1.467224965, '74': 1.841940212, '24': 1.908808766, '75': 1.072454057, '43': 1.893719216}, '74': {'42': 0.752155127, '41': 1.841940212, '75': 1.008879625}, '24': {'166': 0.516563281, '151': 0.379850781, '43': 0.672747826}, '151': {'24': 0.379850781, '238': 0.401932377, '43': 0.743548419}, '75': {'41': 1.072454057, '74': 1.008879625, '43': 2.745290819, '236': 1.714428393, '263': 0.9676856, '262': 0.353001684}, '238': {'151': 0.401932377, '239': 1.038804566, '43': 0.905482208}, '239': {'238': 1.038804566, '143': 0.808808909, '142': 0.424776448, '43': 1.856639868}, '143': {'239': 0.808808909, '142': 0.877859227, '50': 0.864562981}, '142': {'239': 0.424776448, '143': 0.877859227, '43': 1.784337547, '48': 0.987386783}, '43': {'41': 1.893719216, '24': 0.672747826, '151': 0.743548419, '75': 2.745290819, '238': 0.905482208, '239': 1.856639868, '142': 1.784337547, '236': 1.041418012, '237': 0.411360028, '163': 1.448410859}, '236': {'75': 1.714428393, '43': 1.041418012, '263': 0.772601069, '237': 1.015246199, '141': 0.558407954}, '263': {'75': 0.9676856, '236': 0.772601069, '262': 0.746371937, '141': 1.176796651}, '262': {'75': 0.353001684, '263': 0.746371937, '140': 1.430814307}, '237': {'43': 0.411360028, '236': 1.015246199, '141': 0.623623414, '163': 1.458355385}, '141': {'236': 0.558407954, '263': 1.176796651, '237': 0.623623414, '140': 0.491272133, '229': 0.553559177}, '140': {'262': 1.430814307, '141': 0.491272133, '229': 0.984424012}, '202': {}, '50': {'143': 0.864562981, '48': 0.773946522, '246': 1.301641977}, '48': {'142': 0.987386783, '50': 0.773946522, '230': 0.717165657, '163': 1.338997121, '246': 1.961901418, '68': 1.162850323, '100': 0.33349863}, '230': {'163': 0.644279379, '100': 0.52542821}, '163': {'43': 1.448410859, '237': 1.458355385, '230': 0.644279379}, '161': {'230': 0.776417301, '163': 0.286200079, '164': 0.869939744, '170': 0.332850699}, '162': {'237': 0.856220785, '163': 0.736216213, '229': 0.927720686, '170': 0.689766532, '233': 0.462876179}, '229': {'141': 0.553559177, '140': 0.984424012, '233': 0.655406975}, '246': {'50': 1.301641977, '48': 1.961901418, '158': 0.483166619}, '68': {'48': 1.162850323, '246': 0.842284374, '100': 1.325642529, '186': 0.951232502, '90': 0.458001574, '158': 1.157947263, '249': 0.524252799}, '100': {'230': 0.52542821, '68': 1.325642529, '186': 0.39365868, '164': 0.465694503}, '186': {'68': 0.951232502, '100': 0.39365868, '90': 0.567516684, '164': 0.80632758, '234': 0.352228548}, '90': {'68': 0.458001574, '186': 0.567516684, '234': 0.74555897, '249': 0.745340558}, '164': {'100': 0.465694503, '186': 0.80632758, '170': 0.717337117, '234': 0.662046472}, '170': {'164': 0.717337117, '233': 0.972432621, '107': 0.741094789, '137': 0.578769834}, '233': {'229': 0.655406975, '170': 0.972432621, '137': 0.539303266}, '234': {'186': 0.352228548, '90': 0.74555897, '164': 0.662046472, '107': 0.656656916, '113': 0.506456956}, '107': {'170': 0.741094789, '234': 0.656656916}, '137': {'170': 0.578769834, '233': 0.539303266, '107': 1.162314985, '224': 0.200247694}, '158': {'246': 0.483166619, '68': 1.157947263, '249': 0.828769279, '125': 0.383201938}, '249': {'68': 0.524252799, '90': 0.745340558, '158': 0.828769279, '113': 0.989004863, '114': 0.706060794, '125': 0.69407917}, '113': {'234': 0.506456956, '249': 0.989004863, '114': 0.333839335, '79': 0.872343963}, '114': {'249': 0.706060794, '113': 0.333839335, '79': 1.165316508, '211': 0.594743743, '144': 0.206812372}, '224': {'107': 1.116707325, '137': 0.200247694, '79': 1.360546658, '4': 0.257939776}, '79': {'107': 0.392320645, '113': 0.872343963, '114': 1.165316508, '224': 1.360546658, '4': 1.257194097, '148': 0.587055692}, '4': {'224': 0.257939776, '79': 1.257194097, '232': 0.916972809}, '125': {'158': 0.383201938, '249': 0.69407917, '211': 0.750991381, '231': 0.237330556}, '211': {'114': 0.594743743, '125': 0.750991381, '144': 0.618209327, '231': 0.866902949}, '144': {'114': 0.206812372, '211': 0.618209327, '148': 0.612403195, '231': 1.469770854, '45': 0.326205477}, '148': {'79': 0.587055692, '144': 0.612403195, '232': 0.93002779, '45': 0.786840474}, '232': {'4': 0.916972809, '148': 0.93002779, '45': 1.679627818}, '231': {'125': 0.237330556, '211': 0.866902949, '144': 1.469770854, '45': 1.334312913, '209': 0.906468007, '13': 0.876809868, '261': 0.574365766}, '45': {'148': 0.786840474, '232': 1.679627818, '231': 1.334312913, '209': 0.479701503}, '209': {'231': 0.906468007, '45': 0.479701503, '87': 0.381798653}, '13': {'231': 0.876809868, '261': 0.376494064, '12': 0.304267091}, '261': {'231': 0.574365766, '13': 0.376494064, '87': 0.941670575, '12': 0.233645158, '88': 0.306945803}, '87': {'209': 0.381798653, '261': 0.941670575, '88': 0.703676244}, '12': {'13': 0.304267091, '261': 0.233645158, '88': 0.40849985}, '88': {'261': 0.306945803, '87': 0.703676244, '12': 0.40849985}}

outer_dict={}
dist_lst1=[]
neighbors_graph=[]
dist_file=open('taxi_neighborDistances.csv','r')
dist_data=dist_file.read()
dist_lst1=dist_data.split(",")
for i in dist_lst1:
    dist_lst1=[float(j) for j in dist_lst1]
#print(dist_lst1)
k=0
for i in range(0,len(dist_lst1),3):
    dist_lst2=[]
    for j in range(0,3):
        dist_lst2.append(dist_lst1[k])
        k+=1
    neighbors_graph.append(dist_lst2)
   
for i in neighbors_graph:
    i[0]=int(i[0])
    i[1]=int(i[1])

for i in neighbors_graph:
    i[0]=str(i[0])
    i[1]=str(i[1])


#print(neighbors_graph)
#dist_lst2.append(dist_lst1)
#print(dist_lst2)

#print(len(dist_lst))
#print(len(neighbors_graph))

for id_ in objID:
    outer_dict[id_]={}
#print(objID)


for i in neighbors_graph:
    outer_dict[i[0]][i[1]]=i[2]
#print(outer_dict)

init_graph=outer_dict

'''
init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2
'''

clean_data=pd.read_csv("yellow_clean_final.csv")
#clean_data=clean_data.head(10000)
clean_data=clean_data[(clean_data['tpep_pickup_datetime']>= "1/1/2019 16:00") & (clean_data['tpep_pickup_datetime']<= "1/31/2019 19:00")]
clean_data=clean_data[(clean_data['tpep_dropoff_datetime']>= "1/1/2019 16:00") & (clean_data['tpep_dropoff_datetime']<= "1/31/2019 19:00")]
#print(clean_data)
clean_data.to_csv('temporal_clean_data.csv')
clean_data=clean_data.head(10000)
pickup_nodes=[]
dropoff_nodes=[]
pickup_nodes=clean_data["PULocationID"].tolist()
dropoff_nodes=clean_data["DOLocationID"].tolist()
for i in range(0,len(pickup_nodes)):
    pickup_nodes[i]=str(pickup_nodes[i])
    dropoff_nodes[i]=str(dropoff_nodes[i])
#print(pickup_nodes)
ALLpath_dict={}
rec_vel=[]
TripsInfo={}

#RTVE
#finding velocity of each record
rec_vel=clean_data["velocity (km/h)"].tolist()

TripsInfo={}
rec_no=clean_data["SNO"].tolist()
for index,row in clean_data.iterrows():
    TripsInfo[row['SNO']]=[]
#print(TripsInfo)
            

#tripsinfo={1:[],2:[],3:[]}
graph=Graph(objID, init_graph)
for i in range(len(rec_no)):
    previous_nodes,shortest_path=dijkstra_algorithm(graph =graph, start_node=pickup_nodes[i])
    path=print_result(previous_nodes, shortest_path,pickup_nodes,dropoff_nodes, start_node=pickup_nodes[i], target_node=dropoff_nodes[i])
    start_end=path[0]+','+path[-1]
    for i in range(0,len(rec_no)):
        ALLpath_dict[start_end]=[]
    ALLpath_dict[start_end]=path

    
    
#print(ALLpath_dict)

for index,row in clean_data.iterrows():
    #print(index,row)
   dict_index= str(row['PULocationID'])+','+str(row['DOLocationID'])
   TripsInfo[row['SNO']].append(ALLpath_dict[dict_index])
   TripsInfo[row['SNO']].append(row['velocity (km/h)'])

    
#print(TripsInfo)
reg_trips_info={}
#Regional splits
#for i in objID:
regID_temp=objID[13]
for j in rec_no:
    if str(regID_temp) in TripsInfo[j][0]:
        reg_trips_info[j]=[]
        reg_trips_info[j]=TripsInfo[j]
#print(reg_trips_info)
#region count:
reg_count={}
for i in reg_trips_info:
    reg_count[i]=len(reg_trips_info[i][0])
    reg_trips_info[i].append(reg_count[i])
#print(reg_trips_info)
regCountsLst=[]
for i in reg_trips_info:
    regCountsLst.append(reg_trips_info[i][2])
regCountsLst=list(set(regCountsLst))
#print(regCountsLst)

#finding mean velocity of each region count
rcVel_dict={}
for i in regCountsLst:
    flag=0
    rcVel_sum=0
    for j in reg_trips_info:
        if(reg_trips_info[j][2] == i):
            rc_vel=reg_trips_info[j][1]
            #print(rc_vel)
            rcVel_sum+=rc_vel
            flag+=1
    rcVel_dict[i]=rcVel_sum/flag
#print(rcVel_dict)

regCountLst2=[]
regCountVelLst=[]
for i in rcVel_dict:
    regCountLst2.append(i)
    regCountVelLst.append(rcVel_dict[i])
#print(regCountLst2)
#print(regCountVelLst)
regCountLst2.reverse()
#print(regCountLst2)

#weighted mean velocity of region r
weight_mean_nr=0
for i in range(0,len(regCountLst2)):
    weight_mean=regCountVelLst[i]*regCountLst2[i]
    #print(weight_mean)
    weight_mean_nr+=weight_mean
#print(weight_mean_nr)

weight_mean_dr=0
for i in regCountLst2:
    weight_mean_dr+=i
#print(weight_mean_dr)

weight_mean_final=weight_mean_nr / weight_mean_dr
print(weight_mean_final)

                            
    
