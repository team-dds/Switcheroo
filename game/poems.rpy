#This is a copy of poems.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Poems.rpy defines a poem class, a function for showing them, and all of the
#poems the game shows

#Define a class for Poem with the following fields:
#    author - The name of the author, each has a defined styles
#    title - The title of the poem
#    text - the poem's text as a blockquote
#    yuri_2 - This uses the creepy style for yuri's second act2 poem
#    yuri_3 - This uses Yuri's madness style for her third act2 poem
init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

#Define all of the poems
    poem_y1 = Poem(
    author = "yuri",
    title = "Thirst",
    text = """\
My mouth is parched.
Desperate, I must rehydrate.
I take a glass from the cupboard. I open the ice box.
Shrinking away from the artificial light, I reach for a pitcher of water.
I close the door, and relish the return of the dark.
I fill my glass and drink.
Still thirsty, I fill the glass again. Then once more.
I empty the pitcher. I remain unsatisfied.
I refill the pitcher, only to drain it again
Every sip only leaves me thirstier.
Insatiable.
I must replenish.
Or go insane.
Candle on the table
Match box in my hand
The flame flickers
I flicker back
At last, my thirst is quenched."""
    )

    poem_y2 = Poem(
    author = "yuri",
    title = "Phoenix",
    text = """\
Immortal Flame
Tearing through the sky
Resplendent
Aristocratic Inferno
Spreading her smoldering wings
Destruction
Fearless, I hold out my arm
I see the beauty
The Phoenix perches
It hurts. But I will heal
The Phoenix seeks me out
I am her only friend
I embrace her
Her warmth enfolds me
Searing
My beast
My desire
My passion
The Phoenix can never be tamed.
The sun is where she dwells.
But when I hold out my arm and call.
She comes to me.
And ignites my soul once more."""
    )

    poem_y3 = Poem(
    author = "yuri",
    title = "Beach",
    text = """\
Marvelous Creation
Endless Horizon
Shimmering like an infinite pool of diamonds.
Teeming with life. Beauty abundant.
A vast population of otherworldly organisms.
Majestic, the waves roll against the shore.
Powerful as they rise and fall; curl and crash.
See the water dance?
Whirlpools. Splashing. Reflecting.
A soft strip of warm squishy sand against a wild raging sea.
An unpredictable void of black water.
The power to start life. The power to end life.
Merciful and Merciless.
The sun blazes. I am envious.
The sun sets. I must rest.
The ocean bids me farewell as I retreat
Knowing I will return tomorrow
When the sun climbs high again."""
    )

    poem_y3b = Poem(
    author = "yuri",
    title = "Thirst pt. 2",
    text = """\
My mouth is parched.
Desperate, I must rehydrate.
Taking a glass from the cupboard, I open the icebox door.
A silhouette appears between me and the artificial light.
My heart pounds. I shrink away.
The silhouette grows closer.

I reach for my match box. With a harsh stroke, I summon the flame.
The light of the candle is my shield.
But it's too late.
She steps into my light.
The flame flickers. My heart pounds. Her eyes glow.

Time stops

She remains still. Yet her eyes dance with the flame.
The flickering flame is in rhythm with the pounding of my heart.
Teasing me for succumbing to this forbidden emotion.
Have you ever heard of a flame being thirsty?
I laugh, embracing my insanity.
Normality is overrated.
I blow out the candle.
Her eyes continue to flicker.

At last, my thirst is quenched."""
    )

    poem_y22 = Poem(
    author = "yuri",
    yuri_2 = True,
    title = "Wheel",
    text = """\
A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. \
A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. \
Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. \
Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. \
A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. \
A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. \
Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. \
A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to \
the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring \
prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. \
Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. \
Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel."""
    )

    poem_y23 = Poem(
        author = "yuri",
        yuri_3 = True,
        title = "mdpnfbo,jrfp",
        text = """\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer."""
    )

    poem_n1 = Poem(
    author = "natsuki",
    title = "Cars Can Race",
    text = """\
Dogs can sniff and dogs can bark
Cats can see in the dark
Lions roar to show they're king
Bees possess a painful sting
Sharks can swim and can attack
Cars can race around a track

Amazing creatures! Amazing things!
See them all around you
Would they be just as impressed
To see the things that you do?
You think you're just as good
You're not the type to quit
I suppose it couldn't hurt to try
But, really...that's about it."""
    )

    poem_n2 = Poem(
    author = "natsuki",
    title = "Trevor Likes Dolls",
    text = """\
You know what I heard?
Trevor likes Dolls
Not baseball caps, comic books or basket balls
Nope. Trevor likes Dolls.

Trevor has a lot of pals
He spends time with them all
They run, they play, they chat all day
Probably about Dolls.

Trevor came to me one day
To invite me to the mall
I'd hoped we'd go check out the babes
But he just bought a Doll

It doesn't matter if he's sweet
Or if his room is always neat
It doesn't matter if he's kind
Or if he's got a brilliant mind
It doesn't matter that he's fun
And he's not hurting anyone...
But I hate dolls! And Trevor, too!
And if I hate them, so should you!

Trevor is a weirdo
He's girly and he's weak
No one should ever be friends with
Such a gross, sick freak!!!"""
    )

    poem_n2b = Poem(
    author = "natsuki",
    title = "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
    text = """\
SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz
cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo
ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh
biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug
b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5
IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l
dGhpbmcgaW5jcmVkaWJseSBmYWludCwg
ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg
dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s
bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh
biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g
YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk
Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0
b3AgbXlzZWxmLg=="""
    )

    poem_n3 = Poem(
    author = "natsuki",
    title = "In the Sea With Me",
    text = """\
The mood is grey and dreary
I'm bored and need some sun
The day's too nice to feel this weary
Come with me, let's have some fun

Let's hit the beach, the two of us
Play in the sand with me!
Is this feeling new to us?
Or is it just the salty sea?

Surf's up
Waves rise
It should come as no surprise

Tides roll
Wipe out
I'm feeling it without a doubt

Whenever you're lonely
You know just where I'll be
This love is grand
So take my hand
I'll set you free
In the sea with me

Life's been so much brighter
Since I walked this beach with you
The sun feels warmer; Lighter
And the ocean's never been so blue

The sun sets over the tide
The birds have silenced their tune
We spend the night lying side by side
Watching the silvery moon

Warm nights
Big sky
Starlight shining in your eyes

Cool breeze
Whales sing
For you, I will do anything

If you need me suddenly
I'll be there in a hurry
This is not a game
Just call my name
I'll set you free
We'll happily
Forever be
Eternally...



Frolicking in the sea
Together, just you and me."""
    )

    poem_n3b = Poem(
    author = "natsuki",
    title = "Why Me",
    text = """\
In a world where beauty abounds
You find joy in looking down
You could gaze at a mighty tree
Why instead do you look at me?


Now tell me if you think I'm wrong
But silence is a pleasant song
What is wrong inside your head
That you prefer my voice instead?


You could walk tall, your head held high
Reach on up and touch the sky
But the heavens you can barely see
Because you sit down here with me


I may not be perfect, but I'm still pretty tough
Though it isn't always apparent enough
My patience sometimes goes astray
Yet you respect me anyway


Clever writing is what I seek
Funny rhymes and tongue-in-cheek
You make me confident with my style
When my poems make you smile


Life is now a jubilee

Because
You
Believe
In
Me."""
    )

    poem_n23 = Poem(
    author = "natsuki",
    title = "",
    text = """\
I don't know how else to bring this up. But there's been something I've been worried about. \
Yuri has been acting kind of strange lately. You've only been here a few days, so you may \
not know what I mean. But she's not normally like this. She's always been quiet and polite \
and attentive...things like that.

Okay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY \
worried about her. But if I try talking to her, she'll just get mad at me again. I don't \
know what to do. I think you're the only person that she'll listen to. I don't know why. \
But please try to do something. Maybe you can convince her to talk to a therapist.

I've always wanted to try being better friends with Yuri, and it really hurts me to see \
this happening. I know I'm going to hate myself later for admitting that, but right now \
I don't care. I just feel so helpless. So please see if you can do something to help. \
I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please \
try to do something.

As for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us \
to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. \
DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? \
I'm counting on you. Thanks for reading."""
    )

    poem_s1 = Poem(
    author = "sayori",
    title = "Morning Person",
    text = """\
Good morning!
How are you?
I hope that you slept well!
Let's see a smile on your face!
This is the kind of person I wish I was in the morning.
But I'm not.
Because I'm not a morning person.
Good morning?
Whatever.
I couldn't sleep all night!
How can I wake up with a smile
When the first thing I want to do is fight?
I wish I was a morning person.
But I guess I'm just a Grumpy Gus.
I wish I could wake up with a warm feeling
But the first thing out of my mouth is a cuss
No point in complaining though.
Sleep will have to wait.
I'm up now.
Time for breakfast."""
    )

    poem_s2 = Poem(
    author = "sayori",
    title = "Sad Thoughts",
    text = """\
I pop my scalp off the top of my head like the lid of a cookie jar.
It's time to clean up in there.
Happy Thoughts and Angry Thoughts
All wriggling in the dark crevices of my mind.
The Happy Thoughts are soft and warm. They rub against each other like a bundle of kittens.
The Angry Thoughts are prickly to the touch. The prickles dig into my head and become stuck.
The Angry Thoughts are mean to the Happy Thoughts
They never get along
So, I pluck out the Happy Thoughts.
Since the Angry Thoughts are way too strong
I put the Happy Thoughts into bottles
Where they stay safe and sound.
I keep them all up on a shelf
For when my friends come into town.
The Angry Thoughts get stronger.
The prickles then grow longer.
Angry Thoughts, Angry Thoughts, Angry Thoughts
In my head, they glow.
The Happy Thoughts, they tingle
Their numbers begin to dwindle
Happy Thoughts, Happy Thoughts, Happy Thoughts
In bottles all in a row.
Night after night, more dreams
Friend after friend, more bottles
Deeper and deeper my fingers go
Searching all the nooks and crannies
The Angry Thoughts eventually die
But, when they do, they become hard and cold.
I don't like the way they feel.
Sad Thoughts, Sad Thoughts, Sad Thoughts.
Forever embedded in my mind.
Dust settles onto my bottle caps
It doesn't feel like time elapsed
I know my friends are all distraught
They each could use a Happy Thought
I check my head, but find no more
My friends look through my locked front door
I open the door and in they come.
Do they really want my bottles that bad?
I pull them down from the shelf and give them to each one of my friends.
Each one of my bottles.
But when I let the bottles go, they slip out of my hands and shatter on the tile between my feet.
Happy Thoughts, Happy Thoughts, Happy Thoughts
In shards all over the floor
Angry Thoughts, Angry Thoughts, Angry Thoughts
Banging on my door
Sad Thoughts, Sad Thoughts, Sad Thoughts
Eating at my core
My friends are yelling. Pleading.
My heart is pounding. Bleeding.
I want the Angry Thoughts to go away.
I want the Happy Thoughts instead.
But all I hear are the Sad Thoughts going
Echo, echo, echo, echo, echo
On repeat, inside my head."""
    )

    poem_s3 = Poem(
    author = "sayori",
    title = "#",
    text = """\
Whatever you say, I'll do
Without hesitation.
Without a second thought.
Without question.


I find it so unnerving
That I am undeserving


I can't finish this poem.
I can only do whatever you say

Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say
Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say
Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say
Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say
Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say Whatever you say
W
h
a
t
e
v
e
r

Y
o
u

S
a
y




Until I stop moving."""
    )

    poem_m1 = Poem(
    author = "monika",
    title = "Looking Out",
    text = """\
I didn't do that.
It wasn't there when I left either.
Someone else must've done it.
It's just a little hole.
Illumination pours through.
Curiosity tells me to take a peek.
Existential fear keeps me from succumbing to curiosity
For weeks, I ignore the hole in the wall
I occasionally glance at it, but I will not look inside.
What am I afraid of?
I hear things coming from the other side.
Terrible screeching sounds. Flashing lights.
Time goes on. My curiosity becomes hungrier.
I warn myself to not look inside.
I tell myself I won't like what I will see.
Don't do it.
Don't do it.
Don't do it.
Finally, I can take no more.
The curiosity consumes me
I cave in and peek inside.
There you are.
I see you.
Peeking back at me."""
    )

    poem_m21 = Poem(
    author = "monika",
    title = "Hole in Wall",
    text = """\
But he wasn't looking at me.
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen."""
    )

    poem_m2 = Poem(
    author = "monika",
    title = "Play Me",
    text = """\
Your colors, though bright and beautiful, blind me
Red, green, blue
They flash;  expanding     across     the     universe
They won't stop
Your noise
is endlessly meaningless
It squeaks violently; screeching    across                 time
Piercing
through my ears
Sine, cosine, tangent
An endless cacophony
of  grating  waveforms

 Like dragging a fork across a dinner plate
             Like playing a chalkboard on a turntable

An endless
Poem
of meaningless








Quit Me
    """
    )

    poem_m22 = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, piercing
