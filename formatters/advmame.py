import json
import sys
import math
import pygame
import os
pygame.init()

#  TODO Abstract this into a base formatter class
if len(sys.argv) < 3:
    print "Formatter requires 2 arguments, input file and output file name"

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

input_file_data = open(input_file_name).read()
controller_mapping = json.loads(input_file_data)
num_players = len(controller_mapping)

#  Converts our mapping into a emulator specific value
def convert_event(event, default):

    if event["type"] == 3:
        return "or keyboard[%s,%s]" % (event['mod'], pygame.key.name(event["key"]).replace('left ', 'l').replace('right ', 'r'))
    elif event["type"] == 11:
        return "or joystick_button[%d,%s]" % (event['joy'], event["button"])
    elif event["type"] == 7:
        if event['value'] < 0:
            event['value'] = 1
        else:
            event['value'] = 0
        return  "or joystick_digital[%d,0,%s,%s]" % (event['joy'], event["axis"], event["value"] )
	
	return ''

		


player1 = (convert_event(controller_mapping[0]['UP'], 0), 
     convert_event(controller_mapping[0]['DOWN'], 0),
     convert_event(controller_mapping[0]['RIGHT'], 0),
     convert_event(controller_mapping[0]['LEFT'], 0),
     convert_event(controller_mapping[0]['Top 1'], 3), 
     convert_event(controller_mapping[0]['Top 2'], 2),
     convert_event(controller_mapping[0]['Top 3'], 1), 
     convert_event(controller_mapping[0]['Bottom 1'], 0), 
     convert_event(controller_mapping[0]['Bottom 2'], 4),
     convert_event(controller_mapping[0]['Bottom 3'], 6), 
     convert_event(controller_mapping[0]['START'], 9), 
     convert_event(controller_mapping[0]['COIN'], 8),
     convert_event(controller_mapping[0]['*EXIT_PROGRAM'], 5))

player2 = ((convert_event(controller_mapping[1]['UP'], 0), 
     convert_event(controller_mapping[1]['DOWN'], 0),
     convert_event(controller_mapping[1]['RIGHT'], 0),
     convert_event(controller_mapping[1]['LEFT'], 0),
     convert_event(controller_mapping[1]['Top 1'], 3), 
     convert_event(controller_mapping[1]['Top 2'], 2),
     convert_event(controller_mapping[1]['Top 3'], 1), 
     convert_event(controller_mapping[1]['Bottom 1'], 0), 
     convert_event(controller_mapping[1]['Bottom 2'], 4),
     convert_event(controller_mapping[1]['Bottom 3'], 6), 
     convert_event(controller_mapping[1]['START'], 9), 
     convert_event(controller_mapping[1]['COIN'], 8)) 
	 if num_players > 1 else (('',) * 12))
	 
	 
