import socket
import time
#TODO implement threading to close main html sender
#TODO sending JavaScript


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setblocking(0)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('', 80))
formatedboi = ''

serversocket.listen(100)
VERSION = 'HTTP/1.1'
imagefiletypelist = ['png', 'jpeg', 'jpg', 'tiff', 'gif', 'ico']
indexhtmllocation = "index.html"
SERVERNAME = 'shit wip'
basedhtml = f'''{VERSION} 200 OK\r\nServer: ngl kinda ok\r\n'''
basehtml = basedhtml + '\r\n'
errorcode = ''
baseerror = f'''{VERSION} {errorcode}
\r\n'''
def slight(t=0.1069):
    time.sleep(t)
def loadindexhtml(indexhtmllocation=indexhtmllocation,basehtml=basehtml):
    localvar = basedhtml + 'Content-type: text/html\r\n\r\n'
    with open(indexhtmllocation) as reader:
        for line in reader:
            localvar = localvar + line + '\r\n'
    return localvar
def sendHTML(htmllocation, basehtml=basehtml):
    localvar = basehtml
    global errorcode
    try:
        if splitformatedboi[1] == 'html':

            with open(htmllocation) as reader:
                for line in reader:
                    localvar = localvar + line + '\r\n'
                print(localvar)
                clientsocket.send(localvar.encode("utf-8"))
                slight()
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                print('closedhtml')
    except IndexError as e:
        print("not a vaild request")
        errorcode = '404'
        clientsocket.send(loadindexhtml("error.html",baseerror).encode('utf-8'))
        slight()
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
def sendCSS(csslocation='index.css'):
    global basehtml
    global errorcode
    localvar = basehtml
    try:
        if splitformatedboi[1] == 'css':
            localvar = basehtml
            with open(csslocation) as reader:
                for line in reader:
                    localvar = localvar + line + '\r\n'
            print(localvar)

            clientsocket.send(localvar.encode("utf-8"))
            slight()
            clientsocket.shutdown(socket.SHUT_RDWR)
            clientsocket.close()
            print('closedcss')
    except IndexError:
        print("not a vaild request")
        errorcode = '404'
def sendJS(jslocation="index.js"):
    global basehtml
    global errorcode
    localvar = basehtml
    try:
        if splitformatedboi[1] == 'js':
            with open(jslocation) as reader:
                for line in reader:
                    localvar = localvar + line + '\r\n'
            print(localvar)
            clientsocket.send(localvar.encode("utf-8"))
            slight()
            clientsocket.shutdown(socket.SHUT_RDWR)
            clientsocket.close()
            print('closedjs')
    except IndexError:
        print("not a vaild request")


def sendImages():
    global errorcode
    global clientsocket
    try:
        with open(formatedboi, 'rb') as reader:
            tosend = reader.read(-1)
            # print('read file')
            print(formatedboi.split(".")[1])
    except FileNotFoundError as e:
        print(f'{e.filename} was not found')
        errorcode = '404'
        clientsocket.send(loadindexhtml("error.html",baseerror).encode('utf-8'))
        slight()
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
    except PermissionError as e:
        print(f'access to {e.filename} was denied')
        errorcode = '403'
        return
    except OSError as e:
        print(e)
        clientsocket.send(loadindexhtml("error.html",baseerror).encode('utf-8'))
        slight()
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()


    for imagefiletypes in range(len(imagefiletypelist)):
        # print("isfile image?")
        splitformatedboi = formatedboi.split(".")
        if splitformatedboi[1] == imagefiletypelist[imagefiletypes]:
            clientsocket.send(tosend)
            slight(0.1)
            clientsocket.shutdown(socket.SHUT_RDWR)
            clientsocket.close()
            print("closedI")

testhtml = f'''
{VERSION} 200 OK\r\n

<html>\r\n
  <head>\r\n
    <title>An Example Page</title>\r\n
  </head>\r\n
  <body>\r\n
    <p>Hello World, this is a very simple HTML document.</p>\r\n
    <img src="matrix.jpg">
  </body>\r\n
</html>\r\n
'''
indexhtml = loadindexhtml()
# print(basehtml)
# indexhtml = testhtml

endit =f'''
{VERSION} 200 OK
'''

def findfield(splitlist, tofind):
    if splitlist[0] != f'GET / {VERSION}' and decodedrequest[0][0:3] == 'GET':
        for i in splitlist:
            if tofind in i:
                return i
connectiontoll = {}

while True:
    try:
        clientsocket, address = serversocket.accept()
        # connectiontoll[clientsocket] = 0
        # connectiontoll[address] = 0
    except BlockingIOError:
        continue
    # except:
    #     pass

    if clientsocket is not None:
        # print(connectiontoll[clientsocket])
        try:
            # if connectiontoll[clientsocket] == 0:
            print(f"{address[0]}:{address[1]} has connected")
            # clientsocket.send(indexhtml.encode("utf-8"))
            connectiontoll[clientsocket] = 1

        except KeyError:
            continue
        try:
            recieved = clientsocket.recv(1028)
            print(recieved.decode('utf-8'))
            decodedrequest = recieved.decode('utf-8').split('\r\n')
            # print(decodedrequest)
            # print(findfield(decodedrequest, 'User-Agent:'))


        except:
            pass
        try:
            if connectiontoll[clientsocket] <= 1:
                if decodedrequest[0] == f'GET / {VERSION}':
                    try:
                        clientsocket.send(indexhtml.encode("utf-8"))
                        slight()
                        # time.sleep(1)
                        clientsocket.shutdown(socket.SHUT_RDWR)
                        clientsocket.close()
                    except:
                        pass
                if decodedrequest[0] != f'GET / {VERSION}' and decodedrequest[0][0:3] == 'GET':
                    formatedboi = decodedrequest[0].replace("GET ", "")
                    formatedboi = formatedboi.replace(VERSION, "")
                    formatedboi = formatedboi.replace(" ", "")
                    formatedboi = formatedboi[1:]
                    print(formatedboi)
                    splitformatedboi = formatedboi.split('.')
                    # clientsocket.send(loadindexhtml(formatedboi).encode('utf-8'))
                    sendHTML(formatedboi)
                    sendCSS()
                    sendJS()
                    sendImages()
                    # if splitformatedboi[1] == 'png':
                    #     sendImages()
                    # sendCSS()
                    # if splitformatedboi[1] == 'css':
                    #     clientsocket.send(loadindexhtml(formatedboi).encode('utf-8'))




                # if
        except NameError:
            pass
        except KeyError:
            pass
        # except:
        #     print('other')

                # print(formatedboi)
            # print(decodedrequest[0][0:2])
            decodedrequest = []



