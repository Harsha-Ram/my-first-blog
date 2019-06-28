from django.shortcuts import render
	
def post_list(request):
    return render(request, 'blog/post_list.html', {})

#Function post_list is created where post_list takes request and will return the value
#that gets from render function that will render our template blog/post_list.html
