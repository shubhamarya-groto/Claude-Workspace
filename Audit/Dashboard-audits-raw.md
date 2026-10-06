# Dashboard audits – raw text extraction

> Auto-extracted from the two PDFs (Figma table exports). Column order is scrambled by extraction and screenshots are not included; see the originals in `Source files/`. To be restructured.

## Dashboard_audit_other_Tabs

    Dashboard audit other Tabs
    Dashboard(Responsive) Audit
    Issue Type
    Empty states lack direction and
    recovery guidance
    Inconsistent dashboard header and
    page structure across screens
    Empty and incomplete profile states
    do not guide users toward
    completion
    Problem
    Empty states across the platform have very little visual hierarchy, contextual explanation, or
    actionable guidance for users. When users land on a screen with no data, the system does not
    help them understand what to do next, why the page matters, or how to progress further in their
    journey. This creates dead-end experiences and increases drop-off risk, especially during
    onboarding or first-time usage.
    Different dashboard sections use varying header layouts, spacing structures, navigation patterns,
    and contextual information placement. This creates an inconsistent experience where users must
    repeatedly reorient themselves while navigating between modules. The lack of a unified structural
    pattern reduces familiarity, weakens platform cohesion, and increases cognitive load during
    repeated usage.
    Although the onboarding contains only 5 steps, the structure, density, and repetitive
    necessary
    interaction patterns make it feel like a lengthy enterprise setup process. Users may abandon or
    Screenshot
    Proposed Solution
    edesign empty states as guided recovery moments by introducing clear primary CTAs, contextual
    R
    explanations, onboarding prompts, recommended next actions, and visual indicators that help users continue
    Critical
    their workflow instead of feeling stuck.
    Establish a standardized dashboard framework with consistent page headers, breadcrumb behavior,
    Medium
    Sections with missing information only display “Not specified” without explaining why the
    information matters, how it impacts visibility or trust, or what the user should do next. This
    creates dead-end states where users are informed about missing data but are not guided toward
    profile completion. As a result, profiles may remain incomplete, reducing platform engagement,
    discoverability, and overall ecosystem quality.
    low feels longer and heavier than
    F
    Criticality
    contextual actions, information hierarchy, and layout patterns across all modules to create a more predictable
    and cohesive user experience.
    eplace passive “Not specified” states with actionable empty-state guidance that explains the
    benefit of completing each section and provides clear CTAs such as “Add Operational Details,”
    “Improve Company Visibility,” or “Complete Profile” to encourage progression and profile
    completion.
    R
    R
    postpone completion because the perceived effort feels too high.
    M
    odal-based workflow breaks
    R
    user orientation
    and lighter step structures.
    unning the entire onboarding/edit flow inside a modal creates spatial confusion, nested
    scrolling behavior, and weak focus management. Users lose awareness of where they are
    C
    within the platform and the experience feels constrained.
    W
    eak onboarding progression and
    The flow does not explain why users are filling this information, how it benefits them, or how
    guidance
    profile completion impacts discoverability and trust. The experience feels transactional rather
    o save confidence or recovery
    Add contextual onboarding guidance, value-driven messaging, and profile completion benefits throughout
    the journey.
    sers are not informed whether their progress is being saved. In long-form business
    U
    mechanism
    workflows, this creates anxiety around accidental exits, refreshes, or interruptions.
    I
    Information architecture is not
    elated information such as operational details, certifications, compliance, and business
    R
    optimized for decision-making
    eorganize the workflow into clearer sections like Company Information, Operations, Compliance,
    identity are spread across multiple areas without strong logical grouping. This increases
    Complex business/compliance
    I
    ndustry-specific terms such as EMR, OSHA, Net 15, and liability insurance are presented
    terminology lacks support
    without contextual explanations, increasing confusion and inaccurate submissions.
    Selection-heavy interactions
    The workflow heavily depends on chips, dropdowns, and multi-select interactions, which
    create friction
    become difficult to scan and manage as option complexity increases.
    inal step lacks completion
    The onboarding ends abruptly with uploads and submission actions, without reinforcing
    reinforcement
    progress, success, or profile value. Users do not experience a sense of achievement or
    C
    orkflow is not optimized for
    C
    interruption-based usage
    M
    Critical
    to 
    Medium
    Simplify selection patterns using searchable autocomplete, categorized selection groups, and clearer
    interaction models.
    Add a completion summary, profile strength indicator, preview functionality, and success-oriented
    messaging before submission.
    ontractors and vendors may complete this process between tasks or while multitasking, but
    edesign the experience responsively using mobile-first layouts, stacked interactions, and simplified step
    R
    flows.
    The current workflow relies on large modal layouts, dense interactions, and horizontal
    scalability concerns
    N
    Design the workflow around smaller milestones, resumable progress, and flexible completion behavior.
    the current flow assumes uninterrupted long-form completion.
    obile responsiveness and
    Add a review-and-confirmation step with editable summaries and profile preview functionality before final
    selection patterns that may not scale effectively on smaller screens.
    o review or verification stage
    ertifications, and Branding.
    Add helper text, examples, educational tooltips, and 'Why we ask this' explanations where needed.
    closure.
    W
    ntroduce auto-save indicators, draft-saving functionality, and resume-later capabilities.
    R
    cognitive effort and slows completion.
    F
    onvert the flow into a dedicated full-page experience or structured side-panel workflow for better
    navigation and continuity.
    than guided.
    N
    educe cognitive load through progressive disclosure, completion indicators, estimated completion time,
    submission.
    sers cannot validate how their profile will appear publicly or review all entered information
    U
    before submission
    before final submission. This increases uncertainty and reduces submission confidence.
    Pro ject creation flow feels
    The project posting experience requires users to process too many decisions in a single
    operationally heavy
    continuous workflow. Users must simultaneously think about project details, vendor targeting,
    reak the flow into smaller progressive stages such as Project Basics, Scope & Trades, Vendor
    B
    references, and Review & Publish.
    P
    categories, filters, and publishing without progressive guidance. This increases cognitive
    fatigue and slows completion.
    W
    orkflow lacks contextual
    U
    sers are not guided on what makes a good project listing, how vendor matching works, or
    Add contextual guidance, recommendations, examples, and value-driven onboarding throughout the
    guidance and onboarding support
    which details improve engagement and responses. The system assumes platform familiarity
    workflow.
    and procurement knowledge.
    o save-state or interruption
    The platform assumes uninterrupted usage during project creation and search workflows.
    I
    recovery support
    There is no indication of draft saving, auto-save, or resume capability, creating risk during
    sessions.
    N
    ntroduce auto-save, save-as-draft functionality, resumable workflows, and progress persistence across
    longer posting flows.
    Project posting, vendor discovery,
    M
    and search flows feel
    connected workflows. Users must manually switch context between posting work, discovering
    disconnected
    vendors, and managing outreach.
    orkflow lacks prioritization and
    y Projects, Find Trade Partners, and Search Projects behave like isolated modules instead of
    C
    reate interconnected workflows where project creation naturally transitions into vendor discovery,
    invitations, matching, and management.
    W
    I
    mportant decisions such as trade selection, certifications, vendor invitations, and search
    R
    eorganize workflows around priority-based progression and progressively reveal advanced filters/options
    progressive decision-making
    refinement are presented simultaneously without helping users understand what matters most
    when needed.
    first.
    Selection and filtering workflows
    The platform heavily relies on multi-select dropdowns, large filter lists, and manual category
    Simplify filtering and selection using intelligent search, categorized recommendations, autocomplete, and
    create cognitive overload
    selection. As workflows scale, these interactions become mentally exhausting and difficult to
    progressive filtering logic.
    manage efficiently.
    Platform relies too heavily on
    U
    sers are expected to manually search, filter, and discover vendors/projects without proactive
    I
    manual discovery instead of
    system assistance. This increases effort and reduces platform efficiency.
    automated discovery assistance.
    intelligent matching
    N
    o quality validation before
    Critical
    to 
    Medium
    sers can publish projects or perform searches without understanding whether their
    ntroduce smart recommendations, relevance-based matching, suggested vendors/projects, and
    Add completion indicators, quality scoring, missing-information prompts, and publish-readiness validation.
    U
    publishing or searching
    information is complete, optimized, or likely to produce quality results.
    Post-publish workflows lack
    After publishing a project, users receive limited workflow continuity. The platform does not
    I
    lifecycle clarity
    clearly communicate project status, engagement progress, vendor activity, or next
    publishing.
    ntroduce lifecycle states, engagement tracking, activity summaries, and guided next-step workflows after
    recommended actions.
    Empty and low-result states do
    When searches or vendor discovery produce weak/no results, users are not given meaningful
    Add actionable recovery states with suggestions like expanding filters, adjusting criteria, or improving
    not guide recovery
    recovery guidance or alternative actions. This creates dead-end experiences.
    project details.
    orkflow does not adapt based
    ontractors, vendors, and trade partners appear to move through largely similar workflows
    W
    C
    on user role or intent
    despite having different goals and priorities. This creates unnecessary friction and irrelevant
    I
    ntroduce role-based workflows and dynamically prioritize actions, recommendations, and navigation
    based on user intent.
    steps.
    W
    orkflow scalability concerns as
    The current structure relies heavily on manual filtering, category browsing, and repeated
    R
    edesign workflows using scalable search architecture, personalization, saved preferences, and intelligent
    platform grows
    inputs. As categories, projects, and vendors grow, discoverability and usability may degrade
    discovery systems.
    significantly.
    U
    sers managing multiple projects must repeatedly enter similar information and rebuild
    Add reusable templates, saved searches, duplicated projects, autofill behavior, and persistent user
    frequency users
    searches manually, slowing down recurring usage patterns.
    preferences.
    Platform navigation creates
    U
    P
    repeated context switching
    without retaining workflow continuity. This increases mental load and breaks task momentum.
    related actions.
    Large filtering systems, multi-select workflows, and long-form project creation may become
    R
    difficult to complete effectively on mobile devices.
    flows optimized for smaller screens.
    N
    o optimization for repeat or high-
    M
    sers frequently move between project management, vendor discovery, and search sections
    obile flow scalability concerns
    H iring workflow feels overly
    Employers must configure multiple hiring decisions role setup, compensation, benefits,
    manual and cognitively heavy
    requirements, training, and categories in one continuous flow. The experience feels
    reserve project/search context across workflows and create connected navigation states between
    edesign the workflows using mobile-first patterns, progressive interactions, and simplified step-based
    reak the workflow into progressive stages with guided hiring steps and contextual assistance throughout
    B
    the process.
    administrative rather than guided, increasing mental fatigue and slowing completion.
    W
    orkflow lacks guidance,
    The platform assumes users know how to create effective job listings and manually configure
    I
    validation, and intelligent
    hiring details correctly. There is no support around improving applicant quality, validating
    and publish-readiness checks.
    assistance
    listing completeness, or optimizing hiring outcomes.
    o support for interruption-based
    The workflow assumes uninterrupted completion and repeated manual configuration for every
    Add auto-save, draft recovery, resumable workflows, reusable templates, saved preferences, and
    or repeat hiring behavior
    new job posting. There is no visible support for drafts, resumable progress, reusable
    duplicate-job functionality.
    N
    ntroduce hiring guidance, smart recommendations, job quality validation, templates, suggested defaults,
    templates, or persistent hiring preferences.
    Hiring, candidate discovery, and
    post-publish workflows feel
    Job posting, company matching, and hiring management behave like separate modules instead
    C
    reate an end-to-end hiring ecosystem where posting, candidate matching, engagement, and applicant
    disconnected
    of a connected hiring journey. Users are not naturally guided from creating a job to
    management function as one continuous workflow.
    discovering, evaluating, and managing candidates.
    W
    orkflow lacks adaptive
    The same workflow structure is used across different hiring scenarios (internships,
    I
    ntroduce adaptive workflows, progressive disclosure, role-based configurations, and scalable
    prioritization and scalability
    apprenticeships, part-time, full-time, urgent hiring, etc.), while also relying heavily on manual
    recommendation systems that adjust dynamically based on hiring intent and complexity.
    configuration and selection patterns that may become difficult to manage as complexity
    grows.
    Post-publish and low-result states
    After publishing a job or encountering weak/no matches, users are not guided toward
    lack recovery guidance
    meaningful next actions, hiring optimization opportunities, or recovery paths. The workflow
    Critical
    to 
    Medium
    Add lifecycle guidance, hiring insights, engagement tracking, optimisation suggestions, and actionable
    recovery flows for low-performing or inactive listings.
    effectively ends after publishing.
    Platform navigation creates
    repeated hiring context switching
    sers frequently move between dashboard sections, hiring workflows, and candidate
    reserve hiring context, candidate filters, and active workflow states across navigation and related
    U
    P
    discovery without retaining context or continuity, increasing mental load and breaking
    sections.
    workflow momentum.
    Long-form hiring flows, configuration-heavy interactions, and repeated selection patterns may
    R
    concerns
    become difficult to complete effectively on smaller devices.
    based and smaller-screen usage.
    Unnecessary Text Modification
    Why Work here has very high level of Text modification tools which feels unnecessary for
    Keep system light by removing features that add additional load without providing much business benefits.
    unctionality
    listing a job posting.
    M
    obile workflow scalability
    F
    edesign the workflow using mobile-first progressive completion patterns optimised for interruption-
    Support flow opens as a modal
    C
    licking on the Support section opens a small modal overlay instead of taking users to a
    instead of a dedicated support
    dedicated support page. Users typically expect support-related actions to provide a full-page
    for raising issues, tracking requests, viewing support history, and accessing help resources.
    experience
    experience where they can view previous tickets, track issue status, access FAQs, attach files, or
    M
    continue ongoing conversations. The modal format limits context, interrupts workflow continuity,
    C
    Medium
    onvert the support interaction into a dedicated support page or workspace with clear sections
    odal usage should be reserved only for quick actions, while primary support flows should use
    full-page navigation for better continuity and trust.
    and makes the support system feel temporary or lightweight rather than reliable and structured.
    Settings ecosystem lacks a
    Notification settings, billing, user management, and password management behave like
    connected account-management
    isolated pages instead of a unified account administration system. Users are not guided
    flow
    through account setup, team onboarding, payment readiness, or security completion as part of
    uild a unified account-management framework with setup progress, account health indicators,
    B
    onboarding guidance, and connected workflows between settings modules.
    a connected journey.
    Empty states do not guide users
    B
    I
    toward meaningful setup
    not educate users on why setup matters, what benefits they unlock, or what recommended
    milestones, and workflow continuation guidance.
    completion
    next steps are required.
    N
    o visible role, permission, or
    illing, user management, and notification areas contain low-information empty states that do
    ser management appears transactional rather than operational. There is no visible
    ntroduce action-oriented empty states with contextual education, setup recommendations, onboarding
    ntroduce structured role-based access control, permission visibility, approval workflows, activity logs, and
    U
    I
    governance workflow for team
    governance structure for permissions, role hierarchy, approvals, access visibility, or
    collaborative governance patterns.
    management
    collaborative administration behavior.
    Sensitive account actions lack
    C
    ritical actions such as deleting users, changing passwords, and managing billing appear
    Add confirmation layers, security verification flows, recovery mechanisms, audit visibility, action
    protective workflow safeguards
    lightweight despite their operational importance. There is limited evidence of friction,
    summaries, and contextual warnings for high-risk actions.
    validation, recovery, or security assurance during sensitive actions.
    Account security workflow is
    P
    assword management exists as a standalone utility instead of part of an ongoing account
    C
    reate a proactive security center with account health scoring, MFA setup, device/session visibility,
    reactive rather than proactive
    security system. There are no visible indicators around account risk, password health, MFA
    password strength tracking, and security recommendations.
    encouragement, device management, or security posture monitoring.
    orkflow lacks operational
    sers performing account administration tasks may frequently move between billing,
    Critical
    to 
    Medium
    reserve workflow continuity through persistent context, linked account-management actions, and
    W
    U
    continuity across account-
    notifications, users, and security without continuity or contextual retention. This increases
    management tasks
    navigation overhead and slows administrative workflows.
    otification preferences are
    Notification management appears binary and lacks operational granularity for different user
    I
    oversimplified for operational
    roles, project states, hiring workflows, billing events, or team collaboration scenarios.
    digest and escalation logic.
    N
    P
    centralized admin task management.
    ntroduce layered notification controls by category, urgency, role, workflow type, and delivery channel with
    workflows
    Billing workflow lacks
    B
    illing currently appears limited to payment entry and purchase history, without operational
    Expand billing into a full financial-management workflow including invoices, subscriptions, renewal
    subscription and financial
    visibility into subscription status, invoices, usage tracking, renewal logic, failed payments, or
    management, payment recovery, and billing ownership controls.
    management depth
    organizational billing management.
    System feedback lacks continuity
    Success states (such as user deletion) appear temporary and disconnected from larger
    I
    after action completion
    workflow outcomes. Users are not guided toward follow-up actions, undo states, or
    continuation recommendations.
    ntroduce persistent post-action guidance, recovery opportunities, contextual next steps, and workflow
    operational next steps after completing actions.
    orkflow scalability concerns for
    urrent settings workflows appear optimized for very small teams and simple account
    edesign account-management architecture with scalability principles supporting multi-admin
    W
    C
    growing organizations
    structures. As organizations scale, administration complexity, governance needs, and
    environments, department-level controls, advanced permissions, and enterprise-ready administration
    operational coordination may become difficult to manage.
    patterns.
    Primary account can be deleted
    through User Management flow
    R
    estrict deletion access for primary/owner accounts within the User Management flow. Instead, introduce
    The current User Management flow allows deletion of the primary or owner account, which can
    R
    unintentionally lock the organization out of the platform. Since the primary account is typically
    protected account logic where ownership must first be transferred to another verified admin before deletion
    tied to billing, permissions, ownership, and recovery access, deleting it creates a critical
    is allowed. Add clear warnings, confirmation steps, and safeguard messaging to prevent accidental account
    operational and security risk. Users may lose access to company data, subscriptions, and
    lockouts.
    administrative controls without a clear recovery mechanism.
    Critical