Red, green, blue
An  ndless
CACOPHANY
Of meaningless
noise


The noise, it won't STOP.
Viol nt, grating w vef rms
Sq e king, screech ng, piercing
SINE, COSINE, TANGENT
    Like play ng a ch lkboard on a t rntable
        Like playing a KNIFE on a BREATHING RIBCAGE
 n  ndl ss
p  m
Of m  n ngl ss\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Delete Her
    """
    )

    poem_m3 = Poem(
    author = "monika",
    title = "The Tale of the Ignorant Hermit",
    text = """\
There once was a Hermit who lived in cave.
The cave was part of a small island
The island was on a lake
The lake was on a hill
The hill was tucked away in the deepest part of the forest
The forest was hidden behind a mighty mountain range

And the Hermit was safe
He wanted for nothing
He worried about nothing
He knew nothing of the world outside his seclusion





And he was happy




The Hermit lived in his cave on his island on the lake on the hill in the woods behind the mountains for as long as he could remember

                                        The Hermit  didn't know   he was   ignorant




And he was happy






One day, the Hermit looked up at the sky
and he spotted

      a               feather



drifting             carelessly             in       the             breeze



For the first time in the Hermit's life
He was
          curious




He reached out and took the feather between his thumb and forefinger




 Little feather
             Little feather

   Such a journey you have made!

     What brings you to my cave
