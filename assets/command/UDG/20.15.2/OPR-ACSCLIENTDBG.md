---
id: UDG@20.15.2@MMLCommand@OPR ACSCLIENTDBG
type: MMLCommand
name: OPR ACSCLIENTDBG（ACS客户端调试操作）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: ACSCLIENTDBG
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# OPR ACSCLIENTDBG（ACS客户端调试操作）

## 功能

该命令用于向ACS配置客户端发送调试操作。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEBUGTYPE | 调试类型 | 可选必选说明：必选参数。<br>参数含义：用于指定需要调试操作的类型。<br>取值范围：枚举类型。<br>- saveNextSyncdata(保存下次对账文件)：保存客户端下次对账的配置文件。<br>- saveDb(保存客户端数据库)：保存客户端侧DB文件。<br>默认值：无。<br>配置原则：无。 |
| DEBUGVALUE | 调试内容 | 可选必选说明：可选参数。<br>参数含义：<br>自定义调试操作内容。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |
| SERVICENAME | 服务名称 | 可选必选说明：条件必选参数，该参数在<br>“DEBUGTYPE”<br>配置为<br>“saveNextSyncdata”<br>或<br>“saveDb”<br>时为必选参数。<br>参数含义：用于指定需要执行调试操作的微服务名称。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |
| INSTANCEID | 实例ID | 可选必选说明：条件必选参数，该参数在<br>“DEBUGTYPE”<br>配置为<br>“saveNextSyncdata”<br>或<br>“saveDb”<br>时为必选参数。<br>参数含义：用于指定需要执行调试操作的微服务实例ID。<br>取值范围：字符串类型，长度为1~255。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [ACS客户端调试操作（ACSCLIENTDBG）](configobject/UDG/20.15.2/ACSCLIENTDBG.md)

## 使用实例

向ACS配置客户端发送保存下次对账文件调试操作时，执行以下命令：

```
OPR ACSCLIENTDBG: DEBUGTYPE=saveNextSyncdata, SERVICENAME="101", INSTANCEID="hafetcd-pod12-0__104__0";
```

```
%%OPR ACSCLIENTDBG: DEBUGTYPE=saveNextSyncdata, SERVICENAME="101", INSTANCEID="hafetcd-pod12-0__104__0";%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ACS客户端调试操作(OPR-ACSCLIENTDBG)_13590372.md`
