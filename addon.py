import xbmcgui
import xbmcplugin
import xbmcaddon

addon = xbmcaddon.Addon()

# RTHK TV 31
rthktv31 = "http://rthk.hk/apps/screen/rthktv31.m3u8"
# RTHK TV 31
rthktv32 = "http://rthk.hk/apps/screen/rthktv32.m3u8"

item31 = xbmcgui.ListItem('RTHK TV 31')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), rthktv31 , item31, isFolder=0)

item32 = xbmcgui.ListItem('RTHK TV 32')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), rthktv32 , item32, isFolder=0)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
