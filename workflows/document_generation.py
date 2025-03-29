import fast_agent as fast
from core.executive_agents import ceo_agent, cfo_agent, coo_agent
from agents.document_agents import document_generator, pdf_creator, quality_assurance

@fast.chain(
    "business_plan_generator",
    sequence=["ceo_agent", "cfo_agent", "document_generator", "quality_assurance", "pdf_creator"],
    instruction="""Generate comprehensive business plan based on profile data.
    CEO agent provides business vision, strategy, and market analysis.
    CFO agent provides financial projections and funding requirements.
    Document generator creates the complete business plan with proper formatting.
    Quality assurance ensures the document meets professional standards.
    PDF creator finalizes the document for distribution.
    """,
    cumulative=True,
)

@fast.chain(
    "operations_manual_generator",
    sequence=["coo_agent", "document_generator", "quality_assurance", "pdf_creator"],
    instruction="""Generate detailed operations manual based on business activities.
    COO agent provides operational processes, workflows, and policies.
    Document generator creates the complete operations manual with proper formatting.
    Quality assurance ensures the document meets professional standards.
    PDF creator finalizes the document for distribution.
    """,
    cumulative=True,
)

@fast.router(
    name="document_generation_router",
    agents=["business_plan_generator", "operations_manual_generator"],
    instruction="""Route document generation requests to the appropriate workflow.
    Analyze the type of document requested and business context to determine
    which specialized generation workflow should handle the request.
    """,
    model="claude-3.7-sonnet-20250219",
)

# Example usage:
# async with fast.run() as agent:
#     await agent.document_generation_router("Generate comprehensive business plan based on my business profile")