---
id: UDG@20.15.2@MMLCommand@RMV POOLBINDGROUP
type: MMLCommand
name: RMV POOLBINDGROUP（将地址池从地址池组中移除）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: POOLBINDGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池绑定地址池组
status: active
---

# RMV POOLBINDGROUP（将地址池从地址池组中移除）

## 功能

**适用NF：PGW-U、UPF**

![](将地址池从地址池组中移除（RMV POOLBINDGROUP）_82837145.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，1、删除pool与pool group的绑定关系，会减少该pool group下的地址数量，可能导致地址不足引起用户激活失败。 2、如果解除绑定的地址池被其他设备复用，可能出现用户地址冲突，导致业务异常。

该命令用于解除地址池与地址池组的绑定。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 执行该命令时，参数地址池组名和地址池名至少需要填写一项。
- 该命令指定地址池组名和地址池名时，表示解除指定地址池组与指定地址池的绑定关系。指定地址池组名而不指定地址池名时，表示解除指定地址池组与所有已绑定地址池的绑定关系。指定地址池名而不指定地址池组名时，表示解除指定地址池与所有地址池组的绑定关系。
- 地址池绑定和解绑定地址池组等相关配置，均不影响当前已接入用户，仅对新激活用户生效。对于已经与地址池组解绑定的地址池，新用户激活申请地址不可从此地址池中分配。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGROUPNAME | 地址池组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOLGROUP命令配置生成。 |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOL命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POOLBINDGROUP]] · 地址池绑定地址池组中的地址池优先级（POOLBINDGROUP）

## 使用实例

- 删除名为poolgroup1的地址池组和名为pool1的地址池之间的绑定关系：
  ```
  RMV POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="pool1";
  ```
- 删除名为poolgroup1的地址池组与所有地址池的绑定关系：
  ```
  RMV POOLBINDGROUP: POOLGROUPNAME="poolgroup1";
  ```
- 删除名为pool1的地址池与所有地址池组的绑定关系：
  ```
  RMV POOLBINDGROUP: POOLNAME="pool1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-POOLBINDGROUP.md`
