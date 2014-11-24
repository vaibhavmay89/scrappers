from docx import *
import os
doc = Document("sample.docx")
#docbody = doc.xpath('/w:document/w:body', namespaces=wordnamespaces)[0]
# print (search(doc,'your search string'))

def doc_to_text_catdoc(filename):
    (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
    fi.close()
    retval = fo.read()
    erroroutput = fe.read()
    fo.close()
    fe.close()
    if not erroroutput:
        return retval
    else:
        raise OSError("Executing the command caused an error: %s" % erroroutput)



print(doc_to_text_catdoc("sample.doc"))