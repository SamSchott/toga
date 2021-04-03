from ..libs import Gtk
from .base import Widget


class Column(Widget):
    def create(self):
        self.native = Gtk.TreeViewColumn("")
        self.native.interface = self.interface
        self.native._impl = self

    def set_editable(self, value):
        # editable state is handled by CellRenderer
        pass

    def set_title(self, value):
        self.native.set_title(value)

    def set_on_toggle(self, handler):
        pass

    def set_on_change(self, handler):
        pass

    def rehint(self):
        pass
