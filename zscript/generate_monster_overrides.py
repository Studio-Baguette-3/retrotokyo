#!/bin/env python

monsterClasses = [
'Arachnotron',
'Archvile',
'BaronOfHell',
'HellKnight',
'Cacodemon',
'Cyberdemon',
'Demon',
'Spectre',
'ChaingunGuy',
'DoomImp',
'Fatso',
'LostSoul',
'PainElemental',
'Revenant',
'ShotgunGuy',
'SpiderMastermind',
'WolfensteinSS',
'ZombieMan'
]

s = ""

for c in monsterClasses:
    news = '''
class RTXXXXXXXXX : XXXXXXXXX Replaces XXXXXXXXX
{
    Vector3 prevpos;
    float prevspd;
    int i;
    int prevstyle;

    override void PostBeginPlay()
    {
        prevspd = 0.0;
        i = 0;
        prevstyle = GetRenderStyle();
        //self.bBright = true;
    }

    override void Tick()
    {
        PlayerInfo p = players[consoleplayer];
        bool b = Cvar.GetCVar("rt_motionvision", p).GetBool();
        if (!b) {
            self.A_SetRenderStyle(1.0, prevstyle);
            return Super.Tick();
        } else {
            self.A_SetRenderStyle(1.0, STYLE_STENCIL);

            float spd = abs(((self.Pos.x - prevpos.x) * (self.Pos.x - prevpos.x)) + ((self.Pos.y - prevpos.y) * (self.Pos.y - prevpos.y)) + ((self.Pos.z - prevpos.z) * (self.Pos.z - prevpos.z)));
            spd = min(spd, 2000.0);
            spd = (prevspd * 0.8) + (spd * 3.0);
            int x = max(72, min(int(spd), 255));
            if (i > 3)
            {
                self.SetShade(Color(x, x, x)); // TODO: reset this??
                i = 0;
            }
            i = i + 1;
            prevpos = self.Pos;
            prevspd = spd;
            return Super.Tick();
        }
    }
}
    '''.replace('XXXXXXXXX', c)
    s = '%s\n%s' % (s, news)

with open('./monster_overrides.zsc', 'w') as f:
    f.write(s)
