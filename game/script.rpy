# loop progress
default loop_count = 0

# name of the character.
define h = Character("???")
define u = Character("You")
define s = Character("Sophie")
define f = Character("Alex")

# images
image bg room_clean = "images/room/room-clean.png"
image bg room_dark = "images/room/room-dark.png"
image bg room_bloody = "images/room/room-bloody.png"
image hands = "images/misc/hands.png"
image friend smile = "images/friend/smile-long.png"
image friend smile_creepy = Transform("images/friend/smile.png", yoffset=-180, zoom=0.9)
image stranger worried = "images/stranger/worried.png"
image dead_body = "images/misc/body.png"
image friend angry = Transform("images/friend/angry.png", yoffset=-180, zoom=0.9)
image stranger angry = "images/stranger/angry.png"
image stranger angry_cropped = Transform("images/stranger/angry-cropped.png", yoffset=-180)
image stranger smile = "images/stranger/smile.png"
image friend evil = Transform("images/friend/evil.png", yoffset=-180, zoom=0.9)
image stranger evil = "images/stranger/evil.png"

# music and sounds
define audio.heartbeat = "audio/heartbeat.mp3"

label start:

    scene black
    play sound audio.heartbeat
    show screen centered_narration("Thump Thump... Thump Thump...")
    $ renpy.pause()
    stop sound fadeout 5.0
    hide screen centered_narration

    " Your eyes snap open ..."
    scene bg room_clean at Transform(zoom=1.1)
    u "Huhh....there am i???"
    "You push urself upright and freeze."
    show hands at center, Transform(zoom=0.6) with dissolve
    u "My ha-hands?? They're smeared with blood"
    "Sticky, half-dried stains, crusted under your nails."
    u "I don’t remember ho-how—"
    hide hands with dissolve
    
    # frd introduction
    show friend smile at left with dissolve
    f "HEYY, LOOK AT ME!!"
    "You blink hard… and nearly jump."
    u "A-Alex??!"
    u "What are you doing here? How—"
    f "Shhhh...Don’t panic. Don’t think about it. Just stay calm, okay? can you do that for me?"
    "You nod gently."
    f "Good, You can trust me. Don't worry, I’ll help you get out of this."
    f "Forget what you see. Forget what you think you remember."
    "His voice is steady, warm… almost rehearsed."
    "For a moment, You want to believe him."
    hide friend with dissolve

    # strangers introduction
    show stranger worried at right with dissolve
    h "Don’t trust him"
    "Then—another voice. A women you don’t recognize."
    u "W-wait… who the hell are you?!"
    h "Me? …I’m Sophie."
    s "Don’t you dare listen to him!"
    u "W-who are you??"
    s "I just told you— Sophie! And if you want to survive, you better listen."
    s "Look at your hands. LOOK at them!"
    s "You think that blood is his? Or mine? No… it’s YOURS."
    s "He’s lying to you. He always lies. He’s keeping you here!"
    "Her voice shakes, desperate. But her eyes… there’s truth in them or madness..?"
    hide stranger with dissolve

    # body
    show dead_body at center, Transform(zoom=0.5) with dissolve
    "The corpse lies by the door, silent."
    "The blood on the floor glistens. Your pulse pounds in your ears."
    "One of them is lying. Maybe both."
    hide dead_body with dissolve

    show friend angry at left
    show stranger angry_cropped at right 
    "You’re still reeling from the shock of seeing both of them in your apartment."
    "The blood on your hands feels heavier than ever. Your pulse is racing."
    menu:
        "Alone...who will you choose to talk to first????"
        "Talk to Alex":
            jump talk_alex
        "Talk to Sophie":
            jump talk_sophie

# --- Branch: Talk to Alex first ---
label talk_alex:
    hide stranger angry
    show friend smile at left with fade
    f "Thanks, mate, for trusting me."
    u "I’m not trusting you yet… you need to tell me what’s actually going on."
    f "I can’t explain everything right now but i promise i will tell you everything later. You just need to stay calm and listen to me."
    f "Look, one thing is clear...someone is manipulating this. Someone wants you to panic."
    "You watch him closely, trying to read if he’s lying... or telling the truth."

    menu:
        "What do you think of Alex?"
        "Trust him":
            jump trust_alex
        "Accuse him":
            jump accuse_alex

