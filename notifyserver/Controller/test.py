from webob.exc import HTTPAccepted, HTTPBadRequest, HTTPCreated, \
     HTTPInternalServerError, HTTPNoContent, HTTPNotFound, \
     HTTPNotModified, HTTPPreconditionFailed, HTTPOk, \
     HTTPRequestTimeout, HTTPUnprocessableEntity, HTTPMethodNotAllowed, \
     HTTPServiceUnavailable, HTTPUnauthorized

from fileop.FileOp import FileOp

#from Controller.base import Controller

class TestController(object):
    def __init__(self, app ):
        #Controller.__init__(self, app)
        
        print '------haha--------'
        pass

    def PUT(self, req):
        print '-----into put--------'
        user_info = ['test']
        filepath='/tmp/haha/a.txt'
        fop = FileOp(user_info, filepath, req)
        ret = fop.uploadData()
        print 'into get ----------------'
        
        #return HTTPOk(body ='TestController Running',content_type='application/json')
        return ret

    def GET(self, req):
        print '-----into get--------'
        user_info = ['test']
        filepath='/tmp/haha/a.txt'
        fop = FileOp(user_info, filepath, req)
        ret = fop.downloadData()
        print 'into get ----------------'
        
        #return HTTPOk(body ='download over----',content_type='application/json')
        return ret
