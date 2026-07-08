---
id: UNC@20.15.2@MMLCommand@LST OCSGRPBINDING
type: MMLCommand
name: LST OCSGRPBINDING（查询OCS组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OCSGRPBINDING
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- 绑定OCS Group到DCC模板
status: active
---

# LST OCSGRPBINDING（查询OCS组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询UNC上已配置的DCC模板绑定的OCS组信息。用户可以选择显示指定DCC模板的信息，也可以显示所有已配置的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSGRPBINDING]] · OCS组绑定关系（OCSGRPBINDING）

## 使用实例

查询OCS组绑定关系，DCC模板为dcc1，命令为：

```
LST OCSGRPBINDING: DCCTMPLTNAME="dcc1";
```

```

RETCODE = 0  操作成功。

OCS组绑定关系信息
-----------------
               DCC模板名称  =  dcc1
                主备用标记  =  主用
                   OCS组名  =  ocsgroup1
   IMSI/MSISDN号码段组名称  =  seggroup1
IMSI/MSIISDN号码段组优先级  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OCSGRPBINDING.md`
