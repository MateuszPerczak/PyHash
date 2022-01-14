from platform import system as get_system

system: str = get_system()

if system == 'Darwin':
    from AppKit import NSColor

    def get_os_theme() -> str:
        if NSColor.currentControlTint() == NSColor.controlTintFollowWindowBackgroundColor():
            return 'Light'
        return 'Dark'
elif system == 'Windows':
    from winreg import OpenKey, HKEY_CURRENT_USER, KEY_READ, EnumValue

    def get_os_theme() -> str:
        try:
            if EnumValue(OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\\', 0, KEY_READ), 2)[1]:
                return 'Light'
            return 'Dark'
        except Exception:
            return 'Dark'

elif system == 'Linux':
    from gi.repository import Gtk

    def get_os_theme() -> str:
        if Gtk.Settings.get_default().get_property('gtk-application-prefer-dark-theme'):
            return 'Dark'
        return 'Light'


def get_theme() -> str:
    return get_os_theme()


# from winreg import OpenKey, HKEY_CURRENT_USER, KEY_READ, EnumValue

# def get_theme() -> str:
#     try:
#         if EnumValue(OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\\', 0, KEY_READ), 2)[1]:
#             return 'Light'
#         return 'Dark'
#     except Exception:
#         return 'Dark'
