---
id: UNC@20.15.2@MMLCommand@LST USRPROFCHARGE
type: MMLCommand
name: LST USRPROFCHARGE（查询User Profile的计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRPROFCHARGE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- User Profile计费控制
status: active
---

# LST USRPROFCHARGE（查询User Profile的计费配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询User Profile实例的计费配置，具体为：

1、查询User Profile实例配置的在线计费、离线计费方式以及是否开启紧耦合功能。

2、查询User Profile实例绑定的离线计费模板。

3、查询User Profile实例绑定的DCC模板。

4、查询User Profile实例绑定的费率切换组。

5、查询User Profile实例绑定的计费属性实例。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRPROFNAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定User Profile实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRPROFCHARGE]] · User Profile的计费配置（USRPROFCHARGE）

## 使用实例

显示User Profile实例Test的计费相关属性：

```
LST USRPROFCHARGE: USRPROFNAME="Test";
```

```

RETCODE = 0  操作成功

User Profile计费配置
--------------------
      用户模板名称  =  test
 PGW离线计费模板名  =  NULL
 SGW离线计费模板名  =  NULL
GGSN离线计费模板名  =  NULL
      费率切换组名  =  NULL
      计费属性名称  =  NULL
       DCC模板名称  =  NULL
  融合计费模板名称  =  NULL
 SMF离线计费模板名  =  NULL
      融合计费开关  =  继承
      在线计费开关  =  继承
      离线计费开关  =  继承
  业务申请上报模式  =  融合业务申请上报模式
       QBC计费开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRPROFCHARGE.md`
