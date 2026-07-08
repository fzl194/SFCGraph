---
id: UDG@20.15.2@MMLCommand@MOD OSPFV3AUTH
type: MMLCommand
name: MOD OSPFV3AUTH（修改OSPFv3认证配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFV3AUTH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3认证配置
status: active
---

# MOD OSPFV3AUTH（修改OSPFv3认证配置）

## 功能

该命令用于修改在OSPFv3进程下的认证。

![](修改OSPFv3认证配置（MOD OSPFV3AUTH）_49801514.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，如果OSPFv3进程认证与邻居配置不同，可能会使此进程的OSPFv3邻接关系中断，造成业务影响。推荐配置满足复杂度的密码，否则有安全隐患。

## 注意事项

- 该命令执行后立即生效。
- 修改OSPFv3进程认证，请确保和邻居认证配置相同，否则会导致邻接关系中断，影响业务。
- 只有配置了OSPFv3进程后才能使用该命令。
- 当前支持配置的认证算法及密码长度均符合IETF标准规定。
- 配置的密码至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| AUTHKEYID | 验证字标识符 | 可选必选说明：必选参数<br>参数含义：验证字标识符。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| AUTHMODE | 认证类型 | 可选必选说明：必选参数<br>参数含义：认证类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- hmac-sha256：HMAC-SHA256密文验证模式。<br>默认值：无 |
| AUTHTEXT | HMAC-SHA256 密码 | 可选必选说明：必选参数<br>参数含义：HMAC-SHA256 密码 。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 字符不允许包括“？”和空格。<br>- 配置密码时，使用明文格式，长度范围为1~255。<br>- 配置的密码建议至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3AUTH]] · OSPFv3认证配置（OSPFV3AUTH）

## 使用实例

修改OSPFv3进程1下的认证密码：

```
MOD OSPFV3AUTH:PROCID=1, AUTHKEYID=1, AUTHMODE=hmac-sha256,AUTHTEXT="*****";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-OSPFV3AUTH.md`
