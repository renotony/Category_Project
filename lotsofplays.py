from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Plays, Base, Characters, User

engine = create_engine('sqlite:///plays.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

User1 = User(name='Tony DeGeiso', email='tonydegeiso@gmail.com', picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

play1 = Plays(user_id=1, title="Barefoot In The Park")

session.add(play1)
session.commit()

character1 = Characters(user_id=1, name="Corie Bratter", description="a free spirit, newlywed to Paul",
                     play=play1)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Paul Bratter", description="a lawyer, newlywed to Corie",
                     play=play1)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Mrs. Banks", description="Corie's mother",
                     play=play1)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Victor Velasco", description="the neighbor in the attic",
                     play=play1)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Telephone Repair Man", description="comes to fix telephone",
                     play=play1)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Delivery Man", description="delivers furniture",
                     play=play1)

session.add(character6)
session.commit()

play2 = Plays(user_id=1, title="They're Playing Our Song")

session.add(play2)
session.commit()

character1 = Characters(user_id=1, name="Vernon Gersch", description="an established composer",
                     play=play2)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Sonia Walsk", description="a young lyracist",
                     play=play2)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Voices of Vernon Gersch", description="chorus 3 men",
                     play=play2)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Voices of Sonia Walsk", description="chorus 3 women",
                     play=play2)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Voice of Phil the Engineer", description="chours 1 man",
                     play=play2)

session.add(character5)
session.commit()

play3 = Plays(user_id=1, title="Rumors")

session.add(play3)
session.commit()

character1 = Characters(user_id=1, name="Ken Gorman", description="(40) A well-to-do lawyer. Wealthy, but by no means pretentious. Takes charge of the situation. Married to Chris. Halfway through the show, a gunshot causes his temporary deafness.",
                     play=play3)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Chris Gorman", description="(mid-30s) Another lawyer, married to Ken. Beautiful, easily flustered. Frantically tries to maintain normalcy at the party. Has recently quit smoking, which drives her to drink a bit more.",
                     play=play3)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Lenny Ganz", description="(Late 30s, early 40s) A wealthy accountant, distraught over the recent destruction of his new car. Starts the show with an extreme case of whiplash. Intolerant of the gossipy-lifestyle that he is often involved in.",
                     play=play3)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Claire Ganz", description="(Late 30s) Lenny's wife. Very concerned with appearances (hers and others'). Starts the play with a swollen lip. Likes to gossip.",
                     play=play3)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Ernie Cusack", description="(Early 50s) A psychiatrist. Affable, smokes a pipe. Loves his wife very much. Tries to be as helpful as possible cooking the evening's dinner.",
                     play=play3)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Cookie Cusack", description="(40s) Has her own cooking show. Suffers from extreme back spasms. Loves her husband very much. A bit absent-minded at times.",
                     play=play3)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Glenn Cooper", description="(30-40) A handsome man running for State Senate. Worried about his own reputation. Struggles with placating his wife, who is convinced he is having an affair (which he may or may not be).",
                     play=play3)

session.add(character7)
session.commit()

character8 = Characters(user_id=1, name="Cassie Cooper", description="(late 20s, early 30s) Glenn's beautiful wife. Obsesses over her husband's relationships with other women. Quick to anger. Must rub her quartz crystal to calm herself down.",
                     play=play3)

session.add(character8)
session.commit()

character9 = Characters(user_id=1, name="Officer Welch", description="(M) - (30-50) A city police officer having a rough night. Does not tolerate lying. Sees through the classy facade that these high-society types put up.",
                     play=play3)

session.add(character9)
session.commit()

character10 = Characters(user_id=1, name="Officer Pudney", description="(F) - (20-30) Welch's partner. A strong but silent type.",
                     play=play3)

session.add(character10)
session.commit()

play4 = Plays(user_id=1, title="Rose's Dilemma")

session.add(play4)
session.commit()

character1 = Characters(user_id=1, name="Rose", description="a struggling writer",
                     play=play4)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Arlene", description="Rose's daughter and her assistant",
                     play=play4)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Walsh", description="Rose's former lover, a ghost",
                     play=play4)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Clancy", description="an aspiring young novelist",
                     play=play4)

session.add(character4)
session.commit()

play5 = Plays(user_id=1, title="Lost In Yonkers")

session.add(play5)
session.commit()

character1 = Characters(user_id=1, name="Jay", description="16",
                     play=play5)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Arty", description="13 1/2",
                     play=play5)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Eddie", description="Their father, 41",
                     play=play5)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Bella", description="mid-thirties, neat and sweet and pretty",
                     play=play5)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Grandma Kurnitz", description="Eddie and Bella's mother, a big woman, buxom, with a strong and erect body, 70 odd years of age",
                     play=play5)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Louie", description="her other son, 36, doesn't look like he'd be the hugging type",
                     play=play5)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Aunt Gert", description="mid-to-late thirties, another of Grandma Kurnitz's children",
                     play=play5)

