---
id: UNC@20.15.2@MMLCommand@LST RESERVEDCMD
type: MMLCommand
name: LST RESERVEDCMD（查询补丁预留配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESERVEDCMD
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- SGSN
- MME
- SGW-C
- GGSN
- PGW-C
- SMSF
- NCG
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 预留配置
status: active
---

# LST RESERVEDCMD（查询补丁预留配置）

## 功能

**适用NF：AMF、SMF、NRF、SGSN、MME、SGW-C、GGSN、PGW-C、SMSF、NCG、NSSF**

查询补丁预留配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMDNAME | 功能名称 | 可选必选说明：可选参数<br>参数含义：功能名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [补丁预留配置（RESERVEDCMD）](configobject/UNC/20.15.2/RESERVEDCMD.md)

## 使用实例

查询补丁预留配置，其中功能名称为BALCKLIST，请运行以下命令：

```
%%LST RESERVEDCMD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
       功能名称  =  BALCKLIST
    字符串参数1  =  parameter1
    字符串参数2  =  parameter2
    字符串参数3  =  NULL
      整型参数1  =  0
      整型参数2  =  0
      整型参数3  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询补丁预留配置（LST-RESERVEDCMD）_50558743.md`
