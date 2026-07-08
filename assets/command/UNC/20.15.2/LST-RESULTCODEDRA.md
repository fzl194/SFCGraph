---
id: UNC@20.15.2@MMLCommand@LST RESULTCODEDRA
type: MMLCommand
name: LST RESULTCODEDRA（查询DRA返回码控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESULTCODEDRA
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 返回码控制
status: active
---

# LST RESULTCODEDRA（查询DRA返回码控制）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来查询DRA回复的指定结果码控制信息或者所有结果码控制信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>如果配置为“global”则表示全局配置。<br>如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| VENDORID | 设备提供商标识 | 可选必选说明：可选参数<br>参数含义：设备提供商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| RESULTCODEVAL | 返回码 | 可选必选说明：可选参数<br>参数含义：返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESULTCODEDRA]] · DRA返回码控制（RESULTCODEDRA）

## 使用实例

查询VENDORID为0的返回码控制信息：

```
LST RESULTCODEDRA: PCCTEMPLATE="global", VENDORID=0;
RETCODE = 0 操作成功

PCC返回码控制
-------------
                      PCC模板名称 = global
                   设备提供商标识 = 0
Initial流程回滚后使能Holding-Time = 不使能
 Update流程回滚后使能Holding-Time = 不使能
            Terminate流程处理动作 = 缺省动作
               Update流程处理动作 = 宕机备份
              Initial流程处理动作 = 缺省动作
            Terminate流程处理动作 = 缺省动作
                           返回码 = 5xxx
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESULTCODEDRA.md`
