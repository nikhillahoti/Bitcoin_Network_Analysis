import snap
# import os

# Graph = snap.GenRndGnm(snap.PNGraph, 100, 1000)
# print os.system("pwd")
Graph = snap.LoadEdgeList(snap.PNGraph, "../bitcoin_computed/txedgeunique.txt", 0, 1)
G_Nodes = Graph.GetNodes()
G_Edges = Graph.GetEdges()
print "Graph: Nodes %d, Edges %d" % (G_Nodes, G_Edges)

SCComponents = snap.TCnComV()
WCComponents = snap.TCnComV()

snap.GetSccs(Graph, SCComponents)
snap.GetWccs(Graph, WCComponents)

MaxWCCNodes = WCComponents[0]
MaxSCCNodes = SCComponents[0]
# print type(MaxSccNodes)
print MaxSCCNodes.Len()
print MaxWCCNodes.Len()

# Iterate over each edge and check for In, Out

SCCHashmap = snap.TIntH()
for node in MaxSCCNodes:
    SCCHashmap.AddKey(node)

InOutHashmap = snap.TIntH()
for node in MaxWCCNodes:
    if not SCCHashmap.IsKey(node):
        InOutHashmap.AddKey(node)

print InOutHashmap.Len()


In, Out, Tendrils = 0, 0, 0
Ec = 0

for EI in Graph.Edges():
    Ec += 1
    print Ec
    if SCCHashmap.IsKey(EI.GetSrcNId()) and InOutHashmap.IsKey(EI.GetDstNId()):
        Out += 1
    elif InOutHashmap.IsKey(EI.GetSrcNId()) and SCCHashmap.IsKey(EI.GetDstNId()):
        In += 1
    elif InOutHashmap.IsKey(EI.GetSrcNId()) and InOutHashmap.IsKey(EI.GetDstNId()):
        Tendrils += 1

print In, Out, Tendrils

"""
In, Out = 0, 0
Ec = 0
for EI in Graph.Edges():
    if MaxScc[0].IsNIdIn(EI.GetSrcNId()) and not MaxScc[0].IsNIdIn(EI.GetDstNId()):
        Out += 1
        print "Out: %d" % Out
    elif not MaxScc[0].IsNIdIn(EI.GetSrcNId()) and MaxScc[0].IsNIdIn(EI.GetDstNId()):
        In += 1
        print "In: %d" % In



DegToCntV = snap.TIntPrV()
snap.GetInDegCnt(Graph, DegToCntV)

for comp in DegToCntV:
    print comp.GetVal1(), comp.GetVal2()

print "-----------------------------------------------------------------------"

ComponentDist = snap.TIntPrV()
snap.GetSccSzCnt(Graph, ComponentDist)

for comp in ComponentDist:
    print comp.GetVal1(), comp.GetVal2()

print "------------------------------------------------------------------------"

ComponentDist2 = snap.TIntPrV()
snap.GetWccSzCnt(Graph, ComponentDist2)

for comp in ComponentDist2:
    print comp.GetVal1(), comp.GetVal2()

print "-------------------------------------------------------------------------"

Components = snap.TCnComV()
snap.GetSccs(Graph, Components)

print type(Components[0])
l = Components.Len()
print l
print Components[l - 1].Len()
for c in Components:
    print "Size of component is: %d" % c.Len()

*****************************************************

sccHashmap = snap.TIntH()
for node in Components[0]:
    sccHashmap[node] = 1

for EI in Graph.Edges():
    if EI.GetSrcNId() in sccHashmap and EI.GetDstNId() not in sccHashmap:
        Out += 1
    elif EI.GetSrcNId() not in sccHashmap and EI.GetDstNId() in sccHashmap:
        In += 1
******************************************************

In, Out = 0, 0
Ec = 0
for EI in Graph.Edges():
    Ec += 1
    if Components[0].IsNIdIn(EI.GetSrcNId()) and not Components[0].IsNIdIn(EI.GetDstNId()):
        Out += 1
    elif not Components[0].IsNIdIn(EI.GetSrcNId()) and Components[0].IsNIdIn(EI.GetDstNId()):
        In += 1


print
print In, Out


"""