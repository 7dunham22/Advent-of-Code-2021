"""After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically,
big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small
caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you
leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Given these new rules, how many paths through this cave system are there?
"""

routes = '''zi-end
XR-start
zk-zi
TS-zk
zw-vl
zk-zw
end-po
ws-zw
TS-ws
po-TS
po-YH
po-xk
zi-ws
zk-end
zi-XR
XR-zk
vl-TS
start-zw
vl-start
XR-zw
XR-vl
XR-ws'''

routes = routes.strip().split('\n')
routes = [route.split('-') for route in routes]

routeDict = {}
for route in routes:
    routeDict[route[0]] = []
    routeDict[route[1]] = []
for route in routes:
    routeDict[route[0]].append(route[1])
    routeDict[route[1]].append(route[0])

def countPaths(part, seen=[],root='start'):
    if root == 'end':
        return 1
    if root in seen:
        if root == 'start':
            return 0
        if root.islower():
             if part == 1: return 0
             else: part = 1
    return sum(countPaths(part,seen+[root], n) for n in routeDict[root])

print(countPaths(part=1))
print(countPaths(part=2))
