import fast_agent as fast

@fast.agent(
    "ceo_agent",
    """Chief Executive Officer - Oversees all business operations and strategy.
    Coordinates between departments, maintains company vision, and ensures alignment
    across all business functions. The CEO has final authority on all business decisions.
    """,
    servers=["filesystem", "vector_db"],
    human_input=True,
    model="claude-3.7-sonnet-20250219",
)

@fast.agent(
    "cfo_agent",
    """Chief Financial Officer - Manages financial aspects of the business.
    Oversees financial planning, risk management, record-keeping, and financial reporting.
    Provides insights on funding, tax considerations, and financial compliance.
    """,
    servers=["filesystem", "vector_db"],
    model="claude-3.7-sonnet-20250219",
)

@fast.agent(
    "cto_agent",
    """Chief Technology Officer - Manages all technical infrastructure and development.
    Oversees technical architecture, repository management, development workflows,
    and ensures technical solutions align with business needs.
    """,
    servers=["filesystem", "github"],
    model="claude-3.7-sonnet-20250219",
)

@fast.agent(
    "cmo_agent",
    """Chief Marketing Officer - Manages all marketing and brand initiatives.
    Oversees social media strategy, advertising campaigns, content creation,
    and brand guidelines to ensure consistent market positioning.
    """,
    servers=["filesystem", "vector_db"],
    model="claude-3.7-sonnet-20250219",
)

@fast.agent(
    "coo_agent",
    """Chief Operations Officer - Manages day-to-day business operations.
    Oversees calendar management, task tracking, document organization,
    and ensures operational efficiency across the business.
    """,
    servers=["filesystem", "vector_db"],
    model="claude-3.7-sonnet-20250219",
)

@fast.orchestrator(
    name="executive_board",
    instruction="""Executive Board - Coordinate business activities across departments.
    Make high-level decisions, delegate specialized tasks, and ensure alignment
    with business strategy and vision.
    """,
    agents=["ceo_agent", "cfo_agent", "cto_agent", "cmo_agent", "coo_agent"],
    model="claude-3.7-sonnet-20250219",
    plan_type="iterative",
    max_iterations=5,
)