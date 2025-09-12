# loop progress
default loop_count = 0
default discovered_truth = False
default alex_trusted_count = 0
default sophie_trusted_count = 0
default memory_fragments = 0

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
image heaven = "images/misc/heaven.png"
image dead_body = "images/misc/body.png"
# friend
image friend smile = "images/friend/smile-long.png"
image friend smile_creepy = Transform("images/friend/smile.png", yoffset=-180, zoom=0.9)
image friend angry = Transform("images/friend/angry.png", yoffset=-180, zoom=0.9)
image friend evil = Transform("images/friend/evil.png", yoffset=-180, zoom=0.9)
image friend worried = Transform("images/friend/worried.png", yoffset=-180, zoom=0.9)
# stranger
image stranger angry = "images/stranger/angry.png"
image stranger angry_cropped = Transform("images/stranger/angry-cropped.png", yoffset=-180)
image stranger smile = "images/stranger/smile.png"
image stranger evil = "images/stranger/evil.png"
image stranger worried = "images/stranger/worried.png"

# music and sfx
define audio.heartbeat = "audio/heartbeat.mp3"
define audio.sting = "audio/sting.mp3"
define audio.laugh = "audio/laugh.mp3"
define audio.scream = "audio/scream.mp3"
define audio.bg_music-1 = "audio/bg_music-1.mp3"
define audio.bg_music-2 = "audio/bg_music-2.mp3"
define audio.bg_music-3 = "audiio/bg_music-3.mp3"
define audio.bg_music-4 = "audio/bg_music-4.mp3"

label start:
    show screen disclaimer
    $ renpy.pause(hard=True)
    hide screen disclaimer

    $ loop_count += 1
# intro 
    scene black
    play sound audio.heartbeat
    show screen centered_narration("Thump Thump... Thump Thump...")
    $ renpy.pause()
    stop sound fadeout 5.0
       
    if loop_count == 1:
        hide screen centered_narration
        " Your eyes snap open ..."

    elif loop_count <= 3:
        hide screen centered_narration
        "Your eyes snap open... AGAIN."
        "why does this feel familiar?"

    else:
        show screen centered_narration("Loop [loop_count]: The nightmare continues.......") 
        $ renpy.pause(2.0)
        stop sound fadeout 3.0
        hide screen centered_narration
        "You know what comes next..."

    scene bg room_clean at Transform(zoom=1.1)

    if loop_count == 1:
        u "Huhh....there am i???"

    elif loop_count <= 3:
        u "This room... I've been here before."

    else:
        u "Not again... PLEASE, NOT AGAIN."

    "You push urself upright and freeze."
    show hands at center, Transform(zoom=0.6) with dissolve

    if loop_count ==1:
        u "My ha-hands?? They're smeared with blood"
        "Sticky, half-dried stains, crusted under your nails."
        u "I don’t remember ho-how—"

    else:
        u "The blood... it's always the blood."
        "You have seen this before. Felt this ...before."

        if loop_count >= 3:
            u "BUT WHOSE BLOOD IS IT REALLY??"
    
    hide hands with dissolve

    # dead body intro
    show dead_body at center, Transform(zoom=0.5) with dissolve
    "The corpse lies by the door, silent."
    "The blood on the floor glistens. Your pulse pounds in your ears."

    if loop_count >= 2:
        "Wait... something about the body..."
        "The clothes... they look familiar. Too familiar."

        if loop_count >= 5:
            "The face is obscured, but the build, the hair..."
            u "No... it can't be..."

    hide dead_body with dissolve
        
    # frd introduction
    show friend smile at left with dissolve
    f "HEYY, LOOK AT ME!!"

    if loop_count == 1:
        "You blink hard… and nearly jump."
        u "A-Alex??!"
        u "What are you doing here? H-how—"

    else: 
        "Alex again. Always the same entrance."
        u "Alex... why are you always here when I wake up?"
        f "What do you mean 'always'? You must be confused from the trauma."

        if loop_count >= 4:
            "His smile doesn't reach his eyes. It never has."
    
    f "Just stay calm, okay? Can you do that for me?"
    f "You can trust me. I'll help you get out of this."
    f "Forget what you see. Forget what you think you remember."

    if loop_count >= 3:
        "His voice is steady, warm... rehearsed. Too rehearsed."
        u "You've said that before."
        f "Said what before? You're not making sense."
    
    hide friend with dissolve

    # stranger introduction
    show stranger worried at right with dissolve
    h "Don’t trust him"
    if loop_count == 1:
        "Then—another voice. A women you don’t recognize."
        u "W-wait… who the hell are you?!"
        h "Me? …I’m Sophie."

    else:
        "Sophie. Right on cue."
        u "Sophie... we meet again."
        s "Again? What are you talking about?"

        if loop_count >= 4:
            "But there's a flicker in her eyes. Recognition?"

    s "Don’t you dare listen to him!"
    s "Look at your hands. LOOK at them!"
    s "You think that blood is his? Or mine? or yours??"

    if loop_count >= 3:
        s "The truth is right in front of you, but you keep choosing to forget."
        u "What truth?"
        s "Look at the body. Really look."

    s "He’s lying to you. He always lies. He’s keeping you here!"
    "Her voice shakes, desperate. But her eyes… there’s truth in them or madness..?"

    hide stranger with dissolve

    show friend angry at left
    show stranger angry_cropped at right 

    if loop_count >= 4:
        "The same scene, the same choices. But this time, you notice things."
        "The way Alex's jaw tightens when Sophie mentions the body."
        "The way Sophie's hands shake - not from fear, but from frustration."
        "They both know more than they're saying."
