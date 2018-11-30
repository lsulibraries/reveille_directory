Download saxon9He zip
=====================

` https://sourceforge.net/projects/saxon/files/latest/download `


Move the file to /usr/share/java (the latest versio was 9-9-0-2J at time of writing)
------------------------------------------------------------------------------------

` sudo mv ~/Downloads/SaxonHE9-9-0-2J.zip /usr/share/java`

` cd /usr/share/java`

` sudo unzip SaxonHE9-9-0-2J.zip`

` sudo rm SaxonHE9-3-0-5j.zip`


Add the following lines to a file in /usr/bin
---------------------------------------------

` cd /usr/bin`

` nano saxon`

Add these lines to the file and save (Ctl-O). note this is specific to xslt and not xQuery
------------------------------------------------------------------------------------------


` #!/bin/sh`

` exec java -cp /usr/share/java/saxon9he.jar net.sf.saxon.Transform "$@"`


Make the file executable
------------------------

` sudo chmod 755 /usr/bin/saxon`