session.add(character7)
session.commit()

play6 = Plays(user_id=1, title="Brighton Beach Memoirs")

session.add(play6)
session.commit()

character1 = Characters(user_id=1, name="Eugene", description="almost 15",
                     play=play6)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Blanche", description="38",
                     play=play6)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Kate Jerome", description="40 year-old, Blanche's sister, Eugene's mother",
                     play=play6)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Laurie", description="13",
                     play=play6)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Nora", description="her sister, lovely at 16",
                     play=play6)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Stanley Jerome", description="18",
                     play=play6)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Jacob 'Jack' Jerome", description="about 40, Eugene's father",
                     play=play6)

session.add(character7)
session.commit()

play7 = Plays(user_id=1, title="Rose and Walsh")

session.add(play7)
session.commit()

character1 = Characters(user_id=1, name="Rose Steiner", description="She is 64 years old. A Pulitzer-prize winning playwright",
                     play=play7)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Walsh McLaren", description="He is in his mid fifties. A famous mystery writer",
                     play=play7)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Arlene Moss", description="34, Rose's assistant",
                     play=play7)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Gavin Clancy", description="mid 30s. A young, talented, writer",
                     play=play7)

session.add(character4)
session.commit()

play8 = Plays(user_id=1, title="Flora, The Red Menace")

session.add(play8)
session.commit()

character1 = Characters(user_id=1, name="Flora Meszaros", description="A young fashion illustrator, full of hope, optimism, and a desire to take over the world. She is absolutely guileless, willing to take on any challenge, without a trace of brassiness.",
                     play=play8)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Harry Toukarian", description="A shy, intense, oddly handsome artist. He stammers, especially when he is nervous. He has a romantic vision of how to make society perfect.",
                     play=play8)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Charlotte", description="A bit of a misfit, a party zealot,  she is determined to spread Communism singlehandedly. She is dry, droll -- the quintessential comic villian.",
                     play=play8)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Willy", description="Very boyish, spirited. A songwriter who plays the clarinet, Willy, in a sense, serves as the narrator of the play.",
                     play=play8)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Elsa", description="Extremely practical, pulled together, she has aspirations to be a fashion designer and has yet to get up the nerve to get her sketches around town.",
                     play=play8)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Mr. Weiss", description="A former Communist who has lost his jewelry shop to the Depression, he is kindly, knowing.",
                     play=play8)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Maggie", description="Very innocent. Honest. Maggie came to New York from Oklahoma following a dust storm. She is now trying to get a break with her dance partner, Kenny.",
                     play=play8)

session.add(character7)
session.commit()

character8 = Characters(user_id=1, name="Kenny", description="Moving with Ray Bolger-like limberness and comedy, he is very serious about his dancing and determined to get ahead.",
                     play=play8)

session.add(character8)
session.commit()

character9 = Characters(user_id=1, name="Mr. Stanley", description="Arrow Shirt Collar-perfect. The perfect department store executive. Easily disliked.",
                     play=play8)

session.add(character9)
session.commit()

play9 = Plays(user_id=1, title="Chicago")

session.add(play9)
session.commit()

character1 = Characters(user_id=1, name="Velma Kelley", description="Female, 25-40 (Range: Alto, E3-D5) Vaudville performer who is accused of murdering her sister and husband. Hardened by fame, she cares for no one but herself and her attempt to get away with murder.",
                     play=play9)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Roxie Hart", description="Female, 20-30 (Range: Mezzo-Soprano, F3-B4) Reads and keeps up with murder trials in Chicago, and follows suit by murdering her lover, Fred Casely. She stops at nothing to render a media storm with one goal: to get away with it.",
                     play=play9)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Fred Casely", description="Male, 30-50 (Range: Ensemble/Part Flexible) Roxie's short lived lover. Murdered for trying to leave Roxie.",
                     play=play9)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Sergeant Fogarty", description=" Male, 35-55 (Range: Ensemble/Part Flexible) Assigned to Roxie's case. After asking the right questions, he manages to get Roxie to confess.",
                     play=play9)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Amos Hart", description="Male, 30-50 (Range: Baritone, C3-F#4) Roxie's faithful husband. Lies for her and tries to take the blame until he realizes that he has been two-timed by Roxie. Still in love with her, or misguided, he believes anything she says in her pursuit to get out of jail.",
                     play=play9)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Liz", description=" Female, 18-45 (Range: Ensemble, A3-C#5) Prisoner at Cook County Jail. She is imprisoned after shooting two warning shots into her husband's head.",
                     play=play9)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Annie", description="Female, 18-45 (Range: Ensemble, A3-C#5) Prisoner at the Cook County Jail. Murders her lover after finding out he already has six wives. One of those Mormons, ya know.",
                     play=play9)

