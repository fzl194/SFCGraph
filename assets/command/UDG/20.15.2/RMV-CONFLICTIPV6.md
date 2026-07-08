---
id: UDG@20.15.2@MMLCommand@RMV CONFLICTIPV6
type: MMLCommand
name: RMV CONFLICTIPV6（删除本地地址池中冲突IPv6地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CONFLICTIPV6
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 冲突地址管理
- IPv6冲突地址管理
status: active
---

# RMV CONFLICTIPV6（删除本地地址池中冲突IPv6地址）

## 功能

**适用NF：UPF**

该命令用于在某个本地地址池中取消指定IPv6地址或所有IPv6地址的冲突状态。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 设备地址不再和系统上配置的地址池中地址冲突时，需要使用RMV CONFLICTIP命令取消被设置地址的冲突状态。不使用的设备地址允许分配给终端用户，避免造成地址浪费。
- 删除冲突地址只需指定地址池和要删除的地址的prefix，系统会根据指定的prefix在地址池下已经配置的冲突地址中找到已包含该要删除地址的冲突地址，然后删除；。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| V6PREFIX | 冲突IPv6地址前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定冲突IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CONFLICTIPV6]] · 本地地址池中冲突IPv6地址（CONFLICTIPV6）

## 使用实例

- 在本地地址池lap删除指定地址的冲突状态，POOLNAME为“lap”，V6PREFIX为"fc01:0000:0000:0000:0000:0000:0000:0001"：
  ```
  RMV CONFLICTIPV6: POOLNAME="lap", V6PREFIX="fc01:0000:0000:0000:0000:0000:0000:0001";
  ```
- 删除本地地址池lap的所有地址的冲突状态，POOLNAME为“lap”：
  ```
  RMV CONFLICTIPV6: POOLNAME="lap";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-CONFLICTIPV6.md`
