import Levenshtein
import pysrt
import webvtt



paragraph1 = (r"""Oh, I love how music
just gets you pumped!
Right?
Sorry, I just...
I'm excited to be here.
It's been a while.
You know, for a long time,
I wasn't sure I'd ever be back.
Disney bought Fox, there's
the whole boring rights issue,
blabbity, blabbity, blah.
But then, it turned out
they wanted me.
The one guy who shouldn't even
have his own movie.
Much less a franchise.
Marvel's so stupid.
Look, we know
the title of this thing,
so I know what you're wondering.
How are we going to do this
without dishonoring Logan's memory?
And I'll tell you how.
We're not.
I'm gonna let you
in on a little secret.
Wolverine is not dead.
Sure, it made for a perfect
ending to a very sad story.
But that's not how regenerative
healing factors work.
You think I want to be out here
in beautiful Downtown
North Dakota, digging up
the one and only Wolverine?
No thank you.
But the fate of my
entire world is at stake.
He may not be
living his best life,
but he sure as
hell ain't... dead.
Bingo.
Yahtzee.
Yes, yes, yes, yes.
Dammit!
Son of a
bitch!
Fuck!
Mother...
Fucker!
My world is fu---
That was weird.
I'm much calmer now.
Look, I'm not a
man of science,
but you seem
incredibly passed away.
But it's good to see you.
I got to be honest, I've always
wanted to ride with you, Log.
You and me, getting into it. Deadpool
and Wolverine. Just fucking shit up.
Can you imagine
the fun, the chaos...
The residuals?
"G'day, mate. There's
nothing that will bring me
back to life faster than a
big bag of Marvel cash."
Me too, Hugh.
But no.
No, no, no.
Ugh... You had to get
all noble and die for real.
God... dammit!
I could really use
your help right now.
Wait!
I'm warning you,
I am not alone!
Wade Winston Wilson.
You are under arrest by
the Time Variance Authority.
Too many crimes to list.
Come out.
Ohhh.
Death by Dave Flair.
Last chance.
Throw out your weapons
and come out peacefully.
I'm not gonna give you my weapons,
but I promise not to use them.
There are 206 bones
in the human body.
207 if I'm watching Gossip Girl.
Here we go. Maximum effort.
Okay, Peanut. I guess we're
getting that team-up after all.
From outside the box... Score!
I'm soaking wet right now.
To be clear, I'm not
proud of any of this.
The wanton violence, the whiff of
necrophilia... it isn't who I am.
It isn't who I want to be.
Who I want to be?
Well, to help you understand
that, I got to take you back.
A little joy ride I took
through space and time.
To the day that
changed everything.
I can't believe
I'm finally here.
I waited for this
moment for so long.
Thank you, sir, for seeing me.
I firmly believe that my services can
be of great use to your organization.
Now I know, I was caught
smashturbating in the lobby of Stark Tower.
- "Smashturbating?"
- But I can assure you...
I'm sorry, what was that?
Sorry, that's, when you get
those toy Hulk hands, right?
And then you just, you look down, you just...
brace yourself and you ravage the midsection...
I get it. Okay. Okay.
The picture's painted.
You get the gist.
What exactly brings
you here today?
Why I... Wow,
okay. I... I care.
I know I turn everything
into a joke, but I... I care.
I want to use that feeling
for something important.
I want to matter.
Need to show my
girl that I matter.
You know, I feel like I'm
wasting the good stuff here.
- Is the man not gonna be joining us?
- The man?
Yeah, I should save
this if he's gonna...
As far as you're concerned
right now, I'm the man.
- No.
- The man is me.
I am the man in
this circumstance.
And he doesn't do this
kind of thing anymore.
- Cameos?
- Meetings.
Meetings.
Entry level meetings.
Entry level.
Aren't you the chauffeur?
- I...
- Maybe?
A common misconception.
I did begin my career
as Mr. Stark's driver.
Quickly pivoted to
the head of security.
Of course. Yes,
yes, yes, yes.
And why I am
vetting your resume?
You seem to have left out whether or not you
had any experience as a member of a team.
Could you maybe add a
little bit of perspective there?
No, yes.
""")



def srt_to_text(file_path):
    subs = pysrt.open(file_path)
    text = ""
    for sub in subs:
        text += sub.text + "\n"
    return text.strip()
def vtt_to_text(file_path):
    text = ""
    for caption in webvtt.read(file_path):
        text += caption.text + "\n"
    return text.strip()

def isJunk(x):
    return x.isspace()

def compare_paragraphs(string1, string2):
    distance = Levenshtein.distance(string1, string2)

    max_length = max(len(string1), len(string2))
    return (1 - distance / max_length) * 100
print(compare_paragraphs(vtt_to_text("C:/Users/SmiljanicA/Desktop/test.vtt"), srt_to_text("C:/Users/SmiljanicA/Desktop/test.srt")))