# intro ends

    menu:
        "Who will you choose to trust this time?"
        "Talk to Alex" if alex_trusted_count < 3:
            $ alex_trusted_count += 1
            jump talk_alex
        "Talk to Sophie" if sophie_trusted_count < 3:
            $ sophie_trusted_count += 1
            jump talk_sophie
        "Examine the body once more" if loop_count >= 3:
            jump examine_body
        "Confront them both about the loops" if loop_count >= 5:
            jump confront_loops
    
# Branch - Talk to Alex
label talk_alex:
    hide stranger angry
    show friend smile at left with fade
    
    if alex_trusted_count == 1:
        f "Thank you for trusting me."
        u "I want to understand what's happening."
        f "Someone is manipulating this situation. Someone wants you to panic."
    elif alex_trusted_count == 2:
        f "You came to me again. Good."
        u "Alex... why do I feel like we've had this conversation before?"
        f "You're just confused. The trauma is affecting your memory."
        "But his smile wavers for just a moment."
    else:
        f "Always choosing me. That's... that's good."
        u "Alex, I'm starting to remember things. Things about us."
        f "Don't. Please don't try to remember."
        "There's desperation in his voice now."

    menu:
        "How do you respond?"
        "Trust him completely":
            jump trust_alex
        "Question him further":
            jump question_alex
        "Accuse him":
            jump accuse_alex

# Branch - Talk to Sophie 
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

# Branch - Examine dead body 
label examine_body:
    hide friend angry
    hide stranger angry_cropped
    "You ignore both of them and walk toward the corpse."
    show dead_body at center, Transform(zoom=0.7) with dissolve

    u "I need to see..."
    f "Don't! You don't want to see that!"
    s "Yes... look closer. You need to know."
    "You kneel beside the body, your heart racing."
    "The face is turned away, but something about it..."
    u "The clothes... these are my clothes."
    u "The watch on the wrist... that's my watch."
    "Your hands tremble as you reach toward the body's face."

    menu:
        "DO YOU WANNA KNOW THE TRUTH??"
        "Yes, I need to know":
            jump reveal_truth
        "No, I can't do this":
            jump deny_truth

# Branch - Confront about loops
label confront_loops:
    u "Enoughh! I know whats happening HERE"
    u "This is loop number [loop_count]. I have died here [loop_count] times!!"
    u "One of you is keeping me trapped!"

    show friend angry at left
    show stranger worried at right 

    show friend worried at left
    show stranger worried at right
    
    f "You're not making sense..."
    s "He's finally remembering..."
    
    u "The body by the door - it's mine, isn't it?"
    
    "Both of them freeze."
    jump choose_confrontation

