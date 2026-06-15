import random

team = {
    "name": "Uganda Cranes",
    "morale": 70,
    "strength": 70,
    "injuries": 0,
    "wins": 0,
    "losses": 0,
    "stage": "Pre-Tournament",
}


def sep(char="=", width=58):
    print(char * width)


def show_stats():
    injuries_text = f"{team['injuries']} injured" if team["injuries"] else "Full squad"
    print(f"\n  TEAM STATS  |  {team['name']}")
    sep()
    print(f"  Morale  : {'#' * (team['morale'] // 10):<10} {team['morale']}/100")
    print(f"  Strength: {'#' * (team['strength'] // 10):<10} {team['strength']}/100")
    print(f"  Squad   : {injuries_text}")
    print(f"  Record  : {team['wins']}W - {team['losses']}L")
    sep()


def label(stmt, reason):
    sep("-")
    print(f"  LOOP CONTROL -> [{stmt}]")
    print(f"     WHY: {reason}")
    sep("-")


def clamp(val, lo=0, hi=100):
    return max(lo, min(hi, val))


def apply(morale=0, strength=0, injuries=0):
    team["morale"] = clamp(team["morale"] + morale)
    team["strength"] = clamp(team["strength"] + strength)
    team["injuries"] = max(0, team["injuries"] + injuries)


def pre_tournament():
    sep()
    print("  PHASE 1: PRE-TOURNAMENT PREPARATION")
    print("  Run 4 training sessions before the World Cup begins.")
    sep()

    session = 1
    total_sessions = 4

    label(
        "WHILE",
        "Training loop runs WHILE session <= total_sessions. Each iteration is one training session.",
    )

    while session <= total_sessions:
        show_stats()
        print(f"  Session {session}/{total_sessions} - Choose an activity:")
        print("  [1] Intense Drill     (+strength, risk of injury)")
        print("  [2] Friendly Match    (+morale, slight strength boost)")
        print("  [3] Recovery Day      (heal injuries, +morale)")
        print("  [4] Skip Session      (player protest - skip this session)")
        choice = input("\n  Your choice: ").strip()

        if choice == "4":
            label(
                "CONTINUE",
                "Player protest forces session to be skipped. continue jumps immediately to the next iteration without applying any training effect.",
            )
            print("  Players refuse to train! Session skipped - morale drops.")
            apply(morale=-10)
            session += 1
            continue

        if choice == "1":
            injury_risk = random.random()
            if injury_risk < 0.35:
                apply(strength=+10, injuries=+1)
                print("  Intense drill - strength up! But a player got injured.")
            else:
                apply(strength=+12)
                print("  Intense drill - great session! Strength up.")

        elif choice == "2":
            apply(morale=+12, strength=+5)
            print("  Friendly match - good result! Morale and strength up.")

        elif choice == "3":
            healed = min(team["injuries"], 2)
            apply(morale=+8, injuries=-healed)
            if healed:
                print(f"  Recovery day - {healed} player(s) cleared to play. Morale up.")
            else:
                print("  Recovery day - squad is rested. Morale up.")

        else:
            label(
                "PASS",
                "Invalid or unrecognised input. pass is used here as a placeholder for a future Scout Opponents feature.",
            )
            print("  Scouting feature coming soon - nothing happens this turn.")
            pass

        session += 1

    print("\n  Pre-tournament preparation complete!")
    show_stats()
    input("  Press Enter to begin the Group Stage... ")


MATCH_ACTIONS = {
    "1": ("Attack",),
    "2": ("Defend",),
    "3": ("Sub",),
    "4": ("Concede",),
}