session.add(character7)
session.commit()

character8 = Characters(user_id=1, name="June", description="Female, 18-45 (Range: Ensemble, A3-C#5) Prisoner at Cook County Jail. After her husband accuses her of screwing the milk man, he mysteriously runs into her knife ten times.",
                     play=play9)

session.add(character8)
session.commit()

character9 = Characters(user_id=1, name="Hunyak", description="Female, 25-45 (Range: Non-Singing Role) Hungarian Prisoner at Cook County Jail. The only English she speaks is the phase, Not Guilty. Which follows her to her grave.",
                     play=play9)

session.add(character9)
session.commit()

character10 = Characters(user_id=1, name="Mona", description="Female, 18-45 (Range: Ensemble, A3-C#5) Prisoner at Cook County Jail. Murders her lover after he has a round of affairs with other woman, and an occasional man. I guess you could say it was artistic differences.",
                     play=play9)

session.add(character10)
session.commit()

character11 = Characters(user_id=1, name="Martin Harrison", description="Male, 35-55 (Range: Ensemble/Part Flexible) Ensemble member who doubles as the Master of Ceremonies at times.",
                     play=play9)

session.add(character11)
session.commit()

character12 = Characters(user_id=1, name="Matron 'Mama' Morton", description="Female, 30-50 (Range: Alto, F#3-Bb4) Leader of the prisoners of Cook County Jail. The total essence of corruption. Accepts bribes for favors from laundry service to making calls to lawyers. When you're good to Mama, Mama's good to you.",
                     play=play9)

session.add(character12)
session.commit()

character13 = Characters(user_id=1, name="Billy Flynn", description="Male, 35-50 (Range: Baritone Bb2-G4) Established lawyer who hasn't lost a woman's case yet. Master of media manipulation who will get a girl off the hook as long as she can fork up the hefty $5,000 fee.",
                     play=play9)

session.add(character13)
session.commit()

character14 = Characters(user_id=1, name="Mary Sunshine", description="Female, 25-55 (Range: Soprano, Bb3-Bb5) Sob sister reporter from the Evening Star. Believes there is a little bit of good in everyone and will believe anything she is fed that matches her beliefs.",
                     play=play9)

session.add(character14)
session.commit()

character15 = Characters(user_id=1, name="Go-To-Hell-Kitty", description="Female, 21-40 (Range: Ensemble, A3-C#5) Steals the spotlight when she Murders her husband along with three other woman. Her crimes are labeled Lake Shore Drive Massacre.",
                     play=play9)

session.add(character15)
session.commit()

character16 = Characters(user_id=1, name="Harry", description="(Range: Ensemble/Part Flexible) Murdered by Go-To-Hell Kitty for sleeping around with three women behind her back.",
                     play=play9)

session.add(character16)
session.commit()

character17 = Characters(user_id=1, name="Aaron", description="(Range: Ensemble/Part Flexible) Court appointed lawyer for Hunyak. He tries to get her to confess to speed along the trial.",
                     play=play9)

session.add(character17)
session.commit()

character18 = Characters(user_id=1, name="Judge", description="Male, 40-65 (Range: Ensemble/Part Flexible) Judge overseeing Roxie's Trial.",
                     play=play9)

session.add(character18)
session.commit()

character19 = Characters(user_id=1, name="Court Clerk", description="(Range: Ensemble/Part Flexible) Swears people in with their hand on the bible. Blah, Blah, Truth, Truth. Selp-you God.",
                     play=play9)

session.add(character19)
session.commit()

character20 = Characters(user_id=1, name="Chorus", description="SATB",
                     play=play9)

session.add(character20)
session.commit()

play10 = Plays(user_id=1, title="Steel Pier")

session.add(play10)
session.commit()

character1 = Characters(user_id=1, name="Bill Kelly", description="Late 30s. A dare-devil who has crashed his plane. Ever since he first saw Rita at an airshow, he has been in love with her. He is a hot-dog flyer. An American classic. Someone who still believes in the power of having a dream. Strong tenor with good high notes - Ab.",
                     play=play10)

session.add(character1)
session.commit()

