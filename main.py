from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (500,800)

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: 'Add Entry'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current = 'AddEntry'

            OneLineListItem:
                text: 'View Entries'
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = 'ViewEntries'
            OneLineListItem:
                text: 'About'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current = 'About'


NavigationLayout:
    ScreenManager:
        id: screen_manager
        
        Screen:
            name: 'AddEntry'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'Add Entry'
                left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            BoxLayout:
                orientation: 'vertical'
                pos_hint: {'center_y': 0.68}
                size_hint_y: 0.8
                padding: 20
                spacing: 10
                MDLabel:
                    halign: 'center'
                    text: 'Enter Details Below:'
                MDTextField:
                    id: name
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Name'
                    helper_text: 'Enter Full Name'
                    helper_text_mode: 'on_focus'
                MDTextField:
                    id: year
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Year'
                    on_focus: if self.focus: app.YearMenu.open()
                MDTextField:
                    id: branch
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Branch'
                    on_focus: if self.focus: app.BranchMenu.open()
                MDTextField:
                    id: rollno
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Roll Number'
                    helper_text: 'eg. CO19314'
                    helper_text_mode: 'on_focus'
                MDTextField:
                    id: phoneno
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Mobile Number'
                    helper_text: 'Only Indian Mobile Numbers Allowed.'
                    helper_text_mode: 'on_focus'
            FloatLayout:
                MDRaisedButton:
                    text: 'Submit'
                    pos_hint: {'center_x': .5,'center_y': .15}
        Screen:
            name: 'ViewEntries'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'View Entries'
                left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            BoxLayout:
                orientation: 'vertical'
                
        Screen:
            name: 'About'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'About'
                left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            BoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: 'App Made By:'
                    font_style: 'H2'
                    halign: 'center'
                MDLabel:
                    text: 'Arjun Gupta - CO19314'
                    font_style: 'H4'
                    halign: 'center'
                MDLabel:
                    text: 'Charu Chaudhary - CO19319'
                    font_style: 'H4'
                    halign: 'center'
                
        Screen:
            name: 'EntryInfo'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'Details'
                left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            BoxLayout:
                orientation: 'vertical'

    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MyFirstApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

        years = [{"text": f"{i}"} for i in ['1st Year', '2nd Year', '3rd Year', '4th Year']]
        self.YearMenu = MDDropdownMenu(
            caller=self.screen.ids.year,
            items=years,
            position="bottom",
            callback=self.set_year,
            width_mult=100,
            border_margin=0)

        branches = [{"text": f"{i}"} for i in ['CSE', 'ECE', 'Mechanical', 'Civil']]
        self.BranchMenu = MDDropdownMenu(
            caller=self.screen.ids.branch,
            items=branches,
            position="bottom",
            callback=self.set_branch,
            width_mult=4, )

    def set_year(self, instance):
        def set_year(interval):
            self.screen.ids.year.text = instance.text
            self.YearMenu.dismiss()

        Clock.schedule_once(set_year, 0.5)

    def set_branch(self, instance):
        def set_branch(interval):
            self.screen.ids.branch.text = instance.text
            self.BranchMenu.dismiss()

        Clock.schedule_once(set_branch, 0.5)

    def build(self):
        return self.screen


MyFirstApp().run()
