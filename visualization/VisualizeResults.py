import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RULE_INDUCTION = "Rule Induction"
DECISION_TREES = "Decision Trees"
RANDOM_FORESTS = "Random Forests"
VISUAL_TYPES = [RULE_INDUCTION, DECISION_TREES, RANDOM_FORESTS]


class VisualizeResults:

    def __init__(self,
                 read_from,
                 visual_type,
                 save=False,
                 success_value=3):

        if visual_type not in VISUAL_TYPES:
            self.visual_type = RANDOM_FORESTS
        else:
            self.visual_type = visual_type

        if 0 < success_value <= 5:
            self.success_value = success_value
        else:
            self.success_value = 3

        self.read_from = read_from
        self.save = save

    def show_plotting(self):
        df = pd.read_csv(f"../data_mod/{self.read_from}")
        amountp = len(df[df.success >= self.success_value]).__index__()
        amountf = len(df[df.success < self.success_value]).__index__()
        passed = df[df.success >= self.success_value].sum()[1:8] / amountp
        failed = df[df.success < self.success_value].sum()[1:8] / amountf

        index = np.arange(7)
        bar_width = 0.35
        fig, ax = plt.subplots()

        ax.bar(index, passed, bar_width, label="Bestanden")
        ax.bar(index+bar_width, failed, bar_width, label="Durchgefallen")

        ax.set_xlabel("Aktivität")
        ax.set_ylabel("Häufigkeit (erhoben aus allen Daten)")
        ax.set_title(f"Testergebnisse für {self.visual_type}")
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(["VL bes.", "Übung bes.", "GA", "KL gel.",
                            "VL gel.", "ÜB bearb.", "ÜB Punkte"])
        ax.legend(fancybox=True, framealpha=0.5, loc=2)
        if self.save:
            plt.savefig(f"{self.visual_type}.png", transparent=True)
        plt.show()
