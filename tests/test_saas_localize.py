from saas_localize import integrate_saas_localize, automate_translation_workflow, TranslationConfig

def test_integrate_saas_localize():
    config = TranslationConfig(language_pairs=["en-fr", "en-es"], ci_cd_tool="Jenkins")
    result = integrate_saas_localize(config)
    assert result["language_pairs"] == ["en-fr", "en-es"]
    assert result["ci_cd_tool"] == "Jenkins"
    assert result["integration_time"] == "less than 30 minutes"

def test_integrate_saas_localize_empty_language_pairs():
    config = TranslationConfig(language_pairs=[], ci_cd_tool="Jenkins")
    try:
        integrate_saas_localize(config)
        assert False
    except ValueError as e:
        assert str(e) == "At least one language pair is required"

def test_integrate_saas_localize_unsupported_ci_cd_tool():
    config = TranslationConfig(language_pairs=["en-fr"], ci_cd_tool="Unsupported")
    try:
        integrate_saas_localize(config)
        assert False
    except ValueError as e:
        assert str(e) == "Unsupported CI/CD tool"

def test_automate_translation_workflow():
    config = TranslationConfig(language_pairs=["en-fr", "en-es", "en-de", "en-it", "en-pt"], ci_cd_tool="Jenkins")
    result = automate_translation_workflow(config)
    assert result["language_pairs"] == ["en-fr", "en-es", "en-de", "en-it", "en-pt"]
    assert result["workflow_status"] == "automated"

def test_automate_translation_workflow_insufficient_language_pairs():
    config = TranslationConfig(language_pairs=["en-fr", "en-es"], ci_cd_tool="Jenkins")
    try:
        automate_translation_workflow(config)
        assert False
    except ValueError as e:
        assert str(e) == "At least 5 language pairs are required"