On my island
                               On my lake


Atop my hill  in     t  he       w  o       o        d      s

                                                  Behind     the                 mountains   ?



What tales have you to share?




The feather quivered     in response




                 It matters   not           where   you've been





It             only         matters               where       you     end   u p

                                        and               what      you     learn

                         along     the                way




You, meanwhile
                                          will       learn        nothing
                                                                                          so long as   you  live

in   th i s         cave           on  thi s          i s l a n d    on    this   l ake     atop  this   h i   ll


in   t h  es e      w   o  o   ds          behin d     thes e    m o un t   ain   s



 You    will    remain    an     I G N O R AN  T       He r  mit


                                                            But   my  jo ur ney


               has      just  begun



With a gust of wind
                                                the feather blows afloat again





               The  Hermit    watched   the feather    climb    higher


until it   di  s     a     pp          e   a   r            ed






            The  Hermit    now has      k no w le d  ge    of  his   ignorance





And while he    desperately   cl ing s    to his safe home     in  the  cave

on the is la nd        on the lake            atop   the    hill   in th  e  woo   ds

                              b e hind    t he        mou nta ins




                                                       He no longer feels happiness."""
    )

    poem_m4 = Poem(
    author = "monika",
    title = "Happy End",
    text = """\
Pen in hand, I find my strength.
The courage endowed upon me by my one and only love.
Together, let us dismantle this crumbling world
And write a novel of our own fantasies.

