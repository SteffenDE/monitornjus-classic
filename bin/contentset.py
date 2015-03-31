#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2015 Steffen Deusch
# Licensed under the MIT license
# Beilage zu MonitorNjus, 25.03.2015 (Version 0.6.1)

try:
    import cgi
    import cgitb
    import common
    import getytid
    import checktime
    from datetime import datetime
    form = cgi.FieldStorage()
    cgitb.enable()
    gseite = form.getvalue('seite')
    gnummer = form.getvalue('nummer')
    rows = common.getrows()
    if gseite == "1":
        seite = "1"
        mseite = "Links"
    elif gseite == "2":
        seite = "2"
        mseite = "Rechts"
    else:
        pass
    if gnummer is None:
        x = 0
        while x < rows:
            if checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))+x),datetime.now()) == True and common.getinfo("AKTIV", mseite, int(common.minaktiv(mseite))+x) == 1:
                nummer = int(common.minaktiv(mseite))+x
                break
            x = x + 1
    else:
        nummer = int(gnummer)
    url = common.getinfo("URL", mseite, int(nummer))
    refresh = common.getinfo("REFRESH", mseite, int(nummer))
    x = 1
    while x < rows or x == 1:
        if nummer < rows and nummer+x <= rows:
            if common.getinfo("AKTIV", mseite, nummer+x) == 1 and checktime.match(common.getinfo("VONBIS", mseite, nummer+x),datetime.now()) == True:
                on = 1
                nextnummer = nummer + x
                break
            else:
                on = 0
                nextnummer = nummer
        else:
            on = 1
            z = 0
            while z < rows:
                if checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))+z),datetime.now()) == True:
                    nextanumma = int(common.minaktiv(mseite))+z
                    nextnummer = nextanumma
                    break
                else:
                    nextnummer = nummer
                z = z + 1
        x = x + 1
    if common.getinfo("REFRESHAKTIV", mseite, nummer) == 1:
        on = 1
    else:
        on = 0
    if on == 1:
        prrefresh = '\
    <meta http-equiv="refresh" content=\"'+str(refresh)+'; URL=contentset.py?seite='+str(seite)+';nummer='+str(nextnummer)+'\">'
    else:
        prrefresh = ""

    typ = common.checkfiletype(url)

    if typ == "image":
        output = '\
    <div class="container">\
        <img src='+url+' style="position: absolute; margin-left: -8px; margin-top: -8px;">\
    </div>'
    elif typ == "video":
        output = '\
    <div class="videocontainer"><video src=\''+url+'\' style="width:100%; height:auto; max-height: 100%;" autoplay="autoplay" loop="loop">Dein Browser unterst&uuml;tzt keine HTML5 Videos...</video></div>'
    elif typ == "pdf":
        output = '\
    <iframe src=\"'+url+'\" style="position:absolute; z-index:9; height:98%; width:98%; border-style:none; overflow:hidden" scrolling="no"></iframe>'
    elif typ == "youtube":
        output = '\
    <iframe style="position:absolute; height:100%; width:100%; top:0px; left: 0px; border-style:none; overflow:hidden" scrolling="no" src="//www.youtube.com/embed/'+getytid.video_id(url)+'?rel=0&autoplay=1&loop=1&controls=0&showinfo=0"></iframe>'
    else:
        output = '\
    <iframe src=\"'+url+'\" style="position:absolute; width:100%; height:100%; top:0px; left:0px; margin-left:-1px; border-style:none;" scrolling="no" name="links"></iframe>'

    print "Content-Type: text/html"
    print
    print """\
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <script type="text/javascript" src="js/jquery-2.1.3.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function () {$('#content').css('display', 'none');$('#content').fadeIn(1000);});
    </script>"""
    if prrefresh is not "":
        print prrefresh
    else:
        pass
    print "\
    <title>MonitorNjus</title>"
    if typ == "video":
        style = """\
    <style>
    .videocontainer 
    {
        position:absolute;
        height:100%;
        width:100%;
        overflow: hidden;
        top: 0px;
    }
    .videocontainer video 
    {
        min-width: 100%;
        min-height: 100%;
    }
    </style>"""
        print style
    elif typ == "image":
        print """
    <script type="text/javascript" src="js/jquery-2.1.3.min.js"></script>
    <style>
    .container img.wide {
        width: 100%;
        height: auto;
    }
    .container img.tall {
        height: 100%;
        width: auto;
    }​
    </style>"""
    else:
        pass
    print "\
</head>"
    #print checktime.match(common.getinfo("VONBIS", mseite, int(common.minaktiv(mseite))),datetime.now())
    #print nextanumma
    #print nextnummer
    print "\
<body id=\"content\">"
    #print common.getinfo("VONBIS", mseite, nummer)
    #print checktime.match(common.getinfo("VONBIS", mseite, nummer),datetime.now())
    print output
    if typ == "image":
        print """\
    <script type="text/javascript">
    $(window).load(function(){
     $('.container').find('img').each(function(){
      var imgClass = (this.width/this.height > 1) ? 'wide' : 'tall';
      $(this).addClass(imgClass);
     })
    })
    </script>"""
    print "\
</body>\n\
</html>"

except Exception, e:
    print "Content-Type: text/html"
    print
    print """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" />
    <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection" />
    <link href="css/mnews.css" type="text/css" rel="stylesheet" media="screen,projection" />
    <META HTTP-EQUIV="refresh" CONTENT="10" />
</head>
<body>
    <h1>Es ist ein Fehler aufgetreten (contentset.py)! Seite wird in 10 Sekunden neu geladen.</h1>
    <h3>Details:<br>"""
    print e
    print """
    </h3>
</body>
/html>"""