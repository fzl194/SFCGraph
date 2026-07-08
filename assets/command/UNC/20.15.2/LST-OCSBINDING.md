---
id: UNC@20.15.2@MMLCommand@LST OCSBINDING
type: MMLCommand
name: LST OCSBINDING（查询Ocs绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OCSBINDING
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
- OCS绑定OCS Group
status: active
---

# LST OCSBINDING（查询Ocs绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示UNC上已配置的OCS组信息。用户可以选择显示指定的OCS组信息，也可以显示所有已配置的OCS组信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：可选参数<br>参数含义：指定OCS组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：如果不配置则是要查询所有的OCS组。 |

## 操作的配置对象

- [Ocs绑定关系（OCSBINDING）](configobject/UNC/20.15.2/OCSBINDING.md)

## 使用实例

查询OCS绑定关系命令为：

```
LST OCSBINDING:;
```

```

RETCODE = 0  操作成功。

Ocs绑定关系信息
---------------
                  Ocs组名称  =  ocsgroup1
                Ocs主机名称  =  ocs1
    IMSI/MSISDN号码段组名称  =  test02
  IMSI/MSISDN号码段组优先级  =  1
Ocs在OcsGroup中的负荷分担比  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Ocs绑定关系（LST-OCSBINDING）_09896966.md`
