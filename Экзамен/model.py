class XoModel:
    def __init__(self,size):
        print("XoModel")
        self.size = size
        self.game_area = []
        for i in range (self.size):
            row = []
            for j in  range(self.size): 
                cell = ["-"]
                row.append(cell)
            self.game_area.append(row)


    def __str__(self):
        new_matrix = ""
        for r in range(len(self.game_area)) :
            new_matrix += f"{self.game_area[r]}\n"
        return new_matrix

        

    def set (self,row, col, char):
        letters = []
        letters_l = ["a","b","c","d","e","f","g","h","i","j"]
        row_num = None
        for i in range(1, self.size+1):
            let = (letters_l[i-1],i)
            letters.append(let)

        for n in letters:
            if row == n[0]:
                row_num = n[1]
    
        self.game_area[row_num][col] = [char]

    def row(self, row_num):
        return  tuple(str(x[0]) for x in self.game_area[row_num])
    
    def col(self, col_num):
        col = []
        for i in range(self.size):
            col.append((self.game_area[i][col_num-1][0]))
        new_col = col
        col = []
        return  tuple(new_col)
    
    def diag(self, k):
        diag = []
        if k == 1:
            for i in range(self.size):
                diag.append(self.game_area[i][i][0])
            new_diag = diag
            diag = []
            return new_diag
        elif k == -1:
            for i in range(self.size-1,-1,-1):
                diag.append(self.game_area[i][i][0])
            new_diag = diag
            diag = []
            return new_diag



    




        


        





        

        






if __name__ == "__main__":
    model = XoModel(4)
    # print(model.game_area)
    model.__str__()
    model.set("c", 2, "O")
    print(model.game_area)
    print(model.row(2))
    print(model.col(3))
    print(model.diag(1))
    print(model.diag(-1))







