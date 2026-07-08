---
id: UDG@20.15.2@MMLCommand@RMV APNIMSSIGFLTR
type: MMLCommand
name: RMV APNIMSSIGFLTR（删除APN的IMS分类器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APNIMSSIGFLTR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- VOLTE管理
- APN的IMS信令分类器
status: active
---

# RMV APNIMSSIGFLTR（删除APN的IMS分类器）

## 功能

**适用NF：PGW-U、UPF**

![](删除APN的IMS分类器（RMV APNIMSSIGFLTR）_86527119.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认删除规则后合法的IMS信令报文都能命中其中一条规则。

该命令用于删除指定优先级的APN下的IMS信令专用上下文的Filter。当运营商不需要某个信令分类器的规则过滤包时，使用该命令删除该filter。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 执行该命令时，请确认是否会对该APN下的业务造成影响，操作不当，可能会造成语音业务不通。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定静态分组过滤优先级。值越小优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。同一个APN内唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNIMSSIGFLTR]] · APN的IMS分类器（APNIMSSIGFLTR）

## 使用实例

当运营商不需要APN huawei.com的信令分类器的规则过滤包时，使用该命令删除这个filter。配置APN为huawei.com，PRIORITY为3：

```
RMV APNIMSSIGFLTR:APN="huawei.com",PRIORITY=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-APNIMSSIGFLTR.md`
