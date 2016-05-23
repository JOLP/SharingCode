# -*- coding: utf-8 -*-
# Create your views here.
#from django.template.loader import get_template  
#from django.template import Template, Context  
#from django.http import Http404, HttpResponse  
from django.shortcuts import render_to_response
from django.utils import timezone
from sb.models import DjangoBoard
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from sb.pagingHelper import pagingHelper
from django.db import connection


rowsPerPage = 10

def home(request):   
	boardList = DjangoBoard.objects.order_by('-id')[0:10]        
	current_page =1
	totalCnt = DjangoBoard.objects.all().count() 
	
	pagingHelperIns = pagingHelper();
	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
	print 'totalPageList', totalPageList
	
	return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
														'current_page':current_page ,'totalPageList':totalPageList} ) 
	
#===========================================================================================
def show_write_form(request):
	return render_to_response('writeBoard.html')  

#===========================================================================================
@csrf_exempt
def DoWriteBoard(request):
	br = DjangoBoard(
					subject = request.POST['subject'],
					  name = request.POST['name'],
					  mail = request.POST['email'],
					  memo = request.POST['memo'],
					  created_date = timezone.now(),
					  hits = 0
					 )
	br.save()
	
	url = '/listSpecificPageWork?current_page=1' 
	return HttpResponseRedirect(url)    
				   

#===========================================================================================
def viewWork(request):
	pk= request.GET['memo_id']    
	#print 'pk='+ pk
	boardData = DjangoBoard.objects.get(id=pk)
	#print boardData.memo
	
	# Update DataBase
	print 'boardData.hits', boardData.hits
	DjangoBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)
	  
	return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'], 
												'current_page':request.GET['current_page'], 
												'searchStr': request.GET['searchStr'], 
												'boardData': boardData } )            
   
#===========================================================================================
def listSpecificPageWork(request):    
	current_page = request.GET['current_page']
	totalCnt = DjangoBoard.objects.all().count()                  
	
	print 'current_page=', current_page
	
	boardList = DjangoBoard.objects.raw('SELECT Z.* FROM(SELECT X.*, ceil((rownum/%s) as page FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS FROM sb_DJANGOBOARD ORDER BY ID DESC ) X ) Z WHERE page = %s', [rowsPerPage, current_page])
		
	print  'boardList=',boardList, 'count()=', totalCnt
	
	pagingHelperIns = pagingHelper();
	
	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
		
	print 'totalPageList', totalPageList
	
	return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
														'current_page':int(current_page) ,'totalPageList':totalPageList} )

#===========================================================================================

def listSpecificPageWork_to_update(request):
	memo_id = request.GET['memo_id']
	current_page = request.GET['current_page']
	searchStr = request.GET['searchStr']
	
	#totalCnt = DjangoBoard.objects.all().count()
	print 'memo_id', memo_id
	print 'current_page', current_page
	print 'searchStr', searchStr
	
	boardData = DjangoBoard.objects.get(id=memo_id)
	  
	return render_to_response('viewForUpdate.html', {'memo_id': request.GET['memo_id'], 
												'current_page':request.GET['current_page'], 
												'searchStr': request.GET['searchStr'], 
												'boardData': boardData } )    

@csrf_exempt
def updateBoard(request):
	memo_id = request.POST['memo_id']
	current_page = request.POST['current_page']
	searchStr = request.POST['searchStr']        
		
	print '#### updateBoard ######'
	print 'memo_id', memo_id
	print 'current_page', current_page
	print 'searchStr', searchStr
	
	# Update DataBase
	DjangoBoard.objects.filter(id=memo_id).update(
												  mail= request.POST['mail'],
												  subject= request.POST['subject'],
												  memo= request.POST['memo']
												  )
	
  
	url = '/listSpecificPageWork?current_page=' + str(current_page)
	return HttpResponseRedirect(url)    
	  
def DeleteSpecificRow(request):
	memo_id = request.GET['memo_id']
	current_page = request.GET['current_page']
	print '#### DeleteSpecificRow ######'
	print 'memo_id', memo_id
	print 'current_page', current_page
	
	p = DjangoBoard.objects.get(id=memo_id)
	p.delete()
	
	# Display Page    

	totalCnt = DjangoBoard.objects.all().count()  
	pagingHelperIns = pagingHelper();
	
	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
	print 'totalPages', totalPageList
	
	if( int(current_page) in totalPageList):
		print 'current_page No Change'
		current_page=current_page
	else:
		current_page= int(current_page)-1
		print 'current_page--'            
			
	url = '/listSpecificPageWork?current_page=' + str(current_page)
	return HttpResponseRedirect(url)    

@csrf_exempt
def searchWithSubject(request):
	searchStr = request.POST['searchStr']
	print 'searchStr', searchStr
	
	url = '/listSearchedSpecificPageWork?searchStr=' + searchStr +'&pageForView=1'
	return HttpResponseRedirect(url)    
		     
def listSearchedSpecificPageWork(request):
	searchStr = request.GET['searchStr']
	pageForView = request.GET['pageForView']
	print 'listSearchedSpecificPageWork:searchStr', searchStr, 'pageForView=', pageForView
		
	#boardList = DjangoBoard.objects.filter(subject__contains=searchStr)
	#print  'boardList=',boardList
	
	totalCnt = DjangoBoard.objects.filter(subject__contains=searchStr).count()
	print  'totalCnt=',totalCnt
	
	pagingHelperIns = pagingHelper();
	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
	
	 
	boardList = DjangoBoard.objects.raw("""SELECT Z.* FROM ( SELECT X.*, ceil(rownum/ %s) as page \
		FROM ( SELECT ID,SUBJECT,NAME, CREATED_DATE, MAIL,MEMO,HITS FROM SB_DJANGOBOARD \
		WHERE SUBJECT LIKE '%%'||%s||'%%' ORDER BY ID DESC) X ) Z WHERE page = %s""", [rowsPerPage, searchStr, pageForView])
		
	print'boardList=',boardList
	
	return render_to_response('listSearchedSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt, 
														'pageForView':int(pageForView) ,'searchStr':searchStr, 'totalPageList':totalPageList} )            
	 


