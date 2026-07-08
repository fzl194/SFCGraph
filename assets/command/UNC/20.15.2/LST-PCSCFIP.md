---
id: UNC@20.15.2@MMLCommand@LST PCSCFIP
type: MMLCommand
name: LST PCSCFIP（查询P-CSCF地址配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFIP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF的IP地址
status: active
---

# LST PCSCFIP（查询P-CSCF地址配置）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询P-CSCF地址信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFIP]] · P-CSCF地址配置（PCSCFIP）

## 使用实例

查询指定P-CSCF组的P-CSCF地址配置记录:

```
LST PCSCFIP: GROUPNAME="mygroup";
RETCODE = 0   操作成功

结果如下
------------------------
     P-CSCF组名  =  mygroup
     IP地址版本  =  IPV6
       IPv4地址  =  255.255.255.255
       IPv6地址  =  2001:DB8::1
           权重  =  1
 P-CSCF获取方式  =  本地分配
           锁定  =  FALSE
          结对ID = 1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询P-CSCF地址配置（LST-PCSCFIP）_09653781.md`