character2 = Characters(user_id=1, name="Rita Racine", description="Late 30s. Was Lindy's Lovebird - the first woman to kiss Lindbergh when he crossed the Atlantic. Was the darling of the press and the Vaudeville circuit. Over the last few years, however, she has been performing in stage shows...side shows...air shows. And now, as the Depression takes hold of the country - dance marathons. Rita is full of life. Wildly charismatic. And vulnerable. High belt with a good mix.",
                     play=play10)

session.add(character2)
session.commit()

character3 = Characters(user_id=1, name="Shelby Stevens", description="40s. She is one of the marathon's featured performers. Quick. Dry. Biting. Everyone's Girl. Loves the life of the marathon dancer. Loves the marathons. She dances with Luke. Strong low belt with a good head voice.",
                     play=play10)

session.add(character3)
session.commit()

character4 = Characters(user_id=1, name="Mick Hamilton", description="40s. The marathon's promoter. He serves as the marathon's master of ceremonies. Smooth. Stylish. Performs for the crowds. He has fought all his life for what he has been able to call his own. Beneath the polish, he's a street fighter - willing to do anything to get what he wants. Baritone with a strong F.",
                     play=play10)

session.add(character4)
session.commit()

character5 = Characters(user_id=1, name="Mr. Walker", description="55-60. The floor judge. He has been traveling with Michk to the different marathons. A kind man in a dirty business. He is Mick's henchman - the go-between. Must sing. High tenor.",
                     play=play10)

session.add(character5)
session.commit()

character6 = Characters(user_id=1, name="Buddy Becker", description="40-45. Vaudevillian. A non-stop talker. Always quick with a story. Even if no wants to hear it. Oblivious to those around him. Dances with his sister, Bette. Tenor.",
                     play=play10)

session.add(character6)
session.commit()

character7 = Characters(user_id=1, name="Bette Becker", description="35-40. Buddy's sister. Always tries to be optimistic. Tries to see the bright side of everything. Must sing.",
                     play=play10)

session.add(character7)
session.commit()

character8 = Characters(user_id=1, name="Johnny Adel", description="Early 30s. An athlete. Imposing. Someone who wrestled in the Olympics. Sees the marathon as just another sport. Disciplined. Someone who would probably win. Dances with Dora. Baritone.",
                     play=play10)

session.add(character8)
session.commit()

character9 = Characters(user_id=1, name="Dora Foster", description="45-50. An attractive woman who at one time in her life had money. Now she has nothing. Still tries to keep up the facade. Dances with Johnny Adel. Mezzo.",
                     play=play10)

session.add(character9)
session.commit()

character10 = Characters(user_id=1, name="Happy McGuire", description="Early 20s. Precious' husband. Raised on a farm. Strapping. Despite his youth and inexperience, he is much smarter - and even more worldly - than he appears. Lyric baritone.",
                     play=play10)

session.add(character10)
session.commit()

character11 = Characters(user_id=1, name="Precious McGuire", description="The young newlywed. Married to Happy. On the surface seems innocent. Wide-eyed. Fresh. She is however, drive, steely. Determined to get her show so that she never has to return home. Soprano with a lovely high C and an E above that, if possible.",
                     play=play10)

session.add(character11)
session.commit()

character12 = Characters(user_id=1, name="Luke Adams", description="30-35. Quiet. Keeps to himself. Plays instruments. Must play at least one of the following instruments proficiently: harmonica, fiddle, guitar, ukulele, concertina, accordion. Dances with Shelby.",
                     play=play10)

session.add(character12)
session.commit()

character13 = Characters(user_id=1, name="Mick's Picks", description="3 women who sing back-up for Mick during the radio show. They must be oustanding singers with talent for blending and singing tight harmony. Two sopranos. One alto. Must also be able to dance.",
                     play=play10)

session.add(character13)
session.commit()

character14 = Characters(user_id=1, name="Corky", description="Corky",
                     play=play10)

session.add(character14)
session.commit()

character15 = Characters(user_id=1, name="Dr. Johnson", description="Dr. Johnson",
                     play=play10)

session.add(character15)
session.commit()

character16 = Characters(user_id=1, name="Sonny", description="Sonny",
                     play=play10)

session.add(character16)
session.commit()

character17 = Characters(user_id=1, name="Preacher", description="Preacher",
                     play=play10)

session.add(character17)
session.commit()

character18 = Characters(user_id=1, name="The Flying Dunlaps", description="5 actors",
                     play=play10)

session.add(character18)
session.commit()

character19 = Characters(user_id=1, name="Chorus", description="the dancers in the marathon. Must be outstanding dancers who can sing. They must also span a wide range of types and ages. 5 women and 8 men.",
                     play=play10)

session.add(character19)
session.commit()

print('Added new plays!')
