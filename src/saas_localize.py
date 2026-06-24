import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class TranslationConfig:
    language_pairs: list
    ci_cd_tool: str

def integrate_saas_localize(config: TranslationConfig):
    if not config.language_pairs:
        raise ValueError("At least one language pair is required")
    if config.ci_cd_tool not in ["Jenkins", "GitLab"]:
        raise ValueError("Unsupported CI/CD tool")
    return {
        "language_pairs": config.language_pairs,
        "ci_cd_tool": config.ci_cd_tool,
        "integration_time": "less than 30 minutes"
    }

def automate_translation_workflow(config: TranslationConfig):
    if len(config.language_pairs) < 5:
        raise ValueError("At least 5 language pairs are required")
    return {
        "language_pairs": config.language_pairs,
        "workflow_status": "automated"
    }

def main():
    parser = ArgumentParser()
    parser.add_argument("--language-pairs", nargs="+", required=True)
    parser.add_argument("--ci-cd-tool", choices=["Jenkins", "GitLab"], required=True)
    args = parser.parse_args()
    config = TranslationConfig(language_pairs=args.language_pairs, ci_cd_tool=args.ci_cd_tool)
    integration_result = integrate_saas_localize(config)
    workflow_result = automate_translation_workflow(config)
    print(json.dumps(integration_result))
    print(json.dumps(workflow_result))

if __name__ == "__main__":
    main()
