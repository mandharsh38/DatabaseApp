from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
import sqlite_database
from kivymd.uix.snackbar import Snackbar

Window.size = (500, 800)

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
                    id: mobile
                    size_hint: .7, None
                    pos_hint: {'center_x': .5}
                    hint_text: 'Mobile Number'
                    helper_text: 'Only Indian Mobile Numbers Allowed.'
                    helper_text_mode: 'on_focus'
            FloatLayout:
                MDRaisedButton:
                    text: 'Submit'
                    pos_hint: {'center_x': .5,'center_y': .15}
                    on_release: app.AddStudent()
        Screen:
            name: 'ViewEntries'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'View Entries'
                left_action_items: [["menu", lambda x: nav_drawer.set_state('open')]]
            FloatLayout:
                MDRaisedButton:
                    text: 'Search/View Details'
                    pos_hint: {'center_x': .3, 'center_y': .05}
                    on_release: app.ShowGetDetails()
                MDRaisedButton:
                    text: 'Delete a Record'
                    md_bg_color: (1,0,0,1)
                    pos_hint: {'center_x': .7, 'center_y': .05}
                    on_release: app.ShowDel()
                    
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
                size_hint_y: 0.6
                pos_hint: {"top": 0.8}
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
                left_action_items: [["arrow-left", lambda x: app.ShowEntries()]]
            BoxLayout:
                orientation: 'vertical'
                size_hint_y : 0.5
                pos_hint: {'top': 0.85}
                MDLabel:
                    id: name_text
                    halign: 'center'
                MDLabel:
                    id: year_text
                    halign: 'center'
                MDLabel:
                    id: branch_text
                    halign: 'center'
                MDLabel:
                    id: rollno_text
                    halign: 'center'
                MDLabel:
                    id: mobile_text
                    halign: 'center'
        Screen:
            name: 'del'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'Delete An Entry'
                left_action_items: [["arrow-left", lambda x: app.ShowEntries()]]
            MDTextField:
                id: del_stu
                size_hint: .7, None
                pos_hint: {'center_x': .5, 'center_y': 0.55}
                hint_text: 'Roll No.'
                helper_text: "This Student's Record will be permanently deleted"
                helper_text_mode: 'on_focus'
            MDRaisedButton:
                text: 'Delete'
                md_bg_color: (1,0,0,1)
                pos_hint: {'center_x': .5, 'center_y': 0.45}
                on_release: app.DeleteEntry()
        Screen:
            name: 'details'
            MDToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: 'Search Entry'
                left_action_items: [["arrow-left", lambda x: app.ShowEntries()]]
            MDTextField:
                id: get_stu
                size_hint: .7, None
                pos_hint: {'center_x': .5, 'center_y': 0.55}
                hint_text: 'Roll No.'
                helper_text: "Enter Roll No. to view student's details"
                helper_text_mode: 'on_focus'
            MDRaisedButton:
                text: 'Search'
                pos_hint: {'center_x': .5, 'center_y': 0.45}
                on_release: app.GetDetails()
                
    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            screen_manager: screen_manager
            nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class student:

    def __init__(self, name, year, branch, rollno, mobile):
        self.name = name
        self.year = year
        self.branch = branch
        self.rollno = rollno
        self.mobile = mobile


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

    def ShowEntries(self):
        self.root.ids.screen_manager.current = 'ViewEntries'

    def ShowInfo(self):
        self.root.ids.screen_manager.current = 'EntryInfo'

    def ShowDel(self):
        self.root.ids.screen_manager.current = 'del'

    def ShowGetDetails(self):
        self.root.ids.screen_manager.current = 'details'

    def AddStudent(self):
        name = self.root.ids.name.text
        year = self.root.ids.year.text
        branch = self.root.ids.branch.text
        rollno = self.root.ids.rollno.text
        mobile = self.root.ids.mobile.text

        if str(mobile) != '':
            stu = student(name, year, branch, rollno.lower(), mobile)
            sqlite_database.add_student(stu)

            Snackbar(text="Student Added").show()

            self.root.ids.name.text = ''
            self.root.ids.year.text = ''
            self.root.ids.branch.text = ''
            self.root.ids.rollno.text = ''
            self.root.ids.mobile.text = ''

        else:
            Snackbar(text="Please fill in all the details").show()

    def DeleteEntry(self):
        del_stu = self.root.ids.del_stu.text
        sqlite_database.delete_student(del_stu.lower())

        Snackbar(text="Deleted successfully").show()

        self.root.ids.del_stu.text = ''

    def GetDetails(self):
        get_rollno = self.root.ids.get_stu.text
        try:
            list_details = list(sqlite_database.get_student(get_rollno))
            if list_details[0] != '':
                name = list_details[0]
                year = list_details[1]
                branch = list_details[2]
                rollno = list_details[3]
                mobile = list_details[4]

                self.ShowInfo()

                self.root.ids.name_text.text = 'Name :        ' + name
                self.root.ids.year_text.text = 'Year :        ' + year
                self.root.ids.branch_text.text = 'Branch :        ' + branch
                self.root.ids.rollno_text.text = 'Roll No. :        ' + rollno
                self.root.ids.mobile_text.text = 'Phone No. :        ' + str(mobile)

        except:
            Snackbar(text="Student Not Found").show()


MyFirstApp().run()
