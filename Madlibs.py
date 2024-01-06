# #string concatination (how to put string together)
# #suppose we want to create a string that says "subscribe to _______"
# youtuber="Farah Maqbool"#some string variable
# #a few ways to do this
# print("subscribe to" + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
name=input("Enter your name: ")
adj1=input("Adjective: ")
place=input("Place: ")
dish=input("Dish: ")
madlib=f"Hey Myself {name}. Iam very {adj1} to know that you are coming at my {place}. so I am preparing you favourite \
dish {dish}. I hope you enjoy it."
print(madlib)