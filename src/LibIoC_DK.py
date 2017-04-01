'''
Created on Jan 30, 2017

This script includes several useful utilities to analyze IoC.

@author: Andrew D. Kim (aka Daegeon Kim)
'''

import re, requests

pattern = {}
pattern['url'] = '([a-z]{3,}\:\/\/[\S]{16,})[^~!@#$%&*()<>?"]'
pattern['host'] = '(([a-z0-9\-]{2,}\[?\.\]?)+(abogado|ac|academy|accountants|active|actor|ad|adult|ae|aero|af|ag|agency|ai|airforce|al|allfinanz|alsace|am|amsterdam|an|android|ao|aq|aquarelle|ar|archi|army|arpa|as|asia|associates|at|attorney|au|auction|audio|autos|aw|ax|axa|az|ba|band|bank|bar|barclaycard|barclays|bargains|bayern|bb|bd|be|beer|berlin|best|bf|bg|bh|bi|bid|bike|bingo|bio|biz|bj|black|blackfriday|bloomberg|blue|bm|bmw|bn|bnpparibas|bo|boo|boutique|br|brussels|bs|bt|budapest|build|builders|business|buzz|bv|bw|by|bz|bzh|ca|cal|camera|camp|cancerresearch|canon|capetown|capital|caravan|cards|care|career|careers|cartier|casa|cash|cat|catering|cc|cd|center|ceo|cern|cf|cg|ch|channel|chat|cheap|christmas|chrome|church|ci|citic|city|ck|cl|claims|cleaning|click|clinic|clothing|club|cm|cn|co|coach|codes|coffee|college|cologne|com|community|company|computer|condos|construction|consulting|contractors|cooking|cool|coop|country|cr|credit|creditcard|cricket|crs|cruises|cu|cuisinella|cv|cw|cx|cy|cymru|cz|dabur|dad|dance|dating|day|dclk|de|deals|degree|delivery|democrat|dental|dentist|desi|design|dev|diamonds|diet|digital|direct|directory|discount|dj|dk|dm|dnp|do|docs|domains|doosan|durban|dvag|dz|eat|ec|edu|education|ee|eg|email|emerck|energy|engineer|engineering|enterprises|equipment|er|es|esq|estate|et|eu|eurovision|eus|events|everbank|exchange|expert|exposed|fail|farm|fashion|feedback|fi|finance|financial|firmdale|fish|fishing|fit|fitness|fj|fk|flights|florist|flowers|flsmidth|fly|fm|fo|foo|forsale|foundation|fr|frl|frogans|fund|furniture|futbol|ga|gal|gallery|garden|gb|gbiz|gd|ge|gent|gf|gg|ggee|gh|gi|gift|gifts|gives|gl|glass|gle|global|globo|gm|gmail|gmo|gmx|gn|goog|google|gop|gov|gp|gq|gr|graphics|gratis|green|gripe|gs|gt|gu|guide|guitars|guru|gw|gy|hamburg|hangout|haus|healthcare|help|here|hermes|hiphop|hiv|hk|hm|hn|holdings|holiday|homes|horse|host|hosting|house|how|hr|ht|hu|ibm|id|ie|ifm|il|im|immo|immobilien|in|industries|info|ing|ink|institute|insure|int|international|investments|io|iq|ir|irish|is|it|iwc|jcb|je|jetzt|jm|jo|jobs|joburg|jp|juegos|kaufen|kddi|ke|kg|kh|ki|kim|kitchen|kiwi|km|kn|koeln|kp|kr|krd|kred|kw|ky|kyoto|kz|la|lacaixa|land|lat|latrobe|lawyer|lb|lc|lds|lease|legal|lgbt|li|lidl|life|lighting|limited|limo|link|lk|loans|london|lotte|lotto|lr|ls|lt|ltda|lu|luxe|luxury|lv|ly|ma|madrid|maison|management|mango|market|marketing|marriott|mc|md|me|media|meet|melbourne|meme|memorial|menu|mg|mh|miami|mil|mini|mk|ml|mm|mn|mo|mobi|moda|moe|monash|money|mormon|mortgage|moscow|motorcycles|mov|mp|mq|mr|ms|mt|mu|museum|mv|mw|mx|my|mz|na|nagoya|name|navy|nc|ne|net|network|neustar|new|nexus|nf|ng|ngo|nhk|ni|ninja|nl|no|np|nr|nra|nrw|ntt|nu|nyc|nz|okinawa|om|one|ong|onl|ooo|org|organic|osaka|otsuka|ovh|pa|paris|partners|parts|party|pe|pf|pg|ph|pharmacy|photo|photography|photos|physio|pics|pictures|pink|pizza|pk|pl|place|plumbing|pm|pn|pohl|poker|porn|post|pr|praxi|press|pro|prod|productions|prof|properties|property|ps|pt|pub|pw|qa|qpon|quebec|re|realtor|recipes|red|rehab|reise|reisen|reit|ren|rentals|repair|report|republican|rest|restaurant|reviews|rich|rio|rip|ro|rocks|rodeo|rs|rsvp|ru|ruhr|rw|ryukyu|sa|saarland|sale|samsung|sarl|sb|sc|sca|scb|schmidt|schule|schwarz|science|scot|sd|se|services|sew|sexy|sg|sh|shiksha|shoes|shriram|si|singles|sj|sk|sky|sl|sm|sn|so|social|software|sohu|solar|solutions|soy|space|spiegel|sr|st|style|su|supplies|supply|support|surf|surgery|suzuki|sv|sx|sy|sydney|systems|sz|taipei|tatar|tattoo|tax|tc|td|technology|tel|temasek|tennis|tf|tg|th|tienda|tips|tires|tirol|tj|tk|tl|tm|tn|to|today|tokyo|tools|top|toshiba|town|toys|tp|tr|trade|training|travel|trust|tt|tui|tv|tw|tz|ua|ug|uk|university|uno|uol|us|uy|uz|va|vacations|vc|ve|vegas|ventures|versicherung|vet|vg|vi|viajes|video|villas|vision|vlaanderen|vn|vodka|vote|voting|voto|voyage|vu|wales|wang|watch|webcam|website|wed|wedding|wf|whoswho|wien|wiki|williamhill|wme|work|works|world|ws|wtc|wtf|xyz|yachts|yandex|ye|yoga|yokohama|youtube|yt|za|zm|zone|zuerich|zw))'
pattern['ip'] = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
pattern['email'] = '([a-z][_a-z0-9-.]+@[a-z0-9-]+\.[a-z]+)'
pattern['md5'] = '([a-f0-9]{32}|[A-F0-9]{32})'
pattern['sha1'] = '([a-f0-9]{40}|[A-F0-9]{40})'
pattern['sha256'] = '([a-f0-9]{64}|[A-F0-9]{64})'
pattern['cve'] = '(CVE\-[0-9]{4}\-[0-9]{4,6})'
pattern['registry'] = '((HKLM|HKCU|HKU|HKCC|HKCR)\\[\\A-Za-z0-9-_]+)'
pattern['filenme'] = '([A-Za-z0-9-_\.]+\.(exe|dll|bat|sys|js|jar|jpg|png|vb|scr|pif|chm|zip|rar|cab|pdf|doc|docx|ppt|pptx|xls|xlsx|hwp|hwpx|swf|gif|pdb))'
pattern['filepath'] = '[A-Za-z]:\\[A-Za-z0-9-_\.\\]+'

