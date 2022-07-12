# def change_friends(request, operation, pk):
#     friend = User.objects.get(pk=pk)
#     if operation == 'add':
#         Friend.make_friend(request.user, friend)
#     elif operation == 'remove':
#         Friend.lose_friend(request.user, friend)
#     return redirect('home:home')
