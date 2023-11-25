
import matplotlib.pyplot as plt
import numpy as np

import copy
from StackGP import pareto_tournament, print_gp_model, evaluate_gp_model
import utils

def plot_models(models):
    tMods = copy.deepcopy(models)
    [utils.model_to_list_form(mod) for mod in tMods]
    pareto_models = pareto_tournament(tMods)
    for i in pareto_models:
        tMods.remove(i)
    [utils.model_restore_form(mod) for mod in pareto_models]
    [utils.model_restore_form(mod) for mod in tMods]

    pAccuracies = [mod[2][0] for mod in pareto_models]
    pComplexities = [mod[2][1] for mod in pareto_models]

    accuracies = [mod[2][0] for mod in tMods] + pAccuracies
    complexities = [mod[2][1] for mod in tMods] + pComplexities
    colors = ['blue' for i in range(len(tMods))] + ['red' for i in range(len(pAccuracies))]

    fig, ax = plt.subplots()

    sc = plt.scatter(complexities, accuracies, color=colors)
    plt.xlabel("Complexity")
    plt.ylabel("1-R**2")
    names = [str(print_gp_model(mod)) for mod in tMods] + [str(print_gp_model(mod)) for mod in pareto_models]

    label = ax.annotate("", xy=(0, 0),
                        xytext=(np.min(complexities), np.mean([np.max(accuracies), np.min(accuracies)])),
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    label.set_visible(False)

    def update_labels(ind):

        pos = sc.get_offsets()[ind["ind"][0]]
        label.xy = pos
        text = "{}".format(" ".join([names[n] for n in [ind["ind"][0]]]))
        label.set_text(text)
        label.get_bbox_patch().set_facecolor('grey')
        label.get_bbox_patch().set_alpha(0.9)

    def hover(event):
        vis = label.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_labels(ind)
                label.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    label.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    plt.show()


def plot_model_response_comparison(model, inputData, response):
    plt.scatter(range(len(response)), response, label="True Response")
    plt.scatter(range(len(response)), evaluate_gp_model(model, inputData), label="Model Prediction")
    plt.legend()
    plt.xlabel("Data Index")
    plt.ylabel("Response Value")
    plt.show()


def plot_prediction_response_correlation(model, inputData, response):
    plt.scatter(response, evaluate_gp_model(model, inputData), label="Model")
    plt.plot(response, response, label="Perfect Correlation", color='green')
    plt.xlabel("True Response")
    plt.ylabel("Predicted Response")
    plt.legend()
    plt.show()