# the files of interest that written as the result of the malware behavior
foi = {'exe','dll','bat','jpg','png', 'scr', 'zip','rar','cab','pdf','doc','docx','ppt','pptx','xls','xlsx','hwp','hwpx','swf','gif','tmp','pdb'}

################################################################
# Return true if the target file(or full file path) is belong to the file of interest defined by 'foi' variable
# @ inputs
#    target: the filename or full path including file extension.
# @ outputs:
#    Return True if the filename or full path is the file of interest by 'foi' variable, otherwise return False.
def isFileofInterest(target):
    for f in foi:
        if target.lower().endswith('.'+f):
            return True 
     
    return False


################################################################
# Filter valid IoCs from input string by applying the regular expressions of them. 
# @ inputs
#    val: the input string
# @ outputs:
#    Return the list of valid IoCs.    
def filterRegularIoC(val,type=None):
    retval = []
    if type is not None:
        type = type.lower()
    
    if type is None or type == 'url':
        retval.extend(re.findall(pattern['url'],val))
    if type is None or type == 'host':
        retval.extend(re.findall(pattern['host'],val))
    if type is None or type == 'ip':
        retval.extend(re.findall(pattern['ip'],val))
    if type is None or type == 'email':
        retval.extend(re.findall(pattern['email'],val))
    if type is None or type == 'hash' or type == 'md5':
        tmp = re.findall(pattern['md5'],val)
        if len(tmp) != 0:
            retval.extend(tmp)
    if type is None or type == 'hash' or type == 'sha1':
        tmp = re.findall(pattern['sha1'],val)
        if len(tmp) != 0:
            retval.extend(tmp)
    if type is None or type == 'hash' or type == 'sha256':
        tmp = re.findall(pattern['sha256'],val)
        if len(tmp) != 0:
            retval.extend(tmp)
    if type is None or type == 'cve':
        retval.extend(re.findall(pattern['cve'],val))
    if type is None or type == 'registry':
        retval.extend(re.findall(pattern['registry'],val))
    if type is None or type == 'filenme':
        retval.extend(re.findall(pattern['filenme'],val))
    if type is None or type == 'filepath':
        retval.extend(re.findall(pattern['filepath'],val))
    
    if len(retval) == 0:
        return None
    else:
        return retval


