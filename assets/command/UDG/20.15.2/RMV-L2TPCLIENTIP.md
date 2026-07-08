---
id: UDG@20.15.2@MMLCommand@RMV L2TPCLIENTIP
type: MMLCommand
name: RMV L2TPCLIENTIP（删除L2TP绑定的接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: L2TPCLIENTIP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- L2TP组绑定源端接口
status: active
---

# RMV L2TPCLIENTIP（删除L2TP绑定的接口）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除L2TP组上已绑定的源端Gi接口。用户删除指定的源端接口场景，可以指定源端接口名称。

## 注意事项

- 该命令执行后立即生效。
- 该命令不指定源端接口名称场景，只能删除没有用户存在的绑定关系，可以使用LST L2TPCLIENTIP命令查询删除结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2TPGROUPID | L2TP组号 | 可选必选说明：必选参数<br>参数含义：指定L2TP组号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1500。<br>默认值：无<br>配置原则：无 |
| INTERFACENAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：指定源端Gi接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/L2TPCLIENTIP]] · L2TP绑定的接口（L2TPCLIENTIP）

## 使用实例

假设客户不再使用L2TP组1绑定的"giif1/0/0"源端接口与LNS交互，可以使用该命令删除绑定关系：

```
RMV L2TPCLIENTIP:L2TPGROUPID=1,INTERFACENAME="giif1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-L2TPCLIENTIP.md`
