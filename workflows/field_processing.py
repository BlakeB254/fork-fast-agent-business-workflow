import fast_agent as fast
from core.executive_agents import ceo_agent, cfo_agent, cto_agent, cmo_agent, coo_agent

@fast.chain(
    "field_suggestion_workflow",
    sequence=["ceo_agent", "appropriate_department_agent"],
    instruction="""Generate intelligent suggestions for empty fields.
    Based on existing business profile data, industry context, and best practices,
    provide tailored suggestions for completing missing information.
    """,
    cumulative=True,
)

@fast.chain(
    "field_validation_workflow",
    sequence=["ceo_agent", "appropriate_department_agent"],
    instruction="""Validate field values against business rules and regulations.
    Check format, consistency, and compliance with requirements.
    Provide feedback on any issues detected.
    """,
    cumulative=True,
)

@fast.chain(
    "field_context_workflow",
    sequence=["ceo_agent", "appropriate_department_agent"],
    instruction="""Generate helpful contextual information for field completion.
    Provide educational content about why this information matters,
    best practices, and potential business implications.
    """,
    cumulative=True,
)

@fast.router(
    name="field_processing_router",
    agents=["field_suggestion_workflow", "field_validation_workflow", "field_context_workflow"],
    instruction="""Route field processing requests to the appropriate workflow.
    Analyze the type of field processing needed and direct to the
    corresponding specialized workflow.
    """,
    model="claude-3.7-sonnet-20250219",
)

# Example usage:
# async with fast.run() as agent:
#     await agent.field_processing_router("Generate suggestions for empty business_address field")