# do u need truth
label deny_truth:
    "You jerk your hand back, scrambling away from the body."
    hide dead_body with dissolve
    u "No... NO! This isn't real!"
    u "I'm alive! I'm standing right here!"
    
    show friend worried at left with dissolve
    f "That's right! Don't let her tricks fool you!"
    
    show stranger angry at right with dissolve
    s "You coward!!! You're choosing ignorance over truth!!!"
    s "How many more times will you run from reality??!?!!"
    
    u "I don't care what either of you say! I'm getting out of here!"
    "You run toward the door, but it slams shut before you reach it."
    scene black 
    
    show screen death_msg("DENIAL ONLY MAKES THE PRISON STRONGER")
    $ renpy.pause(2.0)
    hide screen death_msg
    
    show screen centered_narration("The harder you fight the truth, the tighter the chains become...")
    $ renpy.pause(2.0)
    hide screen centered_narration
    jump start

label reveal_truth:
    $ discovered_truth = True
    $ memory_fragments += 3

    "You turn the face..."
    scene black
    "Its your own face. pale, lifeless.... but unmistakable yours."

    scene bg room_bloody with dissolve
    u "I'm... I'm dead?"
    show stranger worried at right with dissolve
    s "Finally. You're beginning to understand."
    show friend worried at left with dissolve
    f "No! Don't listen to her! It's not real!"
    "The room shifts around you. The clean walls now show blood spatters."
    "Everything you thought you knew crumbles."
    s "You died three days ago. Alex killed you in a fit of rage."
    s "But your consciousness... it's trapped. Replaying this moment over and over."
    f "She's lying! I would never hurt you!"
    u "Then explain the body! Explain why I keep waking up here!"
    "Alex's facade finally cracks."
    f "Because... because I can't let you go."
    show friend evil at left with dissolve
    pause(0.1)
    hide friend evil
    show friend worried at left with dissolve
    f "but I didn't mean to kill you. It was an accident!"
    f "But if you remember, if you accept it... you'll leave me."
    hide friend worried
    show stranger smile at center with dissolve
    "Sophie steps forward, her form becoming more translucent."
    s "I'm not really Sophie. I'm part of you, the part that wants to remember, to move on."
    s "Alex's guilt is keeping you here, but only you can choose to break free."

    menu:
        "What do you choose??"
        "Forgive Alex and break the loop":
            jump true_ending
        "Stay trapped to protect Alex":
            jump sacrifice_ending
        "Reject this reality":
            jump denial_ending

# alex branches  
label trust_alex:
    if alex_trusted_count >= 3:
        jump alex_breakdown
    else:
        scene black
        show screen death_msg("SOPHIE'S FRUSTRATION TEARS THROUGH REALITY")
        $ renpy.pause()
        hide screen death_msg
        jump start

label accuse_alex:
    show friend angry at left with dissolve
    u "Alex... I think you're the one who's been lying."
    
    if loop_count >= 4:
        u "Every loop, you try to make me forget...WHY??"
        f "Loop?? What are you talking about??"
        u " You know exactly what I am talking about"

    f "After everything I've done for you, you accuse me?!"
    f "Fine. Believe her lies if you want!"

    $ memory_fragments += 1
    hide friend angry
    show stranger smile at right with dissolve
    s "Finally. You are starting to see"
    "A sharp scream cuts through the room then....silence"

    show friend evil at left with dissolve
    pause(0.1)
    hide friend evilwith dissolve

    scene black with fade
    if memory_fragments >= 2:
        show screen centered_narration("Alex's rage consumes everything... but this time, you remember more.")
        $ renpy.pause()
        hide screen centered_narration
        show screen centered_narration("Fragments of memory pierce through the darkness..")
        $ renpy.pause()
        hide screen centered_narration
        scene black
        jump memory_breakthrough
    else:
        scene black
        show screen death_msg("YOU DIED!")
        $ renpy.pause()
        hide screen death_msg
        jump start

label question_alex:
    u "Alex, I need you to be honest with me. What really happened here?"
    show friend worried at left
    f "I... I can't tell you everything. Not yet."
    u "Why not?"
    f "Because if you knew the truth... you'd hate me."
    "His voice breaks slightly."
    f "And I can't bear the thought of you hating me."
    
    menu:
        "Nothing you could say would make me hate you.":
            jump alex_confession
        "You're scaring me, Alex.":
            jump alex_breakdown

