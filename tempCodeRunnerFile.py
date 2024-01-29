self.table.setRowCount(selectResult.shape[0])
        self.table.setColumnCount(selectResult.shape[1])
        self.table.setHorizontalHeaderLabels(defaultHeaderLabels)
        for r in range(selectResult.shape[0]):
            for c in range(selectResult.shape[1]):
                tableItem = QTableWidgetItem(str(selectResult[r,c]))
                self.table.setItem(r,c,tableItem)