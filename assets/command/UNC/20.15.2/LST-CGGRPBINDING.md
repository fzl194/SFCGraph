---
id: UNC@20.15.2@MMLCommand@LST CGGRPBINDING
type: MMLCommand
name: LST CGGRPBINDING（查询CG组绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CGGRPBINDING
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
- 离线计费
- GTPP信令
- CG组管理
- CG组绑定
status: active
---

# LST CGGRPBINDING（查询CG组绑定关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来显示UNC上已配置的离线计费模板绑定CG组信息。用户可以选择显示指定离线计费模板的信息，也可以显示所有已配置的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：可选参数<br>参数含义：指定离线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGGRPBINDING]] · CG组绑定关系（CGGRPBINDING）

## 使用实例

查询CG组绑定关系，离线计费模板为ofctemplate1，命令为：

```
LST CGGRPBINDING: OFCTEMPLATENAME="ofctemplate1";
```

```

RETCODE = 0  操作成功。

CG组绑定关系信息
----------------------------
离线计费模板名 = ofctemplate1
CG组ID = 1
Imsi/Msisdn号码段组名称 = seggroup1
Imsi/Msisdn号码段组优先级 = 1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CGGRPBINDING.md`
