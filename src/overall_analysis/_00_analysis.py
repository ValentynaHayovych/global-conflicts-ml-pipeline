from src.overall_analysis._01_a_plots_war_initiator_won import war_initiator_won
from src.overall_analysis._02_a_plots_war_defendor_lost import war_defendor_lost
from src.overall_analysis._03_a_plots_war_involvement_dbscan import war_involvement
from src.overall_analysis._04_a_final_data_validation import final_data_validation
from src.overall_analysis._05_a_final_ml_data_validation import final_ml_data_validation
import matplotlib.pyplot as plt

def analysis(df, adf):
    
    charts = {
        'war_initiator_won': war_initiator_won(df, adf),
        'war_defendor_lost': war_defendor_lost(df, adf),
        'total_war_involvement': war_involvement(df, adf),
        'final_data_validation': final_data_validation(adf),
        'final_ml_data_validation': final_ml_data_validation(adf)
    }

    for name, ch in charts.items():
        ch.savefig(f'output/analysis/{name}.png', dpi=300)
        plt.close(ch)


