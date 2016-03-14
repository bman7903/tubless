#!/usr/bin/env python

###  This software is issued freely under the liscence Roberts.
###  Like what I've done? Have hate to spare? Just want to pay me?
###  Please consider one of the following

# bitcoin:13xcbqZfFdoR8Awuv49WPwxethh2uzjT6i
# https://www.paypal.me/sanchzrino5/50
# tubless@fnord137.appspotmail.com

from sys import argv, exit
from os import path, mkdir, chdir, environ, listdir, rename, remove, fork, getpid
from subprocess import Popen, PIPE
from re import sub
from PIL import Image, ImageFont, ImageDraw
from threading import Thread
from time import sleep
from requests import get
from PyQt4 import QtGui, QtCore, Qt
from PyQt4.Qt import *
from atexit import register
import youtube_dl
import mechanize
from bs4 import BeautifulSoup
from random import seed, randint
from re import sub
from urllib import unquote
import base64

img64='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'#.encode('hex')
icnz=base64.b64decode(img64)

seed()
avgTime = 3
Time    = ( avgTime * 2)
UAS     = 'Mozilla/5.0'
global urlz
urlz = []

join  = path.join
sep   = path.sep
exist = path.exists

def which( prog ):
  prog = str( prog )
  pth = str( environ['PATH'] )
  for d in pth.split(':'):
     for f in listdir( d ):
       if prog in str(f):
          path = join( sep, d, prog )
          return path

def checkPath( localpath ):
  if not exist( localpath ):
     try:
       mkdir( localpath )
     except:
       print( 'Error creating ' + str( localpth ) )

Home = join( sep, str( environ['HOME'] ), '.ytube' )
checkPath( Home )

font   = QtGui.QFont("eufm10")
font.setBold(True)
font.setWeight(125)
GY = "background-color:rgba(120, 6, 66, 150); color:rgba(255, 165, 0, 255);"

if not exist( Home ):
  global Home
  Home = environ['HOME']
  if not exist( Home ):
    global Home
    Home = 'Choose Base Directory!'
Img = join( sep, Home, 'img' )

Vids  = str( join( sep, str( environ['HOME'] ), 'Videos' ) )
Music = str( join( sep, str( environ['HOME'] ), 'Music' ) )
for e in 'Img Vids Music'.split(' '):
  f = eval( e )
  checkPath( Img )

Pth     = path.dirname(path.abspath(__file__))
SRCH    = str( join( sep, Pth, 'search.py' ) )
IMG     = str( join( sep, Pth, 'img.py' ) )
Py      = str( which( 'python' ) )
Streamr = str( which( 'mpv' ) )
if not 'mpv' in Streamr:
  Streamr = str( which( 'vlc' ) )

Query = ''
for a in argv:
  a = str(a)
  if not 'None' in a:
     if not 'search.py' in a:
       Query = str( str( Query + ' ' + a ).strip() )

def Renew():
   def bash(cmd):
       Popen(cmd, shell=True )
   proc = str( Py + ' ' + SRCH )
   bash(proc)

def isExtensionSupported(filename):
    if filename.endswith('PNG') or filename.endswith('png') or\
     filename.endswith('JPG') or filename.endswith('jpg'):
        return True

def imageFilePaths(paths):
    imagesWithPath = []
    for _path in paths:
        try:
            dirContent = listdir(_path)
        except OSError:
            raise OSError("Provided path '%s' doesn't exists." % _path)

        for each in dirContent:
            selFile = join(_path, each)
            if path.isfile(selFile) and isExtensionSupported(selFile):
                imagesWithPath.append(selFile)
    return list(set(imagesWithPath))

def whenExit():
   g = getpid()
   fork()
   if getpid() == g:
          exit()
   paths = Img
   if isinstance(paths, list):
      imgLst = imageFilePaths(paths)
   elif isinstance(paths, str):
      imgLst =  imageFilePaths([paths])
   else:
      print " You can either enter a list of paths or single path"
   app = QtGui.QApplication(argv) 
   pixmap = QtGui.QPixmap()
   pixmap.loadFromData(icnz)
   icn = QtGui.QIcon( pixmap )
   app.setWindowIcon( icn )
   if imgLst:
       window =  SlideShowPics(imgLst)
       window.setAttribute(Qt.WA_NoSystemBackground)
       window.setAutoFillBackground(True)
       window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       window.show()
       window.raise_()
       app.exec_()
   else:
        msgBox = QtGui.QMessageBox()
        msgBox.setText("No Image found in any of the paths below\n\n%s" % paths)
        msgBox.setStandardButtons(msgBox.Cancel | msgBox.Open);
        if msgBox.exec_() == msgBox.Open:
            main(str(QtGui.QFileDialog.getExistingDirectory(None,
                "Select Directory to SlideShow",
                getcwd())))

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

