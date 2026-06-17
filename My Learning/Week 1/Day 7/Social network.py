# Social network
print()
print("SOCIAL NETWORK ANALYZER\n")

jatin_friends = {"Ravi", "Amit", "Sahil", "Pooja", "Karan", "Neha"}
ravi_friends = {"Jatin", "Amit", "Karan", "Vikram", "Rohit"}
amit_friends = {"Jatin", "Ravi", "Sahil", "Vikram", "Pooja"}
print(f"Jatin's friends: {jatin_friends}")
print(f"Ravi's friends: {ravi_friends}")
print(f"Amit's friends: {amit_friends}")

mutual_jr = jatin_friends & ravi_friends
print(f"Mutual(Jatin & Rahul): {mutual_jr}")

all_people = jatin_friends | ravi_friends | amit_friends
print(f"Total Network: {all_people}")
print(f"Network size: {len(all_people)}")

jatin_only = jatin_friends - ravi_friends
print(f"Jatin knows but ravi doesn't: {jatin_only}")

not_common = jatin_friends ^ amit_friends
print(f"Not common(Jatin XOR Amit): {not_common}")

suggestions = (ravi_friends | amit_friends) - jatin_friends - {"jatin"}
print(f"Suggestions for jatin: {suggestions}")

print(f"\n🔍 Do Jatin and Ravi share any friends? {not jatin_friends.isdisjoint(ravi_friends)}")


print(f"Is Amit's network part of total? {amit_friends.issubset(all_people)}")