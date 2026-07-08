---
id: UNC@20.15.2@MMLCommand@RMV AUTOSCALINGBFD
type: MMLCommand
name: RMV AUTOSCALINGBFD（删除BFD会话自动化配置模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTOSCALINGBFD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BFD会话自动化配置
status: active
---

# RMV AUTOSCALINGBFD（删除BFD会话自动化配置模板）

## 功能

该命令用于删除BFD会话自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 删除该模板时，要保证该模板添加过，且没有被引用。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BFD自动化配置模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOSCALINGBFD]] · BFD会话自动化配置模板（AUTOSCALINGBFD）

## 使用实例

删除一个BFD会话自动化配置模板：

```
RMV AUTOSCALINGBFD:TEMPLATENAME="bfdtemp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BFD会话自动化配置模板（RMV-AUTOSCALINGBFD）_49961546.md`
