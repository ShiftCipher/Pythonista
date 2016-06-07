import plotly
py = plotly.plotly('PythonAPI', 'ubpiol2cve')

x = [0,1,2,3,4,5,6,7,8]
y = [8,7,6,5,4,3,2,1,0]
x2 = [0,1,2,3,4,5,6,7,8]
y2 = [0,1,2,3,4,5,6,7,8]


axesstyle = {
    "type" : "log",
}

layout = {
    "xaxis" : axesstyle,
    "yaxis" : axesstyle,
}


py.plot(x,y,x2,y2,layout=layout)