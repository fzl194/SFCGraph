---
id: UNC@20.15.2@ConfigObject@TALST
type: ConfigObject
name: TALST（跟踪区列表）
nf: UNC
version: 20.15.2
object_name: TALST
object_kind: entity
applicable_nf:
- MME
status: active
---

# TALST（跟踪区列表）

## 说明

**适用网元：MME**

该命令用于增加跟踪区列表，包括：

1. 若输入的TA List标号不存在，表示新建一个跟踪区列表，并且同时为该跟踪区列表新增一个TAI。
2. 若输入的TA List标号已经存在，表示为该跟踪区列表新增一个TAI。
3. 若系统未配置包含UE当前活动的TAI的TA list，ATTACH流程和TAU流程中MME会自动新建包含当前TAI的TA list并在TAU accept消息/Attach accept消息中携带下发给UE。
4. 为了减少用户频繁进行TAU，系统会在符合以下场景的TAU流程中下发包含上次活动的TAI的TA list。
    - 非联合的Intra TAU流程（不包含Inter Handover后的Intra TAU），SGW无改变，TAU Request消息携带“Last visited TAI”并且 [**SET MMFUNC**](../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md) 命令 “LAST TA” 配置为 “YES” 。
    - 联合的Intra TAU流程（不包含Inter Handover后的Intra TAU），SGW无改变，TAU Request消息携带“Last visited TAI”， [**SET MMFUNC**](../MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md) 命令 “LAST TA” 配置为 “YES” 并且VLR无改变。

该命令在附着或TAU流程中给UE下发跟踪区列表，UE在此跟踪区列表中包含的所有TA区中移动时，不再需要发起TAU（Tracking area update）流程，从而减少了跟踪区更新流程的执行。

在配置移动性管理或MME pool等场景中，需要执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TALST]] · ADD TALST
- [[command/UNC/20.15.2/LST-TALST]] · LST TALST
- [[command/UNC/20.15.2/MOD-TALST]] · MOD TALST
- [[command/UNC/20.15.2/RMV-TALST]] · RMV TALST

## 证据

- 原始手册：`evidence/UNC/20.15.2/TALST.md`
- 原始手册：`evidence/UNC/20.15.2/TALST.md`
- 原始手册：`evidence/UNC/20.15.2/TALST.md`
- 原始手册：`evidence/UNC/20.15.2/TALST.md`
