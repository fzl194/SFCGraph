---
id: UNC@20.15.2@MMLCommand@RMV SMFALLOWED5QIS
type: MMLCommand
name: RMV SMFALLOWED5QIS（删除5G用户允许的5QI列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFALLOWED5QIS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC允许接入的5QIs
status: active
---

# RMV SMFALLOWED5QIS（删除5G用户允许的5QI列表）

## 功能

**适用NF：SMF**

该命令用于删除5G用户允许的5QI列表。

## 注意事项

- 命令执行后只对新接入用户生效。

- 删除前请确认和"ISMFDFTQOSCTRL"命令及"SMFNONDFTQOSCTL"命令已不存在引用关系，否则不能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSINDEX | 用户QOS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示允许用户接入的5QI列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| QOS5QISTART | 5QI范围起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许接入的5QI范围的起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| QOS5QIEND | 5QI范围结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许接入的5QI范围的结束值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G用户允许的5QI列表（SMFALLOWED5QIS）](configobject/UNC/20.15.2/SMFALLOWED5QIS.md)

## 使用实例

如果想删除"用户QOS索引"为1, 的5G用户允许的5QI列表，执行如下命令:

```
%%RMV SMFALLOWED5QIS: QOSINDEX=4;%%
RETCODE = 0  Operation succeeded

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G用户允许的5QI列表（RMV-SMFALLOWED5QIS）_14280400.md`
