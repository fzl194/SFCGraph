---
id: UDG@20.15.2@MMLCommand@ADD CONFLICTIP
type: MMLCommand
name: ADD CONFLICTIP（添加本地地址池中冲突IPv4地址）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CONFLICTIP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 冲突地址管理
- IPv4冲突地址管理
status: active
---

# ADD CONFLICTIP（添加本地地址池中冲突IPv4地址）

## 功能

**适用NF：PGW-U、UPF**

该命令用于在本地地址池中标识指定IPv4地址为冲突状态。如果要限制本地地址池中的某个IPv4地址不能分配给终端用户，比如这个地址与系统或其他设备本身的地址冲突，可以使用ADD CONFLICTIP命令标识相应地址为冲突状态，禁止设备地址被分配给终端用户。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 配置冲突IPv4地址前，需要先执行ADD POOL命令配置地址池。
- 如果某地址已经分配给终端用户，此时通过命令配置该地址为冲突地址，命令依然可以执行成功，但是配置生效是在下次分配该地址的时候。
- 配置为冲突状态的IPv4不会分配给用户，该地址池可用地址数减少。
- 一个地址池最多可以设置16个IPv4地址为冲突状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOL命令配置生成。 |
| IPADDRESS | 冲突IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定冲突IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CONFLICTIP]] · 本地地址池中冲突IPv4地址（CONFLICTIP）

## 使用实例

在本地地址池lap指定一个冲突IPv4地址，POOLNAME为“lap” ，IPADDRESS为“10.1.1.1”：

```
ADD CONFLICTIP:POOLNAME="lap",IPADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加本地地址池中冲突IPv4地址（ADD-CONFLICTIP）_82837120.md`