try:
    output_file_data = """
device_video_clock 5 - 50 / 15.62 / 50 ; 5 - 50 / 15.73 / 60
debug_crash no
debug_rawsound no
debug_speedmark no
device_alsa_device default
device_alsa_mixer channel
device_color_bgr15 yes
device_color_bgr16 yes
device_color_bgr24 yes
device_color_bgr32 yes
device_color_bgr8 yes
device_color_palette8 yes
device_color_yuy2 yes
device_joystick auto
device_keyboard auto
device_mouse auto
device_raw_firstkeyhack no
device_raw_mousedev[0] auto
device_raw_mousedev[1] auto
device_raw_mousedev[2] auto
device_raw_mousedev[3] auto
device_raw_mousetype[0] pnp
device_raw_mousetype[1] pnp
device_raw_mousetype[2] pnp
device_raw_mousetype[3] pnp
device_sdl_samples 512
device_sound auto
device_video auto
device_video_cursor auto
device_video_doublescan yes
device_video_fastchange no
device_video_interlace yes
device_video_output auto
device_video_overlaysize auto
device_video_singlescan yes
dir_artwork /home/pi/.advance/artwork:/usr/local/share/advance/artwork
dir_diff /home/pi/.advance/diff
dir_hi /home/pi/.advance/hi
dir_image /home/pi/.advance/image:/usr/local/share/advance/image
dir_inp /home/pi/.advance/inp
dir_memcard /home/pi/.advance/memcard
dir_nvram /home/pi/.advance/nvram
dir_rom /home/pi/.advance/rom:/home/pi/pimame/roms/advmame
dir_sample /home/pi/.advance/sample:/usr/local/share/advance/sample
dir_snap /home/pi/.advance/snap
dir_sta /home/pi/.advance/sta
display_adjust none
display_antialias yes
display_artwork_backdrop yes
display_artwork_bezel no
display_artwork_crop yes
display_artwork_overlay yes
display_aspectx 4
display_aspecty 3
display_beam 1
display_brightness 1
display_buffer no
display_color auto
display_expand 1
display_flicker 0
display_flipx no
display_flipy no
display_frameskip auto
display_gamma 1
display_intensity 1.5
display_interlaceeffect none
display_magnify 1
display_mode auto
display_pausebrightness 1
display_resize fractional
display_resizeeffect auto
display_restore yes
display_rgbeffect none
display_rol no
display_ror no
display_scanlines no
display_skipcolumns auto
display_skiplines auto
display_translucency yes
display_vsync yes
include 
input_hotkey yes
input_idleexit 0
input_map[coin5] auto
input_map[coin6] auto
input_map[coin7] auto
input_map[coin8] auto
input_map[event10] auto
input_map[event11] auto
input_map[event12] auto
input_map[event13] auto
input_map[event14] auto
input_map[event1] auto
input_map[event2] auto
input_map[event3] auto
input_map[event4] auto
input_map[event5] auto
input_map[event6] auto
input_map[event7] auto
input_map[event8] auto
input_map[event9] auto
input_map[p1_dialx] auto
input_map[p1_dialy] auto
input_map[p1_lightgunx] auto
input_map[p1_lightguny] auto
input_map[p1_mousex] auto
input_map[p1_mousey] auto
input_map[p1_paddlex] auto
input_map[p1_paddley] auto
input_map[p1_pedalbrake] auto
input_map[p1_pedalgas] auto
input_map[p1_pedalother] auto
input_map[p1_stickx] auto
input_map[p1_sticky] auto
input_map[p1_stickz] auto
input_map[p1_trackballx] auto
input_map[p1_trackbally] auto
input_map[p2_dialx] auto
input_map[p2_dialy] auto
input_map[p2_lightgunx] auto
input_map[p2_lightguny] auto
input_map[p2_mousex] auto
input_map[p2_mousey] auto
input_map[p2_paddlex] auto
input_map[p2_paddley] auto
input_map[p2_pedalbrake] auto
input_map[p2_pedalgas] auto
input_map[p2_pedalother] auto
input_map[p2_stickx] auto
input_map[p2_sticky] auto
input_map[p2_stickz] auto
input_map[p2_trackballx] auto
input_map[p2_trackbally] auto
input_map[p3_dialx] auto
input_map[p3_dialy] auto
input_map[p3_lightgunx] auto
input_map[p3_lightguny] auto
input_map[p3_mahjong_a] auto
input_map[p3_mahjong_b] auto
input_map[p3_mahjong_bet] auto
input_map[p3_mahjong_c] auto
input_map[p3_mahjong_chance] auto
input_map[p3_mahjong_chi] auto
input_map[p3_mahjong_d] auto
input_map[p3_mahjong_double_up] auto
input_map[p3_mahjong_e] auto
input_map[p3_mahjong_f] auto
input_map[p3_mahjong_flip_flop] auto
input_map[p3_mahjong_g] auto
input_map[p3_mahjong_h] auto
input_map[p3_mahjong_i] auto
input_map[p3_mahjong_j] auto
input_map[p3_mahjong_k] auto
input_map[p3_mahjong_kan] auto
input_map[p3_mahjong_l] auto
input_map[p3_mahjong_m] auto
input_map[p3_mahjong_n] auto
input_map[p3_mahjong_pon] auto
input_map[p3_mahjong_reach] auto
input_map[p3_mahjong_ron] auto
input_map[p3_mahjong_score] auto
input_map[p3_mousex] auto
input_map[p3_mousey] auto
input_map[p3_paddlex] auto
input_map[p3_paddley] auto
input_map[p3_pedalbrake] auto
input_map[p3_pedalgas] auto
input_map[p3_pedalother] auto
input_map[p3_stickx] auto
input_map[p3_sticky] auto
input_map[p3_stickz] auto
input_map[p3_trackballx] auto
input_map[p3_trackbally] auto
input_map[p4_dialx] auto
input_map[p4_dialy] auto
input_map[p4_lightgunx] auto
input_map[p4_lightguny] auto
input_map[p4_mahjong_a] auto
input_map[p4_mahjong_b] auto
input_map[p4_mahjong_bet] auto
input_map[p4_mahjong_c] auto
input_map[p4_mahjong_chance] auto
input_map[p4_mahjong_chi] auto
input_map[p4_mahjong_d] auto
input_map[p4_mahjong_double_up] auto
input_map[p4_mahjong_e] auto
input_map[p4_mahjong_f] auto
input_map[p4_mahjong_flip_flop] auto
input_map[p4_mahjong_g] auto
input_map[p4_mahjong_h] auto
input_map[p4_mahjong_i] auto
input_map[p4_mahjong_j] auto
input_map[p4_mahjong_k] auto
input_map[p4_mahjong_kan] auto
input_map[p4_mahjong_l] auto
input_map[p4_mahjong_m] auto
input_map[p4_mahjong_n] auto
input_map[p4_mahjong_pon] auto
input_map[p4_mahjong_reach] auto
input_map[p4_mahjong_ron] auto
input_map[p4_mahjong_score] auto
input_map[p4_mousex] auto
input_map[p4_mousey] auto
input_map[p4_paddlex] auto
input_map[p4_paddley] auto
input_map[p4_pedalbrake] auto
input_map[p4_pedalgas] auto
input_map[p4_pedalother] auto
input_map[p4_stickx] auto
input_map[p4_sticky] auto
input_map[p4_stickz] auto
input_map[p4_trackballx] auto
input_map[p4_trackbally] auto
input_map[safequit] auto
input_map[service_coin5] auto
input_map[service_coin6] auto
input_map[service_coin7] auto
input_map[service_coin8] auto
input_map[ui_toggle_ui] auto
input_steadykey no
lcd_server none
lcd_speed 4
lcd_timeout 500
misc_bios default
misc_cheat no
misc_cheatfile cheat.dat
misc_difficulty none
misc_eventdebug no
misc_eventfile event.dat
misc_freeplay yes
misc_hiscorefile hiscore.dat
misc_lang none
misc_languagefile english.lng
misc_mutedemo no
misc_quiet yes
misc_safequit yes
misc_smp no
misc_timetorun 0
record_sound no
record_sound_time 15
record_video no
record_video_interleave 2
record_video_time 15
script_coin1 
script_coin2 
script_coin3 
script_coin4 
script_emulation 
script_event1 
script_event10 
script_event11 
script_event12 
script_event13 
script_event14 
script_event2 
script_event3 
script_event4 
script_event5 
script_event6 
script_event7 
script_event8 
script_event9 
script_led1 on(kdb, 0b1); wait(!event()); off(kdb, 0b1);
script_led2 on(kdb, 0b10); wait(!event()); off(kdb, 0b10);
script_led3 
script_play 
script_safequit 
script_start1 
script_start2 
script_start3 
script_start4 
script_turbo while (event()) { toggle(kdb, 0b100); delay(100); } off(kdb, 0b100);
script_video wait(!event()); set(kdb, 0);
sound_adjust auto
sound_equalizer_highvolume 0
sound_equalizer_lowvolume 0
sound_equalizer_midvolume 0
sound_latency 0.05
sound_mode auto
sound_normalize yes
sound_samplerate 44100
sound_samples yes
sound_volume -3
sync_fps auto
sync_resample auto
sync_speed 1
sync_startuptime auto
sync_turbospeed 3
ui_color[help_other] 000000 808080
ui_color[help_p1] 000000 ffff00
ui_color[help_p2] 000000 00ff00
ui_color[help_p3] 000000 ff0000
ui_color[help_p4] 000000 00ffff
ui_color[interface] 000000 ffffff
ui_color[select] 000000 afffff
ui_color[tag] 247ef0 ffffff
ui_font auto
ui_fontsize auto
ui_helpimage auto
ui_translucency 0.8
input_map[p1_doubleleft_up] keyboard[1,scan0] or keyboard[0,8_pad]
input_map[p1_doubleleft_down] keyboard[1,scan0] or keyboard[0,2_pad]
input_map[p1_doubleleft_right] keyboard[1,scan0] or keyboard[0,6_pad]
input_map[p1_doubleleft_left] keyboard[1,scan0] or keyboard[0,4_pad]
input_map[p1_doubleright_up] keyboard[1,scan0] or keyboard[0,r]
input_map[p1_doubleright_down] keyboard[1,scan0] or keyboard[0,f]
input_map[p1_doubleright_right] keyboard[1,scan0] or keyboard[0,g]
input_map[p1_doubleright_left] keyboard[1,scan0] or keyboard[0,d]
input_map[p1_up] keyboard[1,scan0] %s
input_map[p1_down] keyboard[1,scan0] %s
input_map[p1_right] keyboard[1,scan0] %s
input_map[p1_left] keyboard[1,scan0] %s
input_map[p1_button1] keyboard[1,scan0] %s
input_map[p1_button2] keyboard[1,scan0] %s
input_map[p1_button3] keyboard[1,scan0] %s
input_map[p1_button4] keyboard[1,scan0] %s
input_map[p1_button5] keyboard[1,scan0] %s
input_map[p1_button6] keyboard[1,scan0] %s
input_map[p1_button7] keyboard[1,scan0]
input_map[p1_button8] keyboard[1,scan0]
input_map[start1] keyboard[1,scan0] %s
input_map[coin1] keyboard[1,scan0] %s
input_map[ui_cancel] keyboard[1,scan0] keyboard[1,scan0] or keyboard[0,esc] %s
input_map[p2_up] keyboard[1,scan0] %s
input_map[p2_down] keyboard[1,scan0] %s
input_map[p2_right] keyboard[1,scan0] %s
input_map[p2_left] keyboard[1,scan0] %s
input_map[p2_button1] keyboard[1,scan0] %s
input_map[p2_button2] keyboard[1,scan0] %s
input_map[p2_button3] keyboard[1,scan0] %s
input_map[p2_button4] keyboard[1,scan0] %s
input_map[p2_button5] keyboard[1,scan0] %s
input_map[p2_button6] keyboard[1,scan0] %s
input_map[p2_button7] keyboard[1,scan0]
input_map[p2_button8] keyboard[1,scan0]
input_map[start2] keyboard[1,scan0] %s
input_map[coin2] keyboard[1,scan0] %s
    """ % ( player1 +  player2 )
	 
except KeyError, e:
    print "Your input controller configuration didn't support a required button. Error: %s button required." % str(e)
    sys.exit()

directory = os.path.dirname(output_file_name)
if not os.path.exists(directory):
    os.makedirs(directory)


with open(output_file_name, "w") as output_file:
    output_file.write(output_file_data)

print output_file_name + " created."