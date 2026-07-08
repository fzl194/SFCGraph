---
id: UDG@20.15.2@MMLCommand@RMV WHITEURLLIST
type: MMLCommand
name: RMV WHITEURLLIST（删除URL白名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: WHITEURLLIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- URL白名单
status: active
---

# RMV WHITEURLLIST（删除URL白名单）

## 功能

**适用NF：PGW-U、UPF**

![](删除URL白名单（RMV WHITEURLLIST）_82837394.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除白名单与URL及用户模板与白名单之间的绑定关系。

该命令用于删除白名单及白名单下的URL。

## 注意事项

- 该命令执行后立即生效。
- 如果URL白名单被UserProfile绑定（可通过SET WHITEURLLISTBIND命令配置），删除URL白名单时，这个绑定关系也会被删除。
- 如果URL白名单被CfWhiteURLLst引用，支持删除URL白名单下的部分URL，但不支持删除该URL白名单。若想要删除该URL白名单，请先解除绑定关系。
- 删除操作要求：
    - 不允许只输入URL参数。
    - 如果不输入任何参数，表示要删除所有的白名单，删除白名单下的URL。
    - 如果只输入白名单名称，表示要删除该白名单，删除该白名单下的URL。
    - 如果同时输入白名单名称和URL，表示要删除白名单下指定的URL。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTNAME | URL白名单列表名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL白名单列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写。<br>默认值：无<br>配置原则：无 |
| URL | URL | 可选必选说明：可选参数<br>参数含义：该参数用于指定URL。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～119。不区分大小写，不支持通配符，不允许输入*。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WHITEURLLIST]] · URL白名单（WHITEURLLIST）

## 使用实例

- 删除所有白名单配置，可以执行如下命令：
  ```
  RMV WHITEURLLIST:;
  ```
- 删除名称为test的白名单配置，可以执行如下命令：
  ```
  RMV WHITEURLLIST:WHITELISTNAME="test";
  ```
- 删除名称为test的白名单下的，URL为www.huawei.com的配置：
  ```
  RMV WHITEURLLIST:WHITELISTNAME="test",URL="www.huawei.com";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-WHITEURLLIST.md`
