---
id: UDG@20.15.2@MMLCommand@RMV URRGRPBINDING
type: MMLCommand
name: RMV URRGRPBINDING（删除用户模板的URR组绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: URRGRPBINDING
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# RMV URRGRPBINDING（删除用户模板的URR组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除用户模板的URR组绑定关系（RMV URRGRPBINDING）_82837283.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除UrrGrpBinding可能会影响业务计费。 删除UrrGrpBinding可能会导致用户激活失败。

该命令用于根据指定名字删除使用量上报规则的绑定。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| URRGROUPTYPE | URR组绑定类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定URR组绑定类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SERVICE：业务URR组。<br>- SIGNALING：信令URR组。<br>- TCP：TCP重传URR组。<br>- REDIRECT：重定向URR组。<br>默认值：无<br>配置原则：<br>- SERVICE：设定计费属性绑定类型为业务计费属性。<br>- SIGNALING：设定计费属性绑定类型为信令计费属性。<br>- TCP：设定计费属性绑定类型为TCP重传计费属性。<br>- REDIRECT：设定计费属性绑定类型为重定向计费属性。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/URRGRPBINDING]] · 用户模板的URR组绑定关系（URRGRPBINDING）

## 使用实例

假如运营商希望取消名称为“TestUserProfileName”的用户模板下的信令使用量上报规则：

```
RMV URRGRPBINDING: USERPROFILENAME="TestUserProfileName", URRGROUPTYPE=SIGNALING;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除用户模板的URR组绑定关系（RMV-URRGRPBINDING）_82837283.md`
