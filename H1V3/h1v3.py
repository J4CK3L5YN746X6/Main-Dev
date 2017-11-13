import os, time, sys
# Basic Module import
# Third Party Modules
try:
    import colorama
    from colorama import Fore, Style, Back
except:
    print ' [!] Failed To import colorama module please do "pip install colorama"'
    sys.exit(1)

colorama.init(autoreset=True)

class MainOps:

    _Memory_ = {}
   
    # _template_ is the banner text, _type_ is the basic type entry, _msg_ is the message to print to screen, _ssv_ is the boolean variable to set start _Memory_ Placements n
    def _RaiseMsg_(self, _template_='Basic', _type_=None, _msg_=None, _ssv_=False):

        if _ssv_ == True:
            # Create variables pre-proccess
            # Color Append Open
            self._Memory_['system.msg.fore_green']    = Fore.GREEN
            self._Memory_['system.msg.fore_red']      = Fore.RED
            self._Memory_['system.msg.fore_blue']     = Fore.BLUE
            self._Memory_['system.msg.fore_yellow']   = Fore.YELLOW
            self._Memory_['system.msg.fore_white']    = Fore.WHITE
            self._Memory_['system.msg.fore_magenta']  = Fore.MAGENTA
            self._Memory_['system.msg.fore_reset']    = Fore.RESET
            self._Memory_['system.msg.back_green']    = Back.GREEN
            self._Memory_['system.msg.back_red']      = Back.RED
            self._Memory_['system.msg.back_blue']     = Back.BLUE
            self._Memory_['system.msg.back_yellow']   = Back.YELLOW
            self._Memory_['system.msg.back_white']    = Back.WHITE
            self._Memory_['system.msg.back_magenta']  = Back.MAGENTA
            self._Memory_['system.msg.back_reset']    = Back.RESET
            self._Memory_['system.msg.style_dim']     = Style.DIM
            self._Memory_['system.msg.style_nor']     = Style.NORMAL
            self._Memory_['system.msg.style_bri']     = Style.BRIGHT
            self._Memory_['system.msg.style_res']     = Style.RESET
            self._Memory_['system.msg.style_res-all'] = Style.RESET_ALL
            # Color Appending End
            # Template Appending Open
            self._Memory_['system.msg.templates']         = [ 'Basic' ]
            self._Memory_['system.msg.temp.heads']        = [ 'banner', 'warn', 'norm', 'crit' ]
            self._Memory_['system.msg.temp.Basic.banner'] = Fore.GREEN  +' [ @'+Fore.RED   +time.asctime()+Fore.GREEN  +'] <-> '
            self._Memory_['system.msg.temp.Basic.warn']   = Fore.RED    +' ['  +Fore.BLUE  +'WARNING '        +Fore.RED    +' -> '+Fore.WHITE
            self._Memory_['system.msg.temp.Basic.norm']   = Fore.MAGENTA+' ['  +Fore.YELLOW+'NORMAL  '        +Fore,MAGENTA+' -> '+Fore.WHITE
            self._Memory_['system.msg.temp.Basic.crit']   = Fore.RED    +' ['  +Fore.GREEN +'CRITICAL'        +Fore.RED    +' -> '+Fore.WHITE
            # Template Append Close
            return None

        if _template_ not in self._Memory_['system.msg.templates']:
            _template_ = 'Basic'
            pass

        if _type_ not in self._Memory_['system.msg.temp.heads']:
            _type_ = 'crit'
            _msg_  = 'Failed To Set Type Entered Exiting...'
            pass


        banner = self._Memory_['system.msg.'+str(_template_)+'.banner']
        head   = self._Memory_['systen.msg.'+str(_template_)+'.'+str(_type_)]
        print banner+head+_msg_
        return None

    # Start Up Object
    def _StartUp_(self):
        
        self._RaiseMsg_(_ssv_=True)

def Main():
    
    main = MainOps()
    main._StartUp_()

Main()
