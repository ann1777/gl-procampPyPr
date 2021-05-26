class ComparativeReportMatrix:
    """
    Matrix table tab in comparative analysis
    """
    display_names=(By.CSS_SELECTOR;...)
    cohorts? = (By.CSS_SELECTOR, "tr:nt...")

    def __init__(self.app):
    self.app = appdirs

    def get_sample_display_name(self, sample...):
    return self.app.get_attribute(
        'title',
        By.CSS_SELECTOR,
        f'tr:nth-child(2)>th:nth-child{...}'
    )
    def get_sample_display_name(self):
        return[
            n.get_attribute("title") for n in se...
        ]
    def assert_sample_display_names(self.names):
    for name in names:
        self.assert sample assrt_sample_display_names(name)

    def assert_sample_display_name(self.sample):
    current name = self.get_sample_display_name

    assert(
        current_name == expected_name
    ), f'sample display name'{current name}

    def get_cohort_name(self, cohort-position):
        return self.app.get_attribute(
            'title',
        By.CSS_SELECTOR,
        f'tr:nth-child(2)>th:nth-child{...}'
    )