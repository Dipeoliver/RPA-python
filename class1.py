import pyautogui
import time
import pyperclip
import pandas as pd


pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)
pyautogui.click(344, -507, clicks=2)
pyautogui.click(367, -366)
pyautogui.click(1161, -607)
pyautogui.click(1041, -193)
time.sleep(10)
df = pd.read_excel(r"C:/Users/Diego/Downloads/1.xls")
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://www.outlook.com"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press('enter')
print(link)
time.sleep(10)
pyautogui.click(186, -617)
time.sleep(5)
pyautogui.write('dipeoliver@outlook.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press("tab")
texto =f"""
Prezados, bom dia
O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}
Abs.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.hotkey('ctrl', 'enter')
pyautogui.alert("Fim da Automação. Seu computador já voltou a ser seu")