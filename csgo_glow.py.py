import pymem
import pymem.process
import keyboard

dwLocalPlayer = 0xD8B2CC
import pymem
import pymem.process
import keyboard

dwEntityList = (0x4A8F00C)
dwGlowObjectManager = (0x5296FA8)
dwLocalPlayer = (0xD28B1C)
m_iGlowIndex = (0xA428)
m_iTeamNum = (0xF4)
m_bDormant = (0xED)
m_iHealth = (0x100)
m_vecOrigin = (0x138)

def main():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
    
    while True:
        if keyboard.is_pressed('alt'):
            glow_manager = pm.read_int(client + dwGlowObjectManager)
            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_health = pm.read_int(entity + m_iHealth)
                    entity_dormant = pm.read_int(entity + m_bDormant)
                    if not entity_dormant:
                        if entity_team_id != local_player_team_id:
                            if entity_health > 0:
                                glow_index = pm.read_int(entity + m_iGlowIndex)
                                entity_glow = glow
