---
id: UNC@20.15.2@MMLCommand@LST SMFIEADAPTER
type: MMLCommand
name: LST SMFIEADAPTER（查询信元携带控制配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFIEADAPTER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 业务功能灵活控制
- 信元携带策略管理
status: active
---

# LST SMFIEADAPTER（查询信元携带控制配置）

## 功能

**适用NF：SMF**

该命令用于查询控制SMF与周边网元之间消息中的信元是否携带的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IEADAPTERID | 信元控制配置标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信元控制配置的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFIEADAPTER]] · 信元携带控制配置（SMFIEADAPTER）

## 使用实例

查询当前全部配置，执行如下命令：

```
%%LST SMFIEADAPTER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
信元控制配置标识  =  0
  接口和网元类型  =  N16_VSMF
        流程类型  =  PduSessionEstAsVsmf
    流程消息标识  =  PostPduSessionsParameters
  需要控制的信元  =  PduSessionCreateData.RequestType
信元携带控制开关  =  Disable
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFIEADAPTER.md`
