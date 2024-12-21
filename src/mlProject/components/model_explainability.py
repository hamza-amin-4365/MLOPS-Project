import pandas as pd
import shap
import lime
import lime.lime_tabular
import joblib
import numpy as np
from pathlib import Path
from src.mlProject import logger
from src.mlProject.utils.common import save_bin, load_bin
from src.mlProject.entity.config_entity import ModelExplainabilityConfig

class ModelExplainability:
    def __init__(self, config: ModelExplainabilityConfig):
        self.config = config

    def explain_model(self):
        try:
            # Load the trained model
            model = load_bin(Path(self.config.model_path))

            # Load the test data
            test_data = pd.read_csv(self.config.test_data_path)
            X_test = test_data.drop(['quality'], axis=1)

            # --- SHAP Explanations ---
            logger.info("Generating SHAP explanations...")
            explainer = shap.LinearExplainer(model, X_test, feature_perturbation="interventional")
            shap_values = explainer(X_test[:self.config.num_test_instances])

            # Save SHAP values
            np.save(self.config.shap_values_file, shap_values.values)
            logger.info(f"SHAP values saved to {self.config.shap_values_file}")

            # Generate a summary plot (we'll save this differently)
            shap_plot = shap.summary_plot(shap_values, X_test[:self.config.num_test_instances], plot_type="bar", show=False)

            # Save the summary plot using matplotlib (plt)
            import matplotlib.pyplot as plt
            plt.savefig(self.config.xai_report_file.replace(".html", "_shap_summary.png"))  # Save as PNG
            plt.close()
            logger.info(f"SHAP summary plot saved to {self.config.xai_report_file.replace('.html', '_shap_summary.png')}")

            # --- LIME Explanations ---
            logger.info("Generating LIME explanations...")
            lime_explainer = lime.lime_tabular.LimeTabularExplainer(
                training_data=X_test.values,
                feature_names=X_test.columns,
                class_names=['quality'],  # Replace with your actual class names if different
                mode='regression'
            )

            # Explain a single instance (e.g., the first test instance)
            instance = X_test.iloc[0, :].values
            lime_explanation = lime_explainer.explain_instance(
                data_row=instance,
                predict_fn=model.predict,
                num_features=self.config.num_features_lime
            )

            # Save the LIME explanation as HTML
            lime_explanation.save_to_file(self.config.xai_report_file.replace(".html", "_lime.html"))
            logger.info(f"LIME explanation saved to {self.config.xai_report_file.replace('.html', '_lime.html')}")

        except Exception as e:
            logger.error(f"Error during model explainability: {e}")
            raise e