def play_match(opponent, stage, can_draw=True):
    sep()
    print(f"  {stage.upper()}: Uganda Cranes  vs  {opponent}")
    sep()

    our_goals = 0
    their_goals = 0
    minute = 1
    rounds = 9

    eff_strength = clamp(team["strength"] - team["injuries"] * 5)
    base_score = eff_strength / 100

    label(
        "WHILE",
        f"Match loop runs WHILE minute <= {rounds} (each step is about 10 match minutes). Loop ends naturally at full time or earlier via break.",
    )

    while minute <= rounds:
        print(f"\n  ~Minute {minute * 10}/90  |  Cranes {our_goals} - {their_goals} {opponent}")
        print(f"  Morale boost: {'+' if team['morale'] >= 70 else '-'}  |  Eff. Strength: {eff_strength}/100")
        print("  [1] Attack   [2] Defend   [3] Substitute   [4] Concede (give up)")
        choice = input("  Action: ").strip()

        if choice == "4":
            label(
                "BREAK",
                "Manager concedes the match. break exits the while loop immediately, so no more rounds are played.",
            )
            print(f"  Uganda Cranes concedes to {opponent}!")
            their_goals += 3
            break

        if choice == "3":
            if team["injuries"] > 0:
                label(
                    "CONTINUE",
                    "A key player is being substituted due to injury. continue skips this round's attack/defend logic and jumps to the next minute.",
                )
                apply(injuries=-1)
                eff_strength = clamp(team["strength"] - team["injuries"] * 5)
                print(f"  Substitution made. Injuries now: {team['injuries']}. New eff. strength: {eff_strength}/100")
            else:
                print("  No injuries to sub out. Wasting the substitution...")
            minute += 1
            continue

        if choice == "1":
            morale_boost = 0.1 if team["morale"] >= 70 else 0.0
            scored = random.random() < (base_score + morale_boost)
            if scored:
                our_goals += 1
                apply(morale=+5)
                print(f"  GOAL! Cranes score! [{our_goals}-{their_goals}]")
            else:
                if random.random() < 0.3:
                    their_goals += 1
                    apply(morale=-5)
                    print(f"  Counter! {opponent} scores! [{our_goals}-{their_goals}]")
                else:
                    print("  Shot saved! Good attempt though.")

        elif choice == "2":
            if random.random() < 0.2:
                their_goals += 1
                print(f"  {opponent} breaks through defence! [{our_goals}-{their_goals}]")
            else:
                print(f"  Solid defending - {opponent} held back.")

        else:
            label(
                "PASS",
                "Unrecognised input. pass is used as a placeholder for a future Tactical Foul option.",
            )
            print("  Tactical Foul feature coming soon - no action taken.")
            pass

        minute += 1

    sep()
    print(f"  FULL TIME: Cranes {our_goals} - {their_goals} {opponent}")
    sep()

    if our_goals > their_goals:
        print(f"  VICTORY! Uganda Cranes beat {opponent}!")
        apply(morale=+15, strength=+5)
        team["wins"] += 1
        return "win"

    if our_goals < their_goals:
        print(f"  DEFEAT. {opponent} wins.")
        apply(morale=-15, strength=-5)
        team["losses"] += 1
        return "loss"

    if can_draw:
        print("  DRAW - 1 point earned.")
        apply(morale=+5)
        return "draw"

    print("  Draw in knockout! Going to penalties...")
    our_pen = random.randint(3, 5)
    their_pen = random.randint(3, 5)
    print(f"  Penalties - Cranes: {our_pen}  |  {opponent}: {their_pen}")
    if our_pen >= their_pen:
        print("  Cranes win on penalties!")
        apply(morale=+10)
        team["wins"] += 1
        return "win"

    print("  Cranes lose on penalties.")
    apply(morale=-10)
    team["losses"] += 1
    return "loss"


def group_stage():
    sep()
    print("  PHASE 2: GROUP STAGE")
    print("  Win at least 2 of 3 matches to advance.")
    sep()

    group_opponents = ["Egypt", "Mexico", "Japan"]
    points = 0
    group_wins = 0

    for i, opp in enumerate(group_opponents, 1):
        show_stats()
        input(f"  Press Enter to play Group Match {i}/3 vs {opp}... ")
        result = play_match(opp, f"Group Match {i}", can_draw=True)

        if result == "win":
            points += 3
            group_wins += 1
        elif result == "draw":
            points += 1

        print(f"\n  Group points so far: {points}")

        if team["losses"] >= 2:
            label(
                "BREAK",
                "Two group losses make qualification impossible, so break exits the group-match loop early.",
            )
            print("  Eliminated from the group stage. Tournament over.")
            break

        if team["morale"] < 40:
            label(
                "CONTINUE",
                "Morale is critically low. Press conference is cancelled, so continue skips the post-match morale boost routine.",
            )
            print("  Morale too low - press conference skipped. Moving on.")
            continue

        print("  Post-match press conference - fans cheer! +5 morale.")
        apply(morale=+5)

    return group_wins >= 2 or points >= 6