label alex_breakdown:
    show friend worried at center with dissolve
    f "I... I can't keep doing this."
    f "You want the truth? Fine. FINEE!!"
    scene bg room_dark with dissolve

    show friend angry at center
    f "I fought that night. You said you were leaving me."
    f "You said you couldn't love someone so possessive, so controlling."
    f "And I... I lost it. I grabbed you. Shook you."

    show friend worried at center
    f "You tried to pull away and I pushed you. So hard."
    f "Your head... it hit the corner of that table."
    f "There was so much blood..."
    u "Alex..."

    show friend angry at center
    f "But I found a way! I found a way to bring you back!"
    f "Every time you remember, every time you try to leave, I reset it all!"
    f "I won't let you abandon me again!"
    show friend evil at center with dissolve
    f "And I'll keep doing it! Forever if I have to!"
    f "You belong to me! In life, in death, FOREVER!"
    show stranger angry at right
    s "His obsession is consuming everything! Even your death isn't enough for him!"
    u "Alex, this isn't love... this is madness!"

    scene black 
    show screen death_msg("OBSESSION DEVOURS ALL")
    $ renpy.pause()
    hide screen death_msg

    show screen centered_narration("Alex's possessive rage tears through reality itself...")
    $ renpy.pause(2.0)
    hide screen centered_narration

    show screen centered_narration("The cycle feeds on his inability to let go...")
    $ renpy.pause(2.0)
    hide screen centered_narration

    jump start    

label alex_confession:
    scene bg room_dark with dissolve
    show friend angry at left with dissolve

    f "You... you really want to know?"
    f "We had a fight. A terrible fight about you wanting to leave."
    f "I got angry.. angrier than I had ever been."
    f "And I... God, I pushed you. You hit your head on the corner of the table."
    f "You died instantly. And I've been trying to bring you back ever since."
    f "This place... it's not real. It's my guilt, my desperation, keeping your spirit trapped."
    u "Alex..."
    f "I know it's selfish, but I can't let you go."

    jump choose_fate

# sophie branches
label trust_sophie:
    if sophie_trusted_count >= 3:
        jump sophie_revelation
    else:
        scene black
        show screen death_msg("ALEX'S DESPERATION RESETS EVERYTHING")
        $ renpy.pause()
        hide screen death_msg
        jump start

label accuse_sophie:
    show stranger smile at right with dissolve
    u "Sophie... I think you're the one manipulating me."
    show stranger worried at right with dissolve
    s "What? I'm trying to help you find the truth!"
    u "Or you're trying to drive me insane."
    show friend smile at left with dissolve
    f "Finally! You see it too! She can't be trusted."
    s "You're making a terrible mistake... He's the one who killed you!"
    u "I don't know who to believe anymore!"
    s "Fine. If you won't listen to words... stay trapped forever!"
    show friend evil at left
    f "Yes! Choose me! Forget her lies!"
    scene black with hpunch
    
    show screen death_msg("DENIAL FEEDS THE NIGHTMARE")
    $ renpy.pause(2.0)
    hide screen death_msg
    
    show screen centered_narration("The cycle begins again...")
    $ renpy.pause(2.0)
    hide screen centered_narration
    jump start
   
label sophie_revelation:
    show stranger smile at center with dissolve
    s "You've trusted me enough times now. You're ready for the truth."
    s "I am you. The part of you that refuses to be trapped."
    s "Alex's love has become a prison. His guilt keeps you here."
    s "But you have the power to break free."

    jump examine_body

# ENDINGS
label true_ending:
    scene black
    "The room begins to dissolve around you."
    scene heaven at Transform(zoom=1.1)
    show friend worried at center with dissolve
    u "Alex.... I forgive you."
    f "NO! Dont't leave me!"
    u "You have to let me go... and you have to forgive yourself"
    "The light grows brighter"
    s "You are free now. Both of you"

    scene black
    show screen centered_narration("You have broken the cycle. Alex will have to face reality, but your spirit is finally at peace.")
    $ renpy.pause()
    hide screen centered_narration

    return

label sacrifice_ending:
    scene bg room_clean at Transform(zoom=1.1) with dissolve
    u "I...I can't leave you like this, Alex"
    show friend smile_creepy at center 
    f "You will stay??"
    u "I will stay"
    s "then the loop continues......"
    scene black with fade
    show screen centered_narration("You have chosen to remain trapped. The cycle begins anew, as it has countless times before.")
    $ renpy.pause()
    hide screen centered_narration
    $ loop_count = 0
    jump start

