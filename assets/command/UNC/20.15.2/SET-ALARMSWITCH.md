---
id: UNC@20.15.2@MMLCommand@SET ALARMSWITCH
type: MMLCommand
name: SET ALARMSWITCH（设置安全事件告警开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ALARMSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 安全事件告警管理
status: active
---

# SET ALARMSWITCH（设置安全事件告警开关）

## 功能

此命令用于打开或关闭安全事件告警开关。安全事件包括高危操作和鉴权失败。

- 高危操作：是指在MML界面执行已经添加了二次授权的命令。需要进行二次授权的MML命令可以通过**LST SECAUTHMEM**命令查询。
- 鉴权失败：是指用户成功登录到系统后，在页面访问操作或执行MML命令，系统会先进行角色鉴权。若用户角色不满足当前操作要求的角色集类型，系统会提示鉴权失败。

## 注意事项

- 该命令存在系统初始记录，参数STATE (安全事件告警开关)的初始设定值为OFF（关闭）。
- 安全事件告警开关系统默认关闭，通过**SET ALARMSWITCH**命令开启安全事件告警开关后，用户执行高危操作系统会上报ALM-136075高危操作告警，用户操作鉴权失败会上报ALM-136074鉴权失败告警。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| STATE | 安全事件告警开关 | 可选必选说明：必选参数<br>参数含义：安全事件告警开关。<br>取值范围：<br>- ON(开启)<br>- OFF(关闭)<br>默认值：OFF(关闭)。<br>配置原则：无。 |

## 操作的配置对象

- [安全事件告警开关（ALARMSWITCH）](configobject/UNC/20.15.2/ALARMSWITCH.md)

## 使用实例

开启安全事件告警：

```
%%SET ALARMSWITCH: STATE=ON;%%
RETCODE = 0  操作成功

---    END 
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置安全事件告警开关（SET-ALARMSWITCH）_42999600.md`