def knockout_stage():
    rounds = [
        ("Round of 16", "Senegal"),
        ("Quarter-Final", "Argentina"),
        ("Semi-Final", "France"),
        ("FINAL", "Brazil"),
    ]

    sep()
    print("  PHASE 3: KNOCKOUT STAGES")
    print("  One loss and you go home. Win all 4 to lift the trophy.")
    sep()

    label(
        "WHILE",
        "Knockout loop runs WHILE there are still rounds left and the team is still in the tournament. A loss triggers break.",
    )

    stage_index = 0
    while stage_index < len(rounds):
        stage_name, opponent = rounds[stage_index]
        show_stats()
        input(f"\n  Press Enter to play the {stage_name} vs {opponent}... ")
        result = play_match(opponent, stage_name, can_draw=False)

        if result == "loss":
            label(
                "BREAK",
                f"Eliminated in the {stage_name}. In knockouts, one loss ends everything, so break exits the knockout loop.",
            )
            print(f"\n  Uganda Cranes are OUT in the {stage_name}.")
            break

        if result == "win":
            if stage_name == "FINAL":
                label(
                    "BREAK",
                    "World champions. The tournament is over, so break exits the knockout loop because there are no more matches to play.",
                )
                print("\n  UGANDA CRANES WIN THE FIFA WORLD CUP 2026!")
                break

            print("\n  Through to the next round!")

            if team["injuries"] >= 3:
                label(
                    "CONTINUE",
                    f"{team['injuries']} players are injured, so continue skips the celebration and goes straight to the next knockout match.",
                )
                print(f"  {team['injuries']} injured - medical emergency, no celebration.")
                apply(injuries=-1)
                stage_index += 1
                continue

            label(
                "PASS",
                "Placeholder for a post-match press conference feature that is not yet implemented. pass keeps the loop body valid without executing any logic here.",
            )
            print("  Celebration with fans! +10 morale.")
            apply(morale=+10)

        stage_index += 1


def print_summary():
    sep()
    print("  LOOP CONTROL STATEMENTS - ASSIGNMENT SUMMARY")
    sep()
    rows = [
        ("WHILE (Pre-tournament)", "Training loop runs while sessions remain"),
        ("WHILE (Match engine)", "Match clock runs while rounds <= 9"),
        ("WHILE (Knockouts)", "Knockout loop runs while stages remain"),
        ("BREAK (Concede match)", "Manager concedes - exits match loop instantly"),
        ("BREAK (2 group losses)", "Impossible to qualify - exits group loop early"),
        ("BREAK (Knockout loss)", "One loss ends the tournament - exits loop"),
        ("BREAK (Win final)", "Champions! No matches left - exits loop"),
        ("CONTINUE (Skip session)", "Player protest - skips training session"),
        ("CONTINUE (Substitute)", "Injury sub - skips attack logic for that minute"),
        ("CONTINUE (Low morale)", "Morale < 40 - skips post-match press conference"),
        ("CONTINUE (Injuries >= 3)", "Emergency medical - skips celebration round"),
        ("PASS (Training slot)", "Placeholder for future Scout Opponents feature"),
        ("PASS (Match action)", "Placeholder for future Tactical Foul feature"),
        ("PASS (Post-match)", "Placeholder for future Press Conference feature"),
    ]
    for stmt, desc in rows:
        print(f"  [{stmt:<30}]  {desc}")
    sep()
    show_stats()


if __name__ == "__main__":
    sep()
    print("  FIFA WORLD CUP 2026 - UGANDA CRANES MANAGER")
    print("  Guide your team from training camp to the trophy.")
    sep()

    pre_tournament()

    advanced = group_stage()

    if advanced:
        print("\n  Uganda Cranes advance to the Knockout Stage!")
        input("  Press Enter to continue... ")
        knockout_stage()
    else:
        print("\n  Uganda Cranes did not advance from the group stage.")

    print_summary()
