#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QApplication
from PyQt5.QtCore import Qt


def main(): 
    app     = QApplication (sys.argv)
    tree    = QTreeWidget ()
    headerItem  = QTreeWidgetItem()
    item    = QTreeWidgetItem()
    with open('checkbox.css') as style:
        tree.setStyleSheet(style.read())
    for i in range(3):
        parent = QTreeWidgetItem(tree)
        parent.setText(0, "Parent {}".format(i))
        for x in range(5):
            child = QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, "Child {}".format(x))
            child.setCheckState(0, Qt.Unchecked)
    tree.show() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()