# --- Branch: Talk to Sophie first --
label talk_sophie:
    hide friend angry
    show stranger smile at right with fade
    s "Thanks for chosing me but listen to me carefully"
    u "See, I don’t really trust you. Who the hell even are you?"
    s "who i am isnt important ... for now, we need to get out of here before we get killed!!"
    s "Everything you see, everything you remember… it’s not what it seems."
    "You stare at her, trying to decide if she’s telling the truth… or trying to trick you."

    menu:
        "What do you think of Sophie?"
        "Trust her":
            jump trust_sophie
        "Accuse her":
            jump accuse_sophie

#  ENDING 1 -  bad death (by the person)
label trust_alex:
    scene black
    show screen death_msg("YOU DIED!!..THE STRANGER HAS KILLED YOU")
    $ renpy.pause()
    hide screen death_msg
    scene black with fade
    jump start

label trust_sophie:
    scene black
    show screen death_msg("YOU DIED!!..THE FRIEND HAS KILLED YOU")
    $ renpy.pause()
    hide screen death_msg
    scene black with fade
    jump start

label accuse_alex:
    show friend angry at left with dissolve
    u "No, Alex… something about you feels wrong. You’re hiding something."
    f "What?! After everything I’ve done to help you, you accuse me?!"
    f "Fine. Believe her lies if you want—see where that gets you."
    hide friend angry

    show stranger smile at right with dissolve
    s "Finally. You’re starting to see the truth."
    "Their voices clash, echoing in your head. Your pulse is too fast. The room spins…"

    # # 🔊 sudden scream (make sure scream.ogg exists in /game/audio/)
    # play sound "scream.ogg"

    # # sudden flash / violent scene change
    # scene bg room_dark with vpunch 
    # with hpunch
    # hide room_dark with Dissolve
    "A sharp scream cuts through the room—then silence."
    show friend evil at left with dissolve
    pause 0.1 
    hide friend evil with dissolve

    # collapse → fade into black screen
    scene black with fade
    show screen death_msg("YOU DIED!!")
    $ renpy.pause()
    hide screen death_msg
    show screen centered_narration("Alex’s rage consumes everything. Sophie falls first... then you.")
    $ renpy.pause()
    hide screen centered_narration
    scene black with fade
    jump start

label accuse_sophie:
    show stranger angry at right with dissolve
    u "Sophie… no, it’s you. You’re the one pulling the strings here."
    s "Me? After everything I’ve revealed to you, this is how you repay me?"
    s "You really think Alex is the danger here?"

    show friend smile_creepy at left with dissolve
    f "Finally! You see it too. I told you she couldn’t be trusted!"
    "The air grows heavy. Sophie’s smile fades into something darker—something monstrous."
    hide stranger smile
    "A sharp scream cuts through the room—then silence."
    show stranger evil at right with dissolve
    pause 0.1 
    hide stranger evil with dissolve

    # 🔊 sudden scream (optional — add scream.ogg in /game/audio/)
        # play sound "scream.ogg"

    # sudden violent scene change
    # scene bg room_dark with vpunch
    # with hpunch

    "A chilling scream tears through the room—Alex’s scream."

    hide friend angry
    # hide room_dark with Dissolve

    # collapse → fade into black screen
    scene black with fade
    show screen death_msg("YOU DIED!!")
    $ renpy.pause()
    hide screen death_msg
    show screen centered_narration("Sophie strikes Alex down before you can react... then turns on you.")
    $ renpy.pause()
    hide screen centered_narration
    scene black with fade
    jump start

    
    return

# Define a screen to show centered narration text
screen centered_narration(content):

    frame:
        align (0.5, 0.5)
        background None
        xpadding 80
        ypadding 50
        xmargin 100
        ymargin 10

        text content:
            size 40
            color "#FFFFFF"
            font "fonts/Typewriter.ttf"
            textalign 0.5
            xalign 0.5

screen death_msg(content):
    frame:
        align (0.5, 0.15)
        background None
        xpadding 80
        ypadding 50
        xmargin 100
        ymargin 50
        
        text content:
                size 100
                color "#eb1414"
                font "fonts/Typewriter.ttf"
                textalign 0.5
                xalign 0.5