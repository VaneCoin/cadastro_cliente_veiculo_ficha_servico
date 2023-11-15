from modules import *
class Funcs():
    def limpa_tela_principal(self):
        self.item_entry1.delete(0, END)
        self.item_entry2.delete(0, END)
        self.item_entry3.delete(0, END)
        self.item_entry4.delete(0, END)
        self.item_entry5.delete(0, END)
        self.item_entry6.delete(0, END)
        self.item_entry7.delete(0, END)
        self.item_entry8.delete(0, END)
        self.item_entry9.delete(0, END)
        self.item_entry10.delete(0, END)
        self.item_entry11.delete(0, END)
        self.item_entry12.delete(0, END)
        self.valor_entry1.delete(0, END)
        self.valor_entry2.delete(0, END)
        self.valor_entry3.delete(0, END)
        self.valor_entry4.delete(0, END)
        self.valor_entry5.delete(0, END)
        self.valor_entry6.delete(0, END)
        self.valor_entry7.delete(0, END)
        self.valor_entry8.delete(0, END)
        self.valor_entry9.delete(0, END)
        self.valor_entry10.delete(0, END)
        self.valor_entry11.delete(0, END)
        self.valor_entry12.delete(0, END)
        self.box_cliente.delete(0, END)
        self.box_veiculo.delete(0, END)
    def limpa_tela_cliente(self):
        self.nome_cliente.set('')
        self.telefone_cliente.set('')
    def conecta_bd(self):
        self.conn = sqlite3.connect("mecanica.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado")
    def desconecta_bd(self):
        self.conn.close();
        print("Banco de dados desconectado")
    def monta_tabelas(self):
        self.conecta_bd()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS CLIENTE (CLIENTE_ID INTEGER PRIMARY KEY, NOME TEXT, TELEFONE TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS VEICULO (MARCA TEXT, MODELO TEXT, ANO INTEGER, PLACA TEXT PRIMARY KEY, CLIENTE_ID INTEGER, FOREIGN KEY(CLIENTE_ID) REFERENCES CLIENTE(CLIENTE_ID))")
        self.conn.commit()
    def add_cliente(self):
        self.nome_cliente_entry = self.nome_cliente.get()
        self.telefone_cliente_entry = self.telefone_cliente.get()

        if self.nome_cliente_entry and self.telefone_cliente_entry:
            self.conecta_bd()
            self.cursor.execute("INSERT INTO CLIENTE (NOME, TELEFONE) VALUES(?, ?)", (self.nome_cliente_entry, self.telefone_cliente_entry))
            self.conn.commit()
            cliente_id = self.cursor.lastrowid
            self.desconecta_bd()

            global lista_de_clientes
            novo_cliente = (cliente_id, self.nome_cliente_entry, self.telefone_cliente_entry)
            lista_de_clientes.append(novo_cliente)

            self.select_cliente()
            self.limpa_tela_cliente()
        else:
            messagebox.showerror("", "Preencha o nome e o telefone para cadastrar o cliente")
    def deleta_cliente(self):
        item_selecionado = self.treeview_cliente.selection()
        if item_selecionado:
            retorno = messagebox.askquestion("", "Você deseja excluir o cliente selecionado?")
            if retorno == "yes":
                cliente_id = self.treeview_cliente.item(item_selecionado, 'values')[0]
                self.conecta_bd()
                self.cursor.execute("DELETE FROM CLIENTE WHERE CLIENTE_ID=?", (cliente_id,))
                self.conn.commit()
                self.desconecta_bd()
                self.select_cliente()
                messagebox.showinfo("", "Cliente excluido com sucesso")
            else:
                messagebox.showinfo("", "Operação cancelada")
        else:
            messagebox.showinfo("", "Selecione um cliente para excluir")
    def select_cliente(self, widget=None):
        if self.treeview_cliente is not None:
            self.treeview_cliente.delete(*self.treeview_cliente.get_children())
            self.conecta_bd()
            self.cursor.execute("SELECT * FROM CLIENTE ORDER BY CLIENTE_ID;")
            global lista_de_clientes
            lista_de_clientes = self.cursor.fetchall()
            self.desconecta_bd()

            for i in lista_de_clientes:
                self.treeview_cliente.insert("", END, values=i)

            nomes_formatados = [self.formata_lista_clientes(cliente) for cliente in lista_de_clientes]
            self.box_cliente['values'] = nomes_formatados
    def atualiza_combobox(self):
        self.conecta_bd()
        self.cursor.execute("SELECT * FROM CLIENTE ORDER BY CLIENTE_ID;")
        global lista_de_clientes
        lista_de_clientes = self.cursor.fetchall()
        self.desconecta_bd()

        nomes_formatados = [self.formata_lista_clientes(cliente) for cliente in lista_de_clientes]
        self.box_cliente['values'] = nomes_formatados

    def formata_lista_clientes(self, cliente):
        return f"{cliente[0]} - {cliente[1]} - {cliente[2]}"