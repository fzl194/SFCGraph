---
id: UNC@20.15.2@MMLCommand@LST APNPROFSPACE
type: MMLCommand
name: LST APNPROFSPACE（查询APN与Profile Space的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNPROFSPACE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- APN绑定Profile Space
status: active
---

# LST APNPROFSPACE（查询APN与Profile Space的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于查询APN与Profile Space的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPROFSPACE]] · APN与Profile Space的绑定关系（APNPROFSPACE）

## 使用实例

查询APNProfSpace配置，APN为“apn1”：

```
LST APNPROFSPACE: APN="apn1";
```

```

RETCODE = 0  操作成功。

APN绑定Profile Space 信息
-------------------------
           APN名称  =  apn1
Profile Space 名称  =  profilespace2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN与Profile-Space的绑定关系（LST-APNPROFSPACE）_09897055.md`
