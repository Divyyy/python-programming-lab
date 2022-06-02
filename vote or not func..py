def vote(age):
    if age >= 18:
        return 'you can vote'
    else:
        return 'you r not able to can vote'
a = int(input("Enter your age :"))
out = vote(a)
print(out)