def checkIoCType(ioc):
    if len(re.findall(pattern['url'],ioc)) > 0:
        return 'url'
    if len(re.findall(pattern['host'],ioc)) > 0:
        return 'host'
    if len(re.findall(pattern['ip'],ioc)) > 0:
        return 'ip'
    if len(re.findall(pattern['email'],ioc)) > 0:
        return 'email'
    if len(re.findall(pattern['md5'],ioc)) > 0:
        return 'md5'
    if len(re.findall(pattern['sha1'],ioc)) > 0:
        return 'sha1'
    if len(re.findall(pattern['sha256'],ioc)) > 0:
        return 'sha256'
    if len(re.findall(pattern['cve'],ioc)) > 0:
        return 'cve'
    if len(re.findall(pattern['registry'],ioc)) > 0:
        return 'registry'
    if len(re.findall(pattern['filenme'],ioc)) > 0:
        return 'filenme'
    return
    
    
################################################################
# check if the input value is a hash value; md5, sha1, or sha256 
# @ inputs
#    val: the input value
# @ outputs:
#    the hash type if the value is a hash, otherwise return False.  
def isHash(val):
    val = val.encode('utf-8')
    l = len(val)
    if l == 32:
        return 'MD5'
    if l == 40:
        return 'SHA1'
    if l == 64:
        return 'SHA256'
    return False 

################################################################
# Get file timestamp from visutotal site. 
# @ inputs
#    sha256: the hash value to get timestamp
# @ outputs:
#    The timestamp value if it is found.
# @ Caution
#    If this function is called several times continuously, virustotal site block the request thinking that it is not valid request.
def getFileTimestamp(sha256):
    _headers = {"Encoding": "gzip, deflate","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    response = requests.get('https://www.virustotal.com/en/file/'+sha256+'/analysis/#item-detail', headers = _headers)
    tmp = response.text.encode('utf-8')
    if tmp.find('The file you are looking for is not in our database'):
        return False
    
    i = tmp.find('Compilation timestamp')+len('Compilation timestamp</span> ')
    return tmp[i:i+10]
