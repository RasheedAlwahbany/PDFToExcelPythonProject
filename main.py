import tabula
import pandas as pd

def read_pdf(name,output_name):
    # Read pdf into list of DataFrame
    reader = tabula.read_pdf(name, pages='all')

    # convert PDF into CSV file
    tabula.convert_into(name, output_name, output_format="csv", pages='all')

def read_csv(csv_file, excel_file):
    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(csv_file)

    # Write the DataFrame to an Excel file.
    writer = pd.ExcelWriter(excel_file, engine="openpyxl")
    df.to_excel(writer, index=False)
    writer._save()

def main():
    read_pdf("source/Deposit_Slip_ok.pdf","output/PDF_output.csv")
    read_csv("output/PDF_output.csv","output/PDF_output.xlsx")

if __name__ == "__main__":
    main()