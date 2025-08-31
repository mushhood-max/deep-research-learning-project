import os
from dotenv import load_dotenv
from tavily import TavilyClient
from research_agents import FactFinder, SourceChecker, Summarizer
from planning_agent import PlanningAgent
from synthesis_reporter import SynthesisReporter
from report_writer import ReportWriter
import concurrent.futures

# Load environment variables from .env file
load_dotenv()

def get_tavily_api_key():
    """Gets the Tavily API key from the environment variables."""
    return os.getenv("TAVILY_API_KEY")

class LeadResearcher:
    def __init__(self):
        self.planning_agent = PlanningAgent()
        self.fact_finder = FactFinder()
        self.source_checker = SourceChecker()
        self.summarizer = Summarizer()
        self.synthesis_reporter = SynthesisReporter()
        self.report_writer = ReportWriter()

    def research_task(self, task):
        print(f"FactFinder researching: {task}")
        findings = self.fact_finder.research(task)
        source_url = f"https://example.com/{task.replace(' ', '_')}"
        source_reliability = self.source_checker.research(source_url)
        print(source_reliability)
        return findings, f"{source_url} ({source_reliability})"

    def conduct_research(self, query):
        print(f"Lead Researcher received query: {query}")
        
        # Phase 1: Planning
        tasks = self.planning_agent.plan(query)
        print(f"Planning Agent broke query into tasks: {tasks}")

        all_findings = []
        citations = []

        # Phase 2: Parallel Research
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_task = {executor.submit(self.research_task, task): task for task in tasks}
            for future in concurrent.futures.as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    findings, citation = future.result()
                    all_findings.append(findings)
                    citations.append(citation)
                except Exception as exc:
                    print(f"{task} generated an exception: {exc}")

        # Phase 3: Synthesis
        synthesized_report = self.synthesis_reporter.synthesize_and_report(all_findings, query)
        print("Synthesis Reporter created a report.")

        # Phase 4: Final Report
        final_report = self.report_writer.write_report(synthesized_report, citations)
        print("Report Writer generated the final report.")

        return final_report

if __name__ == "__main__":
    lead_researcher = LeadResearcher()
    report = lead_researcher.conduct_research("Compare the environmental impact of electric vs hybrid vs gas cars")
    print("\n--- Final Research Report ---\n")
    print(report)


