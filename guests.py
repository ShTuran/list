guests = ["Anar", "Rufet", "Ali"]
message_Anar= "I'd like to invite you my bd party, Anar\n"
message_Rufet = "I'd like to invite you my bd party, Rufet\n"
message_Ali =  " I'd like to invite you my bd party, Ali\n"
print(message_Ali, message_Anar, message_Rufet)

CantCome_Rufet = guests.remove("Rufet")
print("Cannot come:Rufet")
guests.insert(1, "Nazim")

print(guests)
print("\n")

message_Anar = "I'd like to invite you my bd party, Anar\n"
message_Nazim =  "I'd like to invite you my bd party, Nazim\n"
message_Ali = "I'd like to invite you my bd party, Ali\n"
print(message_Ali, message_Anar, message_Nazim)

guests.insert(0, "Asad")
guests.insert(1, "Namiq")
guests.append("Zaur")

message_Asad =  "I'd like to invite you my bd party, Asad\n"
message_Nmaiq =  "I'd like to invite you my bd party, Namiq\n"
message_Zaur =  "I'd like to invite you my bd party, Zaur\n"


print(f"Our guests number are incresed, here our dinner table list: \n")
print(guests)

cancelled_guest = guests.pop(0)
cancelled_guest = guests.pop(1)
cancelled_guest = guests.pop(2)
cancelled_guest = guests.pop(2)


message_sorry = "I am sorry whom I cancelled their invitation, here new invitation list:"
print(message_sorry)
print("\n")
print(guests)

print("Anar and Nazim are still in our guest list!")


print(guests)