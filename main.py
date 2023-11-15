from modules import *
from functionalities import Funcs

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesize import letter, A4
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# from reportlab.platypus import SimpleDocTemplete, Image
# import webbrowser

root = Tk()
lista_de_clientes = []
listaveiculos=["FORD KA","RENEGADE","FUSCA"]
contador_ficha=0

# class Relatorio():
#     def printFicha(self):
#         webbrowser.open(sum(contador_ficha, 1) + "teste")
#     def geraFichaServico(self):
#         self.c = canvas.Canvas(sum(contador_ficha, 1) + "teste")
#
#         self.nome_cli_rel = self.box_cliente.get()
class Application(Funcs):
    def __init__(self, root):
        self.root = root
        self.conecta_bd()
        self.tela_inicial()
        self.frames_tela()
        self.widgets_frame()
        self.combobox()
        self.monta_tabelas()
        self.nome_cliente = StringVar()
        self.telefone_cliente = StringVar()
        self.nome_entry = None
        self.telefone_entry = None
        self.treeview_cliente = None
        self.limpa_tela_principal()
        self.limpa_tela_cliente()
        self.select_cliente()
        self.atualiza_combobox()
        root.mainloop()

    def tela_inicial(self):
        self.root.title("Ficha de Serviço - Mecânica Coin")
        self.root.configure(background='#e1e5e8')
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)

    def frames_tela(self):
        self.frame1=Frame(self.root)
        self.frame1.place(relx=0.04, rely=0.02, relwidth=0.9, relheight=0.12)

        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.04, rely=0.16, relwidth=0.9, relheight=0.65)

    def widgets_frame(self):
        self.btn_tela_cad_cli = Button(self.frame1, text="Cadastro de Cliente", font=('Georgia 10'), command=self.tela_cadastro_cliente)
        self.btn_tela_cad_cli.place(relx=0.7, rely=0.18, relheight=0.2, relwidth=0.1)

        self.btn_cad_veic = Button(self.frame1, text="Cadastro de Veículo", font=('Georgia 10'), command=self.tela_cadastro_veiculo)
        self.btn_cad_veic.place(relx=0.7, rely=0.63, relheight=0.2, relwidth=0.1)

        self.btn_gerar_ficha = Button(self.frame2, text="Gerar Ficha de Serviço", font=('Georgia 10'))
        self.btn_gerar_ficha.place(relx=0.85, rely=0.9, relheight=0.05, relwidth=0.1)

        self.btn_gerar_ficha = Button(self.frame2, text="Limpar Preenchimento", font=('Georgia 10'), command=self.limpa_tela_principal)
        self.btn_gerar_ficha.place(relx=0.12, rely=0.9, relheight=0.05, relwidth=0.1)

        self.lb_cliente = Label(self.frame1, text="Cliente", font=('Georgia 15'))
        self.lb_cliente.place(relx=0.03, rely=0.01)

        self.lb_veiculo = Label(self.frame1, text="Veículo", font=('Georgia 15'))
        self.lb_veiculo.place(relx=0.03, rely=0.45)

        self.lb_item = Label(self.frame2, text="Item", font=('Georgia 15'))
        self.lb_item.place(relx=0.12, rely=0.01)

        self.lb_valor = Label(self.frame2, text="Valor", font=('Georgia 15'))
        self.lb_valor.place(relx=0.7, rely=0.01)

        self.lb_mao_obra = Label(self.frame2, text="Mão de Obra", font=('Georgia 15'))
        self.lb_mao_obra.place(relx=0.7, rely=0.77)

        self.lb_total = Label(self.frame2, text="Total", font=('Georgia 15'))
        self.lb_total.place(relx=0.645, rely=0.9)

        self.lb_total_valor = Label(self.frame2, text="teste123123", font=('Georgia 15'), bg='#fcba03')
        self.lb_total_valor.place(relx=0.7, rely=0.9)

        self.item_entry1 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry1.place(relx=0.12, rely=0.05, relheight=0.035, relwidth=0.555)

        self.item_entry2 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry2.place(relx=0.12, rely=0.11, relheight=0.035, relwidth=0.555)

        self.item_entry3 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry3.place(relx=0.12, rely=0.17, relheight=0.035, relwidth=0.555)

        self.item_entry4 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry4.place(relx=0.12, rely=0.23, relheight=0.035, relwidth=0.555)

        self.item_entry5 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry5.place(relx=0.12, rely=0.29, relheight=0.035, relwidth=0.555)

        self.item_entry6 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry6.place(relx=0.12, rely=0.35, relheight=0.035, relwidth=0.555)

        self.item_entry7 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry7.place(relx=0.12, rely=0.41, relheight=0.035, relwidth=0.555)

        self.item_entry8 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry8.place(relx=0.12, rely=0.47, relheight=0.035, relwidth=0.555)

        self.item_entry9 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry9.place(relx=0.12, rely=0.53, relheight=0.035, relwidth=0.555)

        self.item_entry10 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry10.place(relx=0.12, rely=0.59, relheight=0.035, relwidth=0.555)

        self.item_entry11 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry11.place(relx=0.12, rely=0.65, relheight=0.035, relwidth=0.555)

        self.item_entry12 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.item_entry12.place(relx=0.12, rely=0.71, relheight=0.035, relwidth=0.555)

        self.valor_entry1 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry1.place(relx=0.7, rely=0.05, relheight=0.035, relwidth=0.1)

        self.valor_entry2 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry2.place(relx=0.7, rely=0.11, relheight=0.035, relwidth=0.1)

        self.valor_entry3 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry3.place(relx=0.7, rely=0.17, relheight=0.035, relwidth=0.1)

        self.valor_entry4 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry4.place(relx=0.7, rely=0.23, relheight=0.035, relwidth=0.1)

        self.valor_entry5 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry5.place(relx=0.7, rely=0.29, relheight=0.035, relwidth=0.1)

        self.valor_entry6 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry6.place(relx=0.7, rely=0.35, relheight=0.035, relwidth=0.1)

        self.valor_entry7 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry7.place(relx=0.7, rely=0.41, relheight=0.035, relwidth=0.1)

        self.valor_entry8 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry8.place(relx=0.7, rely=0.47, relheight=0.035, relwidth=0.1)

        self.valor_entry9 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry9.place(relx=0.7, rely=0.53, relheight=0.035, relwidth=0.1)

        self.valor_entry10 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry10.place(relx=0.7, rely=0.59, relheight=0.035, relwidth=0.1)

        self.valor_entry11 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry11.place(relx=0.7, rely=0.65, relheight=0.035, relwidth=0.1)

        self.valor_entry12 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.valor_entry12.place(relx=0.7, rely=0.71, relheight=0.035, relwidth=0.1)

        self.mobra_entry1 = Entry(self.frame2, font=('Georgia 15'), justify="right")
        self.mobra_entry1.place(relx=0.7, rely=0.81, relheight=0.035, relwidth=0.1)
    def combobox(self):
        self.box_cliente = ttk.Combobox(root, values=lista_de_clientes)
        self.box_cliente.place(relx=0.07, rely=0.045, relheight=0.025, relwidth=0.5)

        self.box_veiculo = ttk.Combobox(root, values=listaveiculos)
        self.box_veiculo.place(relx=0.07, rely=0.098, relheight=0.025, relwidth=0.5)
    def tela_cadastro_cliente(self):
        self.tela_cliente = Toplevel(self.root)
        self.tela_cliente.title("Cadastro de Cliente")
        self.tela_cliente.configure(background='#e1e5e8')
        self.tela_cliente.geometry("900x700")
        self.tela_cliente.resizable(False, False)
        self.tela_cliente.transient(self.root)
        self.tela_cliente.focus_force()
        self.tela_cliente.grab_set()

        self.btn_cadastra_cli = Button(self.tela_cliente, text="Cadastrar Cliente", font=('Georgia 10'), command=self.add_cliente)
        self.btn_cadastra_cli.place(relx=0.75, rely=0.2, relheight=0.04, relwidth=0.2)

        self.btn_deleta_cli = Button(self.tela_cliente, text="Deletar Cliente", font=('Georgia 10'), command=self.deleta_cliente)
        self.btn_deleta_cli.place(relx=0.75, rely=0.6, relheight=0.04, relwidth=0.2)

        self.lb_nome_cliente = Label(self.tela_cliente, text="Nome do Cliente", font=('Georgia 15'))
        self.lb_nome_cliente.place(relx=0.1, rely=0.045)

        self.lb_telefone_cliente = Label(self.tela_cliente, text="Telefone do Cliente", font=('Georgia 15'))
        self.lb_telefone_cliente.place(relx=0.1, rely=0.16)

        self.nome_cliente = Entry(self.tela_cliente, font=('Georgia 15'))
        self.nome_cliente.place(relx=0.1, rely=0.09, relheight=0.04, relwidth=0.6)

        self.telefone_cliente = Entry(self.tela_cliente, font=('Georgia 15'))
        self.telefone_cliente.place(relx=0.1, rely=0.2, relheight=0.04, relwidth=0.6)

        self.treeview_cliente = ttk.Treeview(self.tela_cliente, columns=('1', '2', '3'), height=15, show='headings')
        self.treeview_cliente.heading('1', text="ID do Cliente")
        self.treeview_cliente.heading('2', text="Nome do Cliente")
        self.treeview_cliente.heading('3', text="Telefone do Cliente")

        self.treeview_cliente.column('1', anchor=CENTER, stretch=NO, width=100)
        self.treeview_cliente.column('2', anchor=CENTER, stretch=NO, width=200)
        self.treeview_cliente.column('3', anchor=CENTER, stretch=NO, width=200)

        self.treeview_cliente.place(relx=0.095, rely=0.3, relwidth=0.6, relheight=0.6)

        self.scroll_lista_cli = Scrollbar(self.tela_cliente, orient='vertical')
        self.treeview_cliente.configure(yscroll=self.scroll_lista_cli.set)
        self.scroll_lista_cli.place(relx=0.7, rely=0.3, relwidth=0.02, relheight=0.6)

        self.select_cliente(widget="Combobox")
    def tela_cadastro_veiculo(self):
        self.tela_veiculo = Toplevel()
        self.tela_veiculo.title("Cadastro de Veículo")
        self.tela_veiculo.configure(background='#e1e5e8')
        self.tela_veiculo.geometry("900x800")
        self.tela_veiculo.resizable(False, False)
        self.tela_veiculo.transient(self.root)
        self.tela_veiculo.focus_force()
        self.tela_veiculo.grab_set()

        self.lb_marca_veiculo = Label(self.tela_veiculo, text = "Marca do Veículo", font="Georgia 15")
        self.lb_marca_veiculo.place(relx=0.1, rely=0.05)

        self.lb_modelo_veiculo = Label(self.tela_veiculo, text="Modelo do Veículo", font="Georgia 15")
        self.lb_modelo_veiculo.place(relx=0.1, rely=0.15)

        self.lb_ano_veiculo = Label(self.tela_veiculo, text="Ano do Veículo", font="Georgia 15")
        self.lb_ano_veiculo.place(relx=0.35, rely=0.05)

        self.lb_placa_veiculo = Label(self.tela_veiculo, text="Placa do Veículo", font="Georgia 15")
        self.lb_placa_veiculo.place(relx=0.35, rely=0.15)

        self.lb_cliente = Label(self.tela_veiculo, text="Cliente", font="Georgia 15")
        self.lb_cliente.place(relx=0.1, rely=0.31)

        self.entry_marca_veiculo = Entry(self.tela_veiculo, font="Georgia 15")
        self.entry_marca_veiculo.place(relx=0.1, rely=0.09, relheight=0.04, relwidth=0.2)

        self.entry_modelo_veiculo = Entry(self.tela_veiculo, font="Georgia 15")
        self.entry_modelo_veiculo.place(relx=0.1, rely=0.19, relheight=0.04, relwidth=0.2)

        self.entry_ano_veiculo = Entry(self.tela_veiculo, font="Georgia 15")
        self.entry_ano_veiculo.place(relx=0.35, rely=0.09, relheight=0.04, relwidth=0.2)

        self.entry_placa_veiculo = Entry(self.tela_veiculo, font="Georgia 15")
        self.entry_placa_veiculo.place(relx=0.35, rely=0.19, relheight=0.04, relwidth=0.2)

        self.box_cliente_cad_cli = ttk.Combobox(self.tela_veiculo, values=lista_de_clientes)
        self.box_cliente_cad_cli.place(relx=0.1, rely=0.35, relheight=0.04, relwidth=0.45)

        self.btn_cadastra_veic = Button(self.tela_veiculo, text="Cadastrar Veículo", font=('Georgia  10'))
        self.btn_cadastra_veic.place(relx=0.75, rely=0.2, relheight=0.04, relwidth=0.2)

        self.treeview_veiculo = ttk.Treeview(self.tela_veiculo, columns=('1', '2', '3', '4', '5'), height=15, show='headings')
        self.treeview_veiculo.heading('1', text="Nome do Cliente")
        self.treeview_veiculo.heading('2', text="Marca")
        self.treeview_veiculo.heading('3', text="Modelo")
        self.treeview_veiculo.heading('4', text="Ano")
        self.treeview_veiculo.heading('5', text="Placa")

        self.treeview_veiculo.column('1', anchor=CENTER, stretch=NO, width=120)
        self.treeview_veiculo.column('2', anchor=CENTER, stretch=NO, width=100)
        self.treeview_veiculo.column('3', anchor=CENTER, stretch=NO, width=100)
        self.treeview_veiculo.column('4', anchor=CENTER, stretch=NO, width=100)
        self.treeview_veiculo.column('5', anchor=CENTER, stretch=NO, width=100)

        self.treeview_veiculo.place(relx=0.095, rely=0.4, relwidth=0.6, relheight=0.55)

if __name__ == "__main__":
    app = Application(root)
    root.mainloop()