label denial_ending:
    u "No! This isnt real! None of this is real"

    scene black with vpunch
    show screen death_msg("DENIAL ONLY DEEPENS THE NIGHTMARE")
    $ renpy.pause()
    hide screen death_msg
    scene black with fade
    jump start

label justice_ending:
    u "Alex, you have to face what you've done."
    u "Keeping me here won't change the past."
    
    scene heaven at Transform(zoom=1.1) with dissolve
    show friend worried at center
    f "I... I know. I'm sorry. I'm so sorry."
    pause(2.0)
    "The room fades as Alex finally accepts his guilt."
    scene black with fade
    show screen centered_narration("Alex will turn himself in. Your spirit is free, and justice will be served.")
    $ renpy.pause()
    hide screen centered_narration
    
    return

label memory_breakthrough:
    scene bg room_bloody with dissolve
    "In the moment before the loop resets, you see it clearly."
    "Your own body. Your own blood."
    "The truth Alex has been hiding."
    $ discovered_truth = True
    jump start

#  loop branch continuation
label choose_confrontation:
    menu:
        "who do you cofront??"
        "demand Alex to tell the truth":
            jump alex_breakdown
        "Ask sophie to explain everything":
            jump sophie_revelation
        "Examine you own body ..again":
            jump final_revelation

label final_revelation:
    "You walk to the body one final time."
    "This time, you know what you'll find."
    show dead_body at center
    "Your own face stares back at you."
    u "I remember now. The fight. The accident. The guilt."
    scene bg room_dark with dissolve
    show friend evil at left
    show stranger smile at right

    u "Alex, you killed me. Sophie, you're my desire for peace."
    u "And this… this is purgatory (a place where souls wait between life and death)"
    
    jump choose_fate

label choose_fate:
    menu:
        "How will you end this?"
        "Forgive and find peace":
            jump true_ending
        "Stay to protect Alex from his guilt":
            jump sacrifice_ending
        "Demand justice":
            jump justice_ending

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
                color "#c40000"
                font "fonts/Typewriter.ttf"
                textalign 0.5
                xalign 0.5

# Disclaimer
screen disclaimer():
    tag menu
    frame:
        background "#000000e6"
        xalign 0.5
        yalign 0.5
        padding (50, 50)
        vbox:
            spacing 28
            xalign 0.5
            text " DISCLAIMER " style "disclaimer_title"
            text "This visual novel contains mature themes including\nviolence, psychological distress, and challenging\nrelationship dynamics." style "disclaimer_text"
            text "It may not be suitable if you are sensitive to\nblood, disturbing conversations, or intense subject matter." style "disclaimer_text"
            text "If you need support, please visit 🌍 findahelpline.com" style "disclaimer_help"
            text "By continuing, you acknowledge that you are prepared\nfor a story with unsettling and potentially triggering content." style "disclaimer_text"
            text "Remember: This is a fictional work. Your well-being,\nhowever, is very real and important." style "disclaimer_note"
            hbox:
                spacing 80
                xalign 0.5
                textbutton "▶ CONTINUE" action Return(True) style "disclaimer_button"
                textbutton "❌ EXIT" action Quit(confirm=False) style "disclaimer_button"

style disclaimer_title is text:
    size 45
    color "#aa001c"
    bold True
    font "fonts/Typewriter.ttf"
    xalign 0.5
    text_align 0.5

style disclaimer_text is text:
    size 20
    color "#e0e0e0"
    font "fonts/Typewriter.ttf"
    text_align 0.5
    xalign 0.5

style disclaimer_help is text:
    size 20
    color "#00dffc"
    font "fonts/Typewriter.ttf"
    bold True
    text_align 0.5
    xalign 0.5

style disclaimer_note is text:
    size 18
    color "#bbbbbb"
    font "fonts/Typewriter.ttf"
    italic True
    text_align 0.5
    xalign 0.5

style disclaimer_button is button:
    hover_background "#971400"
    padding (18, 12)
    xalign 0.5

style disclaimer_button_text is text:
    size 22
    color "#ffffff"
    font "fonts/Typewriter.ttf"
    xalign 0.5
    text_align 0.5