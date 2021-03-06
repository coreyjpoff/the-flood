from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Article, Author, ArticleAuthor, ArticleResource
from datetime import date
engine = create_engine('sqlite:///flood.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

res1 = ArticleResource(
  name="photo1",
  article_id="2",
  caption="Photo essay entry 1",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/92016001-Edit.jpg",
  is_title_img=True
)

res2 = ArticleResource(
  name="photo2",
  article_id="2",
  caption="Photo essay entry 2",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316003-Edit.jpg",
  is_title_img=False
)

res3 = ArticleResource(
  name="photo3",
  article_id="2",
  caption="Photo essay entry 3",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316002-Edit.jpg",
  is_title_img=False
)

res4 = ArticleResource(
  name="photo4",
  article_id="2",
  caption="Photo essay entry 4",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316006-Edit.jpg",
  is_title_img=False
)

res5 = ArticleResource(
  name="photo5",
  article_id="2",
  caption="Photo essay entry 5",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006034-Edit-2-Edit.jpg",
  is_title_img=False
)

res6 = ArticleResource(
  name="photo6",
  article_id="2",
  caption="Photo essay entry 6",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006235-Edit.jpg",
  is_title_img=False
)

res7 = ArticleResource(
  name="photo7",
  article_id="2",
  caption="Photo essay entry 7",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006213-Edit-2.jpg",
  is_title_img=False
)

res8 = ArticleResource(
  name="photo8",
  article_id="2",
  caption="Photo essay entry 8",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006314-Edit.jpg",
  is_title_img=False
)

res9 = ArticleResource(
  name="photo9",
  article_id="2",
  caption="Photo essay entry 9",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0005990-Edit-Edit.jpg",
  is_title_img=False
)

res10 = ArticleResource(
  name="photo10",
  article_id="2",
  caption="Photo essay entry 10",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316004-Edit.jpg",
  is_title_img=False
)

res11 = ArticleResource(
  name="photo11",
  article_id="2",
  caption="Photo essay entry 11",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006159-Edit-Edit-4.jpg",
  is_title_img=False
)

res12 = ArticleResource(
  name="photo12",
  article_id="2",
  caption="Photo essay entry 12",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316010-Edit.jpg",
  is_title_img=False
)

res13 = ArticleResource(
  name="photo13",
  article_id="2",
  caption="Photo essay entry 13",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0005953-Edit-2-Edit.jpg",
  is_title_img=False
)

res14 = ArticleResource(
  name="photo14",
  article_id="2",
  caption="Photo essay entry 14",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006217-Edit-2.jpg",
  is_title_img=False
)

res15 = ArticleResource(
  name="photo15",
  article_id="2",
  caption="Photo essay entry 15",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/bread.jpg",
  is_title_img=False
)

res16 = ArticleResource(
  name="photo16",
  article_id="2",
  caption="Photo essay entry 16",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/IMG_3636-Edit-2.jpg",
  is_title_img=False
)

res17 = ArticleResource(
  name="photo17",
  article_id="2",
  caption="Photo essay entry 17",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/recipe.jpg",
  is_title_img=False
)

res18 = ArticleResource(
  name="photo18",
  article_id="2",
  caption="Photo essay entry 18",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/R0006208-Edit-2.jpg",
  is_title_img=False
)

res19 = ArticleResource(
  name="photo19",
  article_id="2",
  caption="Photo essay entry 19",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/river.jpg",
  is_title_img=False
)

res20 = ArticleResource(
  name="photo20",
  article_id="2",
  caption="Photo essay entry 20",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316013-Edit.jpg",
  is_title_img=False
)

res21 = ArticleResource(
  name="photo21",
  article_id="2",
  caption="Photo essay entry 21",
  resource_type="JPG",
  resource_location="/static/articles/2/Photos/100316011-Edit.jpg",
  is_title_img=False
)

res22 = ArticleResource(
    name="photo22",
    article_id="2",
    caption="Photo essay entry 22",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006198-Edit.jpg",
    is_title_img=False
)

res23 = ArticleResource(
  name="photo23",
  article_id="2",
  caption="Photo essay entry 23",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/grattan.jpg",
  is_title_img=False
)

res24 = ArticleResource(
    name="photo24",
    article_id="2",
    caption="Photo essay entry 24",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006232-Edit.jpg",
    is_title_img=False
)

res25 = ArticleResource(
    name="photo25",
    article_id="2",
    caption="Photo essay entry 25",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006160-Edit.jpg",
    is_title_img=False
)

res26 = ArticleResource(
  name="photo26",
  article_id="2",
  caption="Photo essay entry 26",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/horrors.jpg",
  is_title_img=False
)

res27 = ArticleResource(
    name="photo27",
    article_id="2",
    caption="Photo essay entry 27",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006305-Edit.jpg",
    is_title_img=False
)

res28 = ArticleResource(
    name="photo28",
    article_id="2",
    caption="Photo essay entry 28",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006161-Edit.jpg",
    is_title_img=False
)

res29 = ArticleResource(
  name="photo29",
  article_id="2",
  caption="Photo essay entry 29",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/By God.jpg",
  is_title_img=False
)

res30 = ArticleResource(
    name="photo30",
    article_id="2",
    caption="Photo essay entry 30",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006170-Edit-2.jpg",
    is_title_img=False
)

res31 = ArticleResource(
    name="photo31",
    article_id="2",
    caption="Photo essay entry 31",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006276-Edit.jpg",
    is_title_img=False
)

res32 = ArticleResource(
  name="photo32",
  article_id="2",
  caption="Photo essay entry 32",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/coffin.jpg",
  is_title_img=False
)

res33 = ArticleResource(
    name="photo33",
    article_id="2",
    caption="Photo essay entry 33",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/100316009-Edit.jpg",
    is_title_img=False
)

res34 = ArticleResource(
    name="photo34",
    article_id="2",
    caption="Photo essay entry 34",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/92016004-Edit.jpg",
    is_title_img=False
)

res35 = ArticleResource(
  name="photo35",
  article_id="2",
  caption="Photo essay entry 35",
  resource_type="JPG",
  resource_location="/static/articles/2/Handwriting/crazy.jpg",
  is_title_img=False
)

res36 = ArticleResource(
    name="photo36",
    article_id="2",
    caption="Photo essay entry 36",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0005909-Edit-Edit.jpg",
    is_title_img=False
)

res37 = ArticleResource(
    name="photo37",
    article_id="2",
    caption="Photo essay entry 37",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/92016009-Edit.jpg",
    is_title_img=False
)

res38 = ArticleResource(
    name="photo38",
    article_id="2",
    caption="Photo essay entry 38",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/92016010-Edit.jpg",
    is_title_img=False
)

res39 = ArticleResource(
    name="photo39",
    article_id="2",
    caption="Photo essay entry 39",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/92016004-Edit-2.jpg",
    is_title_img=False
)

res40 = ArticleResource(
    name="photo40",
    article_id="2",
    caption="Photo essay entry 40",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006239-Edit.jpg",
    is_title_img=False
)

res41 = ArticleResource(
    name="photo41",
    article_id="2",
    caption="Photo essay entry 41",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/R0006050-Edit.jpg",
    is_title_img=False
)

res42 = ArticleResource(
    name="photo42",
    article_id="2",
    caption="Photo essay entry 42",
    resource_type="JPG",
    resource_location="/static/articles/2/Photos/92016006-Edit.jpg",
    is_title_img=False
)

for i in range(15,42):
    name = 'res'+str(i)
    session.add(globals()[name])
    session.commit()
    

txt.html_text = u'<p>Four young men take off into separate directions on either side of Highway 1806. Two hop the fence crossing from public property and onto private land, trespassing without a second thought. One of them, a direct descendant of the Rockefellers, is fast as hell and pointed in the wrong direction. The other two are bound with the same commitment moving westward, but once their boots hit the freshly watered North Dakota dirt&mdash;they&rsquo;re on sacred ground.</p>\r\n<p>The bones of the Standing Rock Sioux have been upended and exposed to the elements for the first time in hundreds of years. It has been twelve days since a bulldozer wrenched them from their burial site. A stout young man is holding a dog leash attached to a ratchet strap wearing a Carhartt jacket and a cracked pair of leather boots. His red bandana bounces on his chest as he leaps over a sign taped to a barbed wire fence stating&nbsp; &ldquo;NO VIDEO! NO PHOTO!&rdquo;. This is more of a general rule for the daily influx of rubber neckers hoping to photograph the bones of the formerly rested. Tubbs will need to be smudged with sage before he enters the camp again to ward off the negative energy that comes from disrespecting the dead by stepping on their remains.</p>\r\n<p>&ldquo;KIEVA! KIEVA!&rdquo;</p>\r\n<p>The search team expands its circumference, only stopping to look and call out to the Husky that had been freed from her leash earlier that afternoon. The two men on sacred ground crest the tall hill and descend out of site from the camp. Two more travel north on the side of Highway 1806. Twenty-five miles ahead there is a National Guard checkpoint cautioning all who make their way towards camp.</p>\r\n<p>It&rsquo;s been nearly two weeks since private security sicced their dogs on a group of northbound water protectors on a prayer walk. They had travelled close to two miles from the main camp where most media coverage up to this point has been directed. Most on the front line refer to it as &ldquo;Hollywood&rdquo;. This march immediately became a call to action once they noticed bulldozers had jumped ahead of their scheduled path to gore the disputed sacred grounds. A select few hopped a fence to stop the destruction. Mace and attack dogs were used where Kieva was now scampering in the grass, but this brutality only emboldened them. After they crossed back to Highway 1806, they set up camp and have been there ever since.</p>\r\n<p>The search party&rsquo;s cries grow even more faint. Almost as if the two men had driven her from her hiding spot, Kieva&rsquo;s head pops up as she goes full tear eastward towards the highway like someone kicked this dog into fifth gear. None of the perimeter search party sees her yet. Security patrolling the road tries to cut her off before she squeezes between the horizontal barbed wires and back onto the highway. She doesn&rsquo;t pay any mind to anyone&mdash;her zig zags and quick cuts are playful and joyous.&nbsp; Her paws and belly hair are muddy from chasing prairie dogs and birds, and now she is being herded back to camp.</p>\r\n<p>The hand of a member of the security grabs her by the loose skin on the back of her neck, invoking sensory memory of a mother disciplining a puppy. Kieva immediately freezes knowing that the jig is up. Her field trip is over. Steam rises off her fur like her back is on fire, and her panting is deep. Kieva was savoring her first real sprint in days. The rest of the search party approaches from a grouping of tents on the northwest side of the camp towards the captured pup. Another young man collects warm water to bath the dog. Another lights up a rolled cigarette over the Tupperware containing the community cigarettes.</p>\r\n<p>The posse of tense bodies is in the middle of a heated discussion about a missing knife. The aging, ostensibly homeless cowboy who had misplaced his knife the day before had let the dog off her leash so she could use the restroom and didn&rsquo;t monitor her. His mention of the knife was ill timed in the heat of the moment of being asked to join the search party, and in that context, his grievance took a more sinister tone than he may have intended despite the fact that the camp was decidedly and emphatically non-violent. He looked like what Kris Kristofferson would have ended up looking like had he lived &ldquo;Sunday Morning Coming Down&rdquo; without writing it or enjoying the material benefits of such. He was stubborn and too old to be told that he was wrong. This was the root of the problem, and it was about to lead to his recategorization as a man without a home. The spirits were angry and hoped to use this rift to tear apart the camp. This wasn&rsquo;t the first disagreement brought to the circle, and it wouldn&rsquo;t be the last. In fact, under a microscope, the incident was blown out of proportion, escalated by the fact that everyone had been cooped up in their tents all morning because of a cold rainstorm.</p>\r\n<p>Tubbs is panting from his search. He puts Kieva&rsquo;s collar back on her freshly bathed neck. Her breathing is normal now, and she licks his hand.</p>\r\n<p>&ldquo;You fucking idiot. What were you thinking?--</p>\r\n<p>&ldquo;Hey watch it, this is sacred ground.&rdquo; Vlow interjects. He is the group&rsquo;s thoughtful leader.</p>\r\n<p>&ldquo;I&rsquo;m sorry.&rdquo; Tubbs redirects towards the Old Cowboy. &ldquo;This isn&rsquo;t your dog. This is someone&rsquo;s family. She could have been killed. What the fuck were you thinking?&rdquo;</p>\r\n<p>&ldquo;HEY&rdquo; Vlow&rsquo;s interjection was more emphatic the second time around. He was focused and the first to remind everyone of why they were even there. Even the public ground they stood on was sacred and was not to be soiled with profanity or cigarette butts.</p>\r\n<p>Despite the fighting and the moratorium on swearing, this wasn&rsquo;t a summer camp. It was a collection of protectors hell-bent on stopping the advancement of any heavy machinery onto their present location. On the west side of the highway were the bones of ancestors, and on the east was the Missouri River, which supplied water to millions down stream. An almost certain oil spill would endanger the livelihood of those for generations to come. This bisection of past and present weighed heavy on the leaders of the seventh generation.&nbsp;</p>\r\n<p>&ldquo;Alright, emergency meeting! Everybody, circle up!&rdquo; Vlow calls out. A crowd forms around the fire as people exit their tents, some for the first time all day.</p>\r\n<p>Vlow looks on to make eye contact with everyone through his narrow sunglasses and speaks in fragments as if his words are being custom fit for the occasion. He explains what the Old Cowboy has done. He goes on to announce that he had indirectly threatened a member of the team in front of security. Other members of the camp chime in their misgivings with a raised hand between Vlow&rsquo;s pauses. The Old Cowboy is given the opportunity to speak on his own behalf. He is fixated on this knife instead of formulating a sincere apology. Arriving at this camp without a car or any belongings, his provisions were borrowed; it&rsquo;s clear that he values the scant few things he has with him, including the cowboy hat that gave him his namesake. His stubbornness and lack of sincerity in his apology does not bode well for him. It&rsquo;s clear he is used to moving on without hesitation. Just three days before during an argument between security over whether I would be allowed to stay despite my camera and notepad, he clapped his hands together like he had finished a meal that wasn&rsquo;t sitting quite right with him, &ldquo;Alright, I&rsquo;m outta here&rdquo; and tried to urge two young women sitting next to him that they should also be going before all of the white people were driven out of camp. You see, there was a cloud of conspiracy surrounding infiltrators and would-be government officials who might try to enter the camps to derail the movement. Not only that, but up until this point, the only positive media attention they had received was from a first hand account video showing DAPL private security assaulting unarmed protestors. The reporter was charged with criminal trespassing, so in the water protector&rsquo;s minds, the task of media was up to everyone to film and photograph everything. At this point in the movement, outside media was relegated to the same oppressive category as the government and the pipeline. They may not have driven the bulldozers or paved the way for them, but when it was time to get their boots dirty, they made it very clear that water protectors&rsquo; story need not be told.</p>\r\n<p>My would-be-evictor had pulled a stump up to me with his legs spread. He wore a t-shirt and a bright yellow reflective safety vest.&nbsp; His face was wide and wild with sleep deprivation from working security detail patrolling the camp all night, often going days without a full night&rsquo;s rest. The security team&rsquo;s numbers and whereabouts were always a mystery, intended to obfuscate any infiltrators from reporting on the camp. The constant radio chatter served to keep the group up to date and aware when the police or pipeline security was coming back. Relay a slow trickle of these signals to a group of embittered and tired men all day, and it&rsquo;s no wonder these camps were weary of anyone they didn&rsquo;t know. He had intended to interrogate me on my intentions and identity. He didn&rsquo;t like my answers, my face, or a combination of the two and the security began a tense trial by shouting in the structure behind us. Their tone was what alarmed the Old Cowboy. To give him credit, he wasn&rsquo;t too far off, but his expulsion was much more complex than he had initially thought.</p>\r\n<p>It&rsquo;s as if this is the first time a group of women had told him that unwelcome comments about their bodies were off limits, or that making veiled threats without any intention of following through was a cause for concern in a camp of strangers. Because of the inclusive nature of this group, it was best to take people at their word. He was a harmless old man who assumed that everyone had gotten more sensitive, not that people were simply empowered to speak his or her mind to an old white man. Across the street, a monument to white imperialism is hardening as the sun and windy plains begin to dry the muddy remains.</p>\r\n<p>With a show of a majority of hands he is voted out, and for the first time, you can sense the sincerity of his apology in the down facing posture of his head. He walks back to his tent to wait to apologize to Kieva&rsquo;s owner who is 45 miles away in Bismarck washing everyone&rsquo;s clothes and picking up rain boots for a young man who had ruined his camo moccasins that morning while building a mud berm to keep rainwater out of the communal tarp structure.</p>\r\n<p>Kieva returned to her post, nesting in a ball next to a tire, content and unaware of the excitement that she had created. The stakes at the front line were high and the reminders were constant, but Kieva had been instructive in her excursion. This camp was twelve days old, and the stress vacuum they had built for themselves was starting to embellish every coarse word into a declaration of war. The most clear-headed among them found time to sneak off to the casino to sample the buffet, grab a shower, gamble, or hunt for prairie dogs in the mud.</p>\r\n<p>Twice daily, each prayer around this circle was a time to air concerns or grievances after an elder thanked the creator for the meal. Anyone in the camp was welcome to speak up when it was their turn and everyone had to respect their time. It was messy and often tense, but no one could say they weren&rsquo;t given the opportunity to speak. It was not uncommon for the sun to set on their cold dinners while they hashed out what was bothering the group. Emphatically they would echo &ldquo;A-ho!&rdquo; as an affirmation or punctuation on points taken to heart like a Baptist might use &ldquo;AMEN&rdquo; on a Sunday morning. This was the truest, purest form of democracy that I had ever encountered, and it evolved naturally. These tumultuous discussions, without context, could be seen as symptomatic of a troubled community, but no one left the circle until the affliction had been tended to no matter how tedious. This direct confrontation runs counter to most normal group dynamics&mdash;fostering unity and resolve against the black snake that would try to advance through them. The longer that the company waited them out, the colder the weather would become, but then again, this would only harden their resolve. This was the seventh generation with their heels dug in at the nexus of past and present. The first generation old enough to fully appreciate the fast growing and increasingly severe consequences of inaction and the first generation young enough to feel like their lack of action and that of their parents could directly impact the quality of their twilight years and the childhood of all that would follow them.</p>\r\n<p>Upon entering camp, everyone is given a similar spiel. &ldquo;No weapons. No drugs or alcohol. You are risking arrest by being here. Be respectful of the sacred ground and all those who camp on it, and help out when you can. If you need something, we will get it for you.&rdquo; Days are spent accepting donations and fortifying the camp for the fast approaching winter. Those with useful skills make food, build structures, compost, split wood under the watchful eye of the security team.</p>\r\n<p>In the late afternoons while dinner is being cooked and most of the day&rsquo;s tasks have been performed, the more experienced members of the camp choose to inject some levity. An acoustic guitar is often passed around. An older white woman from Chicago wearing a black felt wide-brimmed hat with turquoise and silver chain around the crown stops by with a Bluetooth speaker playing Phish which is occasionally interrupted with a fart machine soundboard she furtively triggers with her phone. Each fart is precious and like the first she&rsquo;s ever heard. Her laughter is contagious and her backrubs are typically middle of the road at best. But she knows that she cannot stay so she does the next best thing, which is to leave the camp more cheerful than she found it. An older native gentleman from Montana is happy to teach everyone how to play Slahal, a native guessing game using two pairs of bones. The bones he carries are from the shin of a deer his niece shot on his property. As a Vietnam veteran, he tries to bring clarity of perspective. This is a marathon, not a race. His face is inviting. His hair is a wiry collection of thin curls, and his teeth he tells me were donated to a young man on his reservation who was trying to rehabilitate himself after getting off meth. He is quick to remind everyone at the sacred grounds that tobacco was never meant to be smoked recreationally. He offers me a pipe filled with dried kinnikinnick, noting that he was once addicted to cigarettes. Before he lays down to nap in his teepee, he notes that everything he is--his Catholic religion, the perversion and commodification of tobacco, and even the idea of working a job are &ldquo;all because of the white man&rdquo;. He urges me to reject what his generation couldn&rsquo;t.</p>\r\n<p>After dinner, the fire becomes more communal as the temperature begins to drop and the wind begins to whip at their backs. There is the sacred fire that is never to die, and there is a cooking fire where a pot of cowboy coffee is almost always brewing. As the circles get bigger, smaller fires form new groups. Guitars, washtub basses, banjos, mandolins, and drums are played. Even without the aid of drugs or alcohol, the discussions get more spirited and often conspiratorial. Talk turns to the use of cell jammers on the camp, chemtrails, 9/11 truth campaigns, and a particularly hazy theory that natives are descendants from aliens. Those with the most tenuous grasp on their constitutional rights seem most inspired to remind everyone of theirs, while others are studying treaty laws ranging back to 1851. Still more just want to sit and color while they give each other stick and poke tattoos. It&rsquo;s like a college party without the lapses in consciousness and instead of risking arrest for underage drinking, they risk being charged with trespassing and obstructing traffic when and if a Sheriff decides to do so. The conspiracies, the intertribal conflict, and the near-constant gossip that they might all be arrested in the morning are an agreeable substitute for alcohol. This coalition of people at the camp range from antifascists, a Rockefeller, socialists, environmentalists, Anonymous, libertarians, and those of all gender identities and sexual orientations. With them they bring different priorities and baggage which drove them to stay at the camp in the first place. But their support of the natives is steadfast under the banner of protecting the water and the land rights of the natives&mdash;alive, dead, and those still to be born.</p>\r\n<p>This was a group comprised of individuals who likely cornered you at a party to discuss conspiracy theories. Constantly posting articles on rapid climate change or the federal government&rsquo;s militarization of the police force as an instrument for protecting property rather than people. These are the people you knew in high school and subsequently hid for posting unsubstantiated claims about GMOs. But then again over the course of nearly two months, Humvees and snipers have been deployed to disperse crowds. LRADs, mace, batons, bean bags, rubber bullets, tasers, and concussion grenades have been used on the water protectors. Airplanes and helicopters circle the camps all day and into the night despite the No-Fly Zone. An infiltrator employed by the pipeline armed with an assault rifle managed to get into the camp. It&rsquo;s not as if I didn&rsquo;t believe military equipment or crowd control tactics implemented in Iraq were being used on our own citizens. I watched the Ferguson protests. It&rsquo;s an entirely different thing to have taken part in a movement that incurs the use of such tactics. To watch a live stream of a young man I know named Tubbs being clubbed over the head with a baton and maced is an entirely different experience. I&rsquo;m still pretty dubious on chemtrails and 9/11 conspiracies, but after this I&rsquo;m not nearly as skeptical about how easily the government would implement such pervasive surveillance and crowd control tactics as I once was.</p>'

art2.html_text = u'<img class="article-image" alt="{{other_images[0].caption}}" src={{other_images[0].resource_location}}>\r\n<img class="article-image" alt="{{other_images[1].caption}}" src={{other_images[1].resource_location}}>\r\n<img class="article-image" alt="{{other_images[3].caption}}" src={{other_images[2].resource_location}}>\r\n<img class="article-image" alt="{{other_images[4].caption}}" src={{other_images[3].resource_location}}>\r\n<img class="article-image" alt="{{other_images[5].caption}}" src={{other_images[4].resource_location}}>\r\n<img class="article-image" alt="{{other_images[6].caption}}" src={{other_images[5].resource_location}}>\r\n<img class="article-image" alt="{{other_images[7].caption}}" src={{other_images[6].resource_location}}>\r\n<img class="article-image" alt="{{other_images[8].caption}}" src={{other_images[7].resource_location}}>\r\n<img class="article-image" alt="{{other_images[9].caption}}" src={{other_images[8].resource_location}}>\r\n<img class="article-image" alt="{{other_images[10].caption}}" src={{other_images[10].resource_location}}>\r\n<img class="article-image" alt="{{other_images[11].caption}}" src={{other_images[11].resource_location}}>\r\n<img class="article-image" alt="{{other_images[].caption}}" src={{other_images[12].resource_location}}>\r\n<img class="article-image" alt="{{other_images[].caption}}" src={{other_images[13].resource_location}}>\r\n<img class="article-image" alt="{{other_images[14].caption}}" src={{other_images[14].resource_location}}>\r\n<img class="article-image" alt="{{other_images[15].caption}}" src={{other_images[15].resource_location}}>\r\n<img class="article-image" alt="{{other_images[16].caption}}" src={{other_images[16].resource_location}}>\r\n<img class="article-image" alt="{{other_images[17].caption}}" src={{other_images[17].resource_location}}>\r\n<img class="article-image" alt="{{other_images[18].caption}}" src={{other_images[18].resource_location}}>\r\n<img class="article-image" alt="{{other_images[19].caption}}" src={{other_images[19].resource_location}}>\r\n<img class="article-image" alt="{{other_images[20].caption}}" src={{other_images[20].resource_location}}>\r\n<img class="article-image" alt="{{other_images[21].caption}}" src={{other_images[21].resource_location}}>\r\n<img class="article-image" alt="{{other_images[22].caption}}" src={{other_images[22].resource_location}}>\r\n<img class="article-image" alt="{{other_images[23].caption}}" src={{other_images[23].resource_location}}>\r\n<img class="article-image" alt="{{other_images[24].caption}}" src={{other_images[24].resource_location}}>\r\n<img class="article-image" alt="{{other_images[25].caption}}" src={{other_images[25].resource_location}}>\r\n<img class="article-image" alt="{{other_images[26].caption}}" src={{other_images[26].resource_location}}>\r\n<img class="article-image" alt="{{other_images[27].caption}}" src={{other_images[27].resource_location}}>\r\n<img class="article-image" alt="{{other_images[28].caption}}" src={{other_images[28].resource_location}}>\r\n<img class="article-image" alt="{{other_images[29].caption}}" src={{other_images[29].resource_location}}>\r\n<img class="article-image" alt="{{other_images[30].caption}}" src={{other_images[30].resource_location}}>\r\n<img class="article-image" alt="{{other_images[31].caption}}" src={{other_images[31].resource_location}}>\r\n<img class="article-image" alt="{{other_images[32].caption}}" src={{other_images[32].resource_location}}>\r\n<img class="article-image" alt="{{other_images[33].caption}}" src={{other_images[33].resource_location}}>\r\n<img class="article-image" alt="{{other_images[34].caption}}" src={{other_images[34].resource_location}}>\r\n<img class="article-image" alt="{{other_images[35].caption}}" src={{other_images[35].resource_location}}>\r\n<img class="article-image" alt="{{other_images[36].caption}}" src={{other_images[36].resource_location}}>\r\n<img class="article-image" alt="{{other_images[37].caption}}" src={{other_images[37].resource_location}}>\r\n<img class="article-image" alt="{{other_images[38].caption}}" src={{other_images[38].resource_location}}>\r\n<img class="article-image" alt="{{other_images[39].caption}}" src={{other_images[39].resource_location}}>\r\n<img class="article-image" alt="{{other_images[40].caption}}" src={{other_images[40].resource_location}}>\r\n<img class="article-image" alt="{{other_images[41].caption}}" src={{other_images[41].resource_location}}>\r\n<img class="article-image" alt="{{other_imagescaption" src={{image.resource_location}}>\r\n'
