# Slide 4 图像生成 Prompt（草稿）

## Slide role

architecture / ontology overview

## Slide title

三层图谱本体与关系全景图

## Goal

Create a single polished 16:9 presentation slide image for a leadership-facing technical deck.
This slide must visually explain the full ontology and relationship structure of the three-layer configuration graph system.
It must feel like a formal technical architecture summary, not a software UI screenshot, not a teaching poster, and not a marketing infographic.

Use Chinese as the primary visible node labels.
English should be removed from the main visible node names or reduced to very small secondary annotation only.
Make the command layer cleaner than a dense ontology draft and preserve executive-slide readability.

## Visual style

Use a clean professional presentation style with strong architecture-diagram readability and management-report tone.
Light background, structured layout, restrained colors, crisp lines, high Chinese text clarity, moderate information density.

Color guidance:
- business layer in blue
- feature layer in green
- task layer in orange
- command layer in red
- evidence layer in gray

## Composition

Use a five-layer top-to-bottom architecture composition.

Top layer:
- a horizontal evidence bar labeled `证据层 / EvidenceSource`

Second layer:
- business graph layer

Third layer:
- feature graph layer

Fourth layer:
- task graph layer

Bottom layer:
- command graph layer

Add a compact right-side callout box for orchestration edges.

## Main content structure

### Evidence layer

Display:
- 证据来源

Show it as a slim top strip spanning the slide.
Use light gray.
Connect it downward with subtle dashed support lines to all layers.

### Business graph layer

Display nodes with Chinese primary labels:
- 业务域
- 场景
- 配置方案
- 业务规则
- 决策点
- 语义对象

Show the main chain:
- BusinessDomain -> NetworkScenario -> ConfigurationSolution

Show side relations:
- ConfigurationSolution linked to BusinessRule
- NetworkScenario / ConfigurationSolution linked to DecisionPoint
- NetworkScenario / ConfigurationSolution linked to SemanticObject

### Feature graph layer

Display nodes with Chinese primary labels:
- 特性
- 子特性
- 特性规则
- License
- 决策点
- 语义对象
- 特性任务编排边

Show:
- Feature -> SubFeature
- Feature / SubFeature self-dependency relation concept
- Feature / SubFeature -> License
- Feature / SubFeature -> FeatureRule
- Feature / SubFeature -> DecisionPoint
- Feature / SubFeature -> SemanticObject
- Feature / SubFeature -> FeatureTaskOrderEdge

### Task graph layer

Display nodes with Chinese primary labels:
- 配置任务
- 任务规则
- 决策点
- 语义对象
- 任务命令编排边

Show:
- ConfigTask -> TaskRule
- ConfigTask -> DecisionPoint
- ConfigTask -> SemanticObject
- ConfigTask -> TaskCommandOrderEdge

### Command graph layer

Display nodes with Chinese primary labels:
- MML 命令
- 命令参数
- 配置对象
- 命令规则

Show:
- MMLCommand -> CommandParameter
- MMLCommand -> ConfigObject
- CommandParameter -> ConfigObject
- CommandRule governing command / parameter / object
- one compact object-to-object relation cluster around ConfigObject

Reduce non-essential command-layer cross-links so the page reads like a leadership framework slide rather than a dense engineering relation map.

## Cross-layer main relations

These should be the boldest relationship lines in the slide:

- ConfigurationSolution -> uses_feature -> Feature / SubFeature
- ConfigurationSolution -> uses_task -> ConfigTask
- Feature / SubFeature -> decomposes_to -> ConfigTask
- ConfigTask -> invokes -> MMLCommand
- SemanticObject -> realized_by -> Feature / SubFeature / ConfigTask / ConfigObject

Show these as the main ontology spine.

## Orchestration callout box

On the right side, create a small highlighted box titled:

`稳定编排关系`

Inside it, show only:

- FeatureTaskOrderEdge
  - 特性下 task 的稳定编排顺序
- TaskCommandOrderEdge
  - task 内命令的稳定执行顺序

Add a small note:

`方案级完整顺序当前不进入主 schema`

At the bottom, add a concise takeaway strip:

`核心思想：把业务问题、产品能力、复用任务和底层命令分层解耦，再通过有限主关系打通。`

## Chinese text requirements

All visible Chinese text must be formal, correct, readable, and presentation quality.
Use concise Chinese labels.
Do not overload the slide with long explanatory paragraphs.

Preferred visible Chinese labels:

- 证据层
- 业务图谱层
- 特性图谱层
- 任务原子层
- 命令图谱层
- 稳定编排关系

## Rendering constraints

- Must look like a polished executive technical architecture slide
- Not a product UI screenshot
- Not a classroom teaching poster
- Not a dense database ER diagram
- Not a marketing illustration
- Keep strong structure and visual hierarchy
- Avoid clutter and crossing lines
- No watermark
- No unrelated logos
- No slide number

## Slide takeaway

The slide should make one idea visually obvious:

The system separates business problem, product capability, reusable task, and command execution into different ontology layers, then connects them through a small number of stable relationships.
