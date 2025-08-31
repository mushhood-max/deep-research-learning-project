class ReportWriter:
    def __init__(self):
        self.name = "ReportWriter"

    def write_report(self, synthesized_findings, citations=None):
        report = f"# Research Report\n\n{synthesized_findings}\n\n"
        if citations:
            report += "## Citations\n\n"
            for i, citation in enumerate(citations):
                report += f"[{i+1}] {citation}\n"
        return report


