---
id: UNC@20.15.2@MMLCommand@RMV PROFILESPACE
type: MMLCommand
name: RMV PROFILESPACE（删除Profile Space）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PROFILESPACE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- Profile Space
status: active
---

# RMV PROFILESPACE（删除Profile Space）

## 功能

**适用NF：PGW-C、SMF**

本命令用于删除Profile Space实例。

## 注意事项

- 该命令执行后立即生效。
- 删除ProfileSpace实例前，请确认是否有用户在使用此ProfileSpace实例。如果有用户使用，不要删除此配置。
- 如果待删除的ProfileSpace实例和APN绑定（通过ADD APNPROFSPACE命令），会自动解除绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ProfileSpace名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Profile Space（PROFILESPACE）](configobject/UNC/20.15.2/PROFILESPACE.md)

## 使用实例

删除ProfileSpace名称为“profilespace1”的ProfileSpace配置：

```
RMV PROFILESPACE:PROFSPACENAME="profilespace1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Profile-Space（RMV-PROFILESPACE）_09897049.md`
