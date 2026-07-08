---
id: UDG@20.15.2@MMLCommand@LST SPECCFGITEM
type: MMLCommand
name: LST SPECCFGITEM（查询产品内部需要调整规格比例的项目）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SPECCFGITEM
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务规格管理
- 内部规格调整管理
status: active
---

# LST SPECCFGITEM（查询产品内部需要调整规格比例的项目）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询产品内部需要调整规格比例的项目。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ITEMNAME | 内部配置项名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要调整规格的内部配置项名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127，不区分大小写。<br>默认值：无<br>配置原则：配置项名称应当与实际业务使用的名称相符，如果不匹配则无法生效，可通过命令DSP SPECCFGINFO查询当前支持规格配置的项目。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECCFGITEM]] · 产品内部需要调整规格比例的项目（SPECCFGITEM）

## 使用实例

查询当前配置的规格调整项目信息，可以执行以下命令：

```
LST SPECCFGITEM:;
```

```

RETCODE = 0  操作成功

结果如下
--------
    内部配置项名称  =  SRR_PER_PDP
配置项规格调整比例  =  120
        微服务类型  =  SessionSGExecSvc
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SPECCFGITEM.md`
