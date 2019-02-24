
def me(con) :
	for post in con :
		print(post)

posts = [
	{
		'author' : 'PremK',
		'title' : 'blog post 1',
		'content' : 'first post content',
		'date_posted' : 'Aug,27,2018'
	},
	{
		'author' : 'SuseeK',
		'title' : 'blog post 2',
		'content' : 'second post content',
		'date_posted' : 'dec,27,2018'
	}
]

context = { 'posts' : posts }

if __name__  == '__main__' :
 	me(context)