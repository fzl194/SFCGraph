---
id: UDG@20.15.2@MMLCommand@RMV XHEADER
type: MMLCommand
name: RMV XHEADER（删除扩展头域）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: XHEADER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 扩展头域
status: active
---

# RMV XHEADER（删除扩展头域）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除扩展头域相关配置。

## 注意事项

- 该命令执行后立即生效。
- 如果一条XHeader被L7Filter绑定，则该条XHeader不允许被删除。
- 如果不输入扩展头域名称，表示删除系统中所有扩展头域配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| XHEADERNAME | 扩展头域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果指定的XHeader同时被L7Filter绑定，那么指定的XHeader无法被删除。 |

## 操作的配置对象

- [扩展头域（XHEADER）](configobject/UDG/20.15.2/XHEADER.md)

## 使用实例

- 如果运营商需要删除一条扩展头域的配置：
  ```
  RMV XHEADER: XHEADERNAME="testxheader";
  ```
- 如果运营商需要删除所有扩展头域的配置：
  ```
  RMV XHEADER:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除扩展头域（RMV-XHEADER）_96818060.md`
