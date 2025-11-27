# define the graph
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = range(26)
graph=[[a,b,2],[a,c,3],[a,d,4],[b,d,1],[b,e,5],[c,d,3],[d,e,2],[e,f,4]]
#[f,g,1],[f,h,2],[g,h,3],[h,i,4],[i,j,5],[j,k,1],[k,l,2],[l,m,3],[m,n,4],[n,o,5],[o,p,1],[p,q,2],[q,r,3],[r,s,4],[s,t,5],[t,u,1],[u,v,2],[v,w,3],[w,x,4],[x,y,5],[y,z,1]]
def adjmatrix(v,g):
    adj=[[0 for i in range(v)]for j in range(v)]
    for i in range(len(g)):
        adj[g[i][0]][g[i][1]]=g[i][2]
        adj[g[i][1]][g[i][0]]=g[i][2] #undirected graph
    return adj

def prims(v,g):
    adj=adjmatrix(v,g)
    vertex=0 #source vertex
    edges=[]
    visited=[]
    minedge=[None,None,float('inf')]
    
    MST=[]
    while(len(MST)!=v-1):
        visited.append(vertex)
        for ed in range(0,v):
            if(adj[vertex][ed]!=0 and ed not in visited):
                edges.append([vertex,ed,adj[vertex][ed]])
        for ed in range(len(edges)):
            if(edges[ed][2]<minedge[2]and edges[ed][1] not in visited):
                minedge=edges[ed]
        MST.append(minedge)
        vertex=minedge[1]
        minedge=[None,None,float('inf')]
        
    return MST

print(prims(6,graph))
                