## DashboardResponsive_Audit

    Dashboard(Responsive) Audit
    Das board Responsive Audit
    h
    Issue Type
    roblem
    P
    Onboarding UX
    riticality
    C
    Zero-state dashboard shows no onboarding guidance. New employers see raw '0' counters and
    red-diamond error alerts with no setup flow or progress bar.
    (
    )
    Screens ot
    roposed Solution
    P
    h
    Replace error alerts with a numbered onboarding checklist. Add progress bar, convert warnings to
    friendly info icons, celebrate first completion with success state.
    Critical
    Modal Interaction
    Dropdown in 'Add New Skill' modal overflows outside the modal boundary onto the dimmed
    overlay, breaking visual containment.
    Modal should dynamically increase height to contain the dropdown, or render inline-expanding list
    within modal body. Set overflow: visible on inner container only.
    Critical
    Scrollability / Affordance
    Dropdown in modal shows only 4 trade categories with no scroll affordance. Users have no
    indication more content exists below.
    Add scrollbar
    Critical
    Modal Interaction
    When dropdown is open, Confirm/Cancel buttons are hidden behind it. Users cannot save without
    closing the dropdown first, which is non-obvious.
    Action buttons must remain visible. Add sticky footer or fix modal height so buttons are always
    shown. Add 'Done selecting' affordance inside the dropdown.
    Critical
    Empty State Design
    All 3 KPI cards show '0' in the same large bold black number with no visual differentiation. They
    don't communicate being unstarted states.
    Show '0' in muted secondary color. Add micro-copy nudging action (e.g. 'Post a job to get
    applications'). Use colored icon banners to differentiate card purpose.
    Critical
    Bu
    tton / Control Labeling
    The action button inside the dropdown is truncated/cut off on the right side. Button text is not
    readable and action is completely ambiguous.
    nsure action button is fully visible within dropdown bounds. Label explicitly ('Clear all' or
    'Deselect all'). Provide enough padding so it is never clipped.
    E
    Critical
    latform Feature — Notifications
    P
    No notification bell, no alert tray, no badge counter exists anywhere. For a hiring/matching
    platform, time-sensitive alerts are core to value proposition.
    Add notification bell with unread badge in top nav. Clicking opens dropdown tray with recent
    alerts and timestamps. Add in-app toast notifications.
    Critical
    esponsive Layout / Mobile UX
    R
    n Mobile, KPI cards switch to vertically stacked layout where icon banner expands into massive
    full-width block, forcing excessive scrolling.
    n mobile, convert KPI cards into compact horizontal cards with icon left and metric details right.
    Icon size should never exceed 48px on mobile.
    O
    O
    Critical
    Mobile Navigation UX
    n 4 px, mobile nav drawer opens almost full-screen but lacks close affordance. No visible
    close button and no dimmed backdrop for outside-tap dismissal.
    O
    Add visible close
    25
    (X)
    button inside drawer header. Ensure hamburger trigger remains accessible.
    Critical
    esponsive Layout / Mobile UX
    R
    n Mobile, section title text wraps across multiple lines while Edit action detaches and floats
    below as a centred icon-only control, becoming visually disconnected.
    n mobile, restructure into vertical layout with title text on top and clearly labeled full-width 'Edit
    Categories' button below. Avoid isolated icon-only actions.
    O
    O
    Critical
    Information Arc itecture
    No top navigation bar exists. The UI relies entirely on sidebar nav, which leaves no persistent
    space for utility actions like search, notifications, or user profile.
    h
    Add a top nav bar spanning the full width.
    Medium
    V
    isual Design Dept
    h &
    Elevation
    Dashboard cards and panels sit on a flat gray background with no consistent shadow or elevation
    system. Layers feel undifferentiated.
    Define a 3-tier elevation system background, card, modal/overlay. Apply consistently.
    Medium
    Empty State Design
    The 'Success Center' section title and content appear even when empty, showing only error
    states no positive success states, no completion animation.
    When all items are resolved, transform to a positive success state: green checkmark animation,
    ' ou're all set ' heading, remove the error icon pattern.
    —
    Y
    !
    Medium
    Iconograp y Consistency
    h
    Sidebar uses mixed icon styles some outlined, some filled, varying stroke weights. The 'Logout'
    icon is noticeably different in weight from the rest.
    Standardize on a single icon library and weight. Audit all icons against a single style spec.
    —
    Medium
    Typography Scale
    ody copy, labels, and card metrics share too similar a type size. The visual hierarchy between
    supporting text and primary data is weak.
    stablish a type scale. Apply consistently across all dashboard components.
    B
    E
    Medium
    olor Usage / Semantic Colors
    C
    Red is used for both the error alerts in 'Success Center' and critical notification states. No
    semantic color system exists warning, info, and error look identical.
    Define semantic color tokens error, warning, info, success. Apply consistently.
    —
    Medium
    Multi-select UX
    When 3 items are selected, the input field shows '+1' overflow with no indication of what the
    hidden item is. Users must open dropdown to recall selections.
    n hover of '+1', show a tooltip listing hidden selections. Make '+1' chip clickable to scroll list to
    those items.
    O
    Medium
    latform Feature — Searc
    P
    h
    No global search exists anywhere. As employer accumulates candidates, messages, and job
    posts, there is no way to search a serious scalability problem.
    Add global search bar in top nav (cmd+K shortcut) that searches across candidates, messages,
    and job posts simultaneously. Results grouped by type.
    —
    Medium
    Microcopy / CTA Labels
    oth error items in Success Center use identical 'Take Action →' link text. Users cannot tell which
    action leads where, adding cognitive load.
    Use descriptive CTA text specific to each action.
    B
    Medium
    a igation Structure
    N v
    ogout sits in main sidebar nav alongside Dashboard and core features same visual weight as
    primary navigation. It is a destructive exit action one misclick away.
    Remove Logout from primary nav. Move to user account dropdown in top nav. If kept in sidebar,
    visually demote it smaller text, muted color, separator line above.
    L
    —
    Medium
    Accessibility
    No focus rings or keyboard navigation states visible on any interactive element. This is a WCAG
    .1 AA compliance failure.
    Add visible focus ring on all interactive elements and target WCAG AA.
    2
    Medium
    esponsive Modal UX
    R
    n 4 px, 'Add New Skill' modal doesn't properly handle long tag content. Tag 'Carpentry Custom Woodworking' clips out of bounds inside the input area.
    O
    Improve tag overflow handling inside modal input by applying truncation, horizontal scrolling, or
    responsive wrapping. Ensure all modal content remains visible.
    25
    Medium
    esponsive Alerts / Alignment
    R
    n tablet Success Center warning icons become visually top-heavy when adjacent body text
    wraps onto multiple lines. Icons appear detached from content block.
    Vertically center alert icons relative to combined heading and body text block using flex
    alignment. Ensure multi-line alert layouts preserve visual balance.
    O
    Medium
    a igation Consistency
    N v
    In mobile navigation drawer, 'Messages' item is missing its icon while every other nav item
    includes one. This breaks alignment consistency.
    Add the missing message/mail icon and audit all navigation items for icon rendering consistency
    across every breakpoint and state.
    Medium
    Mobile Top Bar UX
    n mobile, top bar only displays logo and hamburger menu. No user identity, avatar, account
    access, or notification context is visible.x
    Introduce compact user avatar and notification bell in mobile top bar. Tapping avatar opens
    account actions (profile, settings, logout).
    O
    Medium
    Icon Semantics
    Wrench/spanner icon next to 'Trade categories we are matching you with' implies settings action,
    creating false affordance suggesting it is clickable.
    Replace with neutral tag/label icon or remove entirely. If kept, visually suppress it to signal it is
    decorative.
    Low
    a igation Structure
    N v
    Main content area has no page-level header or breadcrumb. Users cannot confirm their location.
    Pattern won't scale once users navigate into sub-pages.
    Add a top bar with current page title on the left and utility actions (notifications, user avatar) on
    the right.
    Low
    State Management / UX
    Success Center card has no dismiss or 'done' mechanism. It will persist even after users complete
    the listed actions.
    nce items are completed, show card to success state with a Dismiss option. ave option to
    Dismiss the action proposed in Card
    O
    Low
    orm UX / Microcopy
    F
    Search input inside dropdown has no search icon and uninformative placeholder ('Search'). Input
    has no visible border in default state.
    Add search icon left of input.
    Low
    Spacing / Mobile Safe Area
    n Mobile the Safe space is same as that in Table and Laptop, which reduces real estate available
    for actual Content
    nforce a reduced horizontal padding on smaller displays
    O
    E
    Low
    H