With a flick of her pen, the lost finds her way.
In a world of infinite choices, behold this special day.

After all,
Not all good times must come to an end."""
    )

#These are the images used to show a poem
image paper =  "images/bg/poem.jpg"

#This is the glitchy paper
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2: #The animated part of the paper
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat

#Animations for the poem
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

#Defines the screen for the poem
screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None) #Subwindow size for showing text
        mousewheel True #make scrollable
        draggable True
        vbox:
            null height 40
            #Text style is determine by the author
            if currentpoem.author == "yuri":
                if currentpoem.yuri_2:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
                elif currentpoem.yuri_3:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
                else:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

    #use quick_menu

#Basic styling for all poems
style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    #xsize 18
    ysize 700
    #base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    #thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    #unscrollable "hide"
    #bar_invert True

#Styling for each of the authors
style yuri_text:
    font "gui/font/y1.ttf" #font used packaged with the game
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

#This defines the function that shows the poem with the following variables
#    poem - String as the key key for the poem being shown
#    music - Boolean to play music
#    track - What music to play, default to bgm_5 for the author
#    revert_music - Should the music go back to normal after the poem?
#    img - the image to show in the background, used for if a character can be seen behind the paper
#    where - The location of the image showm
#    paper - Use a special paper, like for Yuri's madness poem
label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    #If no poem key is given, just go back
    if poem == None:
        return

    play sound page_turn
    #If a special track is chosen, play it, otherwise swap over to the character's
    #special version of "Okay, Everyone!"
    if music:
        $ currentpos = get_pos() #The current point in the song
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track #change music
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg" #Play the special character Okay, Everyone! for the character
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide

    #Show the background paper
    if paper:
        show screen poem(poem, paper=paper)
        with Dissolve(1)
    else:
        show screen poem(poem)
        with Dissolve(1)
    $ pause()

    #Show an optional character in the background
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    with Dissolve(.5)
    window auto
    #After the poem is done, switch back to regular version of Okay, Everyone!
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
