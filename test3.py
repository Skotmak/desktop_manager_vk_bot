from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    data = [(1, "A"), (2, "B"), (3, "C"), (4, "D")]
    model = QtGui.QStandardItemModel()
    for i, text in data:
        it = QtGui.QStandardItem(text)
        it.setData(i)
        model.appendRow(it)

    @QtCore.pyqtSlot(int)
    def on_currentIndexChanged(row):
        it = model.item(row)
        _id = it.data()
        name = it.text()
        print("selected name: ", name, ", id:", _id)

    w = QtWidgets.QComboBox()
    w.currentIndexChanged[int].connect(on_currentIndexChanged)
    w.setModel(model)
    w.show()
    sys.exit(app.exec_())