class Downloader(QtGui.QDialog):
    def __init__(self, parent=None):
        import youtube_dl
        global ytype, yzurl
        ytype = 'video'
        url = str( yzurl )
        QtGui.QDialog.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet( GY )
        self.url_e = QtGui.QLineEdit( url )
        self.url_e.setFont( font )
        self.url_l = QtGui.QLabel(self.tr("&URL:"))
        self.url_l.setBuddy(self.url_e)
        self.url_l.setFont( font )
        self.connect(self.url_e, QtCore.SIGNAL("textChanged(QString)"), self.update_dir)
        self.strm_b = QtGui.QPushButton(self.tr("Stream"))
        self.strm_b.setDefault(True)
        self.strm_b.setFont( font )
        self.connect(self.strm_b, QtCore.SIGNAL("clicked()"),self.strmF)
        self.quitButton = QtGui.QPushButton(self.tr("Quit"))
        self.quitButton.setFont( font )
        self.connect(self.quitButton, QtCore.SIGNAL("clicked()"), self.Fin)
        self.dwn_b = QtGui.QPushButton(self.tr("Download"))
        self.dwn_b.setDefault(True)
        self.dwn_b.setFont( font )
        self.connect(self.dwn_b, QtCore.SIGNAL("clicked()"),self.dwnFile)
        self.typBox = QtGui.QComboBox(self)
        self.typBox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.typBox.setGeometry(QtCore.QRect(47, 16, 100, 20))
        self.typBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.typBox.setFont(font)
        self.typBox.addItem( 'video' )
        self.typBox.addItem( 'audio' )
        self.connect(self.typBox, QtCore.SIGNAL("activated(QString)"), self.type_chosen)
        topLayout = QtGui.QHBoxLayout()
        topLayout.addWidget(self.url_l)
        topLayout.addWidget(self.url_e)
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addWidget(self.typBox)
        buttonLayout.addWidget(self.strm_b)
        buttonLayout.addWidget(self.quitButton)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.dwn_b)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle(self.tr("downloader"))
        self.url_e.setFocus()

    def enableDownloadButton(self):
        self.downloadButton.setEnabled(not self.urlLineEdit.text().isEmpty())

    def dwnFile(self):
        print('Download')
        g = self.url_e.text()
        global ytype
        if 'audio' in str( ytype ):
           print( 'Downloading audio' )
           g = getpid()
           fork()
           if getpid() == g:
                Renew()
                self.close()
           self.dlMusic()
           self.close()
        if 'video' in str( ytype ):
           print( 'Downloading video' )
           g = getpid()
           fork()
           if getpid() == g:
              Renew()
              self.close()
           self.dlVideo()
           self.close()
        print( str(g) + 'Complete' )

    def type_chosen( self, text ):
        global ytype
        ytype = text
        print(ytype)

    def update_dir( self, text):
        print( text )

    def strmF( self ):
      def bash(cmd):
         Popen(cmd, shell=True)
      yurl = str( self.url_e.text() )
      Proc = str( Streamr + ' ' + yurl )
      bash(Proc)
      self.Fin()

    def Fin( self ):
       Renew()
       self.close()

    def dlVideo( self ):
        chdir( Vids )
        ydl_opts = { 'logger': MyLogger(),
          'progress_hooks': [my_hook], }
        yurl = str( self.url_e.text() )
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
             ydl.download([yurl])

    def dlMusic( self ):
        chdir( Music )
        yurl = str( self.url_e.text() )
        ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
               }],
          'logger': MyLogger(),
          'progress_hooks': [my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([yurl])

class SlideShowPics(QtGui.QMainWindow):
    def __init__(self, imgLst, parent=None):
        super(SlideShowPics, self).__init__(parent)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAutoFillBackground(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self._imageCache = []
        self._imagesInList = imgLst
        self._pause = False
        self._count = 0
        self.animFlag = True
        self.updateTimer = QtCore.QTimer()
        self.connect(self.updateTimer, QtCore.SIGNAL("timeout()"), self.nextImage)
        self.prepairWindow()
        self.nextImage()

    def prepairWindow(self):
        screen = QtGui.QDesktopWidget().screenGeometry(self)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAutoFillBackground(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        size = self.geometry()
        self.resize(320,180)
        self.setStyleSheet("QWidget{background-color: #000000;}")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.buildUi()
        self.playPause()

    def buildUi(self):
        self.label = QtGui.QLabel()
        self.label.resize(640,360)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self.resize(320,180)

    def nextImage(self):
        """ switch to next image or previous image
        """
        if self._imagesInList:
            if self._count == len(self._imagesInList):
                self._count = 0
            global name
            name = str( self._imagesInList[self._count] )
            self.showImageByPath(
                    self._imagesInList[self._count])
            if self.animFlag:
                self._count += 1
            else:
                self._count -= 1

    def showImageByPath(self, path):
        if path:
            image = QtGui.QImage(path)
            pp = QtGui.QPixmap.fromImage(image)
            self.label.setPixmap(pp.scaled(
                    self.label.size(),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation))

    def playPause(self):
        if not self._pause:
            self._pause = True
            self.updateTimer.start(2500)
            return self._pause
        else:
            self._pause = False
            self.updateTimer.stop()

    def keyPressEvent(self, keyevent):
        event = keyevent.key()
        if event == QtCore.Qt.Key_Escape:
            self.close()
        if event == QtCore.Qt.Key_Left:
            self.animFlag = False
            self.nextImage()
        if event == QtCore.Qt.Key_Right:
            self.animFlag = True
            self.nextImage()
        if event == 32:
            self._pause = self.playPause()

    def Proc( self, x, y):
      g = getpid()
      register( whenExit )
      fork()
      if getpid() == g:
         exit()
      global name
      name  = str( name )
      title = name.split('_tle_')[0]
      id    = str( name.split('_tle_')[-1] )
      id    = str( sub( '.jpg', '', id ) )
      url   = str( 'https://www.youtube.com/watch?v=' + id )
      global yzurl
      yzurl = url
      apps = QtGui.QApplication(argv)
      httpWin = Downloader()
      httpWin.setStyleSheet( GY )
      httpWin.move(QtGui.QApplication.desktop().screen().rect().center()- httpWin.rect().center())
      httpWin.exec_()

    def mousePressEvent(self, event):
      x = event.pos().x()
      y = event.pos().y()
      self.Proc( x, y )
      if (event.button() == QtCore.Qt.LeftButton):
         self.drag_position = event.globalPos() - self.pos();
      event.accept();

    def mouseMoveEvent(self, event):
      if (event.buttons() == QtCore.Qt.LeftButton):
           self.move(event.globalPos().x() - self.drag_position.x(),
            event.globalPos().y() - self.drag_position.y());
      event.accept();

def mainz(paths):
    if isinstance(paths, list):
        imgLst = imageFilePaths(paths)
    elif isinstance(paths, str):
        imgLst =  imageFilePaths([paths])
    else:
        print " You can either enter a list of paths or single path"
    app = QtGui.QApplication(argv)
    pixmap = QtGui.QPixmap()
    pixmap.loadFromData(icnz)
    icn = QtGui.QIcon( pixmap )
    app.setWindowIcon( icn )
    if imgLst:
        window =  SlideShowPics(imgLst)
        window.setAttribute(Qt.WA_NoSystemBackground)
        window.setAutoFillBackground(True)
        window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#        window.setWindowIcon( icn )
        window.show()
        window.raise_()
        app.exec_()
    else:
        msgBox = QtGui.QMessageBox()
        msgBox.setText("No Image found in any of the paths below\n\n%s" % paths)
        msgBox.setStandardButtons(msgBox.Cancel | msgBox.Open);
        msgBox.setWindowIcon( icn )
        if msgBox.exec_() == msgBox.Open:
            main(str(QtGui.QFileDialog.getExistingDirectory(None,
                "Select Directory to SlideShow",
                getcwd())))

def Vert( url, pic, info ):
   info   = str( info )
   time   = str( info.split(' ')[0] )
   title  = str( info.split(' ')[-1] )
   imgout = str( join( sep, Img, str( title + '_tle_' + str(pic)  ) ) )
   chdir( Img )
   r = get( url, stream=True )
   with open( imgout, 'wb' ) as f:
      for chunk in r.iter_content( chunk_size=1024 ):
          if chunk:
              f.write( chunk )
              f.flush()
   img = Image.open(imgout)
   draw = ImageDraw.Draw(img)
   try:
     font = ImageFont.truetype("/usr/share/fonts/truetype/dustin/PenguinAttack.ttf", 20)
     draw.text((0, 0),time,(0,255,0),font=font)
     draw.text((0, 160),title,(0,255,0), font=font)
   except:
     draw.text((0, 0),time,(0,255,0) )
     draw.text((0, 160),title,(0,255,0) )
   img.save(imgout)
   f.close()

def View( dir ):
   mainz( dir )

def gparse( soup ):
       base = 'https://www.youtube.com'
       soup = str( soup )
       for e in soup.split('h3 class="yt-lockup-title'):
           e = str( e )
           if e.startswith(' "><a') == True:
              id      = str( e.split('data-context-item-id=')[-1] )
              id      = str( id.split('"')[1] )
              title   = str( e.split('title=')[1] )
              title   = str( title.split('"')[1] )
              title   = str( sub(r'\W+', '', title ) )
              watch   = str( base + '/watch?v=' + id )
              ag      = str( e.split('"yt-lockup-meta-info"><li>')[-1] )
              age     = str( ag.split('</li>')[0] )
              user    = str( e.split(' href="/user')[-1] )
              user    = str( user.split('"')[0] ).strip('/')
              views   = str( sub('</li><li>','', ag ) ).split('</')[0]
              views   = str( sub(age,'',views ) )
              if not 'views' in views:
                views = 'err'
              if len( views ) > 12:
                views = 'err'
              if len( user ) < 4:
                user  = 'None'
              if len( age ) > 12:
                age   = 'err'
              time    = str( e.split('video-time">')[-1] )
              time    = str( time.split('</')[0] )
              thumb   = str( 'https://i.ytimg.com/vi/' + id + '/mqdefault.jpg' )
              if not '<' in id:
                 z    = str( id + '|' + title + '|' + watch + '|' + thumb + '|' + views + '|' + age + '|' + time + '|' + user)
                 global urlz
                 urlz.append( z )

def Next( url, i, pages ):
  base = 'https://www.youtube.com'
  i = i + 1
  if i == pages:
     return
  sleep(1)
  br = mechanize.Browser(factory=mechanize.RobustFactory())
  br.set_handle_robots(False)
  br.set_handle_equiv(False)
  br.addheaders = [('User-agent', UAS)]
  data = br.open( url )
  soup = BeautifulSoup(data.read())
  gparse(soup)
  soup = str( soup )
  for a in soup.split('href='):
     a = str( a )
     strn = str( 'page=' + str( i ) )
     if strn in a:
        b = str( a.split('"')[1] )
        b = str( sub('&amp;','&',b) )
        url = str( base + b )
        Next( url, i, pages )
        break

def tsearch( pages, Query ):
    Query = str( Query )
    Query = str( sub(' ', '+', Query ) )
    base = 'https://www.youtube.com'
    url = str( base + '/results?search_query=' + Query )
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', UAS)]
    data = br.open( url )
    soup = BeautifulSoup( data.read() )
    gparse( soup )
    if pages > 1:
     i = 2
     soup = str( soup )
     for a in soup.split('href='):
        a = str( a )
        strn = str( 'page=' + str( i ) )
        if strn in a:
            b = str( a.split('"')[1] )
            b = str( sub('&amp;','&',b) )
            url = str( base + b )
            Next( url, i, pages )
            break
    global urlz
    return urlz

def Search():
  for e in listdir( Img ):
    f = join( sep, Img, e )
    try:
      remove( f )
    except:
      pass
  f = tsearch( 5, Query )
  for e in f:
      e = str( e )
      id    = str( e.split('|')[0] ).strip()
      title = str( e.split('|')[1] ).strip()
      watch = str( e.split('|')[2] ).strip()
      image = str( e.split('|')[3] ).strip()
      iout  = str( str(id) + '.jpg' ).strip()
      views = str( e.split('|')[4] ).strip()
      views = str( sub(' ','_',views ) )
      age   = str( e.split('|')[5] ).strip()
      age   = str( sub(' ','_',age) )
      time  = str( e.split('|')[6] ).strip()
      user  = str( e.split('|')[7] ).strip()
      info = str( str(time) + '_' + str(views) + '_' + str(user) + '_' + str(age) + ' ' + str(title) )
      t = Thread(target=Vert, args=( image, iout, info) )
      t.start()

la = ( len( argv ) - 1 )

if la < 1:
  print('Usage ./tubless.py yout query')
  exit()

if la > 0:
  Search()
  sleep(5)

View( Img )
