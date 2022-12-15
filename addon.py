import xbmcgui
import xbmcplugin
import xbmcaddon

addon = xbmcaddon.Addon()

# RTHK TV 31
rthktv31 = "http://rthklive1-lh.akamaihd.net/i/rthk31_1@167495/index_2052_av-b.m3u8"
# RTHK TV 31
rthktv32 = "http://rthklive2-lh.akamaihd.net/i/rthk32_1@168450/index_2052_av-b.m3u8"

item31 = xbmcgui.ListItem('RTHK TV 31')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), rthktv31 , item31, isFolder=0)

item32 = xbmcgui.ListItem('RTHK TV 32')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), rthktv32 , item32, isFolder=0)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
