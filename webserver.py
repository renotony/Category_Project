from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from database_setup import Base, Plays, Characters
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///plays.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/plays/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output = ""
            output += "<html><body>"
            output += "<h1>Enter a New Play</h1>"
            output += "<form method = 'POST' enctype='multipart/form-data' action = '/plays/new'>"
            output += "<input name = 'newPlayName' type = 'text' placeholder = 'New Play Name' > "
            output += "<input type='submit' value='Create'>"
            output += "</form></body></html>"
            self.wfile.write(output)
            return

        if self.path.endswith("/edit"):
            playIDPath = self.path.split("/")[2]
            myPlayQuery = session.query(Plays).filter_by(id=playIDPath).one()
            if myPlayQuery:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = "<html><body>"
                output += "<h1>"
                output += myPlayQuery.title
                output += "</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/plays/%s/edit' >" % playIDPath
                output += "<input name= 'newPlayTitle' type='text' placeholder = '%s' >" % myPlayQuery.title
                output += "<input type= 'submit' value='Rename'>"
                output += "</form>"

                self.wfile.write(output)


        if self.path.endswith("/delete"):
            playIDPath = self.path.split("/")[2]

            myPlayQuery = session.query(Plays).filter_by(id=playIDPath).one()

            if myPlayQuery:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Are you sure you want to delete %s?" % myPlayQuery.title
                output += "<form method='POST' enctype = 'multipart/form-data' action='/plays/%s/delete'>" % playIDPath
                output += "<input type = 'submit' value='Delete'>"
                output += "</form>"
                output += "</body></html>"

                self.wfile.write(output)

        if self.path.endswith("/plays"):
            plays = session.query(Plays).all()
            output = ""
            output += "<a href = '/plays/new' > Enter a New Play Here </a></br></br>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output += "<html><body>"
            for play in plays:
                output += play.title
                output += "</br>"
                output += "<a href=' /plays/%s/edit' >Edit </a>" % play.id
                output += "</br>"
                output += "<a href=' /plays/%s/delete' >Delete</a>" % play.id
                output += "</br></br>"
            output += "</body></html>"
            self.wfile.write(output)
            return




    def do_POST(self):
        try:

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

                playIDPath = self.path.split("/")[2]

                myPlayQuery = session.query(Plays).filter_by(id = playIDPath).one()

                if myPlayQuery:
                    session.delete(myPlayQuery)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/plays')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newPlayTitle')
                    playIDPath = self.path.split("/")[2]

                    myPlayQuery = session.query(Plays).filter_by(id=playIDPath).one()
                    if myPlayQuery != []:
                        myPlayQuery.title = messagecontent[0]
                        session.add(myPlayQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/plays')
                        self.end_headers()

            if self.path.endswith("/plays/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newPlayName')

                    newPlay = Plays(title=messagecontent[0])
                    session.add(newPlay)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/plays')
                    self.end_headers()


        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()



    except KeyboardInterrupt:
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()
