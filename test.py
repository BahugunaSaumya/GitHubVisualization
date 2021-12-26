from github import Github


g= Github("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")
usr = g.get_user()
if usr.login is not None:
 print("user:" + usr.login)
if usr.name is not None:
 print("fullname: " +usr.name)
if usr.location is not None:
  print("location: " +usr.location)
if usr.company is not None:
  print("company: " +usr.company)