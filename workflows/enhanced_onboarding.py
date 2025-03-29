import fast_agent as fast
from core.executive_agents import executive_board, ceo_agent, cfo_agent
from agents.business_agents import onboarding_agent, data_manager
from agents.document_agents import document_generator

@fast.chain(
    "enhanced_onboarding_workflow",
    sequence=["executive_board", "onboarding_agent", "data_manager", "document_generator"],
    instruction="""Complete the enhanced business onboarding process with executive oversight.
    Executive board coordinates the overall onboarding strategy.
    Collect and validate flexible business information with intelligent field processing.
    Set up initial data structure with proper metadata for each field.
    Generate starter documentation based on the provided information.
    """,
    cumulative=True,
    continue_with_final=True,
)

@fast.chain(
    "financial_setup_workflow",
    sequence=["cfo_agent", "data_manager", "document_generator"],
    instruction="""Complete the financial setup portion of business onboarding.
    CFO agent provides guidance on financial structure and compliance.
    Collect and validate financial information with intelligent field processing.
    Generate financial documentation based on the provided information.
    """,
    cumulative=True,
)

@fast.chain(
    "business_model_workflow",
    sequence=["ceo_agent", "data_manager"],
    instruction="""Define the business model and revenue streams.
    CEO agent provides guidance on business model selection and validation.
    Collect and process industry-specific revenue model information.
    Generate suggestions based on industry best practices.
    """,
    cumulative=True,
)

@fast.router(
    name="onboarding_router",
    agents=["enhanced_onboarding_workflow", "financial_setup_workflow", "business_model_workflow"],
    instruction="""Route onboarding requests to the appropriate workflow.
    Analyze the onboarding stage and direct to the corresponding specialized workflow.
    """,
    model="claude-3.7-sonnet-20250219",
)

# Example usage:
# async with fast.run() as agent:
#     await agent.onboarding_router("Start enhanced business onboarding for ACME Corp")