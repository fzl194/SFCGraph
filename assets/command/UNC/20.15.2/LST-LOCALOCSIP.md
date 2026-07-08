---
id: UNC@20.15.2@MMLCommand@LST LOCALOCSIP
type: MMLCommand
name: LST LOCALOCSIP（查询本省OCS的IP号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALOCSIP
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 本省OCS的IP号段
status: active
---

# LST LOCALOCSIP（查询本省OCS的IP号段）

## 功能

**适用NF：NCG**

该命令用于查询本省OCS的IP号段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSID | OCS标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。只允许输入字母，数字和中划线。<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALOCSIP]] · 本省OCS的IP号段（LOCALOCSIP）

## 使用实例

查询所有本省OCS的IP号段：

```
LST LOCALOCSIP:;
%%LST LOCALOCSIP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
   OCS标识  =  ocsid001
IP地址类型  =  IPv4地址
  IPv4地址  =  192.168.100.1
  IPv6地址  =  ::
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本省OCS的IP号段（LST-LOCALOCSIP）_45110922.md`
